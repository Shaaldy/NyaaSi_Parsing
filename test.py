import re

match = "Some text [1080p] some more text"

match_q = re.search(r'\[(\d+p)\]', match)
if match_q:
    quality = match_q.group(1)
    print("Quality: " + quality)

match_q = re.search(r'\((\d+p)\)', match)
if match_q:
    quality = match_q.group(1)
    print("Quality: " + quality)