FROM python:3.9.5
ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /opt/website
ENV PYTHONPATH "${PYTHONPATH}:/opt/website"
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /opt/website
