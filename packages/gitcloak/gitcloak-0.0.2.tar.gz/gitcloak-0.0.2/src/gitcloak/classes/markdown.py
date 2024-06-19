import re
import markdown2

class RelativeURLRewriter(markdown2.Markdown):
    def __init__(self, base_url, *args, **kwargs):
        self.base_url = base_url
        super().__init__(*args, **kwargs)

    def postprocess(self, text):
        # Rewrite relative URLs
        def replace_url(match):
            url = match.group(1)
            if not (":" in url or url.startswith("/") or url.startswith("#") or url.startswith("md5-")):
                return f'src="{self.base_url}/{url}"'
            return match.group(0)

        text = re.sub(r'src="([^"]+)"', replace_url, text)
        text = re.sub(r'href="([^"]+)"', replace_url, text)
        return text