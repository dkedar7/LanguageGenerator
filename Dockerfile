FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip3 install https://download.pytorch.org/whl/cpu/torch-1.3.1%2Bcpu-cp37-cp37m-linux_x86_64.whl
RUN pip3 install -r requirements.txt
RUN python downloads.py
CMD exec gunicorn main:app --bind :$PORT