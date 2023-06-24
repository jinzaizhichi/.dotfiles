from google.oauth2.credentials import Credentials
creds = Credentials.from_authorized_user_file('./client_secret.json', scopes=['https://www.googleapis.com/auth/youtube.upload'])


from googleapiclient.discovery import build
youtube = build('youtube', 'v3', credentials=creds)


from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


file = './Mixkit-Heavy-Rain-Drops-15sec-uploadYoutube.mp4'
media = MediaFileUpload(file)

request_body = {
        'snippet':{
            'title':'My uploader video',
            'description':'This is a demo video uploaded from a Python script',
            'tags':['python','youtube api', 'demo'],
            'categoryid':'22',
            },
        'status':{
            'privacyStatus': 'private'
            }
        }
try:
    response = youtube.video().insert(
            part='snippet,status',
            body='request_body',
            media_body=media
            ).execute()
except HttpError as e:
    print(f'An HTTP error{e.resp.status} occurred:{e.content}')
else:
    print(f'Video ID "{response["id"]}" was successfully uploaded.')
