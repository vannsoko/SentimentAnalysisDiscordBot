FROM python:3.11.7


WORKDIR /app


COPY requirements.txt .


RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir


COPY bot.py .


RUN adduser --system --no-create-home nonroot
USER nonroot


CMD ["python", "bot.py"]
