## extract the username form a given mail
## if the mailname is : Aayush@gmail.com it gives output Aayush

mail = input("Enter the mail: ")

pos = mail.find("@")

print("The user name is : " ,mail[0:pos])