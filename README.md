# ZoomUploader
**Automatically upload Zoom recordings to Google Drive**
## SetUp
- `> mkdir $HOME/.zoom-uploader`
- Get Google API token and paste into `$HOME/.zoom-uploader/credentials.json`
- Find directory path into which Zoom downloads recordings; paste into `$HOME/.zoom-uploader/zoom_directory.txt`
- download the `cmd` directory of this repo and place it into `$HOME/.zoom-uploader`
- download Docker if you don't have it
- create DockerHub account if you don't have one
- `> docker login --username=yourhubusername --email=youremail@company.com`
- You should now be able to start the script through `~/.zoom-uploader/cmd/start.sh` (subsequent starts will be much faster)
- Note that, if you have Docker set up to start on boot, this script will also start on boot (Docker automatically starts the script when Docker starts). You still need to start it the first time manually, however.
- You can then stop it through `~/.zoom-uploader/cmd/stop.sh`