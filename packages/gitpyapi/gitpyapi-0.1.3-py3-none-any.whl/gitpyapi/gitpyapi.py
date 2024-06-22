import os as _os
import subprocess as _sp
import re as _re
import requests as _req
import abc as _abc
import typing as _typing
import json5 as _json
import sys as _sys
import shutil as _shut
import tempfile as _temp
import zipfile as _zip
import io as _io

class GitHubBaseError(Exception):
    """
    GitHub Base Exception Class.
    Use this for generally and Errors, if not an Specialized Exception is needed, use this.
    """
    def __init__(self, *args: object) -> None:
        """
        Give Arguments to the Exception.
        Generally, you should give an Message via Arguments.
        """
        self.string = " ".join(args)
        self.message = self.style()
        super().__init__(self.message)

    def style(self) -> str:
        """
        Style the String.
        """
        bred = '\033[41m'
        black = '\033[30m'
        reset = '\033[0m'
        return f"{bred}{black}{self.string}{reset}"
    
class GitHubUrlError(GitHubBaseError):
    """
    Github URL Error, Exception for Errors with the URL.
    Will be activated if the URL is not valid.
    """
    def __init__(self, *args: object) -> None:
        """
        Give Arguments to the Exception.
        """
        super().__init__('URL is not Valid: ', *args)

class RepoNotFoundError(GitHubBaseError):
    """
    Exception Class for Error, if the Github Repo Not Found.
    Will be activated if the Repo not Found.
    """
    def __init__(self, *args: object) -> None:
        """
        Give Arguments to the Exception.
        """
        super().__init__('Repo not found: ', *args)

class GitHubConnectError(GitHubUrlError):
    """
    Exception Class for Error, if the Github Connection Failed.
    Will be activated if the Connection Failed.
    """
    def __init__(self, *args: object) -> None:
        """
        Give Arguments to the Exception.
        """
        super().__init__('Connection Failed, ', *args)

class RepoPrivateError(RepoNotFoundError):
    """
    Exception Class for Error, if the Github Repo is Private.
    Will be activated if the Repo is Private.
    """
    def __init__(self, *args: object) -> None:
        """
        Give Arguments to the Exception.
        """
        super().__init__('Repo is private, ', *args)


class UrlParser:
    """
    Class to Parse any GitHub URL to an https and ssh url
    """
    def __init__(self, url: str) -> None:
        """
        Givt the URL to the Class.
        """
        self.input = url
        self.https, self.ssh = self.parse()
        self.__https__ = self.https
        self.__ssh__ = self.ssh
        self.status = self.check()

    def parse(self) -> tuple[str, str]:
        """
        Parse the URL to a https and ssh url.
        """
        if not 'github.com' in self.input:
            raise GitHubUrlError('URL is not a valid GitHub URL ' + self.input)
        if self.input.startswith('https://'):
            liste = self.input.split('/')
            user = liste[3]
            repo = liste[4]
            if not repo.endswith('.git'):
                repo += '.git'
        elif self.input.startswith('git@'):
            liste = self.input.split(':')
            liste = liste[1].split('/')
            user = liste[0]
            repo = liste[1]
            if not repo.endswith('.git'):
                repo += '.git'
        else:
            raise GitHubUrlError('URL is not a valid GitHub URL ' + self.input)
        https = f'https://github.com/{user}/{repo}'
        ssh = f'git@github.com:{user}/{repo}'
        return tuple([https, ssh])

    def check(self) -> bool:
        """
        Check the Url, if URL Reachable.
        """
        https, ssh = self.parse()
        resp = _req.get(https)
        if resp.status_code == 200:
            return True
        else:
            return False
        
    def __str__(self) -> tuple[str, str]:
        """
        Return the https and ssh url.
        """
        return self.https, self.ssh

class UrlLike(UrlParser):
    """
    Class to Create a UrlLike Object.
    """
    def __init__(self, user: str, repo: str) -> None:
        """
        Give the User and Repo to the Class.
        """
        raw = f'https://github.com/{user}/{repo}'
        super().__init__(raw)
        self.user = user
        self.repo = repo
        self.https = self.__https__
        self.ssh = self.__ssh__
        self.status = self.check()

def create(repo: str, user: str) -> UrlLike:
    """
    Create a UrlLike Object.
    """
    return UrlLike(user, repo)

def clone(repo: str, user: str, branch: str = 'master', path: str = _os.getcwd()) -> None:
    """
    Clone a Current Repo.
    """
    urlobj = create(repo, user)
    https_raw = urlobj.https
    if '.git' in https_raw:
        https_raw = https_raw.split('.git')[0]
    archive = f'{https_raw}/archive/{branch}.zip'
    resp = _req.get(archive)
    if resp.status_code == 200:
        with open(_os.path.join(path, f'{repo}.zip'), 'wb') as f:
            f.write(_io.BytesIO(resp.content).read())
        with _zip.ZipFile(_os.path.join(path, f'{repo}.zip'), 'r') as zip_ref:
            zip_ref.extractall(_os.path.join(path, repo))
        _os.remove(_os.path.join(path, f'{repo}.zip'))
        _os.remove(_os.path.join(path, f'{repo}-{branch}'))
    else:
        raise GitHubConnectError(f'Connection failed for {archive}')

def check_repo(obj: UrlLike) -> bool:
    """
    Check a Repo with Given URL Like Object.
    """
    if obj.status:
        return True
    else:
        return False
    
def check_branch(obj: UrlLike, branch: str = 'master') -> bool:
    """
    Check a Repo for Branch.
    """
    raw = obj.https
    if '.git' in raw:
        raw = raw.split('.git')[0]
    resp = _req.get(f'{raw}/tree/{branch}')
    if resp.status_code == 200:
        return True
    else:
        return False
    
def check(inpt: object, branch: str = 'master', branch_check: bool = False) -> bool:
    """
    Check if the Input is a Repo and if it is, check if the Branch exists.
    Accepted is an UrlLike object and a tuple with the type tuple[user, repo]
    """
    if isinstance(inpt, UrlLike):
        if branch_check:
            return check_branch(inpt, branch)
        else:
            return check_repo(inpt)
    elif isinstance(inpt, tuple):
        user, repo = inpt
        urlobj = create(repo, user)
        if branch_check:
            return check_branch(urlobj, branch)
        else:
            return check_repo(urlobj)
    elif isinstance(inpt, str):
        try:
            obj = UrlParser(inpt)
            if obj.ssh:
                user, repo = obj.ssh.split(':')[1].split('/')
                if repo.endswith('.git'):
                    repo = repo[:-4]  # Remove '.git' from the end of the repo string
                urlobj = create(repo, user)
                if branch_check:
                    return check_branch(urlobj, branch)
                else:
                    return check_repo(urlobj)
        except GitHubUrlError as e:
            raise GitHubUrlError('URL is not a valid GitHub URL: ' + inpt) from e
    elif isinstance(inpt, dict):
        if 'user' in inpt and 'repo' in inpt:
            urlobj = create(inpt['repo'], inpt['user'])
            if branch_check:
                return check_branch(urlobj, branch)
            else:
                return check_repo(urlobj)
        else:
            raise GitHubBaseError('Input is not a valid GitPyAPI Input Object.')
    else:
        raise GitHubBaseError('Input is not a valid GitPyAPI Input Object.')