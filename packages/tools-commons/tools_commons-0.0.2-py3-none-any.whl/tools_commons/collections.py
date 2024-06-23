class LoadingDict(dict):
    def __init__(self, loader, seq=None, **kwargs):
        super().__init__(seq=seq, **kwargs)
        self.loader = loader

    def __missing__(self, key):
        self[key] = self.loader(key)
        return self[key]
