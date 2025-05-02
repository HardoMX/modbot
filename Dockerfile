FROM python:latest

ADD modbot.py .

RUN python -m pip install discord.py azure-identity azure-keyvault-secrets fastapi[standard] uvicorn[standard]

CMD ["python", "./modbot.py"]
