import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
import json

load_dotenv()

# Set up the API client
api_service_name = "youtube"
api_version = "v3"
api_key = os.getenv("API_KEY")

youtube = build(api_service_name, api_version, developerKey=api_key)

def get_channel_handle(channel_handle):
    request = youtube.channels().list(
        part="id",
        forHandle=channel_handle
    )
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        return response['items'][0]['id']
    else:
        raise ValueError("Invalid handle or no channel found.")

def get_uploads_playlist_id(channel_handle):
    request = youtube.channels().list(
        part="contentDetails",
        id=channel_handle
    )
    response = request.execute()
    if 'items' in response and len(response['items']) > 0:
        uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        return uploads_playlist_id
    else:
        raise ValueError("Invalid channel ID or no uploads playlist found.")

def list_videos_from_channel(channel_handle):
    channel_handle = get_channel_handle(channel_handle)
    uploads_playlist_id = get_uploads_playlist_id(channel_handle)
    videos = []
    next_page_token = None

    while True:
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

    return videos

def fetch_videos(handle, output_json=False, output_path=None):
    videos = list_videos_from_channel(handle)
    videos_json = [
        {
            "title": video['snippet']['title'],
            "video_id": video['snippet']['resourceId']['videoId']
        }
        for video in videos
    ]

    if output_json and output_path:
        with open(output_path, 'w') as file:
            json.dump(videos_json, file, indent=4)
    else:
        print(json.dumps(videos_json, indent=4))

