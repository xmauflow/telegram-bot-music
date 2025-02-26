import os
import sys
from os import listdir, mkdir
from shutil import rmtree

from ..logging import LOGGER


def dirr():
    if "assets" not in listdir():
        LOGGER(__name__).warning(
            f"Folder Aset tidak Ditemukan. Silakan kloning repositori lagi."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith((".jpg", ".jpeg")):
            os.remove(file)
    if "downloads" in listdir():
        rmtree("downloads", ignore_errors=True)
    mkdir("downloads")
    if "cache" in listdir():
        rmtree("cache", ignore_errors=True)
    mkdir("cache")
    LOGGER(__name__).info("Direktori Diperbarui.")
