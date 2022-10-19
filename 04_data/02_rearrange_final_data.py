import re

import pandas as pd


dataLocation = '../04_data'
data = pd.read_csv('{}/questionnaire_data.csv'.format(dataLocation), sep=';')

#Move Projectional editing from "Models and languages" to "Editors and modeling environments"
#Col from index 19 to index 39
data.insert(39, 'Editors and modeling environments [Projectional editing]-current', '0')
data['Editors and modeling environments [Projectional editing]-current'] = data['Models and languages [Projectional editing]']
data = data.drop(columns=['Models and languages [Projectional editing]'])

#Col from index 49 to index 69
data.insert(69, 'Editors and modeling environments [Projectional editing]-need', '0')
data['Editors and modeling environments [Projectional editing]-need'] = data['Models and languages [Projectional editing].1']
data = data.drop(columns=['Models and languages [Projectional editing].1'])

data.to_csv('{}/questionnaire_data.csv'.format(dataLocation), sep=';', encoding='utf-8', index=False)
