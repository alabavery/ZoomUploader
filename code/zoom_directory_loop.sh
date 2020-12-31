ZOOM_DIR_PATH=$(python3 ./read_settings.py zoom_directory_path)
while true; do
    inotifywait $ZOOM_DIR_PATH | python3 ./process_zoom_directory_loop.py
done