# The `snowpark` Kedro starter

## Introduction

The code in this repository demonstrates best practice when working with Kedro and Snowpark. It contains a Kedro starter template with some initial configuration and an example pipeline, and originates from the [Kedro documentation about how to work with Snowpark](https://kedro.readthedocs.io/en/stable/tools_integration/snowpark.html).

## Features

### Single configuration in `/conf/base/snowpark.yml`

While Spark allows you to specify many different [configuration options](https://spark.apache.org/docs/latest/configuration.html), this starter uses `/conf/base/snowpark.yml` as a single configuration location.

### `SnowparkSession` initialisation

This Kedro starter contains the initialisation code for `SnowparkSession` in the `ProjectContext` and takes its configuration from `/conf/base/snowpark.yml`. Modify this code if you want to further customise your `SnowparkSession`.