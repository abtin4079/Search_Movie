FROM python:3.9.19-alpine

WORKDIR /app
COPY . /app

RUN pip install fastapi
RUN pip install requests
RUN pip install pydantic
RUN pip install uvicorn
RUN pip install redis
RUN pip install elasticsearch
EXPOSE 8000


CMD [ "python3" , "./main.py" ]