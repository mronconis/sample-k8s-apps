FROM registry.access.redhat.com/ubi8/python-39:latest
 
WORKDIR /deployment
 
COPY ./src/app.py /deployment
COPY ./requirements.txt /deployment
 
RUN pip3 install -r requirements.txt
 
EXPOSE 8080
 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]
