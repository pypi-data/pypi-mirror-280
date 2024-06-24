class OssError(Exception):
    pass


class KeyNotExists(OssError):
    """KEY不存在"""
    pass


class KeyExists(OssError):
    """KEY存在"""
    pass
