import pandas as pd 
from dataclasses import dataclass
import matplotlib.pyplot as plt
import seaborn as sns 
df_students = pd.read_excel('Datathon_Results_MOBILITY_2022_original_Students.xlsx')

@dataclass
class Student:
    sex: str
    faculty: str
    year: str
    days: int
    pc: int
    mobility: dict[str,dict[str,bool]]

students: dict[int, Student] =  dict()
all_modes = ['Combustion or electric motorcycle with non-renewable source charging', 'Electric motorcycle', 'Renfe', 'Combustion vehicle (non-plug-in hybrid, electric or plug-in hybrid with non-renewable source charging),', 'Scooter (or other micro-mobility devices) with non-renewable charging', 'Bicycle', 'Taxi', 'Underground', 'FGC', 'Scooter (or other micro-mobility devices) with renewable charging', 'Bus', 'Tram', 'Electric vehicle (with Zero label and renewable source charging)', 'On foot']
for index, row in df_students.iterrows():
    answer_id = row['Answer ID']
    sex = row['Which of the following options do you identify with most?']
    faculty = row['Select the center where you study:']
    year = row['The subjects you are currently taking, for the most part, correspond to which year?']
    days = row['How many days per week do you usually come to the university?']
    pc = row['Please indicate the postal code from where you usually start your trip to the university:']
    modec_1 = row['Indicate the modes of transport you use to go to the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage 1]']
    modec_2 = row['Indicate the modes of transport you use to go to the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage 2]']
    modec_3 = row['Indicate the modes of transport you use to go to the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage 3]']
    same_route = row['Do you take the same route for coming and going?']
    
    if same_route == 'Yes':
        moder_1, moder_2, moder_3 = modec_1, modec_2, modec_3
    else: 
        moder_1 = row['Indicate the modes of transport you use to return from the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage 1]']
        moder_2 = row['Indicate the modes of transport you use to return from the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage 2]']
        moder_3 = row['Indicate the modes of transport you use to return from the UPC. (only mark the stages that last more than 5 minutes, up to a maximum of 3 stages) [Stage 3]']

    # Initialize student_mobility with all modes set to False
    student_mobility = {'coming': {mode: False for mode in all_modes}, 'return': {mode: False for mode in all_modes}}

    if not pd.isna(modec_1):
        student_mobility['coming'][modec_1] = True
    if not pd.isna(modec_2):
        student_mobility['coming'][modec_2] = True
    if not pd.isna(modec_3):
        student_mobility['coming'][modec_3] = True
    if not pd.isna(moder_1):
        student_mobility['return'][moder_1] = True
    if not pd.isna(moder_2):
        student_mobility['return'][moder_2] = True
    if not pd.isna(moder_3):
        student_mobility['return'][moder_3] = True

    student_info = Student(sex, faculty, year, days, pc, student_mobility)
    students[answer_id] = student_info


