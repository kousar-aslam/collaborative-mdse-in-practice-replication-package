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

threshold = 1

def chartData(data, categories, fileName):
    plotData = {}
    for i in range(len(categories)):
        category = categories[i]
        d = data[category]
        counter = Counter([val.strip() for sublist in d.dropna().str.split(',').tolist() for val in sublist])
        
        #split at threshold 
        counterAboveTreshold = [x for x in counter.items() if x[1]>threshold]
        #anything not above the threshold goes into the 'Other' category
        counterUpToTreshold = [x for x in counter.items() if x[1]<=threshold]
        #sort non-'Other' categories
        counterAboveTreshold = sorted(counterAboveTreshold, key=lambda x: x[1])
        #put the 'Other' category to the final counter
        fullCounter = [('Other', len(counterUpToTreshold))] + counterAboveTreshold

        plotData[category] = fullCounter

    numCharts = len(plotData.keys())
    rows = [len(p) for p in plotData.values()]
    
    fig, axs = plt.subplots(nrows=numCharts, sharex=False, gridspec_kw={'height_ratios': rows})
    
    if len(categories) == 1:
        axs = [axs]
        
    for i, category in enumerate(plotData):
        counter = plotData[category]
        labels, values = zip(*counter)

        #print(labels)
        #print(values)

        indexes = np.arange(len(labels))
        width = 0.75
        
        plt.sca(axs[i])        
        plt.barh(indexes, values, width)
        plt.yticks(indexes, labels, rotation=0)
        #plt.xlabel('Occurrences', fontsize=14)
        plt.title(category, fontsize=14)

        ax = plt.gca()
        labels=ax.get_yticklabels()+ax.get_xticklabels()
        for label in labels:
            label.set_fontsize(12)
        
        figure = plt.gcf()
        figure.set_size_inches(8, 4)
        plt.gcf().tight_layout()

    plt.savefig('{}/{}.pdf'.format(outputLocation, fileName))
    plt.show()

chartData(data, ['background', 'role'], 'latest')