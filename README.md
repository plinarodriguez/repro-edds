# ABioM Computational Modeling Research Project 

Welcome to the top-level directory of my graduate research project titled Agile for Biomedical Modeling (ABioM), which focuses on developing and assessing computational models for medical device applications. This project provides essential resources for conducting credibility assessments of two computational models designed for medical device applications. Included are datasets, Python scripts, Jupyter notebooks, and figures crucial for evaluating the models' credibility. It's important to note that the data and analysis provided here specifically focus on post-processing data obtained from computational model predictions.

## Viewing Jupyter Notebooks

Jupyter Notebook files (.ipynb) included in this repository can be viewed directly on the GitHub browser window. Simply navigate to the desired notebook file and click on it to view its contents.

## Overview

This research aims to develop and evaluate computational models for a medical device, the Electronic Drug Delivery System (EDDS), within a specified context of use and for risk-informed decision making. The computational modeling is broken down by system complexity into two components: the Airflow Model (AFM) and the Heated Airflow Model (HAFM), both of which are essential for comprehending, predicting, and establishing trust in the computational model's reliability under medical device operating conditions. The primary objective of these efforts is to compile computational evidence to ensure the reliability of computational predictions for risk-informed decision-making, emphasizing reproducibility and transparency. To achieve this, the repository encompasses post-processing data, Jupyter notebooks for conducting credibility assessments (Verification, Validation, and Uncertainty Quantification (VVUQ)), Python scripts for calculations and data processing, and comprehensive reports summarizing all analyses.

## References

To ensure that the computational evidence aligns with the highest standards for risk-informed decision-making, we adhered to the following guidelines and standards:

- **FDA Guidelines**: We follow the guidelines provided by the Food and Drug Administration (FDA) for computational modeling in medical device development.This includes the FDA 2016 Guidance Document and the ASME V&V 40 Standard which is FDA Recognized. 
    - [Reporting of Computational Modeling Studies in Medical Device Submissions](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/reporting-computational-modeling-studies-medical-device-submissions)
    - [Recognized Consensus Standards: Medical Devices](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfstandards/detail.cfm?standard__identification_no=38534)
- **ASME VV Standards**: We adhere to the Verification and Validation (V&V) standards outlined by the American Society of Mechanical Engineers (ASME).
    - [V&V 40: Assessing Credibility of Computational Modeling through Verification and Validation: Application to Medical Devices](https://www.asme.org/codes-standards/find-codes-standards/v-v-40-assessing-credibility-computational-modeling-verification-validation-application-medical-devices)
    - [Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer](https://www.asme.org/codes-standards/find-codes-standards/v-v-20-standard-verification-validation-computational-fluid-dynamics-heat-transfer#:~:text=The%20objective%20of%20ASME%20V%20V,at%20a%20specified%20validation%20point.)

## Acronyms

- **ABioM**: Agile Biomedical Modeling, the project name
- **AFM_ANSYS**: Airflow Model developed with ANSYS commercial software
- **HAFM_ANSYS**: Heated Airflow Model developed with ANSYS commercial software
- **EDDS**: Electronic Drug Delivery System
- **VVUQ**: Verification, Validation, and Uncertainty Quantification
- **ASME V&V**: American Society of Mechanical Engineers (ASME) Verification and Validation (V&V)
- **FDA**: Food and Drug Administration 

## Research Question

Our primary research question is:

"How can a collection of computational evidence and artifacts be assembled to support risk-informed decision-making in the medical device industry, while ensuring transparency, reproducibility, and collaboration to build computational credibility and trust?"

## Credibility Goals

### Medical Device 
The Electronic Drug Delivery System (EDDS) consists of several main components: an inlet pipe, an atomizer with 12 heating coils, a connecting pipe to the mouthpiece, and the mouthpiece itself.

EDDS Operation: Fluid enters the device through the inlet pipe and travels through the atomizer, where power is applied to 12 heating coils. As the fluid passes through the atomizer, it is heated, and then flows through the connecting pipe to the mouthpiece. Finally, the heated fluid exits the device through the mouthpiece.

### Credibility Question of Interest
"What are the bioeffects arising from deposition of potential chemicals generated by EDDS onto the oral mucosa?"

### Context of Use

The CFD and heat transfer model will characterize the flow field and temperature distribution of the flow in representative mouth cavities (exiting the mouthpiece) of an EDDS users. The flow field and thermal characteristics translate into bioeffects onto the oral mucosa based on data from the literature (i.e. rate of deposition depends on the flow field and temperature).

### Risk Assessment
Model Risk: less than moderate but more than low
- Model influence: low
- Decision consequence: moderate

Note the potential for cell damage that can result in more absorption of chemicals. 
