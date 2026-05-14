import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.transcript import get_transcript

# যেকোনো public YouTube video দিন
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

try:
    text = get_transcript(url)
    print("✅ সফল!")
    print(f"প্রথম ২০০ character: {text[:200]}")
except ValueError as e:
    print(f"❌ Error: {e}")