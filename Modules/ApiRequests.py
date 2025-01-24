import os

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from Modules.Utils import export_json

load_dotenv()

# Set up the API client
api_service_name = "youtube"
api_version = "v3"
api_key = os.getenv("API_KEY")

youtube = build(api_service_name, api_version, developerKey=api_key)


# Fetch a channel object
def fetch_channel(channel_handle):
    request = youtube.channels().list(
        part="id",
        forHandle=channel_handle
    )
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        return response['items'][0]['id']
    else:
        raise ValueError("Invalid handle or no channel found.")


def fetch_playlist_id(channel_handle):
    request = youtube.channels().list(
        part="contentDetails",
        forHandle=channel_handle
    )
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        return uploads_playlist_id
    else:
        raise ValueError("Invalid channel ID or no uploads playlist found.")


# Fetch all videos object from a channel
def fetch_videos_from_channel(channel_handle):
    uploads_playlist_id = fetch_playlist_id(channel_handle)
    videos = []
    next_page_token = None

    while True:
        try:
            request = youtube.playlistItems().list(
                part="snippet",
                playlistId=uploads_playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()
            videos.extend(response['items'])
            next_page_token = response.get('nextPageToken')

            if not next_page_token:
                break
        except HttpError as e:
            print(f"An error occurred: {e}")
            if e.resp.status == 403:
                print("Quota exceeded.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    export_json(videos, 'target/videos.json')
    return videos


def fetch_captions_desc(video_ids):
    all_captions = []
    for video_id in video_ids:
        try:
            print('Youtube Video Caption Queried: ', video_id)
            request = youtube.captions().list(
                part="snippet",
                videoId=video_id
            )
            response = request.execute()
            all_captions.extend(response['items'])
        except HttpError as e:
            print(f"An error occurred: {e}")
            if e.resp.status == 403:
                print("Quota exceeded.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break
    export_json(all_captions, 'target/captions.json')
    return all_captions
