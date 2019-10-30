FROM ubuntu:18.04
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    poppler-utils \
    python-poppler \
    python3 \
    #python-setuptools \
    python3-pip \
    && apt-get clean \
    && apt-get autoremove

ADD . /home/App
WORKDIR /home/App
COPY . .

RUN pip3 install pytesseract
RUN pip3 install Pillow
RUN pip3 install requests
RUN pip3 install pdf2image

VOLUME ["/data"]
EXPOSE 5000 5000
CMD ["python3","OCRRun.py"]
