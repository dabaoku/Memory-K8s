# FROM：Basic image python 3.8
FROM python:3.8

# upgrade pip version
RUN pip install --upgrade pip

# WORKDI：create working directory
WORKDIR /app

# ADD：add files to image
ADD . /app

# install python package
RUN pip install -r requirements.txt

CMD python app.py