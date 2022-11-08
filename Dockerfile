FROM python:3.9.15

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV PYTHONUNBUFFERED 1

RUN pip3 install flask
RUN pip3 install Flask-SQLAlchemy

# 各種パッケージのインストール
RUN apt update
RUN apt install -y build-essential mecab libmecab-dev mecab-ipadic git
RUN apt install -y sudo
RUN cd /var/lib/mecab/dic;git clone https://github.com/neologd/mecab-ipadic-neologd.git; cd mecab-ipadic-neologd; bin/install-mecab-ipadic-neologd -y

RUN wget "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ" -O CRF++-0.58.tar.gz; tar zxvf CRF++-0.58.tar.gz; cd CRF++-0.58; ./configure; sudo ldconfig; cd -;rm CRF++-0.58.tar.gz

RUN  FILE_ID=0B4y35FiV1wh7SDd1Q1dUQkZQaUU; FILE_NAME=cabocha-0.69.tar.bz2; curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null; CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"; curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}

RUN pip install mecab-python3


