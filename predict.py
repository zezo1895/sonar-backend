import sys
import json
import numpy as np
import joblib

# تحميل النموذج
try:
    model = joblib.load("./model.pkl")
except FileNotFoundError:
    print(json.dumps({'error': 'Model file (model.pkl) not found'}))
    sys.exit(1)

# بيانات اختبار افتراضية (60 ميزة)
default_data = [
    0.02, 0.0371, 0.0428, 0.0207, 0.0954, 0.0986, 0.1539, 0.1601, 0.3109, 0.2111,
    0.1609, 0.1582, 0.2238, 0.0645, 0.0660, 0.2273, 0.3100, 0.2999, 0.5078, 0.4797,
    0.5783, 0.5071, 0.4328, 0.5550, 0.6711, 0.6415, 0.7104, 0.8080, 0.6791, 0.3857,
    0.1307, 0.2604, 0.5121, 0.7547, 0.8537, 0.8507, 0.6692, 0.6097, 0.4943, 0.2744,
    0.0510, 0.2834, 0.2825, 0.4256, 0.2641, 0.1386, 0.1051, 0.1343, 0.0383, 0.0324,
    0.0232, 0.0027, 0.0065, 0.0159, 0.0072, 0.0167, 0.0180, 0.0084, 0.0090, 0.0032
]

try:
    if len(sys.argv) > 1:
        # استلام البيانات من الوسيطات
        input_data = json.loads(sys.argv[1])
        # لو البيانات مصفوفة مباشرة، استخدمها
        if isinstance(input_data, list):
            input_array = np.array(input_data).reshape(1, -1)
        # لو البيانات فيها مفتاح 'data'
        elif isinstance(input_data, dict) and 'data' in input_data:
            input_array = np.array(input_data['data']).reshape(1, -1)
        else:
            raise ValueError("Input must be a list or an object with 'data' key")
    else:
        # استخدام بيانات اختبار افتراضية
        print("No input data provided. Using default test data.")
        input_array = np.array(default_data).reshape(1, -1)

    # التحقق من عدد الميزات
    if input_array.shape[1] != 60:
        raise ValueError(f"Expected 60 features, but got {input_array.shape[1]}")

    # التنبؤ
    prediction = model.predict(input_array)[0]

    # إخراج النتيجة
    print(json.dumps({'prediction': prediction}))

except json.JSONDecodeError:
    print(json.dumps({'error': 'Invalid JSON format'}))
except ValueError as e:
    print(json.dumps({'error': str(e)}))
except Exception as e:
    print(json.dumps({'error': f'An unexpected error occurred: {str(e)}'}))