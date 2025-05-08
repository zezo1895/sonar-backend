FROM node:18

# تثبيت Python ومتطلبات النظام
RUN apt update && apt install -y python3 python3-pip python3-venv

# تعيين مجلد العمل
WORKDIR /app

# نسخ الملفات
COPY . .

# تثبيت باقات Node.js
RUN npm install

# إنشاء بيئة افتراضية وتثبيت باقات Python بداخلها
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# تشغيل السيرفر
CMD ["npm", "start"]
