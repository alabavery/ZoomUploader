# ZoomUploader
Automatically upload Zoom recordings to Google Drive
## General setup
### This is the part of the setup that is needed no matter how you plan to run the program
- `> mkdir $HOME/.zoom-uploader`
- Get Google API token and paste into `$HOME/.zoom-uploader/credentials.json`
- Find directory path into which Zoom downloads recordings; paste into `$HOME/.zoom-uploader/zoom_directory.txt`
- download Docker if you don't have it
- create DockerHub account if you don't have one
- `> docker login --username=yourhubusername --email=youremail@company.com`
- You should now be able to start the script by `cd`'ing into this repo's directory and `./cmd/start.sh` (subsequent starts will be much faster)
- You can then stop it through `./cmd/stop.sh`

## Run on start up
### OSX (Mac)
- 