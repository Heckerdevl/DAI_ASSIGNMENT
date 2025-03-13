import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the dataset
df = pd.read_csv("insurance.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values using mean values
df['bmi'].fillna(df['bmi'].mean(), inplace=True)
df['children'].fillna(df['children'].mean(), inplace=True)
df['charges'].fillna(df['charges'].mean(), inplace=True)

# Removing outliers using IQR method
q1 = df[['age', 'bmi', 'children', 'charges']].quantile(0.25)
q3 = df[['age', 'bmi', 'children', 'charges']].quantile(0.75)
IQR = q3 - q1  # Calculate IQR

# Define Lower and Upper Bound
LB = q1 - 1.5 * IQR
UB = q3 + 1.5 * IQR

# Clip outliers instead of removing them
df[['age', 'bmi', 'children', 'charges']] = df[['age', 'bmi', 'children', 'charges']].clip(LB, UB, axis=1)

# Standardizing categorical columns
df[['sex', 'region']] = df[['sex', 'region']].apply(lambda x: x.str.strip().str.title())

# Display dataset info
print(df.info())

# Plot data
fig, axes = plt.subplots(2, 2, figsize=[12,12])

# Age Distribution
df['age'].plot(kind='hist', bins=20, edgecolor='black', ax=axes[0,0])
axes[0,1].set_xlabel('Age')
axes[0,1].set_ylabel('Count')
axes[0,1].set_title('Age Distribution')

# Charges Distribution
df['charges'].plot(kind='hist', bins=20, edgecolor='black', color='orange', ax=axes[0,1])
axes[0,0].set_xlabel('Charges')
axes[0,0].set_ylabel('Count')
axes[0,0].set_title('Charges Distribution')

# Region Wise Distribution
df['region'].value_counts().plot(kind='pie', autopct='%0.1f%%', ax=axes[1,0])
axes[1,1].set_ylabel('')  
axes[1,1].set_title('Region Wise Distribution')

# Box Plot After Outlier Removal
df['bmi'].plot(kind='box', ax=axes[1,1])
axes[1,0].set_ylabel('BMI')
axes[1,0].set_title('BMI Distribution')

# Adjust layout
plt.tight_layout(pad=3.0)
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# Show the plots
# plt.show()


# Correlation Matrix for Age, Charges and BMI
cor_matrix=df[['age','charges','bmi']].corr()
# print(cor_matrix)


fig1, axes= plt.subplots(2, 2, figsize=(12,12) )

# Scatar Plot between Charges and Age
sns.scatterplot(x=df['charges'],y=df['age'], marker= 'x', color='coral',ax=axes[0,0])
axes[0,0].set_xlabel("Charges")
axes[0,0].set_ylabel("Age")
axes[0,0].set_title("Age v/s Charges Distribution")

# Box Plot of performance score at different ages
sns.boxplot(x=df['age'],y=df['bmi'],ax=axes[0,1])
axes[0,1].set_xlabel("Age")
axes[0,1].set_ylabel("BMI Score")
axes[0,1].set_title("Age v/s BMI Score")

# Density graph of performance score at differnet salary
sns.kdeplot(x=df['charges'], y=df['bmi'], cmap="Blues", fill= True,ax=axes[1,0])
axes[1,0].set_xlabel("Charges")
axes[1,0].set_ylabel("BMI")
axes[1,0].set_title("Charges v/s BMI")

# Count of people in different department with different BMI
sns.countplot(x=df['region'], hue=df['bmi'], palette='viridis', ax=axes[1,1])
axes[1,1].set_xlabel("Region")
axes[1,1].set_ylabel("Count of People")
axes[1,1].set_title("Region-wise People Count for Different BMI Scores")

# Adjust layout
plt.tight_layout(pad=3.0)
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# Plot the data
# plt.show()


# Convert BMI into categorical bins
df['bmi_category'] = pd.cut(df['bmi'], bins=[15, 25, 30, 35, 40, 50], labels=['Underweight', 'Normal', 'Overweight', 'Obese', 'Extremely Obese'])

# Plot with categorical hue
sns.pairplot(df, hue='bmi_category', palette='viridis')

# plt.show()


# Plot heatmap
sns.heatmap(df[['age','bmi','charges']].corr(), cmap='coolwarm', annot=True)

# Add title
plt.title("Correlation Heatmap")

# Show plot
# plt.show()


# Define BMI categories
bins = [0, 18.5, 24.9, 29.9, 50]
labels = ["Underweight", "Normal", "Overweight", "Obese"]
df["bmi_category"] = pd.cut(df["bmi"], bins=bins, labels=labels)

# Create a barplot with a bigger figure size
plt.figure(figsize=(12, 6))  # Increase width and height for better fit
sns.barplot(x="region", y="charges", hue="bmi_category", data=df, palette="viridis", ci=None)

# Customize the plot
plt.title("Average Charges Across Regions for Different BMI Categories", fontsize=14)
plt.xlabel("Region", fontsize=12)
plt.ylabel("Average Charges", fontsize=12)
plt.xticks(rotation=30)  # Slight rotation for readability
plt.legend(title="BMI Category", bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout to fit everything properly
plt.tight_layout()

# Show plot
plt.show()

# Ensure BMI is categorized if it's continuous
bins = [0, 18.5, 24.9, 29.9, 50]
labels = ["Underweight", "Normal", "Overweight", "Obese"]
df["bmi_category"] = pd.cut(df["bmi"], bins=bins, labels=labels)

# Increase figure size for clarity
plt.figure(figsize=(12, 6))

# Violin plot with categorized BMI
sns.violinplot(x="bmi_category", y="age", hue="region", data=df, palette="viridis", scale="width")

# Titles and Labels
plt.title("Age Distribution Across BMI Categories and Regions", fontsize=14)
plt.xlabel("BMI Category", fontsize=12)
plt.ylabel("Age", fontsize=12)

# Adjust Legend Position
plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')

# Improve layout to fit all elements
plt.tight_layout()
plt.show()