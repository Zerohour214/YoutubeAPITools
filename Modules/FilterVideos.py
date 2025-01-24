#Filter an video object by a set of criteria
# Formats
# filter_criteria = {
#         "language": language,
#         "trackKind": track_kind
#     }
def filter_videos(videos, filter_criteria):
    def matches_criteria(caption):
        for key, value in filter_criteria.items():
            if caption['snippet'].get(key) != value:
                return False
        return True

    return [video for video in videos if matches_criteria(video)]
