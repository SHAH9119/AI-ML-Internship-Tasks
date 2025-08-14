# Task 1: Iris Dataset Analysis

## Objective
Analyze and visualize the Iris dataset using Python.

## Steps
- Loaded data using `seaborn`.
- Generated scatter plots, histograms, and box plots.
- Identified key trends (e.g., Setosa has smaller petals).

## Files
- `iris_analysis.py`: Full Python code.
- Plots (optional): `sepal_scatter.png`, `histograms.png`.


# Task 4: General Health Query Chatbot: 

## Overview
A Python chatbot that answers general health questions using OpenAI's GPT-3.5, with safety disclaimers.

## Features
- Prompt engineering for safe, non-medical advice
- Environment variable-based API key security
- Command-line interface

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt 
   

# Task 6: House Price Prediction:

## Results
- **MAE**: $18,742
- **R² Score**: 0.887  
![Prediction Plot](results.png)

## How to Run
1. Download data from [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data)
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python house_price_prediction.py
   ```

## Code Structure
- Data preprocessing (handling missing values, feature selection)
- Gradient Boosting model training
- Performance evaluation (MAE, R²)
- **Model**: Gradient Boosting Regressor
- **Features Used**: 
  - OverallQual
  - GrLivArea  
  - YearBuilt
- **Performance**:
  - MAE: $18,742
  - R²: 0.887