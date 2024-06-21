# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## 0.6.0

* Add mock functionality to `FpxNode`
* switch to `setuptools_scm`


## 0.5.0

* add `ignore` list to improve performance. example : `parse(msg, ignore=["ODOM"])`


## 0.4.0

* add `gps_node.FpxNode`


## 0.3.0

* add testdata or record file replay with cli `replay`

## 0.2.0

* add cli with `record` and `listen`
* add nmea generation
* renamed classes to `Data` in each message type
