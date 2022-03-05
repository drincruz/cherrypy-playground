FROM python:3.8-alpine


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY tut07.py tut07.py
ENTRYPOINT [ "python3", "tut07.py"]
