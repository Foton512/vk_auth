# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtWebKit import QWebView
from PyQt4.QtCore import QUrl
from settings import *

class MainWindow(QMainWindow):
    def __init__(self, model):
        super(MainWindow, self).__init__()
        self.model = model
        self.model.friendsReady.connect(self.showFriends)
        self.initUI()

    def initUI(self):
        self.setGeometry(windowLeft, windowTop, windowWidth, windowHeight)
        self.setWindowTitle(u"Бугагашенька")    

        mainWidget = QWidget()
        mainLayout = QVBoxLayout()
        authButton = QPushButton(u"Получить список друзей")
        authButton.clicked.connect(self.authButtonClicked)
        mainLayout.addWidget(authButton)
        self.textEdit = QTextEdit()
        mainLayout.addWidget(self.textEdit)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        self.browser = QWebView()
        self.browser.urlChanged.connect(self.browserUrlChanged)

        self.show()

    def authButtonClicked(self):
        self.browser.load(QUrl(authUrl))
        self.browser.show()

    def browserUrlChanged(self, url):
        urlStr = url.toString()
        if urlStr[:len(authorizedUrl)] == authorizedUrl:
            fragment = str(url.fragment())
            fragmentParameters = [param.split("=") for param in fragment.split("&")]
            for param in fragmentParameters:
                if param[0] == "access_token":
                    self.model.setAccessToken(param[1])
                    break

            self.browser.hide()
            self.model.getFriendsAsync()

    def showFriends(self, friendsStr):
        self.textEdit.setText(friendsStr)
