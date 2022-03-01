FROM python:3.8-alpine


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY tut12.py tut12.py
ENTRYPOINT [ "python3", "tut12.py"]
