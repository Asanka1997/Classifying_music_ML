@echo off

REM Set Flask application environment variables
set FLASK_APP=app.py
set FLASK_DEBUG=1

REM Starting the Flask application in a new command prompt window
start cmd /k flask run

REM Wait a few seconds to ensure Flask server starts
timeout /t 5

REM Open the default web browser at the Flask app's URL
start http://127.0.0.1:5000

echo Flask app started. Webpage opened in browser.
