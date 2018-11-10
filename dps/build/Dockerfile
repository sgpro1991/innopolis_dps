FROM python:3.6

# Set timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Yekaterinburg /etc/localtime

ADD app /app
ADD conf /conf/
ADD docker-entrypoint.sh /
ADD requirements.txt /
RUN ["pip", "install", "uwsgi"]
RUN ["pip", "install", "-r", "/requirements.txt"]
EXPOSE 8000
RUN chmod +x /docker-entrypoint.sh
WORKDIR /app
ENTRYPOINT ["/docker-entrypoint.sh"]
