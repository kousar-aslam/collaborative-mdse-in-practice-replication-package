# Replication package
### for the paper _Collaborative Model-Driven Software Engineering -- A Systematic Survey of Practices and Needs in Industry_.

The full dataset, analysis scripts, raw results, and transcripts of the focus group discussions are available below.

Install Python requirements before running the scripts by running `pip install -r requirements.txt` from the root folder.

### Transcripts
* `/01_transcripts` - Anonymized transcripts of the focus group sessions.

### Classification framework
* `/02_classification_framework` - Classification framework and definitions of terms.

### Questionnaire
* `/03_questionnaire`
   * `Questionnaire.pdf` - The questionnaire used in the online survey.
   * `Collaborative Model-Driven Software Engineering - An Overview.pdf` - The overview the participants were provided with.

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

### Analysis scripts

* `/05_analysis` - Analysis scripts.
   * `/01_analysis_participant_demographics.py` - Charts of some demographic and descriptive statistics of the participants, their companies, the tools used, model sizes, etc.
   * `/02_analysis_rq1_rq2_rq3.R` - .R script producing PDF, Excel, LaTeX and .txt reports into folder `/06_output`.

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

### References
[1] Franzago, M., Di Ruscio, D., Malavolta, I., & Muccini, H. (2017). Collaborative model-driven software engineering: a classification framework and a research map. IEEE Transactions on Software Engineering, 44(12), 1146-1175.

[2] David, I., Aslam, K., Faridmoayer, S., Malavolta, I., Syriani, E., & Lago, P. (2021, October). Collaborative model-driven software engineering: a systematic update. In 2021 ACM/IEEE 24th International Conference on Model Driven Engineering Languages and Systems (MODELS) (pp. 273-284). IEEE.
