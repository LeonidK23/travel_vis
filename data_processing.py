import pandas as pd

def read_data(file_name):
    with open(file_name) as f:
        data = f.readlines()

    data = [l.strip().split(",") for l in data]

    return data

def get_cities(data):
    cities = set()

    for ride in data:
        source, dist = ride
        cities.add(source)
        cities.add(dist)

    return list(cities)

def get_city_coords(cities):
    city_coord = dict()

    df = pd.read_csv("worldcities.csv")

    related_data = df.loc[df['city_ascii'].isin(cities)]

    for city in cities:
        city_coord[city] = (0, 0)
        city_data = related_data.loc[related_data['city_ascii'] == city]
        if not city_data.empty:
            city_coord[city] = (city_data.iloc[0]['lat'], city_data.iloc[0]['lng'])

    return city_coord

def add_coords(trips, city_coords):
    for trip in trips:
        dep = trip[0]
        dest = trip[1]
        trip += [city_coords[dep], city_coords[dest]]

    return trips
