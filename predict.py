import sys
import json
import numpy as np
import joblib

# تحميل النموذج
model = joblib.load("./model.pkl")

# استلام البيانات من Node.js
input_data = json.loads(sys.argv[1])
input_array = np.array(input_data).reshape(1, -1)

# التنبؤ
prediction = model.predict(input_array)[0]

# إخراج النتيجة
print(json.dumps({'prediction': prediction}))
