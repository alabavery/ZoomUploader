print('python invoked')
import sys
import json
import os
import sys
import time
from read_settings import get_value
from upload import upload_video


def watch_new_dir(dir_name, zoom_base_dir, max_seconds_to_wait):
    new_dir_path = os.path.join(zoom_base_dir, dir_name)
    print("Monitoring \"{dir}\" for mp4 file".format(dir=new_dir_path), flush=True)
    
    # every 10 seconds, see if an mp4 file exists in the newly created directory
    POLL_INTERVAL_SECONDS = 10
    seconds_waited = 0
    while seconds_waited < max_seconds_to_wait:
        video_files = get_video_files(new_dir_path)
        if len(video_files) > 0:
            return os.path.join(new_dir_path, video_files[0])

        time.sleep(POLL_INTERVAL_SECONDS)
        seconds_waited += POLL_INTERVAL_SECONDS
    print("NEVER SAW FILE APPEAR")
    

def get_video_files(dir_path):
    return [file_name for file_name in os.listdir(dir_path) if file_name.endswith('.mp4')]


if __name__ == '__main__':
    print('running python main')
    args = sys.argv[1:]
    print("arguments: ", args)
    # seems that ISDIR and CREATE are sometimes/always combined into one arg: "ISDIR,CREATE"
    # so easiest way to check that they are both present is simply to search args as a string
    str_args = str(args)
    if "ISDIR" in str_args and "CREATE" in str_args:
        print("Found create directory!")
        # last argument is the created dir
        new_dir_name = args[-1]
        # first argument is the dir inotifywait was watching
        base_directory_path = args[0]
        print("new_dir_name: \"{new_dir}\"; base_dir_path: \"{base_dir}\"".format(new_dir=new_dir_name, base_dir=base_directory_path))

        file_name = watch_new_dir(new_dir_name, base_directory_path, get_value('max_seconds_to_wait_for_download'))
        file_path = os.path.join(base_directory_path, new_dir_name, file_name)
        print("mp4 file path: \"{f}\"".format(f=file_path), flush=True)

        # name the Gdrive file as the directory
        upload_video(file_path, new_dir_name)
