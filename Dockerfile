FROM python:3.8

ARG REQUIREMENTS_FILE

WORKDIR /app
EXPOSE 80
ENV PYTHONUNBUFFERED 1

RUN set -x && \
	apt-get update && \
	apt -f install	&& \
	apt-get -qy install netcat-traditional && \
	rm -rf /var/lib/apt/lists/* && \
	wget -O /wait-for https://raw.githubusercontent.com/eficode/wait-for/master/wait-for && \
	chmod +x /wait-for

CMD ["sh", "/entrypoint-web.sh"]
COPY ./docker/ /

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . ./
CMD python manage.py collectstatic --no-input && \
	python manage.py migrate && \
	python manage.py runserver 0.0.0.0:8000
