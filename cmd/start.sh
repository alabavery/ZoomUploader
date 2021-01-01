ZOOM_DIR_PATH=`cat $HOME/.zoom-uploader/zoom_directory.txt`
echo "mounting zoom path of $ZOOM_DIR_PATH"
docker run -d --name zoom-uploader -v "$HOME/.zoom-uploader":"/config_dir_mount" -v $ZOOM_DIR_PATH:"/zoom_dir_mount" --restart always alaverydev/zoom-uploader
