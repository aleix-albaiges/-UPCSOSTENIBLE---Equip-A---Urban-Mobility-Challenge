import pandas as pd
from dataclasses import dataclass
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt 
from tabulate import tabulate

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
                if row['C.P.'] < 9000:
                        if row['C.P.'] in stations_dict.keys():
                                stations_dict[row['C.P.']].append(Station('renfe', row['DESCRIPCION'], (row['LATITUD'], row['LONGITUD']), row['C.P.']))
                        else:
                                stations_dict[row['C.P.']] = [Station('renfe', row['DESCRIPCION'], (row['LATITUD'], row['LONGITUD']), row['C.P.'])]


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


# def read_tram(stations_dict: dict[int, list[Station]]):
#        cols = ['Name', 'Latitude', 'Longitud']
#        df = pd.read_excel('Stops.xlsx', usecols = cols)
#        for i, row in df.iterrows():
#             lat = row['Latitude'].replace(',', '.')
#             long = row['Longitud'].replace(',', '.')
#             post_code = get_zipcode(float(lat), float(long))
#             if post_code in stations_dict.keys():
#                 stations_dict[post_code].append(Station('tram', row['Name'], (float(lat), float(long)), post_code))
#             else:
#                 stations_dict[post_code] = [Station('tram', row['Name'], (float(lat), float(long)), post_code)]


# def graphic(stations_dict: dict[int, list[Station]]) -> None:
        
#         key = list(stations_dict.keys())
#         val = [len(station_list) for station_list in stations_dict.values()]
#         plt.bar(key, val)
#         plt.xlabel('Zip code')
#         plt.ylabel('Number of stations')
#         plt.title('Number of stations for each zone')
#         plt.show()

def transmforma() -> dict[int, str]:
        stat_dict = {}
        cols = ["POBLACIO", "PROVINCIA"]
        df = pd.read_excel("listado-estaciones-rodalies-barcelona.xlsx")
        for i, row in df.iterrows():
                if row["C.P."] not in stat_dict.keys():
                        stat_dict[row["C.P."]] = row["POBLACION"]
        return stat_dict

def main() -> None:
        stations_dict: dict[int, list[Station]] = dict() 
        read_renfe(stations_dict)
        #read_fgc(stations_dict)
        #read_tmb(stations_dict)
        #print(stations_dict)
        #graphic(stations_dict)
        # key = list(stations_dict.keys())
        # val = [len(stations_dict) for stations_dict in stations_dict.values()]
        # print(key, ":",val)
        d: dict[int, int] = {}
        df = pd.DataFrame(d)

        df.to_excel("trens.xlsx", index = False, engine='openpyxl')

        # print(stations_dict)

if __name__ == "__main__":
        main()