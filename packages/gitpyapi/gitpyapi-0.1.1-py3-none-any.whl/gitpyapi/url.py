"""
Class to Works with Git URLS
"""
__all__ = ['create']


class URLLike:
    """
    Class to correct and process Git URLs.
    """
    def __init__(self, url: str):
        """
        Initializes the URLLike instance with a URL.
        """
        self._raw = url
        self._url = self._correct(url)

    def _split(self):
        """
        Splits the URL into its components.
        """
        parts = self._raw.split('/')
        if len(parts) < 5:
            raise ValueError("URL is too short to contain all required parts.")
        self._raw_parts = parts

    def _get_info(self):
        """
        Extracts provider, user, and repository from the URL parts.
        """
        self._provider = self._raw_parts[2]
        self._user = self._raw_parts[3]
        self._repo = self._raw_parts[4]

    def _clean_first(self):
        """
        Creates a simplified path from user and repository.
        """
        self._raw = '/'.join([self._user, self._repo])

    def _build_new(self):
        """
        Builds a new corrected URL.
        """
        self._raw = f'https://{self._provider}/{self._raw}'

    def _correct(self) -> str:
        """
        Corrects the URL through several processing steps.
        """
        self._split()
        self._get_info()
        self._clean_first()
        self._build_new()
        return self._raw

    def __str__(self) -> str:
        """
        Returns the corrected URL as a string.
        """
        return self._url

def create(user: str, repo: str, provider: str = 'github.com'):
    """
    Create a GitHub Repo Url
    """
    url = f'https://{provider}/{user}/{repo}'
    return URLLike(url)