# Airflow Model & Credibility Assessment


## Overview

This repository contains a credibility assessment and analysis for a computational model of an electronic drug delivery system, aimed at evaluating its reliability, accuracy, and validity in predicting operating conditions. The assessment encompasses various aspects, including verification and validation. In particular, this directory is focused on the simplified complexity computational model for the airflow only system using ANSYS CFX. 

## Repository Structure

The repository is structured by analysis type as follows:

- **model_experiments/**: Jupyter Notebook, scripts, data folder, and figures folder which are all necessary for visualizing the nominal and sampling simulation results as well as experiment data visualizations. This also includes an axial profile analysis, exploration of the heat transfer coefficient, geometry, and mesh details. 
- **sampling/**: Jupyter Notebook, scripts, data folder, and figures folder which are all necessary for conducting post-processing on the latin hypercube sampling data files. This includes visualizations of model input profiles.  
- **validation/**: Jupyter Notebook, scripts, data folder, and figures folder which are all necessary for conducting the validation analysis (validation metric comparison). This also includes visualizations, qualitative analysis, and sensitivity analysis. 
- **README.md**: The main README file providing an overview of the repository and guidance for users.
- **requirements.txt**: The required Python packages

## Requirements

To reproduce the credibility assessment and analysis, ensure you have the following dependencies installed:

- Python 3.8.8
- Jupyter Notebook 6.4.5
- Required Python packages (listed in `requirements.txt`)

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. **Data Preparation**:
   - Ensure that the necessary datasets are available in the `data/` directories whithin the corresponding analysis directory.
   - Preprocess the data as needed.

2. **Analysis Workflow**:
   - Navigate to the desired analysis directory.
   - Open and execute the Jupyter Notebooks in sequential order to follow the analysis workflow.
   
3. **Results Interpretation**:
   - Examine the generated visualizations in the `figures/` directory.

## Acknowledgements
This work was funded by the Department of Energy Computational Science Graduate Fellowship (DE-SC0022158).

## Contact

For inquiries or further information, please contact Paulina Rodriguez at plinarodriguez@gmail.com 

