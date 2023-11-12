import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from importdata import *

# Create a DataFrame from the student dictionary
df_students = pd.DataFrame([(s.sex, s.faculty, s.year, s.days, s.pc, s.mobility['coming'], s.mobility['return']) for s in students.values()],
                           columns=['Sex', 'Faculty', 'Year', 'Days', 'Postal Code', 'Coming', 'Return'])

# Count the number of people in each postal code
people_count = df_students.groupby('Postal Code').size().reset_index(name='Total People')

# Count the number of people using specific transport modes in each postal code
transport_mode_counts = df_students[
    df_students['Coming'].apply(lambda x: any(x[mode] for mode in ['Bus', 'FGC', 'Renfe', 'Tram', 'Underground']))
].groupby(['Postal Code']).size().reset_index(name='Mode Count')

# Merge the two DataFrames
merged_df = pd.merge(people_count, transport_mode_counts, on='Postal Code', how='left').fillna(0)

# Calculate the percentage for each transport mode
merged_df['Percentage'] = (merged_df['Mode Count'] / merged_df['Total People']) * 100

# Normalize the percentage
merged_df['Normalized Percentage'] = merged_df['Percentage'] / 100

# Set the weight for the total number of people
weight = 0.5

# Calculate the Weighted Score
merged_df['Weighted Score'] = (1 - weight) * merged_df['Normalized Percentage'] + weight * (merged_df['Total People'] / merged_df['Total People'].max())

# Rank the postal codes based on the Weighted Score
ranked_df = merged_df.sort_values(by='Weighted Score', ascending=False)

# Display the ranked DataFrame
print(ranked_df[['Postal Code', 'Total People', 'Percentage', 'Weighted Score']])

# Plot the distribution of weighted scores
plt.figure(figsize=(12, 6))
sns.barplot(data=ranked_df, x='Postal Code', y='Weighted Score', palette='viridis')
plt.title('Ranking of Postal Codes Based on Public Transportation Service')
plt.xlabel('Postal Code')
plt.ylabel('Weighted Score')
plt.show()

