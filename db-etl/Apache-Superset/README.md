# Superset guide
This Readme is a guide to install and correctly set up a Superset instance.

## Installation

### Install with docker 
**Not recommended! The Superset documentation about docker installation is not updated nor complete!**

If you want to install Superset with docker follow this instructions: https://superset.apache.org/docs/installation/installing-superset-using-docker-compose

### Install with pypi
**Recommended!**

Follow these steps:
- create a virtualenv to download and store superset package.
- follow the instructions in the [documentation](https://superset.apache.org/docs/installation/installing-superset-from-scratch) at the *Installing and initializing Superset* section.
- the command `superset init` will guide you through the creation of an admin user. You can add other users with custom level of permissions at a later time.
- the command `superset run -p 8088 --with-threads --reload --debugger` launches the server. The option `-p` lets you bind a chosen port.

If you activate an instance on the office machines, remember that it may be required to forward the port to access from outside the office.

## Associate databases
Once the instance is active, you will need to associate the databases from which you want to read data. To do this, first you have to install into the virtualenv the python packages to manage the connectivity to your database.

Once done that, you can connect your database to Superset under the *Data > Databases* section and adding a new connection string.

Supported databases, recommended connectivity packages and corresponding string connections are listed [here](https://superset.apache.org/docs/databases/installing-database-drivers).

**Note**: if you want to enable the upload of csv to the connected database, you need to enable the *Allow data upload* option in the *Extra* tab while inserting the new connection string. Uploaded csv will create new tables inside the database.

## Usage

### Datasets
Once connected your database, you need to create a new dataset under the *Data > Datasets* section. Datasets are SQL queries from the tables in your database.

### Charts
Once created a dataset, under the *Charts* section you can create a new chart based on that. You can select a from a fixed set of chart types, the superset ui will let you configure the chart by choosing which data to display, which aggregations and filter to perform, etc.

Charts are created independently from dashboards and can be added to them at a later time.

Most of the available chart types are natively thought to deal with time series data; some of them can also handle non-time series data.

### Dashboard
You can create a new dashboard under the *Dashboard* section. Dashboard can be customized with tabs, markdown texts, headers and previously created charts can be added to it.

