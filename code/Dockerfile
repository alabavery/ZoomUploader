# outside of the docker container, there should be a launcher script
# this script is responsible for passing the correct volume arguments to the container when launched.
# Those arguments are:
# (1) ~/.zoom_uploader, which contains an unchanging credentials.json plus a txt file
# (2) the path contained in ~/.zoom_uploader/zoom_directory_path.txt. It has an initial default value, but
#     ideally we will have way for her to change this value using a web app from within the container.
#     Upon changing the value, she would have to stop the container and run the launcher script again, so
#     it can pass the new value of the zoom directory as a mount.
FROM python:3.8.7-slim-buster
RUN apt-get update && apt-get install -y inotify-tools
RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN mkdir zoom_dir_mount && mkdir config_dir_mount && mkdir app && cd app
COPY . .
CMD ./zoom_directory_loop.sh