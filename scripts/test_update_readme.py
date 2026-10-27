import unittest

from update_readme import replace, writing

FEED = b"""<rss><channel>
<item><title>Kept</title><link>https://x/a</link><pubDate>Wed, 15 Jul 2026 00:00:00 GMT</pubDate>
<category>professional</category></item>
<item><title>Skipped</title><link>https://x/b</link><pubDate>Wed, 15 Jul 2026 00:00:00 GMT</pubDate>
<category>personal</category></item>
</channel></rss>"""

class Test(unittest.TestCase):
    def test_writing_keeps_only_professional(self):
        self.assertEqual(writing(FEED), "- [Kept](https://x/a) (Jul 2026)")

    def test_replace_between_markers(self):
        text = "a\n<!-- R:START -->\nold\n<!-- R:END -->\nb"
        self.assertEqual(replace(text, "R", "new \\1"), "a\n<!-- R:START -->\nnew \\1\n<!-- R:END -->\nb")
        empty = "<!-- R:START -->\n<!-- R:END -->"
        self.assertEqual(replace(empty, "R", "x"), "<!-- R:START -->\nx\n<!-- R:END -->")
        with self.assertRaises(SystemExit):
            replace("no markers", "R", "x")


if __name__ == "__main__":
    unittest.main()
