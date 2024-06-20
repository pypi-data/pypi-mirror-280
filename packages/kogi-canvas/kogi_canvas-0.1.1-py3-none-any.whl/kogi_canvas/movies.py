import subprocess
import ffmpeg

_installed = False

def is_ffmpeg_installed():
    global _installed
    if _installed == True:
        return True
    try:
        # FFmpegがインストールされているかを確認
        result = subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        _installed = True
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def install_ffmpeg(sync=False):
    if is_ffmpeg_installed():
        return

    # # パッケージリストを更新
    # subprocess.Popen(["apt-get", "update"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # FFmpegをインストール
    if sync:
        subprocess.run(["apt-get", "install", "-y", "ffmpeg"], check=True)
        print("FFmpeg installation complete.")    
    else:
        subprocess.Popen(["apt-get", "install", "-y", "ffmpeg"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("FFmpeg installation started in the background.")

def create_video(uuid0, framerate, filename):
    install_ffmpeg(sync=True)
    (
        ffmpeg
        .input(f'canvas{uuid0}/frame%04d.png', framerate=framerate)
        .output(filename, vcodec='libx264', pix_fmt='yuv420p')
        .run(overwrite_output=True)
    )