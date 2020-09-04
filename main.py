import smtplib

# Adress and port of your SMTP provider
EMAIL_PROVIDER = "smtp.gmail.com"
EMAIL_PROVIDER_PORT = 465

# Credentials of your account at that provider
SENDING_ACCOUNT_ADRESS = ""
SENDING_ACCOUNT_PASSWORD = ""

# Params of email
ADRESSES_OF_RECEIVERS = [] # List of receiver adresses
SUBJECT = "Test"
MESSAGE = "Test message"

email_text = f"From: {SENDING_ACCOUNT_ADRESS}\nTo: {ADRESSES_OF_RECEIVERS}\nSubject: {SUBJECT}\n\n{MESSAGE}"

with smtplib.SMTP_SSL(EMAIL_PROVIDER, EMAIL_PROVIDER_PORT) as server_con:
  try:
    server_con.ehlo()
    
    server_con.login(SENDING_ACCOUNT_ADRESS, SENDING_ACCOUNT_PASSWORD)
  except Exception as e:
    print(f"Failed to init!\n{e}")

  try:
    server_con.sendmail(SENDING_ACCOUNT_ADRESS, ADRESSES_OF_RECEIVERS, email_text)
  except Exception as e:
    print(f"Failed to send email!\n{e}")