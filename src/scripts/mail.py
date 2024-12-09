import smtplib

From = "efimovilya9087@gmail.com"
password = "sc67Ui192sdL"
Subject = "Successfully"
Text = ("Your authorisation is complete!"
            "Thanks for your support with our test project.")

def send_mail(email: str):
    To = email

    smtp_server = smtplib.SMTP("smtp.email.com", 5090)
    smtp_server.starttls()
    smtp_server.login(From, password)

    smtp_server.sendmail(From, To,
                         f"Subject: {Subject}\n\n{Text}")

    smtp_server.quit()

send_mail(email="sasha916382@gmail.com")