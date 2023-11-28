# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import re

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

#Reflect an existing database into a new model
Base = automap_base()

#Reflect the tables
Base.prepare(autoload_with=engine)


# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# Find the most recent date in the data set.
def date_previous_year():
    #Create session.
    session = Session(engine)

    #Define most recent date in Measurement dataset; 
    #Next, use most recent date to calculate the date one year from last date.
    most_recent_date = session.query(func.max(Measurement.date)).first()[0]
    first_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)

    #Close session
    session.close()

    #Return date
    return(first_date)
#1. '/'
#   - Start at the homepage.
#   - List all the available routes.
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start (enter as YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/end (enter as YYYY-MM-DD/YYYY-MM-DD)"

    )
    
    
#2. [ /api/v1.0/precipitation ]
#  - Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using [date] as the key and [prcp] as the value.
#  - Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")

def precipitation():
    #Create session.
    session = Session(engine)
    
    #Query precipitation data from last 12 months via most recent date from Measurement table.
    prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= date_previous_year).order_by(Measurement.date.desc()).all()

    #Close session.
    session.close()
    
     #Create dictioinary from row data & Append list of prcp_list
    prcp_list = []
    for date, prcp in prcp_data:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_list.append(prcp_dict)
        
    #Return list of jsonified precipitation data for the previous 12 months
    print(f"Results for Precipitation - {prcp_dict}")
    return jsonify(prcp_list)


#3. [ /api/v1.0/stations ]
#  - Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():

    #Create session.
    session = Session(engine)

    #Query station data from Station dataset
    station_data = session.query(Station.station).all()

    #Close session.
    session.close()

    #Convert list of tuples into regular list
    station_list = list(np.ravel(station_data))

    #Return list of jasonified station data
    return jsonify(station_list)
    
#4. [ /api/v1.0/tobs ]
#  - Query the dates and temperature observations of the most-active station for the previous year of data.
#  - Return a JSON list of temperature observations for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():

    #Create session.
    session = Session(engine)

    #Query tobs data from last 12 months via most recent date from Measurement table.
    tobs_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281')\
                        .filter(Measurement.date >= date_previous_year()).all()
    
    #Close session.
    session.close()

    #Create dictionary from row data & Append list of tobs_list
    tobs_list = []
    for date, tobs in tobs_data:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)

    #Return list of jsonified tobs data from previous 12 months
    return jsonify(tobs_list)
    
    
    
#5. [ /api/v1.0/ ] and [ /api/v1.0// ]
#  - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
#. - For a specified start, calculate [TMIN], [TAVG], and [TMAX] for all the dates greater than or equal to the start date.
#. - For a specified start date and end date, calculate [TMIN], [TAVG], and [TMAX] for the dates from the start date to the end date, inclusive.
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")

def determine_temps(start=None, end=None)
    
    #Create session.
    session = Session(engine)

    #Make a list to query min, avg, max temps
    func_results =[func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    #Check for end date, then perform task
    if end == None:
        #Query data from state date to most recent date.
        start_data = session.query(*func_results)\
                            .filter(Measurement.date >= start).all()
        
        #Convert list of tuples into regular list.
        start_list = list(np.ravel(start_data))

        #Return list of jsonified min, avg, max temps for a specific start date.
        return jsonify(start_list)
    else:
        #Query data from start date to end date
        start_end_data = session.query(*func_results)\
                                .filter(Measurement.date >= start)\
                                .filter(Measurement.date <= end).all()
        
        #Convert list of tuples into regular list
        start_end_list = list(np.ravel(start_end_data))

        #Return list of jsonified min, avg, and max temps for a specific start-end date range.
        return jsonify(start_end_list)
    #Close session.
    session.close()
    
#HINTS:Join the station and measurement tables for some of the queries.
#HINTS:Use the Flask [jsonify] function to convert your API data to a valid JSON response object.
        
#DO NOT CODE BELOW HERE--------------------------------|
# ˅˅˅˅˅ Define main branch; DO NOT CODE BELOW HERE--------------------------------|
if __name__ == '__main__':
        app.run(debug=True)
