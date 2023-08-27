import ssl
import smtplib
from email.message import EmailMessage
from emoji import emojize
class User:
    def name(self):
        self.name = input("Please enter your name:\t")
        print(f"\nWelcome {self.name} to TerMail. Send email directly from TerMail.")
user1 = User()
user1.name()
while(True):
    
    print('''\nChoose the option to procced.
                1. Send email
                2. Exit from TerMail. \n''')
    op = int(input())
    if op == 2:
        exit()
    elif op == 1:
        print("\nTo send email please fill the following field.\n")
        sender_Email = str(input("Sender email :\t"))
        receiver_Email = str(input("Receiver email :"))
        print('\nUsing your password from file pass.txt.')
        password = open("pass.txt",'r').read()
        subject = str(input('''Subject :\t'''))
        body = str(input('''Body :\t'''))

        message = EmailMessage()
        message['From'] = sender_Email
        message['To'] = receiver_Email
        message['Subject'] = subject
        message.set_content(body)

        print(emojize("\n Email is sending. Please wait:hourglass_done:..."))

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
                server.login(sender_Email,password)
                server.sendmail(sender_Email,receiver_Email,message.as_string())
            print(emojize("\nCongratulation! Email is successfully sent.:check_mark_button:"))

        except Exception as e:
            print(e)

    else:
        print("You entered invalid option. Please reenter.\n")