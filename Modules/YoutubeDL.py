import yt_dlp

def download_captions(video_url, output_dir='target/dumps/caption'):
    options = {
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'skip_download': True,
        'writeautomaticsub': True,
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_url])