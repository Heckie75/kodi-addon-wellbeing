import xbmcaddon
import xbmcgui
import sys
import time

addon = xbmcaddon.Addon()

if __name__ == "__main__":

    if len(sys.argv) > 1 and sys.argv[1] == "status":

        pass

    elif len(sys.argv) > 1 and sys.argv[1] == "action=reset":

        addon.setSettingInt("sum", -1)

    elif len(sys.argv) > 1 and sys.argv[1] == "reset":

        time.sleep(1)  # wait for settings to be saved
        addon.setSettingInt("sum", -1)

    elif len(sys.argv) > 1 and sys.argv[1] == "action=limit":

        time_ = sys.argv[2][6:]
        addon.setSetting("limit", time_)

    elif len(sys.argv) > 1 and sys.argv[1] == "limit":

        time.sleep(1)  # wait for settings to be saved
        time_ = xbmcgui.Dialog().numeric(
            2, addon.getLocalizedString(32075), addon.getSetting("limit_%i" % time.localtime().tm_wday))
        if time_:
            addon.setSetting("limit", time_)

    else:
        addon.openSettings()
