FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install dependencies
RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    binutils libproj-dev

#work directory
RUN mkdir /src
WORKDIR /src
COPY . /src

RUN pip install -r requirements.txt
EXPOSE 4001
