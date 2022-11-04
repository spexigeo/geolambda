import json
from osgeo import gdal
import os
import urllib.parse
import boto3
import gdal2tiles
from pathlib import Path
import glob
import requests

s3 = boto3.resource('s3')

class Api(object):

    def __init__(self, host=None, version='v1'):
        if host is None:
            host = os.environ.get('SPEXI_API_URL')
        self.host = host
        self.version = version
        self.token = ''

    @property
    def headers(self):
        return {
            'Authorization': 'Bearer {}'.format(self.token)
        }

    def url(self, path):
        return self.host + '/' + self.version + '/' + path

    def get(self, path, params=None, **kwargs):
        return requests.get(self.url(path), params, headers=self.headers, verify=False, **kwargs)

    def post(self, path, data=None, **kwargs):
        return requests.post(self.url(path), data=data, headers=self.headers, verify=False, **kwargs)

    def put(self, path):
        return requests.put(self.url(path), verify=False, headers=self.headers)

    def login(self, email=None, password=None):
        if email is None:
            email = os.environ.get('SPEXI_EMAIL')
        if password is None:
            password = os.environ.get('SPEXI_PASSWORD')
        response = self.post('login', {'email': email, 'password': password}).json()
        if not response['success']:
            raise Exception(response['error'])
        self.token = response['data']['token']

def lambda_handler(event, context):
    
    api = Api()
    api.login()
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    s3key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    ## Paths
    tmp_path = '/tmp/geopdf.pdf'
    tiff_path = '/tmp/geopdf.tif'
    tiles_path = '/tmp/tiles/'
    new_folder_path = s3key.replace('.pdf', '') ## This path points to the same folder the PDF was uploaded to
    
    ## Download file from S3
    s3.Bucket(bucket).download_file(s3key, tmp_path)
    
    [project_id, pdf_name] = new_folder_path.split('/')
    
    ## Convert into tiff and generate tileset
    src = gdal.Open(tmp_path)
    dst = gdal.Translate(tiff_path, src, options = '-co COMPRESS=LZW')
    dst = None
    gdal2tiles.generate_tiles(tiff_path, tiles_path, zoom='11-17', webviewer='none')
    
    ## Upload tileset to S3
    p = Path(tiles_path)
    mydirs = list(p.glob('**'))
    for mydir in mydirs:
        fileNames = glob.glob(os.path.join(mydir, '*png'))
        fileNames = [f for f in fileNames if not Path(f).is_dir()]
        rows = len(fileNames)
        for i, fileName in enumerate(fileNames):
            head_x, x = os.path.split(str(fileName))
            head_y, y = os.path.split(head_x)
            head_z, z = os.path.split(head_y)
            awsPath = f"{new_folder_path}/{z}/{y}/{x}"

            s3.meta.client.upload_file(fileName, bucket, awsPath)
    
    awsPath = f"{new_folder_path}/geopdf.tif"
    s3.meta.client.upload_file(tiff_path, bucket, awsPath)
    
    pdfs_response = api.get(f'pdf?project_id={project_id}').json()
    if not pdfs_response['success']:
        raise Exception(pdfs_response['error'])
    pdfs = pdfs_response['data']
    pdf = next(p for p in pdfs if p['name'] == pdf_name)
    pdf_id = pdf['id']
    if (pdf):
        print('selected ID', pdf_id)
        api.put(f'pdf/{pdf_id}?status=done')

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
