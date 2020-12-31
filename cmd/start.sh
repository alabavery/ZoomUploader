ZOOM_DIR_PATH=`cat $HOME/.zoom-uploader/zoom_directory.txt`
docker run --name zoom-uploader -d -v "$HOME/.zoom-uploader":"/config_dir_mount" -v $ZOOM_DIR_PATH:"/zoom_dir_mount" alaverydev/zoom-uploader
