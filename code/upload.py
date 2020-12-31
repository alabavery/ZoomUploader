from apiclient.http import MediaFileUpload
from drive_service import get_drive_service

def upload_video(path_on_disk, name_to_give_in_drive):
    file_metadata = {'name': name_to_give_in_drive}
    media = MediaFileUpload(path_on_disk, mimetype='video/mp4')
    file = get_drive_service().files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file.get('id'))
