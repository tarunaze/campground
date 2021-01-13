import smtplib

my_email = "campgroundsite@gmail.com"
his_email = "tarunvb.cs18@rvce.edu.in"
password = "camp@123"
message = "hi tarun!"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(my_email,password)
print("Login success")
server.sendmail(my_email,his_email,message)