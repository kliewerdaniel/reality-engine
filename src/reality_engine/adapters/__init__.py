import os, glob, json

class DirectoryAdapter:
    def __init__(self, directory):
        self.directory = directory
    def fetch(self):
        out=[]
        for p in glob.glob(os.path.join(self.directory, "*")):
            out.append({"path": p, "content": open(p).read() if os.path.isfile(p) else ""})
        return out

class RssAdapter:
    def __init__(self, feed_url):
        self.feed_url = feed_url
    def fetch(self):
        return [{"feed": self.feed_url, "items": []}]
