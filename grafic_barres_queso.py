import pandas as pd 
from dataclasses import dataclass
import matplotlib.pyplot as plt 
from dataframe import *

def graph(students: dict[int, Student]) -> None:
    pt =  [0,0]
    am = [0,0]
    private_pol = [0,0]
    private_no_pol = [0,0]
    pt_am = [0,0]
    pt_priv_pol = [0,0]
    pt_priv_no_pol = [0,0]
    am_priv_pol = [0,0]
    am_priv_no_pol = [0,0]
    pt_am_priv_pol = [0,0]
    pt_am_priv_no_pol = [0,0] 
    others = [0,0]


    for student in students.values():
        mob = student.mobility
        if mob['coming']['public_transport'] and not mob['coming']['active'] and not mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            pt[0] += 1
        
        elif not mob['coming']['public_transport'] and mob['coming']['active'] and not mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            am[0] += 1
        
        elif not mob['coming']['public_transport'] and not mob['coming']['active'] and mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            private_pol[0] += 1
        
        elif not mob['coming']['public_transport'] and not mob['coming']['active'] and not mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            private_no_pol[0] += 1

        elif mob['coming']['public_transport'] and mob['coming']['active'] and not mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            pt_am[0] += 1

        elif mob['coming']['public_transport'] and not mob['coming']['active'] and mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            pt_priv_pol[0] += 1
    
        elif mob['coming']['public_transport'] and not mob['coming']['active'] and not mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            pt_priv_no_pol[0] += 1
            
        elif not mob['coming']['public_transport'] and mob['coming']['active'] and mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            am_priv_pol[0] += 1

        elif not mob['coming']['public_transport'] and mob['coming']['active'] and not mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            am_priv_no_pol[0] += 1

        elif mob['coming']['public_transport'] and mob['coming']['active'] and mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            pt_am_priv_pol[0] += 1

        elif mob['coming']['public_transport'] and mob['coming']['active'] and not mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            pt_am_priv_no_pol[0] += 1

        # stupid people
        elif mob['coming']['public_transport'] and not mob['coming']['active'] and mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            others[0] += 1

        elif not mob['coming']['public_transport'] and mob['coming']['active'] and mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            others[0] += 1


        # Return
        if mob['return']['public_transport'] and not mob['coming']['active'] and not mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            pt[1] += 1
        
        elif not mob['return']['public_transport'] and mob['coming']['active'] and not mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            am[1] += 1
        
        elif not mob['return']['public_transport'] and not mob['coming']['active'] and mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            private_pol[1] += 1
        
        elif not mob['return']['public_transport'] and not mob['coming']['active'] and not mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            private_no_pol[1] += 1

        elif mob['return']['public_transport'] and mob['coming']['active'] and not mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            pt_am[1] += 1

        elif mob['return']['public_transport'] and not mob['coming']['active'] and mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            pt_priv_pol[1] += 1
    
        elif mob['return']['public_transport'] and not mob['coming']['active'] and not mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            pt_priv_no_pol[1] += 1
            
        elif not mob['return']['public_transport'] and mob['coming']['active'] and mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            am_priv_pol[1] += 1

        elif not mob['return']['public_transport'] and mob['coming']['active'] and not mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            am_priv_no_pol[1] += 1

        elif mob['return']['public_transport'] and mob['coming']['active'] and mob['coming']['private_pollution'] and not mob['coming']['private_no_pollution']:
            pt_am_priv_pol[1] += 1

        elif mob['return']['public_transport'] and mob['coming']['active'] and not mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            pt_am_priv_no_pol[1] += 1

        # stupid people
        elif mob['return']['public_transport'] and not mob['coming']['active'] and mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            others[1] += 1

        elif not mob['return']['public_transport'] and mob['coming']['active'] and mob['coming']['private_pollution'] and mob['coming']['private_no_pollution']:
            others[1] += 1


# How do people exactly move from their home to their school? 
    vals = [pt[0], am[0], private_pol[0], private_no_pol[0], pt_am[0],pt_priv_pol[0], pt_priv_no_pol[0], am_priv_pol[0], am_priv_no_pol[0],
        pt_am_priv_pol[0], pt_am_priv_no_pol[0], others[0]]
    
    fig, ax = plt.subplots(figsize = (16,9))
    ax.plot("PT", label = "PT = Public transport", color = '#1f77b4')
    ax.plot("AM", label = "AM = Active mobility", color = '#ff7f0e')
    ax.plot("Priv_p", label = "Priv_p = Private pollution", color = '#2ca02c')
    ax.plot("Priv_no_p", label = "Priv_no_p = Private no pollution", color = '#d62728')
    ax.plot("PT+AM", label = "Public transpot + Active mobility", color = '#9467bd')
    ax.plot("PT+Priv_p", label = "Public transport + Private pollution", color = '#8c564b')
    ax.plot("PT+Priv_no_p", label = "Public transport + Private no pollution", color = '#e377c2')
    ax.plot("Pirv_p+AM", label = "Private pollution + active mobility", color = '#7f7f7f')
    ax.plot("Priv_no_p+AM", label = "Private no pollution + Active mobility", color = '#bcbd22') 
    ax.plot("PT+AM+Priv_p", label = "Pubic transport + Activity mobility, Private pollution", color = '#17becf') 
    ax.plot("PT+AM+P_no_p", label = "Public transport, Active mobility, Public no pollution", color = '#ff5733')
    ax.plot("Other ", label = "Other",color = '#33ff57')

    leg = ax.legend(loc='lower left', shadow=True, fontsize='x-small', title = 'How do people exactly move from their home to their school?')
    #colors = ['blue','red','orange','green','blue','purple', 'pink', 'yellow', 'black', 'grey','brown', 'beige', 'light blue']
    colors = colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#ff5733', '#33ff57']
    ax.pie(vals, colors = colors)
    plt.show() 
    




    groups = ["PT", "AM", "Priv_p", "Priv_no_p", "PT+AM", "PT+Priv_p","PT+Priv_no_p", "Pirv_p+AM", "Priv_no_p+AM", "PT+AM+Priv_p", "PT+AM+P_no_p", "Others"]
    valors = [pt[0] + pt[1], am[0] + am[1], private_pol[0] + private_pol[1], private_no_pol[0] +private_no_pol[1], pt_am[0] + pt_am[1],
        pt_priv_pol[0] + pt_priv_pol[1], pt_priv_no_pol[0] + pt_priv_no_pol[1], am_priv_pol[0] + am_priv_pol[1], am_priv_no_pol[0] + am_priv_no_pol[1],
        pt_am_priv_pol[0] + pt_am_priv_pol[1], pt_am_priv_no_pol[0] + pt_am_priv_no_pol[1], others[0] + others[1]]

    fig, ax = plt.subplots(figsize =(16, 9))
    #Horizontal Bar Plot
    ax.barh(groups, valors)
    plt.show()
    # Pie plot 
    fig, ax = plt.subplots(figsize = (16,9))
    ax.plot("PT", label = "PT = Public transport", color = '#1f77b4')
    ax.plot("AM", label = "AM = Active mobility", color = '#ff7f0e')
    ax.plot("Priv_p", label = "Priv_p = Private pollution", color = '#2ca02c')
    ax.plot("Priv_no_p", label = "Priv_no_p = Private no pollution", color = '#d62728')
    ax.plot("PT+AM", label = "Public transpot + Active mobility", color = '#9467bd')
    ax.plot("PT+Priv_p", label = "Public transport + Private pollution", color = '#8c564b')
    ax.plot("PT+Priv_no_p", label = "Public transport + Private no pollution", color = '#e377c2')
    ax.plot("Pirv_p+AM", label = "Private pollution + active mobility", color = '#7f7f7f')
    ax.plot("Priv_no_p+AM", label = "Private no pollution + Active mobility", color = '#bcbd22') 
    ax.plot("PT+AM+Priv_p", label = "Pubic transport + Activity mobility, Private pollution", color = '#17becf') 
    ax.plot("PT+AM+P_no_p", label = "Public transport, Active mobility, Public no pollution", color = '#ff5733')
    ax.plot("Other ", label = "Other",color = '#33ff57')


    legend = ax.legend(loc='upper left', shadow=True, fontsize='small', title = "General graphic")
    #colors = ['blue','red','orange','green','blue','purple', 'pink', 'yellow', 'black', 'grey','brown', 'beige', 'light blue']
    colors = colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd','#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf','#ff5733', '#33ff57']
    ax.pie(valors, colors = colors)
    plt.show() 

def main() -> None:
    df = pd.read_excel('Datathon_Results_MOBILITY_2022_original_Students.xlsx')
    students: dict[int, Student] =  dict()
    fill(df, students)
    graph(students)


if __name__ == '__main__':
    main()
