from Modules.Utils import import_json
from Modules.ApiRequests import fetch_captions_desc, fetch_videos_from_channel, fetch_playlist_id

# The output_json parameter is here because Youtube API has a quota limit. Saves yeh token y'all.

if __name__ == "__main__":
    language = "en"
    channel_handle = "@GawrGura"
    filter_criteria = {
        "language": "en",
        "trackKind": "standard",
    }
    # print(fetch_playlist_id(channel_handle))
    videos = import_json('target/videos.json')
    if not videos:
        videos = fetch_videos_from_channel(channel_handle)
    video_ids = [video['snippet']['resourceId']['videoId'] for video in videos]
    print(video_ids)
    captions = import_json('target/captions.json')
    if not captions:
        captions = fetch_captions_desc(video_ids)
    # print(json.dumps(captions, indent=4))
