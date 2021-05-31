import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


route_list = ["/api/v1.0/precipitation", "/api/v1.0/stations", "/api/v1.0/tobs", "/api/v1.0/2016-08-14", "/api/v1.0/2016-08-14/2017-07-02"]


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
#    return ( "Welcome to the homepage"
    return(
        f"Precipitation for the last year of data set:  {route_list[0]}<br/>"
        f"The list of stations:  {route_list[1]}<br/>"
        f"Precipitation for the last year of the station with most observations:  {route_list[2]}<br/>"
        f"Enter a start date to get temperature stats for all dates after entry:  {route_list[3]}<br/>"
        f"Enter a start and end date to get temperature stats for all dates between entries:  {route_list[4]}"
    )

@app.route(route_list[0])
def precipitation():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    month_int = ""
    day_int = ""
    for index, letter in enumerate(recent_date[0]):
        if index == 5 or index == 6:
            month_int = month_int + letter
        if index == 8 or index == 9:
            day_int = day_int + letter
        
    a_month = relativedelta(months=1)
    date_format = dt.date(int(recent_date[0][0:4]), int(month_int), int(day_int))
    prev_year_date = date_format - (a_month * 12)

    sel = [Measurement.date, Measurement.prcp]

    results = session.query(*sel).filter(Measurement.date >= prev_year_date).\
    order_by(Measurement.date.desc()).all()
 

    precipitation = [{result[0]: result[1]} for result in results]
    return jsonify(precipitation)
    session.close()

@app.route(route_list[1])
def stations():
    session = Session(engine)

    results = session.query(Measurement.station).\
    group_by(Measurement.station).all()
    return jsonify(results)
    session.close()

@app.route(route_list[2])
def tobs():
    session = Session(engine)

    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    month_int = ""
    day_int = ""
    for index, letter in enumerate(recent_date[0]):
        if index == 5 or index == 6:
            month_int = month_int + letter
        if index == 8 or index == 9:
            day_int = day_int + letter
        
    a_month = relativedelta(months=1)
    date_format = dt.date(int(recent_date[0][0:4]), int(month_int), int(day_int))
    prev_year_date = date_format - (a_month * 12)

    sel = [Measurement.date, Measurement.tobs]

    results = session.query(*sel).filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date > prev_year_date).\
    order_by(Measurement.date.desc()).all()

    return jsonify(results)
    session.close()

@app.route(route_list[3])
def start(start):
    session = Session(engine)

    sel = [Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    results = session.query(*sel).group_by(Measurement.date).filter(Measurement.date >= start).all()

    date_stats = [{"Date": result[0], "Min": result[1], "Max": result[2], "Average": result[3],} for result in results]
    return jsonify(date_stats)

    return jsonify(results)
    session.close()

@app.route(route_list[4])
def startend(start, end):
    session = Session(engine)

    sel = [Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    results = session.query(*sel).group_by(Measurement.date).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    date_stats = [{"Date": result[0], "Min": result[1], "Max": result[2], "Average": result[3],} for result in results]
    return jsonify(date_stats)
    session.close()

if __name__ == '__main__':
    app.run(debug=True)
    