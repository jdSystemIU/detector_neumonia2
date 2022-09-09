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

COPY . /app
WORKDIR /app
CMD ["python", "main.py"]
