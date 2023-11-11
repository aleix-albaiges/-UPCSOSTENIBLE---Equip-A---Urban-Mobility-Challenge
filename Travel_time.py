import pandas as pd 
import matplotlib.pyplot as plt
import networkx as nx

df = pd.read_csv('Enquesta_mobilitat.csv', sep = ';')



dest_counties: set[int] = {2, 3, 4, 6, 10}
travel_times: dict[int, dict[int, dict[int, list[float]]]] = {i: {j: {k: list() for k in range(1, 4)} for j in range(1, 13)} for i in dest_counties}

dict_dest: dict[int, str] = {2: 'Baix Llobregat', 3: 'Barcelonès', 4: 'Garraf', 6: 'Vallès Occidental', 10: 'Bages'}
dict_orig: dict[int, str] = {1: 'Alt Penedès', 2: 'Baix Llobregat', 3: 'Barcelonès', 4: 'Garraf', 5: 'Maresme', 6: 'Vallès Occidental', 7: 'Vallès Oriental', 8: 'Anoia', 9: 'Berguedà', 10: 'Bages', 11: 'Moianès', 12: 'Osona'}
dict_transp: dict[int, str] = {1: 'Active Mobility', 2: 'Public Transport', 3:'Private Transport'}


for index, row in df.iterrows():
    if row['V03A'] == 4 and row['COM_O2'] not in {98, 99} and row['COM_D2'] in dest_counties and row['V03G_R3'] != 99:
        travel_times[row['COM_D2']][row['COM_O2']][row['V03G_R3']].append(row['V03F'])

def transform_to_average_float(nested_dict):
    if isinstance(nested_dict, dict):
        return {key: transform_to_average_float(value) for key, value in nested_dict.items()}
    elif isinstance(nested_dict, list):
        return sum(nested_dict) / len(nested_dict) if len(nested_dict) > 0 else 0.0
    else:
        return nested_dict

def remove_keys_with_zero_mean(nested_dict):
    if isinstance(nested_dict, dict):
        return {key: remove_keys_with_zero_mean(value) for key, value in nested_dict.items() if value != 0.0}
    else:
        return nested_dict

travel_mean_times = transform_to_average_float(travel_times)


for dest, valuesorig in travel_mean_times.items():
    for orig, valuesdest in valuesorig.items():
        for transport, mean_time in valuesdest.items():
            if mean_time != 0.0:
                print(f'The aproximate travel time of {dict_orig[orig]} to {dict_dest[dest]} with {dict_transp[transport]} is aprox {round(mean_time, 2)} minuts.')





