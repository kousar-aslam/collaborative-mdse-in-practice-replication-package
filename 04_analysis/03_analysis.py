import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import os

fileLocation = '../03_data'
data = pd.read_csv('{}/data-preprocessed.csv'.format(fileLocation), sep=';')

outputLocation = '../05_output/descriptive'
if not os.path.exists(outputLocation):
    os.makedirs(outputLocation)


def chartData(data, fileName):
    counter = Counter([val.strip() for sublist in data.dropna().str.split(',').tolist() for val in sublist])
    counter2Plus = [x for x in counter.items() if x[1]>1]
    counter1 = [x for x in counter.items() if x[1]==1]

    print(counter2Plus)
    print(len(counter1))

    counter2Plus += {('Other', len(counter1))}

    labels, values = zip(*counter2Plus)

    print(labels)
    print(values)

    indexes = np.arange(len(labels))
    width = 0.5

    plt.bar(indexes, values, width)
    plt.xticks(indexes, labels, rotation=30)
    plt.ylabel('Occurrences', fontsize=14)
    
    ax = plt.gca()
    labels=ax.get_xticklabels()+ax.get_yticklabels()
    for label in labels:
        label.set_fontsize(12)
    
    figure = plt.gcf()
    figure.set_size_inches(8, 6)
    
    plt.gcf().tight_layout()

    plt.savefig('{}/{}.pdf'.format(outputLocation, fileName))
    
    plt.show()

chartData(data['background'], 'latest')