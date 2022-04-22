FROM python:3.8.13-alpine3.15

ENV PYTHONPATH "${PYTHONPATH}:/src"

# Install curl
RUN apk add curl

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Add required files
COPY ./ ./

# Install requirements
RUN pip install -r /requirements.txt

CMD ["gunicorn", "-w 1", "-b", "0.0.0.0:8080", "src.app:app"]
