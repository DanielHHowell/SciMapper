FROM tiangolo/uwsgi-nginx:python3.7

COPY ./app /app

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader averaged_perceptron_tagger

CMD ["python", "./Flasker.py"]
