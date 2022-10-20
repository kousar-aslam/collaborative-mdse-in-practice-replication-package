# Replication package
### for the paper _Collaborative Model-Driven Software Engineering – A Systematic Survey of Practices and Needs in Industry_.

The full dataset, analysis scripts, raw results, and transcripts of the focus group discussions are available below.

Install Python requirements before running the scripts by running `pip install -r requirements.txt` from the root folder.

### Transcripts
* `/01_transcripts` – Anonymized transcripts of the focus group sessions.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09&color=00ff00) Added warnings in a README in the folder.

### Classification framework
* `/02_classification_framework` – Classification framework and definitions of terms.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09&color=00ff00) Updated in the Overleaf project and added a new PDF here.

### Questionnaire
* `/03_questionnaire`
   * `Questionnaire.pdf` – The questionnaire used in the online survey.
   * `Collaborative Model-Driven Software Engineering – An Overview.pdf` – The overview the participants were provided with.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09&color=00ff00) Added warnings in a README in the folder.

### Data

* `/04_data` – Raw data and data preparation scripts.
   * `/questionnaire` – Raw data in `.xlsx` with the sensitive information removed.
   * `/studies` – Data collected from the replication packages of the systematic mapping studies [1] and [2].
      *  `/01_original_2016.xlsx` – Original data from [1].
      *  `/02_extension_to_orignial_2021.xlsx` – Extension to `01_original_2016.xlsx` collected in [2].
      *  `/03_update_2021.xlsx` – Original data from [2] augmenting the classification framework of [1] with new categories.
      *  `/04_extension_to_original_2022.xlsx` – Extracted data for the current study. These categories were introduced in [2] but were not extracted for [1] retrospectively.
   * `00_remove_sensitive_information.py` – Removes sensitive information from `questionnaire/questionnaire_data_raw.xlsx` and saves the clean data in `questionnaire/questionnaire_data.xlsx`. (The `questionnaire/questionnaire_data_raw.xlsx` file is removed from the final public package.)
   * `01_prepare_data.py` – Pre-processes questionnaire data for the analysis of demographics (and outputs `demographics_data.csv`) and for the analysis of the RQs (and outputs `questionnaire_data.csv`). Consolidates data from the studies (and outputs `studies/studies_data.xlsx`). Pre-processes consolidated studies data for RQ4 (and outputs `studies_data.csv`).
   * `demographics_data.csv` – Data file containing the demographics of participants.
   * `questionnaire_data.csv` – Data file containing pre-processed and cleaned questionnaire data.
   * `studies_data.csv` – Data file containing data about academic output.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09&color=00ff00)

### Analysis scripts

* `/05_analysis` – Analysis scripts.
   * `01_analysis_participant_demographics.py` – Charts of some demographic and descriptive statistics of the participants, their companies, the tools used, model sizes, etc.
   * `02_generate_latex_tables.py` – Generates LaTeX tables used in the paper. The `/template` folder contains the LaTeX template.
   * `03_analysis_RQs.R` – .R script for analyzing the RQs. Produces Likert plots, need-adoption matrices, and Excel reports into folder `/06_output`.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09&color=00ff00)

### Results

Upon running the analysis scripts, the following directory structure is produced. (New runs of the script will remove the previously generated folders.)
* `/06_output`
   * `/aggregated` – Aggregated descriptive statistics of the three dimensions.
      * `/xlsx/Aggregated.xlsx` – Adoption and needs aggregated over every feature group, in an Excel table for allowing further inspection and exploration.
      * `/xlsx/Studies.xlsx` – Publication output and needs aggregated over every feature group, in an Excel table for allowing further inspection and exploration.
   * `/demographics` – Demographic statistics of the participants, their companies, the tools used, model sizes, etc.
   * `/likert` – Likert charts in PDF files with the adoption-need pairs of feature groups charted next to each other.
   * `/likert-annotated` – Likert charts annotated with feature labels.
   * `/tables` – LaTeX tables used in the paper.

![](https://img.shields.io/static/v1?label=&message=R2.08/R2.09&color=00ff00)

### References
[1] Franzago, M., Ruscio, D. D., Malavolta, I., & Muccini, H. (2018). Collaborative Model-Driven Software Engineering: A Classification Framework and a Research Map. In IEEE Transactions on Software Engineering (Vol. 44, Issue 12, pp. 1146–1175). Institute of Electrical and Electronics Engineers (IEEE). https://doi.org/10.1109/tse.2017.2755039

[2] David, I., Aslam, K., Faridmoayer, S., Malavolta, I., Syriani, E., & Lago, P. (2021). Collaborative Model-Driven Software Engineering: A Systematic Update. In 2021 ACM/IEEE 24th International Conference on Model Driven Engineering Languages and Systems (MODELS). 2021 ACM/IEEE 24th International Conference on Model Driven Engineering Languages and Systems (MODELS). IEEE. https://doi.org/10.1109/models50736.2021.00035
