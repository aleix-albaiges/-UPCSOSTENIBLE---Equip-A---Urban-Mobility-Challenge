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
    values = [sum(len(lst) for lst in vals.values()) for  vals in stops_dict.values()]

    plt.bar(keys, values)
    plt.xticks([])
    plt.ylabel('Number of stations')
    plt.title('Number of stations for each zone')
    plt.savefig("better_served_zones.png")

if __name__ == "__main__":
    main()
