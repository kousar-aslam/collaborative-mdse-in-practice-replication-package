# Replication package
### for the paper _Collaborative Model-Driven Software Engineering: Practices and Needs in Industry_.

The full dataset, analysis scripts, raw results, and transcripts of the focus group discussions are available below.

### Transcripts
* `/01_transcripts` -  Anonymized transcripts of the focus group sessions.


### Questionnaire
* `/02_questionnaire`
   * `questionnaire.pdf` - The questionnaire used in the online survey.
   * `Collaborative Model-Driven Software Engineering - An Overview.pdf` - The overview the participants were provided with.

### Data

* `/03_data` - Data.
   * `/latest` - Raw data in `.xlsx` and `.csv`.

### Analysis scripts

* `/04_analysis` - Analysis scripts.
   * `/01_prepare.py` - Creates a `/03_data/data.csv` from the questionnaire spreadsheet downloaded as an Excel.
   * `/02_preprocess.py` - Takes the relevant demographic columns from the full data file, cleans them up by merging similar concepts, cleaning up numeric data, and cleaning up comma-separated values. Exports the clean data into `/03_data/data-preprocessed.csv`.
   * `/03_analysis.py` - Analysis script producing descriptive demographic charts into folder `/05_output/descriptive`. Input: `/03_data/data-preprocessed.csv`.
   * `/likert.r` - .R script producing PDF, Excel, LaTeX and .txt reports into folder `/05_output`. Input: `/03_data/data.csv`.

Install Python requirements before running the scripts by running `pip install -r requirements.txt`.

Upon running the `/likert.r` script, the following directory structure is produced. (New runs of the script will remove the previously generated folders.)
* `/05_output`
   * `/aggregated` - Aggregated descriptive statistics of the three dimensions.
      * `/xlsx/Aggregated.xlsx` - Adoption and needs aggregated over every feature group, in an Excel table for allowing further inspection and exploration.
   * `/likert` - Likert charts in PDF files with the adoption-need pairs of feature groups charted next to each other.
   * `/tables-latex` - Adoption and needs for every category, in LaTeX tables.
      * `/aggregated` - Adoption and needs aggregated over every feature group, ordered by the different metrics, in LaTeX tables.
   * `/tables-txt` - Adoption and needs for every feature group, in .txt files.

Upon running the `/03_analysis.py` script, the following directory structure is produced.
* `/05_output`
   * `/descriptive` - Charts of some descriptive statistics of the participants, their companies, the tools used, model sizes, etc.
