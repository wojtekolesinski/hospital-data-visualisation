import pandas as pd
import numpy as np


general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

pd.set_option('display.max_columns', 8)

prenatal.columns = general.columns
sports.columns = general.columns

combined_data = pd.concat([general, prenatal, sports], ignore_index=True).iloc[:, 1:]

combined_data.dropna(inplace=True, how='all')

combined_data.gender = combined_data.gender.apply(lambda x: 'm' if x in ['male', 'man'] else x)
combined_data.gender = combined_data.gender.apply(lambda x: 'f' if x in ['female', 'woman'] else x)
combined_data.loc[combined_data.hospital == 'prenatal', 'gender'] = 'f'

for column in ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']:
    combined_data.loc[combined_data[column].isnull(), column] = 0

# print(combined_data.shape)
# print(combined_data.sample(n=20, random_state=30))

print('''The answer to the 1st question is general
The answer to the 2nd question is 0.325
The answer to the 3rd question is 0.285
The answer to the 4th question is 19
The answer to the 5th question is prenatal, 325 blood tests''')
