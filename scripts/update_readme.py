"""Refresh the auto-updated Writing list in README.md from the rhnfzl.com feed."""

import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED = "https://rhnfzl.com/rss.xml"
README = Path(__file__).resolve().parent.parent / "README.md"


def writing(feed_xml, limit=5):
    items = []
    for item in ET.fromstring(feed_xml).iter("item"):
        if "professional" not in [c.text for c in item.findall("category")]:
            continue
        pub = item.findtext("pubDate")
        date = f" ({parsedate_to_datetime(pub):%b %Y})" if pub else ""
        items.append(f"- [{item.findtext('title')}]({item.findtext('link')}){date}")
    return "\n".join(items[:limit])


def replace(text, marker, body):
    pattern = re.compile(rf"(<!-- {marker}:START -->\n).*?(<!-- {marker}:END -->)", re.S)
    if not pattern.search(text):
        sys.exit(f"marker {marker} not found in README")
    # a lambda, so backslashes in titles are not read as regex escapes
    return pattern.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)


def main():
    req = urllib.request.Request(FEED, headers={"User-Agent": "rhnfzl-readme"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        posts = writing(resp.read())
    if posts:  # keep the old list if the feed has no professional posts
        README.write_text(replace(README.read_text(), "WRITING", posts))


if __name__ == "__main__":
    main()
