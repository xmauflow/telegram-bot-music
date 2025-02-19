import asyncio
from youtubesearchpython import VideosSearch
from cilik.utils.changers import time_to_seconds

def get_yt_info_id(videoid):
    url = f"https://www.youtube.com/watch?v={videoid}"
    results = VideosSearch(url, limit=1)
    for result in results.next()["result"]:  # Updated to use next() for pagination
        title = result["title"]
        duration_min = result["duration"]
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
        return title, duration_min, duration_sec, thumbnail
    return None  # Return None if no result found

def get_yt_info_query(query: str):
    results = VideosSearch(query, limit=1)
    for result in results.next()["result"]:  # Updated to use next() for pagination
        title = result["title"]
        duration_min = result["duration"]
        thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        videoid = result["id"]
        duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
        return title, duration_min, duration_sec, thumbnail, videoid
    return None  # Return None if no result found

def get_yt_info_query_slider(query: str, query_type: int):
    results = VideosSearch(query, limit=10)
    result = results.next()["result"]  # Updated to use next() for pagination
    if len(result) > query_type:
        title = result[query_type]["title"]
        duration_min = result[query_type]["duration"]
        videoid = result[query_type]["id"]
        thumbnail = result[query_type]["thumbnails"][0]["url"].split("?")[0]
        duration_sec = int(time_to_seconds(duration_min)) if duration_min else 0
        return title, duration_min, duration_sec, thumbnail, videoid
    return None  # Return None if the query_type is out of range

async def get_m3u8(videoid):
    link = f"https://www.youtube.com/watch?v={videoid}"
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().strip().split("\n")[0]  # Use strip() to clean up the output
    else:
        return 0, stderr.decode().strip()  # Return error if no stdout
