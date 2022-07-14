from yt_dlp import YoutubeDL
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url', type=str)
parser.add_argument('-f', '--format', required=False, type=str, default='720p')
parser.add_argument('-o', '--output', required=False, type=str, default='%(title)s')
args = parser.parse_args()

extension = 'mp4'
url = args.url.strip()
resolution = int(args.format.strip().rstrip('p'))
output = f'{args.output.rstrip("." + extension)}.{extension}'

ydl = YoutubeDL()
response = ydl.extract_info(url, download=False)
for format in response['formats']:
    if format['ext'] == extension and (format['height'] == resolution or format['format_note'] == f'{resolution}p'):
        try:
            ydl = YoutubeDL({'format': format['format_id'], 'outtmpl': output})
            ydl.download([url])
            exit(0)
        except:
            pass
