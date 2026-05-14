from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def get_video_id(url: str) -> str:
    """YouTube URL থেকে video ID বের করে"""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        raise ValueError("Invalid YouTube URL")


def get_transcript(url: str) -> str:
    """Video এর transcript return করে"""
    try:
        video_id = get_video_id(url)
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id)

        # সব text একসাথে জোড়া দিন
        full_text = " ".join([snippet.text for snippet in fetched])
        return full_text

    except TranscriptsDisabled:
        raise ValueError("এই video তে transcript নেই")
    except NoTranscriptFound:
        raise ValueError("Transcript খুঁজে পাওয়া যায়নি")
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")