#!/usr/bin/env python3
"""
YouTube Transcript Tool
Usage: python tools/youtube_transcript.py <youtube_url_or_id>
Fetches the full transcript of a YouTube video and prints it to stdout.
"""

import sys
import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def extract_video_id(url_or_id: str) -> str:
    patterns = [
        r"(?:v=)([a-zA-Z0-9_-]{11})",
        r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})",
        r"(?:embed/)([a-zA-Z0-9_-]{11})",
        r"^([a-zA-Z0-9_-]{11})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract video ID from: {url_or_id}")


def get_transcript(url_or_id: str) -> str:
    video_id = extract_video_id(url_or_id)

    try:
        api = YouTubeTranscriptApi()

        # Try English first, then any available language
        try:
            fetched = api.fetch(video_id, languages=["en", "en-US", "en-GB"])
        except Exception:
            # Fall back to listing and grabbing whatever is available
            transcript_list = api.list(video_id)
            transcript = next(iter(transcript_list))
            fetched = transcript.fetch()

        full_text = " ".join(entry.text for entry in fetched)
        return f"[Video ID: {video_id}]\n\n{full_text}"

    except TranscriptsDisabled:
        return f"Error: Transcripts are disabled for video {video_id}."
    except Exception as e:
        return f"Error fetching transcript: {e}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/youtube_transcript.py <youtube_url_or_id>")
        sys.exit(1)

    result = get_transcript(sys.argv[1])
    print(result)
