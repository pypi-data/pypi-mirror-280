from ..scripts import Scripted
#=====================================================================

class SMessage:

    def __init__(self, **kwargs):
        self.errors = kwargs.get("errors", None)
        self.result = kwargs.get("result", None)
        self.status = kwargs.get("status", False)
        self.filesize = kwargs.get("filesize", 0)
        self.captions = kwargs.get("captions", None)
        self.location = kwargs.get("location", None)
        self.filename = kwargs.get("filename", None)
        self.filelink = kwargs.get("filelink", None)
        self.username = kwargs.get("username", None)
        self.password = kwargs.get("password", None)
        self.extension = kwargs.get("extension", ".tmp")

#=====================================================================

class BMessage:

    def __init__(self, **kwargs):
        self.formatid = kwargs.get("formatid", Scripted.DATA01)
        self.filesize = kwargs.get("filesize", Scripted.DATA01)
        self.filename = kwargs.get("filename", Scripted.DATA01)
        self.duration = kwargs.get("duration", Scripted.DATA01)
        self.formatQu = kwargs.get("formatQu", Scripted.DATA01)
        self.formatex = kwargs.get("formatex", Scripted.DATA01)

#=====================================================================
