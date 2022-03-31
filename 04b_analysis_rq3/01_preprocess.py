import pandas as pd
import re

fileLocation = '../03b_data_rq3'

originalForm = 'original-2016.xlsx'
extension2021Form = 'extension-to-orignial-2021.xlsx'
updateForm = 'update-2021.xlsx'
extension2022Form = 'extension-2022.xlsx'

original = pd.read_excel('{}/{}'.format(fileLocation, originalForm))
extension2021 = pd.read_excel('{}/{}'.format(fileLocation, extension2021Form))
update = pd.read_excel('{}/{}'.format(fileLocation, updateForm))
extension2022 = pd.read_excel('{}/{}'.format(fileLocation, extension2022Form))



"""Pre-process original"""
#Trim dataframe
original = original.iloc[:, :original.columns.get_loc('Notes')+1]
original = original.drop(['Title', 'Authors', 'Institutions', 'Page count', 'Reviewer names', 'Search method', 'Source', 'Main study', 'Snowball activity', 'Notes about M1/M2 (private attribute)', 'UML diagrams', 'System domain', 'System domain type', 'System parts', 'Workspace awareness score', 'Limitations and challenges', 'Future work', 'Keywords', 'Venue', 'Venue (complete name)', 'Year', 'Publisher', 'Publication type', 'Citations (Google scholar)', 'References', 'Collaboration goals', 'Modeling purposes', 'Prescribed SE activities', 'Research method', 'Readiness level (value)', 'Readiness level (range)', 'Tool availability', 'Quality of the research', 'Notes'], axis=1)

#Fix typo in column names
original.rename(columns={'Communication mean links': 'Communication means links'}, inplace=True)

#Drop corrected columns
duplicateCols = [column for column in original.columns if '.1' in column]
originalCols = list(map(lambda x: str(x).replace('.1', '').strip(), duplicateCols))
original = original.drop(originalCols, axis=1)
for column in duplicateCols:
    original.rename(columns={column: column.replace('.1', '').strip()}, inplace=True)

#Strip every column name for safety
for column in original.columns:
    original.rename(columns={column: column.strip()}, inplace=True)

"""Pre-process extensions"""
#Clean column names
extension2021.columns= list(map(lambda x: str(x).replace('(Istvan)', '').strip(), extension2021.columns.values.tolist()))
#Drop columns not required
extension2021 = extension2021.drop(['Mnemonic name', 'Title', 'Authors', 'Institutions'], axis=1)
extension2022 = extension2022.drop(['Mnemonic name', 'Title', 'Authors', 'Institutions'], axis=1).iloc[:, 0:4]

#Join extensions
extensions = pd.merge(extension2021, extension2022, on='ID', how='outer')


"""Join extension2021 into the original"""
fullOriginal = pd.merge(original, extensions, on='ID', how='outer')



"""Pre-process merged full original"""
#Calculate number of papers
fullOriginal['Papers'] = fullOriginal['Additional papers'].map(lambda x: 1+len(re.findall(r'\[.*?\]', x)[0].split(',')) if len(re.findall(r'\[.*?\]', x))>0 else 1)
fullOriginal = fullOriginal.drop(['Additional papers'], axis=1)

#Drop obsolete columns
fullOriginal = fullOriginal.drop(['Collaboration types (lock spec)'], axis=1)

#Drop columns obsolete by duplication (_x), rename retained ones (_y)
obsoleteCols = [column for column in fullOriginal.columns if '_x' in column]
fullOriginal = fullOriginal.drop(obsoleteCols, axis=1)
retainedCols = [column for column in fullOriginal.columns if '_y' in column]
for column in retainedCols:
    fullOriginal.rename(columns={column: column.replace('_y', '').strip()}, inplace=True)

#Strip every column name for safety
for column in fullOriginal.columns:
    fullOriginal.rename(columns={column: column.strip()}, inplace=True)

    

"""Pre-process update"""
update = update.drop(['Paper ID', 'Title', 'Authors', 'Institutions', 'Page count', 'Reviewer names', 'Additional papers in the cluster', 'Source', 'Snowballing round', 'Notes about M1/M2 (private attribute)', 'UML diagrams', 'System domain', 'System domain type', 'System parts', 'Collaboration workflow', 'Unit of sync', 'External VCS means', 'Workspace awareness score', 'Limitations and challenges', 'Future work', 'Keywords', 'Venue', 'Venue (complete name)', 'Year', 'Publisher', 'Publication type', 'Citations (Google scholar)', 'References', 'Collaboration goals', 'Modeling purposes', 'Prescribed SE activities', 'Evaluation', 'Readiness level (value)', 'Readiness level (range)', 'Tool availability', 'Quality of the research', 'Notes'], axis=1)

#Rename columns
update.rename(columns={'ClusterID' : 'ID', 'Cluster mnemonic' : 'Mnemonic name', 'Cluster size' : 'Papers', 'Editor type flexibility/agility' : 'Editor type', 'Multi-views' : 'Multi-view scenarios', 'View support' : 'Multi-views', 'Language(s) custo- mization support' : 'Language(s) adaptation', 'Workflow (Ivano)' : 'Collaboration workflow', 'Conflict awareness (User)' : 'Conflict awareness - user'}, inplace=True)



"""Order columns of the original and the update"""
columnOrder =[
    'ID',
    'Mnemonic name',
    'Papers',
    'Collaboration subject',
    'Multi-views',
    'Multi-view scenarios',
    'Language-specific',
    'Language(s) adaptation',
    'Modeling framework',
    'Reuse support',
    'Validation support',
    'Editor type',
    'Client type',
    'Tool support - CLIENT',
    'Workspace awareness',
    'Roles',
    'Approach-specific stakeholders',
    'Stakeholder types',
    'Collaborating parties',
    'Collaboration types',
    'Collaboration workflow',
    'Diff/merge domain',
    'Versioning support',
    'VCS architecture',
    'Branching',
    'Model merging support',
    'Conflict detection',
    'Conflict resolution support',
    'Consistency model',
    'Conflict awareness - user',
    'Conflict mgmt approach',
    'Locking',
    'Network architecture',
    'Shared workspace',
    'Communication type',
    'Communication means - builtin',
    'Communication means - external',
    'Communication means - mixed',
    'Communication means links',
    'Design decision: discussion',
    'Design decision: session history'
]
fullOriginal = fullOriginal.reindex(columns=columnOrder)
update = update.reindex(columns=columnOrder)

"""
for column in fullOriginal.columns.values.tolist():
    print(column)
print("------")
for column in update.columns.values.tolist():
    print(column)
"""

"""Merge original and update"""
full = pd.concat([fullOriginal, update])
#full.to_excel("full.xlsx", index=False)

#Group by mnemonic
fullGrouped = full.groupby('Mnemonic name', as_index=False).agg(lambda x: ", ".join(map(str, x)))
fullGrouped = fullGrouped.reindex(columns=columnOrder)
#fullGrouped.to_excel("fullGrouped.xlsx", index=False)

#Retain earlier ID
fullGrouped['ID'] = fullGrouped['ID'].map(lambda x: x.split(',')[0])
#Sum papers
fullGrouped['Papers'] = fullGrouped['Papers'].map(lambda x: sum(list(map(int, x.split(',')))))


#Remove no words
noWords = ['NO', 'N_I', 'NAN', '-']
def removeNoWords(l):
    l = [l.remove(nw) for nw in noWords if nw in l]

#Remove synonyms
synonyms = {
    'PROJECTIVE' : 'PROJ',
    'SYNTHETIC' : 'SYN',
    'TECH' : 'TECHN'
}
def removeSynonyms(l):
    for preferred, synonym in synonyms.items():
        indexes = [l.index(x) for x in l if synonym==x]
        for i in indexes:
            l[i] = preferred

#Remove exact duplicates
def removeDuplicates(l):
    l = list(dict.fromkeys(l))
    return l
    
#Transformation = removeSynonyms + removeDuplicates + removeNoWords
def transform(element):
    l = [y.upper().strip() for y in element.split(',')]
    removeSynonyms(l)
    l = removeDuplicates(l)
    removeNoWords(l)
    return l


skip = ['Papers']
for column in fullGrouped.columns.values.tolist(): #simplyFilterDuplicates:
    if column not in skip:
        fullGrouped[column] = fullGrouped[column].map(lambda x: ", ".join(transform(x)))

"""Persist data"""
fileName = 'data-preprocessed'
fullGrouped.to_excel('{}/{}.xlsx'.format(fileLocation, fileName), index=False)
fullGrouped.to_csv('{}/{}.csv'.format(fileLocation, fileName), sep=";", index=False)