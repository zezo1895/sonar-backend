const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();
const PORT = process.env.PORT || 5000;
const corsOptions = {
  origin: 'http://localhost:5173', // مصدر الواجهة الأمامية
};
app.use(cors(corsOptions));
app.use(bodyParser.json());

app.get('/hello', (req, res) => {
  res.json({ message: 'Hello from Node.js!' });
});

app.post('/predict', (req, res) => {
  const input = req.body.input_data;

  // التحقق من البيانات
  if (!input || !Array.isArray(input) || input.length !== 60) {
    return res.status(400).json({ error: 'input_data must be an array of 60 numbers' });
  }

  // مسار Python (عدله حسب مسار البيئة الافتراضية بتاعتك)
  const pythonPath = 'C:\\Users\\EXTRA\\Desktop\\react-rock\\sonar-backend\\venv\\Scripts\\python.exe';
  const python = spawn(pythonPath, ['./predict.py', JSON.stringify(input)]);

  let result = '';
  let errorOutput = '';

  // جمع الناتج من stdout
  python.stdout.on('data', (data) => {
    result += data.toString();
  });

  // جمع الأخطاء من stderr
  python.stderr.on('data', (data) => {
    errorOutput += data.toString();
  });

  // عند انتهاء تشغيل Python
  python.on('close', (code) => {
    if (code !== 0) {
      console.error('Python process exited with code:', code);
      console.error('Python error output:', errorOutput);
      return res.status(500).json({ error: 'Python script failed', details: errorOutput });
    }

    try {
      const output = JSON.parse(result);
      res.json(output);
    } catch (err) {
      console.error('Failed to parse Python output:', result);
      console.error('Error:', err.message);
      res.status(500).json({ error: 'Failed to parse Python output', details: result });
    }
  });

  // معالجة أخطاء spawn
  python.on('error', (err) => {
    console.error('Failed to start Python process:', err.message);
    res.status(500).json({ error: 'Failed to start Python process', details: err.message });
  });
});

app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});