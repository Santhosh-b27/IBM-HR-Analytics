from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

#Load the Dataset
df = pd.read_csv(r"D:\Projects\IBM HR Analytics\HR-Employee-Attrition.csv")
pd.set_option("display.max_columns", None)
print(df)

#Print the top 5 row&column of Dataset
print(df.head())

#check foe missing value
print(df.isnull().sum())

#Information
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Visualize missing values (if any) using a heatmap
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Check the distribution of the target variable
print(df['Attrition'].value_counts())

# Visualize the target variable
sns.countplot(data=df, x='Attrition', palette='Set2')
plt.title("Attrition Distribution")
plt.show()



# Identify categorical columns
categorical_columns = df.select_dtypes(include=['object']).columns
print("Categorical Columns:", categorical_columns)

# Plot bar charts for categorical variables
for col in categorical_columns:
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x=col, hue='Attrition', palette='Set2')
    plt.title(f"{col} Distribution by Attrition")
    plt.xticks(rotation=45)
    plt.show()

# Identify numerical columns
numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
print("Numerical Columns:", numerical_columns)

# Summary statistics of numerical columns
print(df[numerical_columns].describe())

# Plot histograms of numerical columns
df[numerical_columns].hist(figsize=(12, 10), bins=20, color='teal')
plt.suptitle("Histograms of Numerical Columns")
plt.show()

# Boxplots to visualize outliers in numerical columns
for col in numerical_columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df, x='Attrition', y=col, palette='Set2')
    plt.title(f"{col} by Attrition")
    plt.show()

# Correlation matrix
correlation_matrix = df[numerical_columns].corr()

# Visualize correlation using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

# Scatter plot for key relationships
sns.scatterplot(data=df, x='Age', y='MonthlyIncome', hue='Attrition', palette='Set2')
plt.title("Age vs Monthly Income by Attrition")
plt.show()

# Pair plot to visualize relationships
sns.pairplot(df[['Age', 'MonthlyIncome', 'YearsAtCompany', 'Attrition']], hue='Attrition', palette='Set2')
plt.show()




