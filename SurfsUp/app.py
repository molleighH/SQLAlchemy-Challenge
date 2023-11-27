# Import the dependencies.
import numpy as np
import pandas as pd 
import datetime as dt 
import re 

#Python SQLtoolkit & ORM
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.inspection import inspect 
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#Create engine to hawaii.sqlite
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()


# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement 

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
#Find the most recent date in the data set.

#1.[ / ]
#  - Start at the homepage.
#  - List all the available routes.

@app.route("/")
def welcome():
    return(
        f"Welcome to the Hawaii Climate Analysis API!<br/>"

#2. [ /api/v1.0/precipitation ]
#  - Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using [date] as the key and [prcp] as the value.
#  - Return the JSON representation of your dictionary.

#3. [ /api/v1.0/stations ]
#  - Return a JSON list of stations from the dataset.

#4. [ /api/v1.0/tobs ]
#  - Query the dates and temperature observations of the most-active station for the previous year of data.
#  - Return a JSON list of temperature observations for the previous year.

#5. [ /api/v1.0/ ] and [ /api/v1.0// ]
#  - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#. - For a specified start, calculate [TMIN], [TAVG], and [TMAX] for all the dates greater than or equal to the start date.
#. - For a specified start date and end date, calculate [TMIN], [TAVG], and [TMAX] for the dates from the start date to the end date, inclusive.

#HINTS:Join the station and measurement tables for some of the queries.

#HINTS:Use the Flask [jsonify] function to convert your API data to a valid JSON response object.