from Modules.FetchVideosWithManualCaptions import get_filtered_captions
import json

if __name__ == "__main__":
    video_id = "M7FIvfx5J10"
    language = "en"
    filtered_captions = get_filtered_captions(video_id, language, from_json=False, json_path='output.json')
    print(json.dumps(filtered_captions, indent=4))

