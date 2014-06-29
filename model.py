# -*- coding: utf-8 -*-

from PyQt4.QtCore import QObject, pyqtSignal
from threading import Thread
import json
import urllib
from settings import *

class Model(QObject):
    friendsReady = pyqtSignal(str)

    def setAccessToken(self, accessToken):
        self.accessToken = accessToken

    # Запускает getFriends в отдельном потоке. Если все делать в одном потоке, интерфейс будет висеть
    # Для запуска одного метода вряд ли будет заметно, но если делать что-то тяжелое, то еще как будет
    def getFriendsAsync(self):
        thread = Thread(target = self.getFriends)
        thread.setDaemon(True)
        thread.start()

    def getFriends(self):
        res = urllib.urlopen(getFriendsUrl.format(accessToken = self.accessToken)).read()
        resDict = json.loads(res)
        friendsStr = u"\n".join([u"{lastName} {firstName}".format(
                     lastName = friend["last_name"], firstName = friend["first_name"])
                     for friend in resDict["response"]])
        self.friendsReady.emit(friendsStr)
