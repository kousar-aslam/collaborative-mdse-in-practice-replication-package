import pandas as pd
import re

dataLocation = '../04_data'

def preprocessQuestionnaireData():
    fileLocation = '{}/questionnaire'.format(dataLocation)
    data = pd.read_excel('{}/questionnaire_data.xlsx'.format(fileLocation))
    
    analysisData = data.iloc[:,1:13]
    
    #Column 0: Background (nominal, category). Preprocessing: bring similar roles to a common form.
    analysisData.iloc[:, 0] = analysisData.iloc[:, 0].map(lambda x: "Researcher" if re.search("research", str(x), re.IGNORECASE) else x)
    analysisData.iloc[:, 0] = analysisData.iloc[:, 0].map(lambda x: "Technical (STEM)" if str(x)=="Computer System Validation / GAMP5" else x)
    
    #Column 1: experience in years. Preprocessing: parse integers from free-text field.
    analysisData.iloc[:, 1] = analysisData.iloc[:, 1].map(lambda x: re.findall("[0-9]+", str(x))[0])
    
    #Column 2: Role (nominal, category). Preprocessing: bring similar roles to a common form.
    roles = ['Architect', 'Director', 'Research']
    replacements = {
        'Principal Software Engineer' : 'Senior Software Eng.',
        'Senior Software Developer' : 'Senior Software Eng.',
        'Senior Developer' : 'Senior Software Eng.',
        'Senior Development Engineee' : 'Senior Software Eng.',
        'Team Lead' : 'Team/Tech Lead',
        'Group Lead' : 'Team/Tech Lead',
        'Head of' : 'Team/Tech Lead',
        'Team Leader' : 'Team/Tech Lead',
        'Engineering Lead' : 'Team/Tech Lead',
        'Workflow Technology Lead' : 'Team/Tech Lead',
        'Scientist' : 'Research',
        'President' : 'CEO'
    }
    for role in roles:
        analysisData.iloc[:, 2] = analysisData.iloc[:, 2].map(lambda x: role if re.search(role, str(x), re.IGNORECASE) else x)
    for original, replacement in replacements.items():
        analysisData.iloc[:, 2] = analysisData.iloc[:, 2].map(lambda x: replacement if re.search(original, str(x), re.IGNORECASE) else x)
    
    #Column 3: Location (nominal, category). Preprocessing: bring similar roles to a common form.
    countries = ['Austria', 'Belgium', 'Canada', 'Finland', 'France', 'Germany', 'Hungary', 'India', 'Italy', 'Japan', 'Luxembourg', 'Netherlands', 'Sweden', 'Switzerland', 'USA']
    replacements = {
        'EU mainly' : 'Across Europe',
        'Tokyo' : 'Japan',
        'United States' : 'USA',
        'U.S.' : 'USA'
    }
    fullReplace = {
        'NL' : 'Netherlands'
    }
    for country in countries:
        analysisData.iloc[:, 3] = analysisData.iloc[:, 3].map(lambda x: country if re.search(country, str(x), re.IGNORECASE) else x)
    for original, replacement in replacements.items():
        analysisData.iloc[:, 3] = analysisData.iloc[:, 3].map(lambda x: replacement if re.search(original, str(x), re.IGNORECASE) else x)
    for original, replacement in fullReplace.items():
        analysisData.iloc[:, 3] = analysisData.iloc[:, 3].map(lambda x: replacement if str(x).strip()==original else str(x).strip())
        
    #Column 4: Company size (nominal, category). Preprocessing: nothing.
    
    #Column 5: Primary sector (nominal, category). Preprocessing: bring similar roles to a common form.
    sectors = ['Automotive', 'Consulting', 'Safety-critical systems', 'Automation', 'Machine learning']
    replacements = {
        'Telecoms' : 'Telecom',
        'Telecom.' : 'Telecom',
        'IT Consultancy' : 'Consulting',
        'safety-critical system engineering' : 'Safety-crit. sys.',
        'Communication network design' : 'Networks',
        'IT Services' : 'IT',
        'Information technology' : 'IT',
        'Research' : 'R&D',
        'Model-based design' : 'MBSE',
        'Software development' : 'Software',
        'Software and Services' : 'Software'
    }
    for sector in sectors:
        analysisData.iloc[:, 5] = analysisData.iloc[:, 5].map(lambda x: sector if re.search(sector, str(x), re.IGNORECASE) else x)
    for original, replacement in replacements.items():
        analysisData.iloc[:, 5] = analysisData.iloc[:, 5].map(lambda x: replacement if re.search(original, str(x), re.IGNORECASE) else x)
        
    #Column 6: Primary application domain (nominal, category). Preprocessing: bring similar roles to a common form.
    domains = ['Automotive']
    replacements = {
        'Automative' : 'Automotive',
        'Robot' : 'Robotics',
        'Connected car' : 'Automotive',
        'Medical' : 'Healthcare',
        'Health' : 'Healthcare',
        'driving' : 'Automotive',
        'Communication' : 'Telecom',
        'BFSI' : 'Finance',
        'Software modelling tool' : 'Software tools',
        'Software publisher' : 'Software tools'
    }
    for domain in domains:
        analysisData.iloc[:, 6] = analysisData.iloc[:, 6].map(lambda x: domain if re.search(domain, str(x), re.IGNORECASE) else x)
    for original, replacement in replacements.items():
        analysisData.iloc[:, 6] = analysisData.iloc[:, 6].map(lambda x: replacement if re.search(original, str(x), re.IGNORECASE) else x)

    #Column 7: collaborating users. Preprocessing: parse integers from free-text field.
    replacements = {
        '1-5' : '5',
        '30-50' : '50',
        '30 in project, 500 in business' : '500'
        }
    for original, replacement in replacements.items():
        analysisData.iloc[:, 7] = analysisData.iloc[:, 7].map(lambda x: replacement if re.search(original, str(x), re.IGNORECASE) else x)
    analysisData.iloc[:, 7] = analysisData.iloc[:, 7].map(lambda x: re.findall("[0-9]+", str(x))[0])
    
    #Column 8: Tools (nominal, category). Preprocessing: split comma-separated values, bring similar roles to a common form.
    fullReplace = {
        'Enterprise Architect (Sparx)' : 'Enterprise Architect',
        'UAModeler + Sublime Text + Visio' : 'UAModeler, Sublime Text, Visio',
        'Proprietary (vendor), ISA-88, ISA-95' : 'Proprietary',
        'proprietery technology' : 'Proprietary',
        'Enterprise Architect + home-grown AUTOSAR tool' : 'Enterprise Architect, Custom AUTOSAR tool'
    }
    replacements = {
        'enterprise architect' : 'Enterprise Architect',
        'Entreprise arc' : 'Enterprise Architect',
        'MagidDraw' : 'MagicDraw',
        'MagicDraw with Teamwork Cloud' : 'MagicDraw, Teamwork Cloud',
        'MagicDraw / Cameo' : 'MagicDraw, Cameo',
        'Teanwork Cloud' : 'Teamwork Cloud',
        'Custom AUTOSAR tool' : 'Custom tool',
        'Homegrown MDSD platform' : 'Custom tool',
        'Custom platform' : 'Custom tool'
        }
    for original, replacement in fullReplace.items():
        analysisData.iloc[:, 8] = analysisData.iloc[:, 8].map(lambda x: replacement if x.strip()==original else x.strip())
    for original, replacement in replacements.items():
        analysisData.iloc[:, 8] = analysisData.iloc[:, 8].map(lambda x: str(x).strip().replace(original, replacement) if re.search(original, str(x), re.IGNORECASE) else x.strip())
    
    #Column 9: Project length (nominal, category). Preprocessing: nothing.
    
    #Column 10: Project size. Preprocessing: Nothing - data is too diverse.
    
    #Column 11: Model size. Preprocessing: Retain short label (small, medium, large)
    analysisData.iloc[:, 11] = analysisData.iloc[:, 11].map(lambda x: str(x).split(' ')[0])

    analysisData.columns=['background', 'experience', 'role', 'location', 'companySize', 'sector', 'domain', 'collaborators', 'tools', 'projectLength', 'projectSize', 'modelSize']

    #Save analysis data as CSV for the Demographics analysis
    analysisData.to_csv('{}/demographics_data.csv'.format(dataLocation), sep=';', encoding='utf-8', index=False)
    
    #Save full data file as CSV for the R analysis
    data.to_csv('{}/questionnaire_data.csv'.format(dataLocation), sep=';', encoding='utf-8', index=False)


def prepareStudiesData():
    fileLocation = '{}/studies'.format(dataLocation)
    original = pd.read_excel('{}/01_original_2016.xlsx'.format(fileLocation))
    extension2021 = pd.read_excel('{}/02_extension_to_orignial_2021.xlsx'.format(fileLocation))
    update = pd.read_excel('{}/03_update_2021.xlsx'.format(fileLocation))
    extension2022 = pd.read_excel('{}/04_extension_to_original_2022.xlsx'.format(fileLocation))

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
    fileName = 'studies_data'
    fullGrouped.to_excel('{}/{}.xlsx'.format(fileLocation, fileName), index=False)
    
def occurrences(df, column, pattern=None):
    if pattern:
        return int(df[column].str.count(pattern).sum())
    else:
        return df[column].count()
    
def preprocessStudiesData():
    data = pd.read_excel('{}/studies/studies_data.xlsx'.format(dataLocation))
    
    features = {}
    
    ################################################################################
    """MODEL MANAGEMENT"""
    
    """Models and languages"""
    #Collaboration at the model level
    features['collab-model'] = occurrences(data, 'Collaboration subject', 'M1')
    #Collaboration at the metamodel level
    features['collab-metamodel'] = occurrences(data, 'Collaboration subject', 'M3|M2')
    #Multi-view modeling (e.g. different views for different stakeholders)
    features['mvm'] = occurrences(data, 'Multi-view scenarios', 'MULTI-VIEW')
    #Import of an external language into the modeling environment
    features['import'] = occurrences(data, 'Language(s) adaptation', 'IMPORT')
    
    """Model manipulation"""
    #Model validation
    features['validation'] = occurrences(data, 'Validation support')
    
    """Editors and modeling environments"""
    #Visual editors
    features['editor-visual'] = occurrences(data, 'Editor type', 'GRA')
    #Textual editors
    features['editor-textual'] = occurrences(data, 'Editor type', 'TEX')
    #Tabular editors
    features['editor-tab'] = occurrences(data, 'Editor type', 'TAB')
    #Tree-based editors
    features['editor-tree'] = occurrences(data, 'Editor type', 'TREE')
    #Sketch-based editors
    features['editor-sketch'] = occurrences(data, 'Editor type', 'SKE')
    #Editors supporting multiple types of notations
    features['editor-multi'] = occurrences(data, 'Editor type', ',')
    #Desktop-based modeling environments
    features['device-desktop'] = occurrences(data, 'Client type', 'DESKTOP')
    #Web-based modeling environments
    features['device-web'] = occurrences(data, 'Client type', 'BROWSER')
    #Mobile device based modeling environments
    features['device-mobile'] = occurrences(data, 'Client type', 'MOBILE')
    
    ################################################################################
    """COLLABORATION"""
    """Stakeholder management & access control"""
    #User presence visualization
    features['user-presence'] = occurrences(data, 'Workspace awareness', 'USERS | UPED | HSE')

    """Collaboration dynamics"""
    features['human-machine-collab'] = occurrences(data, 'Collaborating parties', 'HUMAN-MACHINE')
    
    """Versioning"""
    #Internal versioning support
    features['versioning-internal'] = occurrences(data, 'Versioning support', 'INTERNAL')
    #Model differencing based on the modeling language, not on the file contents
    features['versioning-models'] = occurrences(data, 'Versioning support', 'MODELS')
    #Model differencing
    features['diff'] = occurrences(data, 'Diff/merge domain')
    #Model merging
    features['merge'] = occurrences(data, 'Model merging support', 'YES')
    #Version branching
    features['branching'] = occurrences(data, 'Branching')
    
    """Conflicts and consistency"""
    #Locking
    features['locking'] = occurrences(data, 'Locking')


    
    ################################################################################
    """COMMUNICATION"""
    
    
    print(features)
    
#preprocessQuestionnaireData()
#prepareStudiesData()    
preprocessStudiesData()


































