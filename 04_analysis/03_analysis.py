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

#collection for non-default category thresholds
thresholds = {
    'companySize' : 0,
    'projectLength' : 0
}

#collection for non-default order categories
orderByCategory = ['companySize', 'modelSize', 'projectLength']

#collection for non-default pretty printed categories
prettyPrintCategory = {
    'companySize' : 'Company size',
    'projectLength' : 'Project length',
    'modelSize' : 'Model size'
}

orders = {
    'companySize' : ['1-9', '10-24', '25-49', '50-99', '100-249', '250-499', '500+'],
    'projectLength' : ['0-3', '4-12', '13-24', '25-36', '37-48', '49-60', '61+'],
    'modelSize' : ['small', 'medium', 'large']
}

def chartData(data, categories, color, fileName):
    plotData = {}
    for i in range(len(categories)):
        category = categories[i]
        d = data[category]
        counter = Counter([str(val).strip() for sublist in d.dropna().str.split(',').tolist() for val in sublist])
        
        #split at threshold
        threshold = thresholds[category] if category in thresholds.keys() else 1
        counterAboveTreshold = [x for x in counter.items() if x[1]>threshold]
        
        if threshold > 0: #anything not above the threshold goes into the 'Other' category
            counterUpToTreshold = [x for x in counter.items() if x[1]<=threshold]
        
        #sort non-'Other' categories
        if category in orderByCategory:
            counterAboveTreshold = [tuple for x in orders[category] for tuple in counterAboveTreshold if tuple[0] == x]
            counterAboveTreshold.reverse()
        else:
            counterAboveTreshold = sorted(counterAboveTreshold, key=lambda x: x[1])
        
        if threshold > 0 and len(counterUpToTreshold) > 0: #put the 'Other' category to the final counter
            counterAboveTreshold = [('Other', len(counterUpToTreshold))] + counterAboveTreshold

        plotData[category] = counterAboveTreshold

    numCharts = len(plotData.keys())
    rows = [len(p) for p in plotData.values()]
    
    fig, axs = plt.subplots(nrows=numCharts, sharex=False, gridspec_kw={'height_ratios': rows})
    
    if len(categories) == 1:
        axs = [axs]
        
    for i, category in enumerate(plotData):
        counter = plotData[category]
        
        print(counter)
        
        labels, values = zip(*counter)

        #print(labels)
        #print(values)

        indexes = np.arange(len(labels))
        width = 0.75
        
        plt.sca(axs[i])        
        plt.barh(indexes, values, width, color=color)
        plt.yticks(indexes, labels, rotation=0)
        #plt.xlabel('Occurrences', fontsize=14)
        title = prettyPrintCategory[category] if category in prettyPrintCategory.keys() else category.capitalize()
        plt.title(title, fontsize=14)

        ax = plt.gca()
        labels=ax.get_yticklabels()+ax.get_xticklabels()
        for label in labels:
            label.set_fontsize(12)
        
        figure = plt.gcf()
        figure.set_size_inches(8, 0.3*sum(rows))
        plt.gcf().tight_layout()

    plt.savefig('{}/{}.pdf'.format(outputLocation, fileName))
    plt.show()

chartData(data, ['background', 'role'], '#42b6f5', 'person')
chartData(data, ['location', 'companySize', 'sector', 'domain'], '#ffa1c0', 'company')
chartData(data, ['tools', 'projectLength', 'modelSize'], '#a8a8a8', 'model-project')