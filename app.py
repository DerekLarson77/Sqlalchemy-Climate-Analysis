import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///titanic.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Passenger = Base.classes.passenger

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

route_list = ["/api/v1.0/precipitation", "/api/v1.0/stations", "/api/v1.0/tobs", "/api/v1.0/<start>", "/api/v1.0/<start>/<end>"]

@app.route("/")
def home():
    for route in route_list:
        print(route) 
    
@app.route(route_list[0])
def precipitation():
    
@app.route(route_list[1])
def stations():

@app.route(route_list[2])
def tobs():
  
@app.route(route_list[3])
def start():
    
@app.route(route_list[4])
def end():
    


if __name__ == '__main__':
    app.run(debug=True)
    