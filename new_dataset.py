import pandas as pd
from dataframe import *
data = []

# Map faculty names to numbers
faculty_mapping = {'School of Telecommunications and Aerospace Engineering of Castelldefels (EETAC)': 1, 'School of Industrial, Aerospace and Audiovisual Engineering of Terrassa (ESEIAAT)': 2, 'Higher Technical School of Architecture of Barcelona (ETSAB)': 3, 'Polytechnic University School of Building of Barcelona (EPSEB)': 4, 'Higher Technical School of Industrial Engineering of Barcelona (ETSEIB)':5, 'Higher Technical School of Telecommunications Engineering of Barcelona (ETSETB)':6, 'Faculty of Mathematics and Statistics (FME) ':7,'School of Engineering of Barcelona East (EEBE):':8, 'Barcelona School of Informatics (FIB)':9,'Polytechnic School of Engineering of Vilanova i la Geltrú (EPSEVG)':10, 'School of Architecture of Vallès (ETSAV)':11,'Higher Technical School of Engineering of Roads, Canals and Ports of Barcelona (ETSECCPB)':12, 'Faculty of Optics and Optometry of Terrassa (FOOT)':13,'Polytechnic School of Engineering of Manresa (EPSEM)':14, 'Faculty of Nautical of Barcelona (FNB)':15,'School of Agricultural Engineering and Biosystems of Barcelona (EEABB)':16}  

for student in students.values():
    # Extract information from the student object
    sex = (1 if student.sex =='Man' else 0)
    faculty = faculty_mapping.get(student.faculty, 0)  # Use 0 for unknown faculty
    days = student.days
    postal_code = student.pc
    public_transport = student.mobility['coming']['public_transport'] and student.mobility['return']['public_transport']
    fastest = student.fastest
    cheapest = student.cheapest
    most_comfortable = student.most_comfortable
    only_option = student.only_option
    environment = student.environment
    healthiest = student.healthiest
    no_private_vehicle = student.no_private_vehicle

    # Append the data to the list
    data.append([sex, faculty, days, postal_code, 1 if public_transport else 0,fastest,cheapest,most_comfortable,only_option,environment,healthiest,no_private_vehicle])

# Create a DataFrame
columns = ['sex', 'faculty', 'days', 'postal_code', 'public_transport','fastest', 'cheapest','most_comfortable','only_option','environment','healthiest','no_private_vehicle']
new_dataset = pd.DataFrame(data, columns=columns)

# Display the new dataset
print(new_dataset.head())

# Save the new dataset to a CSV file
new_dataset.to_csv('new_dataset.csv', index=False)
