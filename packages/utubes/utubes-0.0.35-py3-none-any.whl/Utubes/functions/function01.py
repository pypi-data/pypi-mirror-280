import os, asyncio
from .collections import SMessage
from ..scripts import Okeys, Flite, Scripted
from yt_dlp import YoutubeDL, DownloadError
#===============================================================================================

class DownloadER:

    async def metadata(link, command):
        with YoutubeDL(command) as ydl:
            try:
                moonus = ydl.extract_info(link, download=False)
                return SMessage(result=moonus)
            except Exception as errors:
                return SMessage(errors=errors)

#===============================================================================================

    async def extracts(link, command):
        with YoutubeDL(command) as ydl:
            try:
                moonus = ydl.extract_info(link, download=False)
                return SMessage(result=moonus)
            except Exception as errors:
                return SMessage(errors=errors)

#===============================================================================================

    async def download(link, command, progress):
        loop = asyncio.get_event_loop()
        with YoutubeDL(command) as ydl:
            try:
                filelink = [link]
                ydl.add_progress_hook(progress)   
                await loop.run_in_executor(None, ydl.download, filelink)
                return SMessage(status=True)
            except DownloadError as errors:
                return SMessage(status=False, errors=errors)
            except Exception as errors:
                return SMessage(status=False, errors=errors)

#===============================================================================================

    async def filename(link, command, length=60, clean=Flite.DATA01, format=Okeys.DATA01):
        with YoutubeDL(command) as ydl:
            try:
                meawes = ydl.extract_info(link, download=False)
                moonus = ydl.prepare_filename(meawes, outtmpl=format)
                texted = Scripted.DATA01.join(clean.get(chao, chao) for chao in moonus)
                moones = texted[:length]
                return SMessage(result=moones, captions=moonus)
            except Exception as errors:
                return SMessage(result="Unknown.tmp", errors=errors)

#===============================================================================================
