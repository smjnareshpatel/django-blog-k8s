# 1. Base image
FROM python:3.11-slim

# 2. Prevent .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set working directory
WORKDIR /code

# 4. Install netcat for wait script
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# 5. Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy entire project
COPY . /code/

# 7. Make wait script executable
COPY wait_for_db.sh /code/wait_for_db.sh
RUN chmod +x /code/wait_for_db.sh

# 8. Start process: wait for DB, collect static, start Gunicorn
CMD ["sh", "-c", "/code/wait_for_db.sh && python manage.py collectstatic --noinput && gunicorn myproject.wsgi:application --workers=1 --bind 0.0.0.0:8000 --access-logfile - --forwarded-allow-ips='*' --proxy-allow-from='*' --timeout 60"]


