FROM python:3.8.2-alpine

RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc gfortran python python-dev py-pip build-base wget openssl openssl-dev freetype-dev libpng-dev openblas-dev libffi-dev libxml2-dev libxslt-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# TODO Replace with git repo for better builds
COPY ./pach_screener ./

CMD [ "scrapy", "crawl", "constituents", "-o", "pfs_dev/constituents.csv", "-t", "csv" ]
CMD [ "/bin/sh"]

