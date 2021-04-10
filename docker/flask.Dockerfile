FROM python:3.6
RUN mkdir /usr/src/app/
COPY ./flask/ /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 82
RUN pip install -r requirements.txt
CMD ["python", "/usr/src/app/app.py"]