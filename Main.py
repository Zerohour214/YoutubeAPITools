from Modules.FetchVideosWithManualCaptions import get_filtered_captions
from Modules.FetchAllVideoFromChannel import fetch_videos
import json

if __name__ == "__main__":
    language = "en"
    channel_handle = "@GawrGura"

    # filtered_captions = get_filtered_captions(video_id, language, from_json=False, json_path='output.json')
    fetch_videos(channel_handle, output_json=True, output_path='target/video_lists.json')
