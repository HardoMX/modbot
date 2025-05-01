FROM python:latest

ADD test.py .

RUN python -m pip install discord.py azure-identity azure-keyvault-secrets

CMD ["python", "./test.py"]
