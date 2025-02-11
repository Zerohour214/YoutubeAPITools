import yt_dlp

def download_captions(video_url, output_dir='target/dumps/caption'):
    options = {
        'writesubtitles': True,
        'subtitleslangs': ['en'],
        'skip_download': True,
        'writeautomaticsub': True,
        'cookiefile': 'bin/cookies.txt', # Use https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc?pli=1, to get the Cookie file, and paste it in bin. This is for bypassing age-restricted videos.
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_url])