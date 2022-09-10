FROM python:3.9.1
RUN apt-get update && apt-get install -y

RUN pip install -U pip
RUN pip install pyautogui
RUN pip install python-xlib

COPY requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

RUN pip install pyautogui
RUN pip install python-xlib

RUN apt-get install python3-opencv -y 
RUN pip install opencv-contrib-python-headless
WORKDIR /app
RUN curl "https://www.dropbox.com/s/yx6n606i7cfcvoz/WilhemNet_86.h5?dl=1" -L -o WilhemNet_86.h5


COPY . /app
CMD ["python", "main.py"]
