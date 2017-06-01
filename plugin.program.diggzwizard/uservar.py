import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Diggz Fire Builds Wizard'
EXCLUDES       = [ADDON_ID, 'plugin.program.diggzwizard']
# Text File with build info in it.
BUILDFILE      = 'http://jed.one/diggzwizard.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'http://jed.one/Diggzwizardapk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Diggz Builds Youtube help videos'
YOUTUBEFILE    = 'http://jed.one/Diggzwizardyoutube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://jed.one/DiggzWizardaddons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://jed.one/DiggzWizardpngs/eminencelogo.jpg'
ICONMAINT      = 'http://jed.one/DiggzWizardpngs/maintenance.png'
ICONAPK        = 'http://jed.one/DiggzWizardpngs/apkinstaller.png'
ICONADDONS     = 'http://jed.one/DiggzWizardpngs/addoninstaller-1.png'
ICONYOUTUBE    = 'http://jed.one/DiggzWizardpngs/youtube.png'
ICONSAVE       = 'http://jed.one/DiggzWizardpngs/savedata.png'
ICONTRAKT      = 'http://jed.one/DiggzWizardpngs/trakt.png'
ICONREAL       = 'http://jed.one/DiggzWizardpngs/real-debrid-1.png'
ICONLOGIN      = 'http://jed.one/DiggzWizardpngs/login.png'
ICONCONTACT    = 'http://jed.one/DiggzWizardpngs/contact%20us.png'
ICONSETTINGS   = 'http://jed.one/DiggzWizardpngs/settingsicon.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'dodgerblue'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']Diggz[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Enjoy Diggz Fire Builds.\r\n\r\nFor support, join Diggz Tech Talk on Facebook: https://www.facebook.com/groups/1760004300910864/'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = 'http://jed.one/DiggzWizardpngs/Facebook_Contact_Directories.png'
CONTACTFANART  = 'http://jed.one/DiggzWizardpngs/fanart.jpg'
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'No'
# Url to wizard version
WIZARDFILE     = ''
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'No'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'No'
# Url to notification file
NOTIFICATION   = ''
# Use either 'Text' or 'Image'
HEADERTYPE     = ''
HEADERMESSAGE  = ''
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
#########################################################