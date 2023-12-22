# MWT
Middleware Technologies

## Issue

The following command works in browser, but not with curl and I can't figure out what I miss:
https://symmetrical-invention-rpv679657qx2pwgq-5000.app.github.dev/headers

## My App

### Structure

My App consists of the following services:

#### Frontend

A webfrontend created with vue.js containing a possibility to upload a csv file, select a header from it and display the r-squared score of the linear regression model for the selected column.

#### Backend

A flask service that takes a csv file and returns its headers as well as take a column header, trains a linear regression model and calculate the r-squared value for it and send it back.

#### Database

A postgres database to persist the data.

### Usage

The workflow starts with uploading a csv file in the frontend. This will be sent to the backend, where the columns headers are extracted and sent back to the frontend. There you can select one header, which is sent to the backend that trains a linear regression model for this column as the target. It calculates the r-squared value and returns it to the frontend, where it is displayed.
