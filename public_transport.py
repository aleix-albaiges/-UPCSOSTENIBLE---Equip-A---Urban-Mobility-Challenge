''' PLOTS A GRAPHIC OF THE NUMBER OF PULBIC TRANSPORT STATIONS I EACH POST CODE'''

import pandas as pd
import estacions
import matplotlib.pyplot as plt

def main():
    try:
        stops = pd.read_csv('postcode_stops.txt')
    except FileNotFoundError:
        estacions.reader()
        stops = pd.read_csv('postcode_stops.txt')
    stops_dict = stops.to_dict()

    keys = list(stops_dict.keys())
    values = [len(lst) for lst in stops_dict.values()]

    plt.bar(keys, values)
    plt.xlabel('Zip code')
    plt.ylabel('Number of stations')
    plt.title('Number of stations for each zone')
    plt.show()



main()
