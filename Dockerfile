# Gunakan image Python versi terbaru atau sesuai kebutuhan
FROM python:3.12

# Set work directory di dalam container
WORKDIR /app

# Salin semua file ke dalam container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan aplikasi Flask
CMD ["python", "app.py"]
