import pandas as pd
from dataclasses import dataclass
from geopy.geocoders import Nominatim

@dataclass
class Station:
        type: str
        name: str
        coords: tuple[int, int]        
        postcode: int


def get_zipcode(lat: float, long: float) -> int|None:
        geolocator = Nominatim(user_agent="datathon2023FME")
        location = geolocator.reverse((lat, long), language="es")
        try:
                return int(location.raw['address']['postcode'])
        except:
                try:
                        location = geolocator.geocode(location.raw['address']['quarter'])
                        return int(location.raw['display_name'].split(',')[6])
    
                except:
                        try:
                                location = geolocator.geocode(location.raw['address']['district'])
                                return int(location.raw['display_name'].split(',')[5])
                        except:
                              return None
        



def read_renfe(stations_dict: dict[int, list[Station]]):
        cols = ['DESCRIPCION', 'LATITUD', 'LONGITUD', 'C.P.']
        df = pd.read_excel("listado-estaciones-rodalies-barcelona.xlsx", usecols=cols)
        for i, row in df.iterrows():
                if row['C.P.'] in stations_dict.keys():
                        stations_dict[row['C.P.']].append(Station('renfe', row['DESCRIPCION'], (row['LATITUD'], row['LONGITUD']), row['C.P.']))
                else:
                         stations_dict[row['C.P.']] = [Station('renfe', row['DESCRIPCION'], (row['LATITUD'], row['LONGITUD']), row['C.P.'])]
                df = pd.DataFrame([stations_dict])
                df.to_csv('postcode_stops.txt', index=False)         
        

def read_fgc(stations_dict: dict[int, list[Station]]):
        cols = ["stop_lat", "stop_lon", "stop_name"]
        df = pd.read_csv("stops_fgc.txt", usecols=cols)
        for i, row in df.iterrows():
                post_code = get_zipcode(row["stop_lat"], row["stop_lon"])
                if post_code is not None: 
                        if post_code in stations_dict.keys():
                                stations_dict[post_code].append(Station('FGC', row['stop_name'], (row["stop_lat"], row["stop_lon"]), post_code))
                        else:
                                stations_dict[post_code] = [Station('FGC', row['stop_name'], (row["stop_lat"], row["stop_lon"]), post_code)]
                        df = pd.DataFrame([stations_dict])
                        df.to_csv('postcode_stops.txt', index=False)

def read_tmb(stations_dict: dict[int, list[Station]]):
        cols = ["stop_lat", "stop_lon", "stop_name"]
        df = pd.read_csv("stops_tmb.txt", usecols=cols)
        for i, row in df.iterrows():
                post_code = get_zipcode(row["stop_lat"], row["stop_lon"])
                if post_code is not None:
                        if post_code in stations_dict.keys():
                                stations_dict[post_code].append(Station('TMB', row['stop_name'], (row["stop_lat"], row["stop_lon"]), post_code))
                        else:
                                stations_dict[post_code] = [Station('TMB', row['stop_name'], (row["stop_lat"], row["stop_lon"]), post_code)]
                        df = pd.DataFrame([stations_dict])
                        df.to_csv('postcode_stops.txt', index=False)



def reader():
        stations_dict: dict[int, list[Station]] = dict()
        read_renfe(stations_dict)
        read_tmb(stations_dict)
        read_fgc(stations_dict)
