import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np

data = pd.read_csv('../03_data/latest/data-processed.csv', sep=';')

person_background = data.iloc[:,1]
person_experience = data.iloc[:,2]
person_role = data.iloc[:,3]
company_location = data.iloc[:,4]
company_size = data.iloc[:,5]
company_sector = data.iloc[:,6]
company_appdomain = data.iloc[:,7]
project_collaboratingPeople = data.iloc[:,8]
project_platform = data.iloc[:,9]
project_length = data.iloc[:,10]
project_systemSize = data.iloc[:,11]
project_modelSize = data.iloc[:,12]


def chartPlatforms():
    counter = Counter([val.strip() for sublist in project_platform.dropna().str.split(',').tolist() for val in sublist])
    platform2Plus = [x for x in counter.items() if x[1]>1]
    platform1 = [x for x in counter.items() if x[1]==1]

    print(platform2Plus)
    print(len(platform1))

    platform2Plus += {('Other', len(platform1))}

    labels, values = zip(*platform2Plus)

    print(labels)
    print(values)

    indexes = np.arange(len(labels))
    width = 0.5

    plt.bar(indexes, values, width)
    plt.xticks(indexes, labels, rotation=30)
    
    figure = plt.gcf()
    figure.set_size_inches(8, 6)
    
    plt.gcf().tight_layout()
    plt.savefig('../05_output/descriptive/platforms.pdf')
    
    plt.show()
    

    

chartPlatforms()