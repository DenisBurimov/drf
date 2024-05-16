FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

# Copy only the dependency files to install them
COPY requirements.txt /code/

# Install dependencies
RUN pip install --upgrade pip && pip install -r /code/requirements.txt

COPY . /code/
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate
EXPOSE 8000
