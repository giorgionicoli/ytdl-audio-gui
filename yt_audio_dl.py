import subprocess  # nosec
import urllib.request

# pip install git+https://github.com/ifahadone/pytube.git
import pytube


def download_audio(url, file_name):

    content = pytube.YouTube(url)
    streams = content.streams.filter(only_audio=True).order_by("abr").desc()
    response = urllib.request.urlopen(streams.first().url)  # nosec

    if not file_name:
        file_name = "_".join(content.title.split(" "))

    if not file_name.endswith(".mp3"):
        file_name += ".mp3"

    command = ("ffmpeg", "-y", "-i", "-", file_name)
    process = subprocess.Popen(command, stdin=subprocess.PIPE)  # nosec

    while True:
        chunk = response.read(16 * 1024)
        if not chunk:
            break
        process.stdin.write(chunk)

    process.stdin.close()
    process.wait()
