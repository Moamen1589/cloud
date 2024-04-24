FROM python:alpine
RUN pip install nltk
 WORKDIR /app

 COPY stopwords.py /app

 COPY  paragraphs.txt /app

CMD ["python","stopwords.py"]
