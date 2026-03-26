# Data Cleaning ETL Portfolio Project

This project demonstrates an end-to-end ETL data cleaning workflow built for a structured real-world dataset and sanitized for portfolio use.

The notebook and supporting modules show how raw data is loaded, inspected, cleaned, validated, deduplicated, and exported with logging and checkpointing along the way.

## What This Project Demonstrates

- Dynamic path handling
- Logging for traceability
- File discovery and read configuration
- Raw data inspection
- Column selection and structure standardization
- Field-level cleaning
- Dataset-specific validation rules
- Deduplication using completeness scoring
- Final quality review and visual reporting
- Export of cleaned data and rejected records

## Project Structure

```text
data-cleaning-etl-portfolio/
├── ETLDevProjects/
│   └── RH/
│       ├── utils/
│       │   └── path_utils.py
│       ├── extract/
│       │   └── read_settings.py
│       ├── transform/
│       │   ├── validate.py
│       │   └── rh_guardian.ipynb
│       └── load/
│           └── export_utils.py
├── README.md
├── requirements.txt
└── .gitignore
```
## Notes

This notebook was originally built around a specific structured dataset and has been sanitized for portfolio use.

The ETL framework, folder scaffolding, logging, validation flow, and deduplication strategy are reusable. However, several cleaning and validation steps remain schema-specific, so downstream field references may need to be updated when adapting the notebook to a different dataset.

---

## How to Run

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Open the notebook:

```
ETLDevProjects/RH/transform/rh_guardian.ipynb
```

3. Update the configuration section at the top of the notebook if using a different dataset or file name.  

4. Run the notebook cells from top to bottom.

## Output

### The workflow generates:
cleaned output files
rejected/garbage records
checkpoint files
logging output
a quality report visualization

## Purpose

This project was created to showcase practical data cleaning, validation, and ETL organization in a notebook-based workflow with reusable support modules.
