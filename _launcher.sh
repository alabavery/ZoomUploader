# WORK IN PROGRESS...

# function to run the actual program, with both config dir and zoom dir mounted
# should only run this function if you know that credentials.json
# and zoom_directory.txt already exist
run_main () {
    ZOOM_DIR_PATH=`cat $HOME/.zoom-uploader/zoom_directory.txt`
    docker run -v "$HOME/.zoom-uploader":"/config_dir_mount" -v $ZOOM_DIR_PATH:"/zoom_dir_mount" zoom-uploader-daemon
}

HAVE_CREDENTIALS=false
if [ -f "$HOME/.zoom-uploader/credentials.json" ]; then
    HAVE_CREDENTIALS=true
fi
HAVE_ZOOM_PATH=false
if [ -f "$HOME/.zoom-uploader/zoom_directory.txt" ]; then
    HAVE_ZOOM_PATH=true
fi
# if we have credentials.json and the path to the zoom videos dir, launch the
# main program
if [ $HAVE_CREDENTIALS = true ] && [ $HAVE_ZOOM_PATH = true ]; then
    run_main
else
    # if not, launch the config app, then, when that process has exited,
    # launch the main program
    docker run -v "$HOME" -p 3000:3000 zoom-config-app && run_main
fi