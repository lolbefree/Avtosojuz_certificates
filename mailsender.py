import smtplib
import ssl
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart  # New line
from email.mime.base import MIMEBase  # New line
from email import encoders  # New line
from PIL import Image
import os
import time
import win32com.client as win32


def sender(receiver_emails, receiver_names, name_file):
    print("use sender")

    # User configuration
    sender_email = "Gift_cert@avtosojuz.ua"
    sender_name = "Gift_cert"

    receiver_emails = [receiver_emails]
    receiver_names = [receiver_names]
    filename2 = f"{name_file}"
    print(name_file, receiver_emails, receiver_names)
    # Email body

    text = """Ви придбали автомобіль VW і ми пропонуємо Вам скористатися подарунковим сертифікатом на обслуговування автомобіля.
У Вас є можливість провести технічне обслуговування автомобіля та оплатити вартість робіт та запчастин подарунковим сертифікатом.
Сертифікат не можна обміняти на гроші. Сплачені сертифікатом послуги або запчастини поверненню не підлягають.
Термін дії сертифіката 3 роки з моменту видачі.
Ваш АВТОСОЮЗ!
"""
    email_body = """<p>{}</p>""".format(text)


    for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
            # Configurating user's info
            msg = MIMEMultipart()
            msg['To'] = formataddr((receiver_name, receiver_email))
            msg['From'] = formataddr((sender_name, sender_email))
            msg['Subject'] = 'Подарунковий сертифікат для Вас, ' + receiver_name

            msg.attach(MIMEText(email_body, 'html'))

            try:
                # Open PDF file in binary mode
                cwd = os.getcwd()
                f = f"{cwd}\\" + filename2
                print(f)
                with open(f, "rb") as attachment:
                                part = MIMEBase("application", "octet-stream")
                                part.set_payload(attachment.read())

                # Encode file in ASCII characters to send by email
                encoders.encode_base64(part)

                # Add header as key/value pair to attachment part
                part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= giftcert.png",
                )
                msg.attach(part)
            except Exception as e:
                    break

            try:
                    # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
                    server = smtplib.SMTP('10.10.10.47', 25)
                    # Encrypts the email
                    # We log in into our Google account
                    # Sending email from sender, to receiver with the email body
                    server.sendmail(sender_email, receiver_email, msg.as_string())
            except Exception as e:
                    break
            #finally:
                    #server.quit()
                   # time.sleep(20)


def add_attachments(to_address, filename):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = '{}'.format(to_address)
    mail.Subject = ''
    mail.Body = ''
    mail.HTMLBody = '<h2></h2>'  # this field is optional

    # To attach a file to the email (optional):
    attachment = filename
    print(attachment)
    mail.Attachments.Add(attachment)
    mail.display()

