# -*- coding: utf-8 -*-

windowLeft = 100
windowTop = 100
windowWidth = 800
windowHeight = 700

appId = 4434173
authorizedUrl = "https://oauth.vk.com/blank.html"
authUrl = "https://oauth.vk.com/authorize?client_id={appId}&scope=2&redirect_uri={redirectUrl}&display=page&v=5.21&response_type=token".format(
          appId = appId, redirectUrl = authorizedUrl)
getFriendsUrl = "https://api.vk.com/method/friends.get?order=name&fields=first_name,last_name&access_token={accessToken}"
