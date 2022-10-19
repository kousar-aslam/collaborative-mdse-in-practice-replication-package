# Replication package
### for the paper _Collaborative Model-Driven Software Engineering -- A Systematic Survey of Practices and Needs in Industry_.

The full dataset, analysis scripts, raw results, and transcripts of the focus group discussions are available below.

Install Python requirements before running the scripts by running `pip install -r requirements.txt` from the root folder.

### Transcripts
* `/01_transcripts` - Anonymized transcripts of the focus group sessions.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09–TODO!!!&color=ff0000) Add warnings.

### Classification framework
* `/02_classification_framework` - Classification framework and definitions of terms.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09–OK&color=00ff00) Add warnings about R2.08 and R2.09.

### Questionnaire
* `/03_questionnaire`
   * `Questionnaire.pdf` - The questionnaire used in the online survey.
   * `Collaborative Model-Driven Software Engineering - An Overview.pdf` - The overview the participants were provided with.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09–TODO!!!&color=ff0000) Add warnings.

### Data

* `/04_data` - Raw data and data preparation scripts.
   * `/questionnaire` - Raw data in `.xlsx` with the sensitive information removed.
   * `/studies` - Data collected from the replication packages of the systematic mapping studies [1] and [2].
      *  `/01_original_2016.xlsx` - Original data from [1].
      *  `/02_extension_to_orignial_2021.xlsx` - Extension to `01_original_2016.xlsx` collected in [2].
      *  `/03_update_2021.xlsx` - Original data from [2] augmenting the classification framework of [1] with new categories.
      *  `/04_extension_to_original_2022.xlsx` - Extracted data for the current study. These categories were introduced in [2] but were not extracted for [1] retrospectively.
   * `/00_remove_sensitive_information.py` - Removes sensitive information from `questionnaire/questionnaire_data_raw.xlsx` and saves the clean data in `questionnaire/questionnaire_data.xlsx`.
   * `/01_prepare_data.py` - Pre-processes questionnaire data for the analysis of demographics (and outputs `demographics_data.csv`) and for the analysis of RQ1, RQ2, RQ3 (and outputs `questionnaire_data.csv`); consolidates data from the studies (and outputs `studies/studies_data.xlsx`); pre-processes consolidated studies data for RQ3 (and outputs `studies_data.csv`).

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09–TODO!!!&color=ff0000) Introduce changes.

### Analysis scripts

* `/05_analysis` - Analysis scripts.
   * `/01_analysis_participant_demographics.py` - Charts of some demographic and descriptive statistics of the participants, their companies, the tools used, model sizes, etc.
   * `/02_analysis_rq1_rq2_rq3.R` - .R script producing PDF, Excel, LaTeX and .txt reports into folder `/06_output`.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09–TODO!!!&color=ff0000) Introduce changes.

### Results

Upon running the analysis scripts, the following directory structure is produced. (New runs of the script will remove the previously generated folders.)
* `/06_output`
   * `/aggregated` - Aggregated descriptive statistics of the three dimensions.
      * `/xlsx/Aggregated.xlsx` - Adoption and needs aggregated over every feature group, in an Excel table for allowing further inspection and exploration.
   * `/descriptive` - Demographic and descriptive statistics of the participants, their companies, the tools used, model sizes, etc.
   * `/likert` - Likert charts in PDF files with the adoption-need pairs of feature groups charted next to each other.
   * `/tables-latex` - Adoption and needs for every category, in LaTeX tables.
      * `/aggregated` - Adoption and needs aggregated over every feature group, ordered by the different metrics, in LaTeX tables.
   * `/tables-txt` - Adoption and needs for every feature group, in .txt files.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09–TODO!!!&color=ff0000) Introduce changes.

### References
[1] Franzago, M., Ruscio, D. D., Malavolta, I., & Muccini, H. (2018). Collaborative Model-Driven Software Engineering: A Classification Framework and a Research Map. In IEEE Transactions on Software Engineering (Vol. 44, Issue 12, pp. 1146–1175). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/tse.2017.2755039

[2] David, I., Aslam, K., Faridmoayer, S., Malavolta, I., Syriani, E., & Lago, P. (2021). Collaborative Model-Driven Software Engineering: A Systematic Update. In 2021 ACM/IEEE 24th International Conference on Model Driven Engineering Languages and Systems (MODELS). 2021 ACM/IEEE 24th International Conference on Model Driven Engineering Languages and Systems (MODELS). IEEE. https://doi.org/10.1109/models50736.2021.00035
