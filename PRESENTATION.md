# Early Diabetes Prediction System
## Cloud Computing & DevOps with AI/ML - Presentation
**Student:** Grace Kihonge | **Year:** 2026

---

## Slide 1: The Problem

> 537 million adults globally live with diabetes.
> Most cases are diagnosed too late.

**The Question:**
Can we use machine learning to predict diabetes risk
early enough to save lives?

**Our Answer:** Yes - using TensorFlow + AWS SageMaker.

---

## Slide 2: Our Solution

A cloud-based AI system that:
- Takes 8 patient health measurements as input
- Predicts diabetes risk in real time
- Returns a probability score + confidence level
- Is accessible via a REST API endpoint on AWS

**Example:**
- Input: Glucose=148, BMI=33.6, Age=50
- Output: **"Diabetic - 82% confidence"**

---

## Slide 3: The Dataset

**Pima Indians Diabetes Database**
- 768 patients, 8 health features
- Source: UCI Machine Learning Repository
- Target: 0 = Not Diabetic, 1 = Diabetic

| Feature | Example Value |
|---------|--------------|
| Glucose | 148 mg/dL |
| BMI | 33.6 |
| Age | 50 years |
| Blood Pressure | 72 mm Hg |
| Insulin | 80 mU/L |

---

## Slide 4: Cloud ML Pipeline

```
Raw Data → S3 Storage
       ↓
SageMaker Processing → Clean & split data
       ↓
SageMaker Training → TensorFlow model
       ↓
Model Registry → Version & approve
       ↓
SageMaker Endpoint → Live REST API
       ↓
Hospital App → Real-time predictions
```

**Monitoring:** CloudWatch + SageMaker Model Monitor

---

## Slide 5: Model Architecture

**TensorFlow Neural Network**

```
Input Layer      →  8 patient features
Dense Layer 1    →  32 neurons (ReLU)
Dropout          →  20% (prevents overfitting)
Dense Layer 2    →  16 neurons (ReLU)
Dropout          →  20%
Output Layer     →  1 neuron (Sigmoid → probability)
```

- Total parameters: 833
- Optimizer: Adam
- Loss: Binary Crossentropy
- Training: 100 epochs, batch size 32

---

## Slide 6: Results

| Metric | Score | Meaning |
|--------|-------|---------|
| Test Accuracy | 74% | 74 in 100 patients correctly predicted |
| ROC-AUC | 0.82 | Strong - above 0.80 is excellent for medical ML |
| F1 (Not Diabetic) | 0.81 | Very good at identifying healthy patients |
| F1 (Diabetic) | 0.61 | Decent at catching diabetic patients |

**Confusion Matrix:**
- 83 healthy patients correctly identified ✅
- 31 diabetic patients correctly identified ✅
- 17 missed diabetic cases ⚠️ (flagged for clinical follow-up)

---

## Slide 7: Training Performance

**Accuracy curve:** Both training and validation accuracy
climbed steadily and stabilized around 80% - no overfitting.

**Loss curve:** Both training and validation loss dropped
consistently across 100 epochs - healthy learning confirmed.

![Training History](training_history.png)
![Confusion Matrix](confusion_matrix.png)

---

## Slide 8: Deployment on AWS

**Live endpoint deployed on AWS SageMaker:**

- Endpoint: `diabetes-prediction-endpoint-v2`
- Instance: `ml.m5.large`
- Framework: TensorFlow 2.12

**Sample API Call:**
```json
Input:
{"instances": [[6, 148, 72, 35, 80, 33.6, 0.627, 50]]}

Output:
{"prediction": "Diabetic", "probability": 0.82, "confidence": "82.0%"}
```

---

## Slide 9: Business Impact

**Who benefits:**
- Hospitals → flag high-risk patients automatically
- Clinicians → prioritize patients for testing
- Patients → earlier diagnosis = better outcomes

**Why cloud matters:**
- Scales to thousands of predictions per day
- No local hardware needed
- Pay only for what you use on AWS
- Model monitored 24/7 via CloudWatch

**Cost of early detection vs late treatment:**
Early intervention reduces long-term diabetes
treatment costs by up to 30%.

---

## Slide 10: Conclusion

 Real-world problem identified — diabetes detection
 Public dataset sourced and cleaned
 TensorFlow neural network built and trained
 Model evaluated - ROC-AUC of 0.82
 Deployed live on AWS SageMaker
 REST API ready for hospital integration
 Full documentation on GitHub

**GitHub Repository:**
https://github.com/Grace4549/diabetes-prediction-aws-ml

---

*Cloud Computing & DevOps with AI/ML | Grace Kihonge | 2026*
