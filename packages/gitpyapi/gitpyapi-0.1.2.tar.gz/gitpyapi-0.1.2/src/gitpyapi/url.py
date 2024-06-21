import requests as _req
import io as _io
import zipfile as _zip
import os as _os
from gitpyapi import GitHubBaseError

class urllike:
    """
    Class to Manipulate URL.
    """
    def __init__(self, url: any):
        """
        Initialize the URL.
        """
        self.__type__ = type(url)
        self.__url__ = url
        
    def _convert(self):
        """
        Converted the Input URL to https and ssh URL.
        """
        if self.__type__ == str:
            if self.__url__.startswith('git@'):
                _tmp = self.__url__.split(':')
                self.__provider__ = _tmp[0].split('@')[1]
                self.__user__ = _tmp[1].split('/')[0]
                self.__repo__ = _tmp[1].split('/')[1]
            elif self.__url__.startswith('https://'):
                _tmp = self.__url__.split('/')
                self.__provider__ = _tmp[3]
                self.__user__ = _tmp[4]
                self.__repo__ = _tmp[5]
            else:
                raise GitHubBaseError('Invalid URL')
        elif self.__type__ == list:
            self.__url__ = " ".join(self.__url__)
            if self.__url__.startswith('git@'):
                _tmp = self.__url__.split(':')
                self.__provider__ = _tmp[0].split('@')[1]
                self.__user__ = _tmp[1].split('/')[0]
                self.__repo__ = _tmp[1].split('/')[1]
                if '.git' in self.__repo__:
                    self.__repo__ = self.__repo__.replace('.git', '')
            elif self.__url__.startswith('https://'):
                _tmp = self.__url__.split('/')
                self.__provider__ = _tmp[3]
                self.__user__ = _tmp[4]
                self.__repo__ = _tmp[5]
                if '.git' in self.__repo__:
                    self.__repo__ = self.__repo__.replace('.git', '')
            else:
                raise GitHubBaseError('Invalid URL')
        else:
            raise GitHubBaseError('Invalid URL')
        
        self.__ssh__ = f"git@{self.__provider__}:{self.__user__}/{self.__repo__}"
        self.__https__ = f"https://{self.__provider__}/{self.__user__}/{self.__repo__}"
    
    def __str__(self) -> tuple[str, str]:
        """
        Return the URL.
        """
        self._convert()
        return (self.__ssh__, self.__https__)
    
    def __repr__(self) -> str:
        """
        Return the URL.
        """
        self._convert()
        return f"{self.__ssh__} | {self.__https__}"
    

def url(user: str, repo: str, provider: str = 'github.com') -> tuple[str, str]:
    """
    Return the Correct SSH and HTTPS URL.
    """
    raw = f"https://{provider}/{user}/{repo}"
    return urllike(raw)

def archive(user: str = None, repo: str = None, provider: str = 'github.com', repo_url: str = None, branch: str = 'master') -> str:
    """
    Return the Correct Archiv URL.
    """
    if repo_url is None and user is None and repo is None:
        raise GitHubBaseError('Invalid Value, min a url or repo, user and provider data must given')
    
    if repo_url is not None:
        _tmp = urllike(repo_url).__https__
    else:
        _tmp = url(user, repo, provider).__https__

    arurl = f"{_tmp}/archive/{branch}.zip"
    return arurl

def clone(user: str = None, repo: str = None, provider: str = 'github.com', repo_url: str = None, branch: str = 'master') -> str:
    """
    Clone the Repo
    """
    arurl = archive(user, repo, provider, repo_url)
    repo = urllike(arurl).__repo__
    _folder_name = f"{repo}-{branch}"
    _new_name = repo
    req = _req.get(arurl)
    with open('tmp.zip', 'wb') as f:
        f.write(_io.BytesIO(req.content).read())
    with _zip.ZipFile('tmp.zip', 'r') as zip_ref:
        zip_ref.extractall(_folder_name)
    _os.rename(_folder_name, _new_name)
    _os.remove('tmp.zip')
    return _new_name