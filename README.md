# Employee Performance Prediction Project

## **Project Overview**
This project is designed to predict employee performance using historical HR and production data. The system helps HR managers make **data-driven decisions** regarding appraisals, promotions, training programs, and workforce optimization. The predictions are made using **Machine Learning models** trained on past employee metrics.

---

## **Internship Details**
- **Intern Name:** KANDANATHI CHITTEM BALAJI 
- **Internship Program:** SmartInternz Virtual Internship Program  
- **Role:** Machine Learning Intern  
- **Duration:** 1 SEP  – 10 OCT  

---

## **Objectives**
- Predict employee performance based on historical data.  
- Identify employees requiring performance improvement or additional training.  
- Provide actionable insights to HR teams for appraisals and promotions.  
- Optimize workforce allocation for productivity improvement.  

---

## **Dataset**
The dataset contains **1197 records** and **14 features**. Key features include:  

| Feature | Description |
|---------|-------------|
| `date` | Date of the record |
| `quarter` | Financial quarter |
| `department` | Employee department |
| `day` | Day of the week |
| `team` | Employee team |
| `targeted_productivity` | Expected productivity target |
| `SMV` | Standard Minute Value (time required per task) |
| `wip` | Work in progress (some missing values) |
| `over_time` | Hours worked beyond regular hours |
| `incentive` | Extra rewards/bonuses |
| `idle_time` | Time when employees were not productive |
| `idle_men` | Number of idle employees |
| `no_of_style_change` | Changes in product styles affecting workflow |
| `no_of_workers` | Total workers involved |
| `actual_productivity` | Actual productivity achieved (target variable) |

---

## **Data Preprocessing**
- Handled missing values (e.g., `wip` column).  
- Encoded categorical variables (`department`, `day`, `quarter`) using Label Encoding.  
- Standardized numerical features using scaling techniques.  
- Split the dataset into **training and testing sets**.  

---

## **Machine Learning Models**
- **Linear Regression**  
- **XGBOOST**  (Best Performing)
- **Random Forest Regressor**   

**Evaluation Metrics:**  
- Mean Squared Error (MSE)
- Mean absolute Error(MAE) 
- R² Score  

XGBoost gave the highest prediction accuracy.

---

## **Prediction Demo**
The system takes employee metrics as input:  
- quarter
- department
- Training hours  
- Incentives  
- SMV  
- Idle time, etc.  

It predicts the employee’s **expected performance score as (low , medium , high )**, helping HR teams make objective decisions.

---

## **Results & Insights**
- Key features affecting performance: `targeted_productivity`, `SMV`, `incentive`.  
- Provides actionable insights for HR:
  - Identifying employees needing training.  
  - Optimizing team allocation.  
  - Data-driven promotion decisions.  

---


