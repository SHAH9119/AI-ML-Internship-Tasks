import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# --- Step 1: Load Data ---
DATA_PATH = r"C:\Users\Syed Haider Ali\Downloads\house-prices-advanced-regression-techniques\train.csv"

try:
    data = pd.read_csv(DATA_PATH)
    print("Data loaded successfully!")
    print(f"Dataset shape: {data.shape}")
except FileNotFoundError:
    print(f"Error: File not found at {DATA_PATH}")
    print("Please download the dataset from:")
    print("https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data")
    exit()

# --- Step 2: Data Preprocessing ---
# Handle missing values
numeric_cols = data.select_dtypes(include=[np.number]).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

# Select features and target
features = [
    'OverallQual', 'GrLivArea', 'TotalBsmtSF',
    '1stFlrSF', 'YearBuilt', 'FullBath'
]
X = data[features]
y = data['SalePrice']

# --- Step 3: Train-Test Split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Step 4: Train Model ---
model = GradientBoostingRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)
model.fit(X_train, y_train)

# --- Step 5: Evaluate ---
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Performance:")
print(f"MAE: ${mae:,.0f}")
print(f"R² Score: {r2:.3f}")

# --- Step 6: Visualization ---
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)

# Save the plot
plot_path = os.path.join(os.path.dirname(DATA_PATH), "price_prediction_plot.png")
plt.savefig(plot_path)
print(f"\nPlot saved to: {plot_path}")

# --- Step 7: Save Model ---
model_path = os.path.join(os.path.dirname(DATA_PATH), "house_price_model.pkl")
joblib.dump(model, model_path)
print(f"Model saved to: {model_path}")

# --- Sample Prediction ---
sample_house = [[7, 1500, 800, 1200, 1995, 2]]  # Modify with your own values
predicted_price = model.predict(sample_house)[0]
print(f"\nSample House Prediction: ${predicted_price:,.0f}")