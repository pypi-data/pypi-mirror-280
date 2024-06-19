import re
import markdown2


class RelativeURLRewriter(markdown2.Markdown):
    """A Markdown postprocessor that rewrites relative URLs to match the raw file URL."""

    def __init__(self, base_url, *args, **kwargs):
        """Initialize the RelativeURLRewriter.

        Args:
            base_url (str): The base URL to prepend to relative URLs.
        """
        self.base_url = base_url
        super().__init__(*args, **kwargs)

    def postprocess(self, text: str) -> str:
        """Rewrite relative URLs in the Markdown text.

        Args:
            text (str): The Markdown text.

        Returns:
            str: The Markdown text with relative URLs rewritten.
        """

        def replace_url(match):
            """A subfunction to replace the URL in a found match.

            Args:
                match (re.Match): The match object.

            Returns:
                str: The replacement string, either the original URL or the rewritten URL.
            """

            url = match.group(1)
            if not (
                ":" in url
                or url.startswith("/")
                or url.startswith("#")
                or url.startswith("md5-")
            ):
                return f'src="{self.base_url}/{url}"'
            return match.group(0)

        text = re.sub(r'src="([^"]+)"', replace_url, text)
        text = re.sub(r'href="([^"]+)"', replace_url, text)
        return text
