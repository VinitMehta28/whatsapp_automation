
import pywhatkit
# import win32clipboard(optional)
from datetime import datetime

# Send a whatsapp Message to a contact at current time 
 pywhatkit.sendwhatmsg('+919157746137', 'Hi', datetime.now().hour, datetime.now().minute)

# Send a whatsapp Message to a contact current time plus 2 mminutes Message will be Delivered. 
 pywhatkit.sendwhatmsg('+919157746137', 'Hi', datetime.now().hour, datetime.now().minute + 1)

#  Send an Image to a Contact in whatsapp with the no Caption
 pywhatkit.sendwhats_image("+919157746137", "images/imagez.jpg",7, 56)
 pywhatkit.sendwhats_image("+919157746137", "images/imagez.jpg",datetime.now().hour, datetime.now().minute + 1)

# send image in Whatsapp Group with Caption Message that you want to give.
pywhatkit.sendwhats_image('FDO9PTe4UD0DG2B02c8Na5',"images/imageaz.jpg", 'Hi', datetime.now().hour, datetime.now().minute)

# send image in Whatsapp Group with no Caption Message.
 pywhatkit.sendwhatmsg_to_group('FDO9PTe4UD0DG2B02c8Na5', 'Hi', datetime.now().hour, datetime.now().minute + 1 )


# send a Whatsapp Group Message  to a Specific Time .
 pywhatkit.sendwhatmsg_to_group('FDO9PTe4UD0DG2B02c8Na5', 'Hi',  7, 38)

# send a Whatsapp Group Messge Instantly.
 pywhatkit.sendwhatmsg_to_group_instantly("FDO9PTe4UD0DG2B02c8Na5", "Hey All!")


