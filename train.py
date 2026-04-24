import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import joblib

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameters
params = {
    "n_estimators": 100,
    "max_depth": 5,
    "random_state": 42
}

# MLflow setup
mlflow.set_experiment("iris-classification")

with mlflow.start_run():
    # Train model
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")

    # Log params and metrics
    mlflow.log_params(params)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)

    # Log and register model
    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        registered_model_name="IrisClassifier"
    )

    print(f"Accuracy: {acc:.4f}, F1: {f1:.4f}")
    print("Model registered in MLflow Model Registry as 'IrisClassifier'")

# Save locally for FastAPI
joblib.dump(model, "model.joblib")
print("Model saved to model.joblib")
