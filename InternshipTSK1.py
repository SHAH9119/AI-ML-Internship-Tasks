# Import libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Set matplotlib backend for PyCharm (prevents blank plots)
plt.switch_backend('TkAgg')  # or 'Qt5Agg'

# Load the Iris dataset
iris = sns.load_dataset('iris')

# =================================================================
# 1. Data Inspection
# =================================================================
print("=" * 40)
print("1. Dataset Inspection")
print("=" * 40)
print("\nShape of the dataset:", iris.shape)
print("\nFirst 5 rows:\n", iris.head())
print("\nSummary statistics:\n", iris.describe())
print("\nData types and missing values:\n")
iris.info()

# =================================================================
# 2. Visualizations
# =================================================================
# Set style for all plots
sns.set(style="whitegrid")

# -----------------------------------------------------------------
# 2.1 Scatter Plot (Sepal Length vs. Width)
# -----------------------------------------------------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris, x='sepal_length', y='sepal_width', hue='species', palette="deep")
plt.title("Sepal Length vs. Sepal Width by Species", fontsize=14)
plt.xlabel("Sepal Length (cm)", fontsize=12)
plt.ylabel("Sepal Width (cm)", fontsize=12)
plt.legend(title='Species')
plt.show()

# -----------------------------------------------------------------
# 2.2 Histograms (Feature Distributions)
# -----------------------------------------------------------------
iris.hist(figsize=(12, 10), bins=15, edgecolor='black')
plt.suptitle("Distributions of Iris Dataset Features", y=1.02, fontsize=16)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------
# 2.3 Box Plots (Outlier Detection)
# -----------------------------------------------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris.drop(columns='species'), palette="Set2")
plt.title("Box Plots of Iris Features (Outlier Detection)", fontsize=14)
plt.ylabel("Measurement (cm)", fontsize=12)
plt.show()

