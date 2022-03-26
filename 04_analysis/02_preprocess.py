import pandas as pd
import re

fileLocation = '../03_data'
data = pd.read_excel('{}/data.xlsx'.format(fileLocation))

analysisData = data.iloc[:,1:13]

def preprocess():
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
    for country in countries:
        analysisData.iloc[:, 3] = analysisData.iloc[:, 3].map(lambda x: country if re.search(country, str(x), re.IGNORECASE) else x)
    for original, replacement in replacements.items():
        analysisData.iloc[:, 3] = analysisData.iloc[:, 3].map(lambda x: replacement if re.search(original, str(x), re.IGNORECASE) else x)
        
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
    sectors = ['Automotive']
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
    for sector in sectors:
        analysisData.iloc[:, 6] = analysisData.iloc[:, 6].map(lambda x: sector if re.search(sector, str(x), re.IGNORECASE) else x)
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
    replacements = {
        'enterprise architect' : 'Enterprise Architect',
        'Entreprise arc' : 'Enterprise Architect',
        'MagidDraw' : 'MagicDraw',
        'MagicDraw with Teamwork Cloud' : 'MagicDraw, Teamwork Cloud',
        'MagicDraw / Cameo' : 'MagicDraw, Cameo'
        }
    fullReplace = {
        'Enterprise Architect (Sparx)' : 'Enterprise Architect',
        'UAModeler + Sublime Text + Visio' : 'UAModeler, Sublime Text, Visio',
        'Proprietary (vendor), ISA-88, ISA-95' : 'Proprietary',
        'proprietery technology' : 'Proprietary'
    }
    for original, replacement in replacements.items():
        analysisData.iloc[:, 8] = analysisData.iloc[:, 8].map(lambda x: str(x).strip().replace(original, replacement) if re.search(original, str(x), re.IGNORECASE) else x.strip())
    for original, replacement in fullReplace.items():
        analysisData.iloc[:, 8] = analysisData.iloc[:, 8].map(lambda x: replacement if x.strip()==original else x.strip())
    
    #Column 9: Project length (nominal, category). Preprocessing: nothing.
    
    #Column 10: Project size. Preprocessing: Nothing - data is too diverse.
    
    #Column 11: Model size. Preprocessing: Retain short label (small, medium, large)
    analysisData.iloc[:, 11] = analysisData.iloc[:, 11].map(lambda x: str(x).split(' ')[0])

preprocess()

analysisData.columns=['background', 'experience', 'role', 'location', 'companySize', 'sector', 'domain', 'collaborators', 'tools', 'projectLength', 'projectSize', 'modelSize']

print(analysisData)

#Save as CSV
analysisData.to_csv('{}/data-preprocessed.csv'.format(fileLocation), sep=';', encoding='utf-8', index=False)

