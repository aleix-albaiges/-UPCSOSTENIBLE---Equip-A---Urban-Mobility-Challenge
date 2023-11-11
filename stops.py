import pandas as pd
from dataclasses import dataclass
from geopy.geocoders import Nominatim

@dataclass
class Station:
        type: str
        name: str
        coords: tuple[int, int]        
        postcode: int


def get_zipcode(lat: float, long: float) -> int:
        geolocator = Nominatim(user_agent="DatathonFME2023")
        location = geolocator.reverse((lat, long), language="en")
        try:
                return int(location.raw['address']['postcode'])
        except:
                print("No s'han pogut processar les coordenades")
                return 0
  


def read_renfe(stations_dict: dict[int, list[Station]]):
        cols = ['DESCRIPCION', 'LATITUD', 'LONGITUD', 'C.P.']
        df = pd.read_excel("listado-estaciones-rodalies-barcelona.xlsx", usecols=cols)
        for i, row in df.iterrows():
                if row['C.P.'] in stations_dict.keys():
                        stations_dict[row['C.P.']].append(Station('renfe', row['DESCRIPCION'], (row['LATITUD'], row['LONGITUD']), row['C.P.']))
                else:
                         stations_dict[row['C.P.']] = [Station('renfe', row['DESCRIPCION'], (row['LATITUD'], row['LONGITUD']), row['C.P.'])]
              
        

def read_bus(stations_dict: dict[int, list[Station]]):
        cols = ['NOM_PARADA', 'GEOMETRY']
        df = pd.read_excel("parades.xlsx", usecols=cols)
        df[['Longitude', 'Latitude']] = df['GEOMETRY'].str.extract(r'\((.*?) (.*?)\)')
        for i, row in df.iterrows():
                post_code = get_zipcode(float(row['Latitude']), float(row['Longitude']))
                assert post_code is not None
                if post_code in stations_dict.keys(): 
                        stations_dict[post_code].append(Station('bus', row['NOM_PARADA'], (row['Latitude'], row['Longitude']), post_code))
                else:
                        stations_dict[post_code] = [Station('bus', row['NOM_PARADA'], (row['Latitude'], row['Longitude']), post_code)]

def read_metro():
      ...
      
        


def main() -> None:
        stations_dict: dict[int, list[Station]] = dict() 
        read_renfe(stations_dict)
        read_bus(stations_dict)
        print(stations_dict)

if __name__ == "__main__":
        main()
