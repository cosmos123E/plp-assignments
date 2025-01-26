import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset from sklearn
    iris_data = load_iris()
    iris_df = pd.DataFrame(
        data=iris_data.data, 
        columns=iris_data.feature_names
    )
    iris_df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

    # Display first few rows
    print("First 5 rows of the dataset:")
    print(iris_df.head())

    # Check data types and missing values
    print("\nDataset Info:")
    print(iris_df.info())

    print("\nMissing Values:")
    print(iris_df.isnull().sum())

    # No missing values in Iris dataset, but if there were:
    # iris_df = iris_df.dropna()  # or fillna() if needed

except FileNotFoundError as e:
    print(f"Error: {e}")

# Task 2: Basic Data Analysis
# Compute basic statistics
print("\nBasic Statistics:")
print(iris_df.describe())

# Grouping and computing mean
grouped_means = iris_df.groupby('species').mean()
print("\nMean values by species:")
print(grouped_means)

# Patterns or findings
print("\nInteresting Findings:")
print("Setosa has the smallest petal length and width on average, while Virginica has the largest.")

# Task 3: Data Visualization
plt.figure(figsize=(12, 10))

# Line Chart (dummy trend over time, not present in Iris, simulated for petal length)
plt.subplot(2, 2, 1)
sns.lineplot(data=iris_df.iloc[:30], x=range(30), y='petal length (cm)', label='Petal Length')
plt.title('Trend of Petal Length (Simulated)')
plt.xlabel('Index')
plt.ylabel('Petal Length (cm)')
plt.legend()

# Bar Chart
plt.subplot(2, 2, 2)
sns.barplot(x=grouped_means.index, y='petal length (cm)', data=grouped_means)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Petal Length (cm)')

# Histogram
plt.subplot(2, 2, 3)
sns.histplot(iris_df['sepal length (cm)'], kde=True, color='purple')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')

# Scatter Plot
plt.subplot(2, 2, 4)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')

plt.tight_layout()
plt.show()
