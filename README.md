# Diabetes Prediction with TensorFlow on AWS SageMaker

## Project Overview
A machine learning classification model that predicts diabetes risk 
based on patient health indicators, deployed on AWS SageMaker as a 
real-time REST API endpoint.

## Problem Statement
Early diabetes detection improves patient outcomes and reduces 
healthcare costs. This model predicts whether a patient is likely 
diabetic based on 8 diagnostic health measurements.

## Dataset
- **Source:** Pima Indians Diabetes Database (UCI / Kaggle)
- **Size:** 768 patients, 9 features
- **Target:** Binary classification (0 = Not Diabetic, 1 = Diabetic)

## Model Architecture
- Framework: TensorFlow 2.18
- Type: Neural Network (Sequential)
- Layers: Input(8) → Dense(32, ReLU) → Dropout(0.2) → Dense(16, ReLU) → Dropout(0.2) → Dense(1, Sigmoid)
- Total parameters: 833

## Results
| Metric | Score |
|--------|-------|
| Test Accuracy | 74.0% |
| ROC-AUC | 0.82 |
| F1 (Not Diabetic) | 0.81 |
| F1 (Diabetic) | 0.61 |

## Cloud Architecture
- **Storage:** AWS S3 (dataset + model artifacts)
- **Training:** AWS SageMaker Training
- **Deployment:** AWS SageMaker Endpoint (ml.t2.medium)
- **Monitoring:** AWS CloudWatch + SageMaker Model Monitor

## Project Structure
diabetes-prediction-aws-ml/
├── diabetes_prediction.ipynb  # Main notebook
├── diabetes.csv               # Dataset
├── code/
│   └── inference.py           # SageMaker inference script
├── training_history.png       # Accuracy & loss curves
├── confusion_matrix.png       # Confusion matrix
└── README.md                  # This file

## How to Run
1. Clone this repository
2. Upload diabetes.csv to your AWS S3 bucket
3. Open diabetes_prediction.ipynb in AWS SageMaker Studio
4. Run all cells in order

## Author
Grace Kihonge
Cloud Computing & DevOps with AI/ML Assessment — 2026
