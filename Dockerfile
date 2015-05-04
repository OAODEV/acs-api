from ubuntu:14.04
maintainer jesse.miller@adops.com

run apt-get update && apt-get install -y \
    python \
    python-dev \
    python-pip

run pip install pymongo

run mkdir /app
add api.py /app/api.py
workdir /app

expose 8000

cmd ["python", "-u", "api.py"]