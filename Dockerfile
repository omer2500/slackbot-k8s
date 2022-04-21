FROM python:alpine3.15

# Install curl
RUN apk add curl

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"

# Add required files
COPY bot.py /app/bot.py
COPY requirements.txt /app/requirements.txt

# Install requirements
RUN pip install -r /app/requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "/app/bot.py" ]
