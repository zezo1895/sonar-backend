# صورة أساسية تحتوي على Node.js
FROM node:18

# تثبيت Python والمكتبات المطلوبة
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# إعداد مجلد العمل
WORKDIR /app

# نسخ ملفات المشروع
COPY . .

# تثبيت مكتبات Node.js
RUN npm install

# إعداد بيئة افتراضية لـ Python
RUN python3 -m venv /app/venv

# تثبيت مكتبات Python
RUN /app/venv/bin/pip install -r requirements.txt

# تعيين الأمر الافتراضي
CMD ["npm", "start"]