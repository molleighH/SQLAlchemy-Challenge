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
engine = create_engine("sqlite:///hawaii.sqlite")

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
def date_previous_year():
    #Create the session. 
    session = Session(engine)
    
    #Define the most recent date in the Measurement dataset. Then, use most_recent_date to calculate the date one year from the last date.
    most_recent_date = session.query(func.max(Measurement.date)).first()[0]
    first_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    #Close the session. 
    session.close()
    
    #Return the date. 
    return(first_date)

#Define welcome route.
#1.[ / ]
#  - Start at the homepage.
#  - List all the available routes.

@app.route("/")
def home():     #Create a welcome function.
    return "" <h1> Welcome to Honolulu, Hawaii Climate API! </h1>
    <h3> The routes available are: </h3>
    <ol>
    <li><a href = "/api/v1.0/precipitation"> Percipitation </a>: <strong>/api/v1.0/preciptation</strong></li>
    <li><a href = "/api/v1.0/stations"> Stations </a>: <strong>/api/v1.0/stations</strong></li>
    <li><a href = "/api/v1.0/tobs"> TOBS </a>: <strong>/api/v1.0/tobs</strong></li>
    <li>To retrieve the minimum, average, and maximum temperatures for a specific start date, use <strong>/api/v1.0/&ltstart&gt</strong> (replace start and end date in yyyy-mm-dd format)</li>
    <li>To retrieve the minimum, average, and maximum temperatures for a specific start-end range, use <strong>/api/v1.0/&ltstart&gt/&ltend&gt</strong> (replace start and end date in yyyy-mm-dd format</li>)
    </ol>
    ""

#2. [ /api/v1.0/precipitation ]
#  - Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using [date] as the key and [prcp] as the value.
#  - Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():
    #Create the session.
    session = Session(engine)
    
    #Query precipitation data from last 12 months via most recent date from Measurement table.
    prcp_data = session.query(Measurement.data, Measurement.prcp).filter(Measurement.date >= date_previous_year()).all()
    
    #Close session. 
    session.close()
    
    #New Dictionary from row data & Append to prcp_list
    prcp_list = []
    for date, prcp in prcp_data:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_list.append(prcp_dict)
        
    #Return a list of jasonified prcp data from previous 12 months. 
    return jsonify(prcp_list)

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
        
#DO NOT CODE BELOW HERE--------------------------------|
if __name__ == '__main__':
        app.run(debug=True)