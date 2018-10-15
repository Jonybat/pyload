# -*- coding: utf-8 -*-

from pyload.plugins.internal.deadhoster import DeadHoster


class NetloadIn(DeadHoster):
    __name__ = "NetloadIn"
    __type__ = "hoster"
    __version__ = "0.55"
    __pyload_version__ = "0.5"
    __status__ = "stable"

    __pattern__ = r"https?://(?:www\.)?netload\.(in|me)/(?P<PATH>datei|index\.php\?id=10&file_id=)(?P<ID>\w+)"
    __config__ = []  # TODO: Remove in 0.6.x

    __description__ = """Netload.in hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [
        ("spoob", "spoob@pyload.net"),
        ("RaNaN", "ranan@pyload.net"),
        ("Gregy", "gregy@gregy.cz"),
    ]