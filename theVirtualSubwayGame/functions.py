from theVirtualSubwayGame import db
from theVirtualSubwayGame.models import Toronto, Sheffield
import random


def generateStation(city):

    # Check which location was selected (Toronto, London or Sheffield)
    # Load/Open database of stations linked to the city
    # Randomly select a station based on the city that was selected
    if city == 'toronto':
        
        r = random.randrange(1, db.session.query(Toronto).count() + 1)
        station = db.session.query(Toronto).get(r)
        return station

    elif city == 'sheffield':
        
        r = random.randrange(1, db.session.query(Sheffield).count() + 1)
        station = db.session.query(Sheffield).get(r)
        return station

    elif city == 'london':
        return 0

    else:
        return 0

    
# Use google maps Places Seatch API to find the station location
#def getLocation(station):

    #Define maps Client
 #   gmaps = googlemaps.Client(key = get_api_key())

    # Define search
  #  stationLocation = gmaps.find_place(input = station, input_type = 'textquery')

   # return stationLocation

# Use google maps Places Seatch API to find the station location nearest pub

# Load directions from this station to the pub