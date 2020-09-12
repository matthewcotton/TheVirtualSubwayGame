from flask import render_template, url_for, flash, redirect
from theVirtualSubwayGame import app
from theVirtualSubwayGame.functions import generateStation
from theVirtualSubwayGame.models import Toronto, Sheffield
from theVirtualSubwayGame.googleAPIKey import get_api_key
import googlemaps
import time # make sure this is needed 

#Define maps Client
gmaps = googlemaps.Client(key = 'AIzaSyCqPtcw0b8C8D2c0UeRK72sDLi-bcxwWPk')

#
@app.route('/')
def index():
    return render_template('index.html')

# Route where user selects the Toronto TTC
@app.route('/ttc')
def ttc():
    
    # Randomly selection a station from the TTC network
    station = generateStation('toronto')

    # Check that a statuion is returned
    if station is None:
        flash("A station could not be randomly selected.")
        return redirect(url_for('index'))

    # Define station search term
    stationSearch = str(station) + '+station+Toronto+ON+CA'

    # Get map location for the station
    stationID = gmaps.find_place(input = stationSearch, input_type = 'textquery')

    # Check that the Google Maps API returns some data
    if stationID is False:
       flash("Error finding" + stationSearch + " station.")
       redirect(url_for('index'))

    # Get detailed place information 
    stationLocation = gmaps.place(place_id = stationID["candidates"][0]["place_id"], fields = ['name', 'geometry/location'])

    # Find closest pub to station
    loc = str(stationLocation["result"]["geometry"]["location"]["lat"]) + ',' + str(stationLocation["result"]["geometry"]["location"]["lng"])
    pubData = gmaps.places_nearby(location = loc, rank_by = 'distance', keyword = 'pub')

    # Modify pub Plus Code to replace "+" with "%2B"
    pubPlusCode = pubData["results"][0]["plus_code"]["global_code"]
    pubPlusCode = pubPlusCode.replace("+", "%2B")

    # Modify station Plus Code to replace "+" with "%2B"
    #stationPlusCode = 

    # Pull out station name from StationLocation data to pass to pub.html
    stationName = stationLocation["result"]["name"]

    # Pull out pub name from pubData to pass to pub.html
    pubName = pubData["results"][0]["name"]

    return render_template('pub.html', stationSearch=stationSearch, stationName=stationName, pubName=pubName, pubPlusCode=pubPlusCode, stationLocation=stationLocation, API_Key=get_api_key())

#
@app.route('/tube')
def tube():

    flash("Nope not yet.")
    return redirect(url_for('index'))


#
@app.route('/supertram')
def supertram():

    # Randomly selection a station from the TTC network
    station = generateStation('sheffield')

    # Check that a statuion is returned
    if station is None:
        flash("A station could not be randomly selected.")
        return redirect(url_for('index'))

    # Define station search term
    stationSearch = str(station) + '+tram+stop+Sheffield+UK'

    # Get map location for the station
    stationID = gmaps.find_place(input = stationSearch, input_type = 'textquery')

    # Check that the Google Maps API returns some data
    if len(stationID["candidates"]) < 1:
       flash("Error finding" + stationSearch + " tram stop.")
       return redirect(url_for('index'))

    # Get detailed place information 
    stationLocation = gmaps.place(place_id = stationID["candidates"][0]["place_id"], fields = ['name', 'geometry/location'])

    # Find closest pub to station
    loc = str(stationLocation["result"]["geometry"]["location"]["lat"]) + ',' + str(stationLocation["result"]["geometry"]["location"]["lng"])
    pubData = gmaps.places_nearby(location = loc, rank_by = 'distance', keyword = 'pub')

    # Modify pub Plus Code to replace "+" with "%2B"
    pubPlusCode = pubData["results"][0]["plus_code"]["global_code"]
    pubPlusCode = pubPlusCode.replace("+", "%2B")

    # Modify station Plus Code to replace "+" with "%2B"
    #stationPlusCode = 

    # Pull out station name from StationLocation data to pass to pub.html
    stationName = stationLocation["result"]["name"]

    # Pull out pub name from pubData to pass to pub.html
    pubName = pubData["results"][0]["name"]

    return render_template('pub.html', stationSearch=stationSearch, stationName=stationName, pubName=pubName, pubPlusCode=pubPlusCode, stationLocation=stationLocation, API_Key=get_api_key())
