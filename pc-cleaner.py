from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move
import logging

# Specify source and destination directories
source_dir = ""  # Fill in
dest_dir_sfx = ""  # Fill in
dest_dir_music = ""  # Fill in
dest_dir_video = ""  # Fill in
dest_dir_image = ""  # Fill in
dest_dir_documents = ""  # Fill in

# Supported file types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1

    while exists(join(dest, name)):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def move_file(dest, entry, name):
    if exists(join(dest, name)):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        rename(old_name, new_name)
    move(entry, dest)

def on_cleaner():
    with scandir(source_dir) as entries:
        for entry in entries:
            name = entry.name
            check_audio_files(entry, name)
            check_video_files(entry, name)
            check_image_files(entry, name)
            check_document_files(entry, name)

def check_audio_files(entry, name):
    for audio_extension in audio_extensions:
        if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
            if entry.stat().st_size < 10_000_000 or "SFX" in name:  # 10 Megabytes
                dest = dest_dir_sfx
            else:
                dest = dest_dir_music
            move_file(dest, entry, name)
            logging.info(f"Moved audio file: {name}")

def check_video_files(entry, name):
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):
            move_file(dest_dir_video, entry, name)
            logging.info(f"Moved video file: {name}")

def check_image_files(entry, name):
    for image_extension in image_extensions:
        if name.endswith(image_extension) or name.endswith(image_extension.upper()):
            move_file(dest_dir_image, entry, name)
            logging.info(f"Moved image file: {name}")

def check_document_files(entry, name):
    for documents_extension in document_extensions:
        if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
            move_file(dest_dir_documents, entry, name)
            logging.info(f"Moved document file: {name}")
