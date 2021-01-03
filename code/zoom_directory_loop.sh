#!/bin/bash
ZOOM_DIR_PATH=$(python3 ./read_settings.py zoom_directory_path)
echo "inotifywait will watch $ZOOM_DIR_PATH"

OUTPUT=""
while true; do
    OUTPUT=$(inotifywait -e create $ZOOM_DIR_PATH)
    python3 ./process_zoom_directory_loop.py $OUTPUT
done