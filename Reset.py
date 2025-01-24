import json

if __name__ == "__main__":
    def replace_content_with_empty_array(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file, indent=4)
    # Example usage
    replace_content_with_empty_array('target/videos.json')
    replace_content_with_empty_array('target/captions.json')