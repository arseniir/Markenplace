FROM python:3.10.12
# RUN apt-get update && apt-get install -y \
#     libpq-dev \
#     redis-server \
#     && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /dj_map

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
# EXPOSE 8000

# COPY . /dj_map

# WORKDIR /dj_map
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]




