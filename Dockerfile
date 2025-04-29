FROM python:latest

ADD test.py .
ADD secrets.yaml .

RUN python -m pip install discord.py PyYAML

CMD ["python", "./test.py"]
