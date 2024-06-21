class GitHubBaseError(Exception):
    """
    Base Exception Class for GitPyAPI.
    Is the Base Class for all other Exceptions in the GitPyAPI Runtime.
    """
    def __init__(self, content: any):
        """
        Initial the Exception Class.
        """
        if type(content).__name__ == 'str':
            self.__message__ = content
        elif type(content).__name__ == 'list':
            self.__message__ = " ".join(content)
        else:
            raise TypeError("'content' must be type: 'str' or 'list'.")
        self.__type__ = type(content).__name__
        super().__init__(self._style(content))

    @staticmethod
    def _get_color(code: int) -> str:
        """
        Get the Color.
        """
        if code > 9:
            raise ValueError("The Color int value should not be Higher then 9")
        color = f"\033[3{str(code)}m"
        return color

    @staticmethod
    def _style(*args: object):
        """
        Style the Content.
        """
        _tmp = []
        for arg in args:
            _tmp.append(arg)
        content = " ".join(_tmp)
        red = 1
        green = 2
        yellow = 3
        cyan = 6
        reset = 0
        message = GitHubBaseError._get_color(red) + "[" + GitHubBaseError._get_color(green) + "*" + GitHubBaseError._get_color(red) + "]" + GitHubBaseError._get_color(reset) + " " + GitHubBaseError._get_color(cyan) + content +  GitHubBaseError._get_color(reset)
        return message