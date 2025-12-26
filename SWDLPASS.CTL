###############################################################################
#
#  -------------------------------------------
#  - FRAMEWORX SOFTWARE DOWNLOAD VIA NETWORK -
#  -------------------------------------------
#
#  File Name: CLEARNV.SCP
#
#  FUNCTIONAL DESCRIPTION.
#	This script file is used to cause the scorer to reboot. Currently, the
#	scorer will always do a NV RAM clear prior to the rebooting via the
#	software download.  This will change once the new "CLEARNV" command is
#	added to the command interpreter.
#
#
#  MODIFICATION HISTORY.
#	T. J. Leppien	11/16/95.	Original.
#	T. J. Leppien	12/01/95.	Added the new header.
#       T. J. Leppien   10/14/96.       Added the copying of the script file
#                                       to the new c:\swdlpass.ctl.
#
###############################################################################

//
// Enable the LAN notification of success.
//

copy   (L) c:\clearnv   (L) c:\swdlpass.ctl


//
// reboot the scorer (which also clears NV RAM)
//

reboot

end

