# Telco Customer Churn Prediction and AutoAI Deployment
 ## Project Overview
This project focuses on developing a machine learning model to predict the likelihood of customer churn (attrition) within a telecommunications company. To accelerate model development and optimization, the project leveraged the AutoAI capability within the IBM watsonx.ai platform. The final objective was to deploy the chosen model as a REST API service for real-time predictions in a production environment.

## Key Objectives
Model Development: Create a high-accuracy classification model for predicting the binary Churn outcome.
Automation: Utilize AutoAI to automatically discover the best algorithms, feature engineering steps, and hyperparameter settings.
Production Deployment: Publish the superior model as an Online API Endpoint, making it consumable by external business applications.

 ## Dataset and Preliminary Analysis
Dataset: The project utilizes the industry-standard Telco Customer Churn Data set.
Features: Includes over 20 columns such as customerID, gender, tenure, Contract, MonthlyCharges, and TotalCharges.
Target Variable: Churn (Yes/No).
# Core Findings (Model Importance)
The model identified several high-impact drivers of churn:
Contract Type: Customers on Month-to-month contracts show the highest risk of attrition compared to long-term commitments.
Tenure: Customers with shorter tenure are significantly more likely to churn.
Service Usage: Lack of complementary services (e.g., Online Security and Tech Support) increases churn probability.

 ## Model Training: Automation with AutoAI
The AutoAI feature was central to the project, automating the entire model selection and optimization process.
Detail
Description
Platform
IBM watsonx.ai
Experiment Type
Binary Classification
Selected Pipeline
Pipeline 2
Core Algorithm
Optimized XGBoost Classifier
Final Accuracy
~80.5%

Pipeline 2 was chosen as the best-performing model, demonstrating superior accuracy and robustness after undergoing automated preprocessing (handling missing data, encoding categorical variables, and advanced feature engineering).
 ## Technical Documentation
Detailed performance metrics, including the ROC AUC, F1 Score, Confusion Matrix, and Feature Importance for the selected model, are available here:
docs/Pipeline_2_Details.pdf

# Model Deployment and API Publication
The final XGBoost model was transitioned from the development environment to a live production state.
Promotion: The best model was promoted to a dedicated Deployment Space.
Deployment Type: Published as an Online Deployment API service (churnapi).
Access: Real-time predictions are accessed via the Public Endpoint using a valid IBM Cloud IAM API Key for authentication.

## API Integration and Final Result
The API integration uses native Python and the requests library to authenticate, structure the input data, and request a prediction.
src/predict_churn.py
This Python script successfully handles IAM token retrieval and sends the scoring payload.
Scoring Scenario:
