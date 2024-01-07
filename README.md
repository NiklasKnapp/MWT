# MWT
Middleware Technologies

## Status

Backend with database connection and persisting the data works. Only frontend connection fails.

## Issues

### Backend

Only one upload works, a second one fails, so the data is not changeable.

### Frontend

Frontend connection does not work yet. To see what happens you can uncomment the frontend from the docker-compose file, trigger the upload in the backend via https://vigilant-space-halibut-4w9vq4vpgrrc5r55-5000.app.github.dev/upload and try to get the headers by clicking the "Get headers" button in the frontend, accessible via https://vigilant-space-halibut-4w9vq4vpgrrc5r55-8080.app.github.dev/

I get "Failed to load resource: net::ERR_NAME_NOT_RESOLVED" in the browser concole.

Don't forget to start clean using docker-compose up --build.

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

- For backend testing start the containers with docker-compose up --build to set up everything clean (no data in database)
- Go to https://vigilant-space-halibut-4w9vq4vpgrrc5r55-5000.app.github.dev/upload to upload the test.csv file
- Go to https://vigilant-space-halibut-4w9vq4vpgrrc5r55-5000.app.github.dev/headers to get all the headers from the data
- Go to https://vigilant-space-halibut-4w9vq4vpgrrc5r55-5000.app.github.dev/train/G1 to calculate the r-squared value for the G1 column (you can replace this with any other column)