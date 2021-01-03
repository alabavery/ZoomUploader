FROM python:3.8.7-slim-buster
RUN apt-get update && apt-get install -y inotify-tools
RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN mkdir zoom_dir_mount config_dir_mount app
COPY . /app
WORKDIR /app
ENTRYPOINT [ "/app/zoom_directory_loop.sh" ]