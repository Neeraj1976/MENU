

print("\t\t\t\tWelcome to our App")
print("\t\t\t\t------------------")

print("""
press 1: send WhatsApp
press 2: send SMS
press 3: call someone
press 4: mail someone
press 5: scrape top 5 results
press 6: schedule an email
press 7: send email with image attachment
press 8: run a train
press 9: Live Video Streaming
press 10: Print data in tabular Format
press 11: Rainbow color
press 12: live video through mobile cam
press 13: Search Students by College Name.....
press 14 : Create Your Own WebPage fully Automated...
press 15 : Marks Predictor
""")

ch = input("Enter your choice: ")


import all_functions

if int(ch) == 1:
	all_functions.whatmsg()
	
	
elif int(ch) == 2:
	all_functions.Sendsms()
	

elif int(ch) == 3:
	all_functions.PhoneCall()



elif int(ch) == 4:
	all_functions.sendEmail()


elif int(ch) == 5:
	all_functions.topsearch()


elif int(ch) == 6:
	all_functions.scheduleEmail()



elif int(ch) == 7:
	all_functions.email_attachment()


elif int(ch) == 8:
	all_functions.runTrain()



elif int(ch) == 9:
	all_functions.liveStream()



elif int(ch) == 10:
	all_functions.studentdata()



elif int(ch) == 11:
	all_functions.rainbowColor()



elif int(ch) == 12:
	all_functions.mobile_cam()



elif int(ch) == 13:
	all_functions.searchStudent()



elif int(ch) == 14:
	all_functions.webpage()
	
	
elif int(ch) == 15:
	
	



	
else:
    print("Invalid choice, please try again.")
    
    
    
    
	
