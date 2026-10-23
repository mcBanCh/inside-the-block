FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY itb ./itb
COPY tests ./tests
# keys are NEVER baked into the image: mount ./keys at /keys (read-only) or pass ITB_PAYER_KEYPAIR_JSON
ENTRYPOINT ["python", "-m", "itb", "--data", "/data"]
CMD ["all"]
