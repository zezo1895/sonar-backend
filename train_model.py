import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# تحميل البيانات
data = pd.read_csv("./Copy of sonar data (1).csv", header=None)
X = data.drop(columns=60)
y = data[60]

# تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify=y, random_state=1)

# تدريب النموذج باستخدام Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# حفظ النموذج
joblib.dump(model, "model.pkl")

# تقييم النموذج
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model trained with accuracy: {accuracy:.4f}")
