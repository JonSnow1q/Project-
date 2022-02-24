mportpywhatkit
 #SendaWhatsAppMessagetoaContactat1:30PM 
pywhatkit.sendwhatmsg("+910123456789","Hi",13,30) 
#SameasabovebutClosestheTabin2SecondsafterSendingtheMessage
 pywhatkit.sendwhatmsg("+910123456789","Hi",13,30,15,True,2)
#SendanImagetoaGroupwiththeCaptionasHello 
pywhatkit.sendwhats_image("AB123CDEFGHijklmn","Images/Hello.png", "Hello")
 #SendanImagetoaContactwiththenoCaption 
pywhatkit.sendwhats_image("+910123456789","Images/Hello.png")
 #SendaWhatsAppMessagetoaGroupat12:00AM
 pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn","HeyAll!",0,0) 
#SendaWhatsAppMessagetoaGroupinstantly 
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn","Hey All!") 
#PlayaVideoonYouTube pywhatkit.playonyt("PyWhatKit")
