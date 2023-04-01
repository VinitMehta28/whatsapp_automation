
import pywhatkit
# import win32clipboard
from datetime import datetime

# # Send a whatsapp Message to a contact at current time 
# pywhatkit.sendwhatmsg('+919157746137', 'Hi', datetime.now().hour, datetime.now().minute)

# # Send a whatsapp Message to a contact current time plus 2 mminutes Message will be Delivered. 
# pywhatkit.sendwhatmsg('+919157746137', 'Hi', datetime.now().hour, datetime.now().minute + 1)

# # Send an Image to a Contact in whatsapp with the no Caption
# pywhatkit.sendwhats_image("+919157746137", "images/imagez.jpg",7, 56)
# pywhatkit.sendwhats_image("+919157746137", "images/imagez.jpg",datetime.now().hour, datetime.now().minute + 1)

# # send image in Whatsapp Group with Caption Message that you want to give.
pywhatkit.sendwhats_image('FDO9PTe4UD0DG2B02c8Na5',"images/imageaz.jpg", 'Hi', datetime.now().hour, datetime.now().minute)

# # send image in Whatsapp Group with no Caption Message.
# pywhatkit.sendwhatmsg_to_group('FDO9PTe4UD0DG2B02c8Na5', 'Hi', datetime.now().hour, datetime.now().minute + 1 )


# # send a Whatsapp Group Message  to a Specific Time .
# pywhatkit.sendwhatmsg_to_group('FDO9PTe4UD0DG2B02c8Na5', 'Hi',  7, 38)

# send a Whatsapp Group Messge Instantly.
# pywhatkit.sendwhatmsg_to_group_instantly("FDO9PTe4UD0DG2B02c8Na5", "Hey All!")
# input('Enter...')



# import pywhatkit

# # Send a WhatsApp Message to a Contact at 1:30 PM
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

# # Same as above but Closes the Tab in 2 Seconds after Sending the Message
# pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# # Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# # Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# # Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# # Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# # Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")