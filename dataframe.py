import pandas as pd 
from dataclasses import dataclass
import matplotlib.pyplot as plt 

@dataclass
class Student:
    sex: str
    faculty: str
    year: str
    days: int
    pc: int
    mobility: dict[str,dict[str,bool]]
    fastest: bool
    cheapest: bool
    most_comfortable: bool
    only_option: bool
    environment: bool
    healthiest: bool
    no_private_vehicle: bool

def category_transport(type_transp: str) -> str:
        active = {'On foot','Bicycle'}
        public_transport = {'Renfe','FGC', 'Underground', 'Tram'}
        private_pollution = {'Taxi', 'Combustion or electric motorcycle with non-renewable source charging', 'Combustion vehicle (non-plug-in hybrid, electric or plug-in hybrid with non-renewable', 'Scooter (or other micro-mobility devices) with non-renewable charging'}
        private_no_pollution = {'Electric motorcycle', 'Scooter (or other micro-mobility devices) with renewable charging', 'Combustion vehicle (non-plug-in hybrid, electric or plug-in hybrid with non-renewable source charging),', 'Electric vehicle (with Zero label and renewable source charging)'} 

        if type_transp in active: return 'active'
        if type_transp in public_transport: return 'public_transport'
        if type_transp in private_pollution: return 'private_pollution'
        if type_transp in private_no_pollution: return 'private_no_pollution' 
        else: return ''  # mypy don't get mad

def fill(df, students: dict[int, Student]) -> dict[int, Student]:
    all_modes = ['Combustion or electric motorcycle with non-renewable source charging', 'Electric motorcycle', 'Renfe', 'Combustion vehicle (non-plug-in hybrid, electric or plug-in hybrid with non-renewable source charging),', 'Scooter (or other micro-mobility devices) with non-renewable charging', 'Bicycle', 'Taxi', 'Underground', 'FGC', 'Scooter (or other micro-mobility devices) with renewable charging', 'Bus', 'Tram', 'Electric vehicle (with Zero label and renewable source charging)', 'On foot']

    for index, row in df.iterrows():
        answer_id = row['Answer ID']
        sex = row['Which of the following options do you identify with most?']
        faculty = row['Select the center where you study:']
        year = row['The subjects you are currently taking, for the most part, correspond to which year?']
        days = row['How many days per week do you usually come to the university?']
        pc = row['Please indicate the postal code from where you usually start your trip to the university:']
        fastest = row["Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the fastest]"]
        cheapest = row["Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the cheapest]"]
        most_comfortable = row["Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the most comfortable]"]
        only_option = row["Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the only option]"]
        environment = row["Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It has a lower environmental impact]"]
        healthiest = row["Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [It's the healthiest]"]
        no_private_vehicle = row["Please indicate the main reasons why you use the transport combinations you have marked in the previous question. (Select up to a maximum of two options) [I need the private vehicle for other trips]"]
        

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

        categories: set[str] = {'active', 'public_transport', 'private_pollution', 'private_no_pollution'}

        # Initialize student_mobility with all modes set to False
        student_mobility = {'coming': {mode: False for mode in all_modes}, 'return': {mode: False for mode in all_modes}}
        student_mobility = {'coming': {category: False for category in categories}, 'return': {category: False for category in categories}}

        if not pd.isna(modec_1):
            student_mobility['coming'][modec_1] = True
            category = category_transport(modec_1)
            student_mobility['coming'][category] = True
        if not pd.isna(modec_2):
            student_mobility['coming'][modec_2] = True
            category = category_transport(modec_2)
            student_mobility['coming'][category] = True
        if not pd.isna(modec_3):
            student_mobility['coming'][modec_3] = True
            category = category_transport(modec_3)
            student_mobility['coming'][category] = True
        if not pd.isna(moder_1):
            student_mobility['return'][moder_1] = True
            category = category_transport(moder_1)
            student_mobility['return'][category] = True
        if not pd.isna(moder_2):
            student_mobility['return'][moder_2] = True
            category = category_transport(moder_2)
            student_mobility['return'][category] = True
        if not pd.isna(moder_3):
            student_mobility['return'][moder_3] = True
            category = category_transport(moder_3)
            student_mobility['return'][category] = True
        

        student_info = Student(sex, faculty, year, days, pc, student_mobility, 1 if fastest == 'Yes' else 0, 1 if cheapest == 'Yes' else 0, 1 if most_comfortable == 'Yes' else 0, 1 if only_option == 'Yes' else 0, 1 if environment == 'Yes' else 0, 1 if healthiest == 'Yes' else 0, 1 if no_private_vehicle == 'Yes' else 0)
        students[answer_id] = student_info
    return students



students = fill(pd.read_excel('Datathon_Results_MOBILITY_2022_original_Students.xlsx'),dict())
