from django.http import JsonResponse
from ipware import get_client_ip
import requests
import pandas as pd 
from math import dist
import json

# read the dataset from a csv file and sotre it into dataframe
df = pd.read_csv("food-truck-data.csv")

# to calculate the distance between tow points
def get_dist(lat1, long1, lat2, long2): 
    return dist((lat1, long1), (lat2, long2))

# to get the nearest number of trucks
def get_nearest_trucks(*loc, num):
    all_dists = []

    # loop through Latitude and Longitude in the dataframe to calculate the distance between given location and all trucks locations
    for locid, lat, long in zip(df['locationid'],df['Latitude'], df['Longitude']):
        
        # append the pair of distances and locationid
        all_dists.append((locid, get_dist(*loc, lat, long)))

    # sort the distances according to the distance
    all_dists.sort(key=lambda x:x[1])
    locIDs, dists = zip(*all_dists[:num])

    # get the nearest trucks with their locationid
    newdf = df[df['locationid'].isin(locIDs)].copy()

    # return the json representation of the nearest trucks
    return newdf.to_json(orient='records')

# view function that display json representation of the nearest trucks 
# it returns 5 trucks by default
def get_trucks(request, pk=5):
    
    # get the ip of the requested user
    ip, public = get_client_ip(request)
    
    # use the default public ip address for testing on localhost
    if not public:
        ip = "216.73.163.219"

    # get the latitude and longitude from the ip address
    try: 
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        if response.status_code == 200:
            data = response.json()
            lat, lon = map(float, data['loc'].split(','))
            tucks_json = get_nearest_trucks(lat, lon, num = pk)

            # convert string to json
            tucks_json = json.loads(tucks_json)

            return JsonResponse(tucks_json, safe=False)

    except Exception as e:
        return JsonResponse([{"Error": f"{e}"}], safe=False)