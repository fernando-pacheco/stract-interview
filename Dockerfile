FROM python:3.12-slim

WORKDIR /stract-app

RUN apt update && apt install -y python3-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]