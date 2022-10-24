# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## 2.1.0 - 2022-10-24

### Added
- Poppler installation for PDF support
- GDAL 3.2.1 built with flag `--with-poppler` to support PDF
- Forcing installation on some libraries with expired certificates
- gdal2tiles module added on python layer 

## [Unreleased] - 2018-12-20

### Added
- Added deployments to `eu-west-2` and `eu-north-1`

### Fixed
- README updates regarding versions

### Changed
- Keep symlinks when zipping, resulting in smaller deploy package
- Python Lambda Layers no longer need the base GeoLambda layer in addition to the python layer
- Manually compile sqlite3 used in Proj, GDAL, nghttp2
- GDAL 3.2.1
- Proj 7.2.1
- GEOS 3.8.1
- GeoTIFF 1.5.1
- HDF4 4.2.15
- HDF5 1.10.7
- NetCDF 4.7.4
- Nghttp2 1.41.0
- OpenJPEG 2.4.0
- libJPEG Turbo 2.4.0
- Curl 7.73.0
- Webp 1.1.0
- Zstd 1.4.5
- OpenSSL 1.1.1
- In python layer:
    - Python 3.7.4 -> 3.7.9
    - rasterio 1.1.0 -> 1.2.0
    - shapely 1.6.4.post2 -> 1.7.1
    - pyproj 2.4.0 -> 3.0.0.post1

### Removed
- GDAL Elasticsearch driver


## [v2.0.0] - 2019-10-25

### Added
- Added OpenSSL, which is used to compile versions of Python 3.7+, it is not packaged in GeoLambda Layer
- OPENSSL_VERSION=1.0.2

### Changed
- Updated GDAL, PROJ, and Geotiff libraries.
- GDAL_VERSION=3.0.1
- PROJ_VERSION=6.2.0
- GEOTIFF_VERSION=1.5.1


## [v1.2.0] - 2019-10-24

### Added
- A Python GeoLambda Layer is now published, along with the base Lambda Layer. The base layer *must* be included in any Lambda that uses the Python GeoLambda layer. It includes the Python libraries GDAL, rasterio, pyproj, and shapely.
- Base geolambda includes OpenSSL 1.0.2, as this is required for compiling Python 3.7+. It is not included in the Lambda layer, just the base layer for ease of creating different versions of Python child images.


### Changed
- The python diectory, and the new Lambda layer, now uses Python 3.7.4
- GDAL_VERSION=2.4.2
- GEOS_VERSION=3.8.0
- NETCDF_VERSION=4.7.1
- NGHTTP2_VERSION=1.39.2
- OPENJPEG_VERSION=2.3.1
- CURL_VERSION=7.66.0
- LIBJPEG_TURBO_VERSION=2.0.3
- WEBP_VERSION=1.0.3
- ZSTD_VERSION=1.4.3


## [v1.1.0] - 2018-03-22

### Added
- Make compatible with Lambda Layers
- Python example
- Improve documentation
- More libraries (CURL with http2, webp, zstd, libjpegturbo)
- GeoTIFF now compiled from scratch rather than GGDAL builtin
- Published public lambda layers - see README for ARNs
- GEOTIFF_VERSION=1.4.3
- OPENJPEG_VERSION=2.3.0
- LIBJPEG_TURBO_VERSION=2.0.1
- CURL_VERSION=7.59.0
- NGHTTP2_VERSION=1.35.1
- WEBP_VERSION=1.0.1
- ZSTD_VERSION=1.3.8

### Changed
- Major refactor, GeoLambda base now runtime agnostic contains system libraries only
- GDAL_VERSION=2.4.1
- GEOS_VERSION=3.7.1
- HDF4_VERSION=4.2.14
- HDF5_VERSION=1.10.5
- NETCDF_VERSION=4.6.2

### Removed
- Removed Python codes to make geolambda system libraries only


## [v1.0.0] - 2018-07-27

Initial release

Package Versions
- PROJ_VERSION=5.2.0
- GEOS_VERSION=3.6.2
- HDF4_VERSION=4.2.12
- SZIP_VERSION=2.1.1
- HDF5_VERSION=1.10.1
- NETCDF_VERSION=4.6.1
- OPENJPEG_VERSION=2.3.0
- PKGCONFIG_VERSION=0.29.2
- GDAL_VERSION=2.3.1

[Unreleased]: https://github.com/sat-utils/sat-stac/compare/master...develop
[v2.1.0]: https://github.com/developmentseed/geolambda/compare/2.0.0...2.1.0
[v2.0.0]: https://github.com/developmentseed/geolambda/compare/1.2.0...2.0.0
[v1.2.0]: https://github.com/developmentseed/geolambda/compare/1.1.0...1.2.0
[v1.1.0]: https://github.com/developmentseed/geolambda/compare/1.0.0...1.1.0
[v1.0.0]: https://github.com/developmentseed/geolambda/tree/1.0.0
