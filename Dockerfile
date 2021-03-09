FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 5000
CMD [ "python", "-u", "web_service.py", "--host=0.0.0.0"] 