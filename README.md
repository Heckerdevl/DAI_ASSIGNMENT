## 📌 Overview of the Dataset
- Contains records related to **medical insurance costs** and **demographic attributes**.  
- **Key attributes include:**  
  - **Age (years)** – Age of the individual.  
  - **Sex (Male/Female)** – Gender of the individual.  
  - **BMI (Body Mass Index)** – A measure of body fat.  
  - **Children** – Number of children the individual has.  
  - **Smoker (Yes/No)** – Indicates whether the person is a smoker.  
  - **Region** – Geographic location (Southwest, Southeast, Northwest, Northeast).  
  - **Charges (USD)** – Total medical insurance cost.  
- Useful for **analyzing healthcare expenses** and **predictive modeling** in insurance cost estimation.  

---

## 📊 Data Check
✔ **Missing Values:**  
  - **BMI** → 12 missing values  
  - **Charges** → 5 missing values  

✔ **Duplicates:**  
  - Only **1 duplicate** found  

✔ **Data Types:**  
  - **Integer:** `Age`, `Children`  
  - **Float:** `BMI`, `Charges`  
  - **Categorical (Object):** `Sex`, `Smoker`, `Region`  

---

## 📈 Univariate Analysis
- Majority of people are **below 20 years old**.  
- Most individuals have **medical charges below $5000**.  
- The **Southeast** region has the highest number of people.  

---

## 📊 Bivariate Analysis
- **Older individuals** tend to have **higher medical costs**.  
- **BMI remains relatively constant** across ages but contains **outliers**.  
- **Higher BMI** is linked to **higher medical charges**.  
- **BMI distribution** is similar across all **regions**.  

---

## 📉 Multivariate Analysis
✔ **Pair Plot** – Shows relationships between numerical variables.  
✔ **Heatmap** – Highlights **correlations** between features.  
✔ **Grouped Bar Chart** – Shows **salary variations across categories**.  
✔ **Violin Plot** – Demonstrates **age distribution variations**.  
