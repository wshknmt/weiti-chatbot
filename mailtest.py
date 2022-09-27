import smtplib, ssl

sender_email = "wirtualnydziekanat2022@gmail.com"  # Enter your address
receiver_email = "wshknmt@gmail.com"  # Enter receiver address
password = "bjxgyfgiifotttfp"
message = """\
Subject: Hi there

This message is sent from Python."""


port = 465  # For SSL
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(sender_email, password)
smtpserver.sendmail(sender_email, receiver_email, message)
