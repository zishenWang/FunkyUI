# This file is generated by objective.metadata
#
# Last update: Sun Mar 22 08:55:49 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$NSPrefPaneHelpMenuAnchorKey$NSPrefPaneHelpMenuInfoPListKey$NSPrefPaneHelpMenuTitleKey$NSPreferencePaneCancelUnselectNotification$NSPreferencePaneDoUnselectNotification$NSPreferencePaneSwitchToPaneNotification$NSPreferencePaneUpdateHelpMenuNotification$NSPreferencePrefPaneIsAvailableNotification$"""
enums = """$NSUnselectCancel@0$NSUnselectLater@2$NSUnselectNow@1$"""
misc.update(
    {
        "kNSPrefPaneHelpMenuAnchorKey": "anchor",
        "kNSPrefPaneHelpMenuTitleKey": "title",
        "kNSPrefPaneHelpMenuInfoPListKey": "NSPrefPaneHelpAnchors",
    }
)
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"NSPreferencePane", b"autoSaveTextFields", {"retval": {"type": "Z"}})
    r(b"NSPreferencePane", b"isSelected", {"retval": {"type": "Z"}})
    r(b"NSPreferencePane", b"replyToShouldUnselect:", {"arguments": {2: {"type": "Z"}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE