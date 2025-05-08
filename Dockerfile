FROM node:18

# تثبيت Python
RUN apt update && apt install -y python3 python3-pip

# تعيين مجلد العمل
WORKDIR /app

# نسخ الملفات
COPY . .

# تثبيت باقات Node.js
RUN npm install

# تثبيت باقات Python
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# تشغيل السيرفر
CMD ["npm", "start"]
