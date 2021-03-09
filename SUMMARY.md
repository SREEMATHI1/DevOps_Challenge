1.Understanding the requirements & planned accordingly

2.Wrote an application in Flask framework using Python.

#Importing the packages required for the application
*from flask import Flask, jsonify, json
from os import environ, path
from dotenv import load_dotenv
import boto3
from boto3.dynamodb.conditions import Key* 

#Created requirements.txt file.
#Wrote helper class to convert a DynamoDB item to JSON
#Setting up the environment path.
#Writing code to check the health status of the container 
#Wrote minimal testcase to test the application

3.Tested the application locally

4.Containerizing the application using Docker

#Written Dockerfile for containerization.

5. Used Docker-compose by creating docker-compose.yml file

6. Created an account in Travis-CI

7. Synchronizing Github to Travis-CI

8. Wrote .travis.yml for Continuous Integration setup

9. Triggered automatic build in Travis-CI & updated the docker images

10. Validated the results by /secret & /health in browser.


