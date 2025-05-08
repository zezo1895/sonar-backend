# استخدم صورة فيها Node.js
FROM node:18

# تثبيت Python وكل الأدوات اللازمة
RUN apt update && apt install -y python3 python3-pip

# إنشاء مجلد داخل الحاوية
WORKDIR /app

# نسخ كل ملفات المشروع
COPY . .

# تثبيت باقات Node.js
RUN npm install

# تثبيت باقات Python
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# بدء تشغيل السيرفر
CMD ["npm", "start"]
