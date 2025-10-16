from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

# === DATASET ===
# Study hours (X) and whether the student passed (y)
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

# === MODEL TRAINING ===
model = LogisticRegression()
model.fit(X, y)

# === PREDICTION ===
hours = np.linspace(0, 7, 100).reshape(-1, 1)
probabilities = model.predict_proba(hours)[:, 1]

# Print a few sample predictions
print("Predicted probability for 3 study hours:", round(model.predict_proba([[3]])[0][1], 2))
print("Predicted probability for 6 study hours:", round(model.predict_proba([[6]])[0][1], 2))

# === VISUALIZATION ===
plt.figure(figsize=(7, 5))
plt.scatter(X, y, color='blue', label='Actual Data (Pass/Fail)')
plt.plot(hours, probabilities, color='red', label='Sigmoid Curve (Predicted Probability)')
plt.axhline(0.5, color='gray', linestyle='--', label='Decision Boundary (0.5)')
plt.xlabel('Study Hours')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression: Study Hours vs. Pass Probability')
plt.legend()
plt.grid(True)
plt.show()
