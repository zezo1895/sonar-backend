const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();
const PORT = process.env.PORT || 5000;
const corsOptions = {
  origin: 'http://localhost:5173', // تحديد المصدر الذي يمكنه الوصول
};
app.use(cors(corsOptions));
app.use(bodyParser.json());

app.get('/hello', (req, res) => {
  res.json({ message: 'Hello from Node.js!' });
});

app.post('/predict', (req, res) => {
  const input = req.body.input_data;

  if (!input || input.length !== 60) {
    return res.status(400).json({ error: 'input_data لازم تكون مصفوفة 60 قيمة' });
  }

  const python = spawn('python3', ['./predict.py', JSON.stringify(input)]);

  let result = '';
  python.stdout.on('data', (data) => {
    result += data.toString();
  });

  python.stderr.on('data', (data) => {
    console.error('Error:', data.toString());
  });

  python.on('close', () => {
    try {
      const output = JSON.parse(result);
      res.json(output);
    } catch (err) {
      res.status(500).json({ error: 'فشل في تحليل نتيجة Python' });
    }
  });
});

app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});
