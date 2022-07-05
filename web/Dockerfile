FROM python:3.8

WORKDIR /app
COPY . /app
# How you install your python packages may differ
RUN pip install -r /app/requirements.txt

# Ensure the path here is correct
ENV FLASK_APP /app/app.py

EXPOSE 8080
EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]