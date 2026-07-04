"""
Transcript extraction utilities for YouTube videos.
Handles URL parsing and transcript fetching via LangChain's YoutubeLoader.
"""

import re
from langchain_community.document_loaders import YoutubeLoader


def extract_video_id(url: str) -> str | None:
    """
    Extract the video ID from various YouTube URL formats.

    Supports:
        - https://www.youtube.com/watch?v=VIDEO_ID
        - https://youtu.be/VIDEO_ID
        - https://www.youtube.com/embed/VIDEO_ID
        - https://www.youtube.com/v/VIDEO_ID

    Args:
        url: A YouTube video URL string.

    Returns:
        The video ID string, or None if the URL is invalid.
    """
    patterns = [
        r'(?:youtube\.com\/watch\?v=)([\w-]{11})',
        r'(?:youtu\.be\/)([\w-]{11})',
        r'(?:youtube\.com\/embed\/)([\w-]{11})',
        r'(?:youtube\.com\/v\/)([\w-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def get_transcript(video_url: str) -> str:
    """
    Fetch the transcript for a YouTube video using LangChain's YoutubeLoader.

    Args:
        video_url: The full YouTube video URL.

    Returns:
        The full transcript as a single concatenated string.

    Raises:
        Exception: If the transcript cannot be fetched (e.g., captions disabled).
    """
    loader = YoutubeLoader.from_youtube_url(
        video_url,
        add_video_info=False,
        language=["hi"]
    )
    docs = loader.load()
    transcript = docs[0].page_content
    return transcript
