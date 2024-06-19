
class EmptyURLException(Exception):
    def __init__(self, message="URL is empty"):
        self.message = message
        super().__init__(self.message)


class InvalidURLException(Exception):
    def __init__(self, message="URL is invalid"):
        self.message = message
        super().__init__(self.message)


class InvalidSchemeException(Exception):
    def __init__(self, message="Schema is invalid"):
        self.message = message
        super().__init__(self.message)


class NoSchemeException(Exception):
    def __init__(self, message="No Scheme"):
        self.message = message
        super().__init__(self.message)


class NoNetLocException(Exception):
    def __init__(self, message="No Netloc"):
        self.message = message
        super().__init__(self.message)


class InvalidNetlocException(Exception):
    def __init__(self, message="Invalid Netloc"):
        self.message = message
        super().__init__(self.message)
