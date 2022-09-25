import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def moveDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes :
            return category
    return 'MISC' #If filetype doesn't exist in dict

def organizeDirectory():
    for item in os.scandir() :
        if item.is_dir() :
            continue
        filepath = Path(item)
        filesuffix = filepath.suffix.lower()
        if filesuffix == ".py" :
            continue
        directorytomove = moveDirectory(filesuffix)
        directorytomovepath = Path(directorytomove)
        if not directorytomovepath.is_dir() :
            directorytomovepath.mkdir()
        filepath.rename(directorytomovepath.joinpath(filepath))

organizeDirectory()