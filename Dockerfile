FROM python:3
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python downloads.py
CMD python main.py