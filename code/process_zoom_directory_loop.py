import sys
import json
import os
from read_settings import get_all


def watch_new_dir(dir_name, zoom_base_dir, max_seconds_to_wait):
    import time
    from upload import upload_video

    new_dir_path = os.path.join(zoom_base_dir, dir_name)
    
    # every 10 seconds, see if an m4a file exists in the newly created directory
    POLL_INTERVAL_SECONDS = 10
    seconds_waited = 0
    while seconds_waited < max_seconds_to_wait:
        video_files = get_video_files(new_dir_path)
        if len(video_files) > 0:
            # return upload_video(os.path.join(new_dir_path, video_files[0]), video_files[0])
            return os.path.join(new_dir_path, video_files[0])

        time.sleep(POLL_INTERVAL_SECONDS)
        seconds_waited += POLL_INTERVAL_SECONDS
    

def get_video_files(dir_path):
    return [file_name for file_name in os.listdir(dir_path) if file_name.endswith('.m4a')]



if __name__ == '__main__':
    # pretty sure there's only ever one line, but seems we have to iterate to access stdin
    for line in sys.stdin:
        if "CREATE" in line and "ISDIR" in line:
            new_dir_name = line.strip().split()[-1]
            config = get_all()
            
            print(watch_new_dir(
                new_dir_name,
                config['zoom_directory_path'],
                config['max_seconds_to_wait_for_download'],
            ))
            
            break
