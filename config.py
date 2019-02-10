userOption = None
from aqt import mw

def getConfig():
    global userOption
    if userOption is None:
        userOption = mw.addonManager.getConfig(__name__)
    return userOption

def updateConfig():
    mw.addonManager.writeConfig(__name__,userOption)

def newConf():
    global userOption
    userOption = None
mw.addonManager.setConfigUpdatedAction(__name__,newConf)
