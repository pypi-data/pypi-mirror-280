"""
Class to Works with Git URLS
"""
__all__ = ['create']


class URLLike:
    """
    Correct URL's as like

    """
    def __init__(self, url: str):
        """
        Set the Url
        """
        self._raw = url
        self._url = self._correct(url)

    def _split(self):
        """
        Step 1 from the URLLike work
        """
        self._raw = self._raw.split('/')

    def _get_info(self):
        """
        Step 2 From the URLLike Work
        """
        self._provider = self._raw[2]
        self._user = self._raw[3]
        self._repo = self._raw[4]

    def _clean_first(self):
        """
        Step 3 From the URLLike Work
        """
        self._raw = '/'.join([self._user, self._repo])

    def _build_new(self):
        """
        Step 4 From the URLLike Work
        """
        self._raw = 'https://' + self._provider + '/' + self._raw

    def _correct(self):
        """
        Step 5 From the URLLike Work
        """
        self._split()
        self._get_info()
        self._clean_first()
        self._build_new()
        return self._raw

    def __str__(self):
        """
        Return the URL
        """
        return self._url

def create(user: str, repo: str, provider: str = 'github.com'):
    """
    Create a GitHub Repo Url
    """
    url = f'https://{provider}/{user}/{repo}'
    return URLLike(url)