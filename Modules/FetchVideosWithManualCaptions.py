import json
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

# Set up the API client
api_service_name = "youtube"
api_version = "v3"
api_key = os.getenv("API_KEY") # Replace with your actual API key

# Construct the service
youtube = build(api_service_name, api_version, developerKey=api_key)


# Function to list captions
def list_captions(video_id, from_json=False, json_path=None):
    if from_json and os.path.exists(json_path):
        print('JSON LOADED')
        with open(json_path, 'r') as file:
            response = json.load(file)
    else:
        print('Youtube Queried')
        request = youtube.captions().list(
            part="snippet",
            videoId=video_id
        )
        response = request.execute()
    return response


def filter_captions_by_language(captions, language):
    return [caption for caption in captions['items'] if caption['snippet']['language'] == language and caption['snippet']['trackKind'] == 'standard']

def get_filtered_captions(video_id, language, from_json=False, json_path=None):
    captions = list_captions(video_id, from_json, json_path)
    filtered_captions = filter_captions_by_language(captions, language)
    return filtered_captions
