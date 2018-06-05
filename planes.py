import pandas as pd
import numpy as np


airlines = pd.read_csv('airlines.csv', na_values=['\\N'])
airports = pd.read_csv('airports.csv', na_values=['\\N'])
routes = pd.read_csv('routes.csv', na_values=['\\N'])

def mean_routes(airlines, airports, routes):
    '''
    Find the mean number of routes per airport by country. Use the source
    airport to determine the country and don't worry about whether the flight
    is interational or domestic.
    Example:
    Some country has 3 airports
    Airport1 is the source of 5 flights
    Airport2 is the source of 3 flights
    Airport3 is the source of 8 flights
    Average for the country: 5.333
    Returns: Series where the index is the country name and the values are the
    means rounded to 3 decimal places
    Other notes:
    It might be possible to do this using just one groupby but the solution used two
    '''
    alles =routes.merge(airports, how='left' ,left_on='src_airport', right_on='iata')
    return alles.groupby(['country','src_airport']).size().groupby(level=0).mean().round(3)

def main():
    print(mean_routes(airlines, airports, routes))

if __name__ == '__main__':

    main()
