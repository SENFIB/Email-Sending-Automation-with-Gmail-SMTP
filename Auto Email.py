import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Give user Email
user_email = input("لطفا ایمیل خود را وارد نمایید:\n"
                   "Enter Your Email Address:\n")

# Give User Email App-Password
email_code = input("لطفا کد برنامه ی ایمیل خود را وارد نمایید:\n"
                   "Enter Your Email App-Password:\n")

# Use This App For Send Many Users AD on Email And Set The Server (Gmail)
email_server = smtplib.SMTP('smtp.gmail.com', 587)
email_server.starttls()
email_server.login(user_email, email_code)

# Set CSV To Var
send_emails = "emails.csv"
delete_emails  = "delete.csv"
for_delete = "for_delete.txt"

# Create File Csv Send Email
def add_email_to_csv(email):
    if not os.path.exists(send_emails):
        open(send_emails, "w", encoding="utf-8").close()

    with open(send_emails, 'a', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([email.casefold()])


# Give Subject Email And Set In App For Send
def subject_txt():
    with open("subject.txt", "r", encoding="utf-8") as f1:
        subject = f1.readlines()

    return ''.join(subject)


# Give Text Email And Set In App For Send
def main_txt():
    with open("main.txt", "r", encoding="utf-8") as f2:
        main = f2.readlines()

    return ''.join(main)


# Delete Users Unsubscribe
def clean_emails():

    if not os.path.exists(for_delete):
        open(for_delete, "w").close()

    if not os.path.exists(delete_emails):
        open(delete_emails, "w").close()

    with open(for_delete, 'r', encoding="utf-8") as ready_file:
        del_emails = []
        for line in ready_file:
            del_emails.append(line.strip().casefold())

    with open(delete_emails, 'w', newline="", encoding="utf-8") as delete_file:
        writer = csv.writer(delete_file)
        for email in del_emails:
            writer.writerow([email])

    with open(send_emails, 'r', newline="", encoding="utf-8") as file:
        emails = list(csv.reader(file))

    filter_email = []
    for row in emails:
        if row and row[0] not in del_emails:
            filter_email.append(row[0])

    with open(send_emails, 'w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for email in filter_email:
            writer.writerow([email])


# Give And Set The Main Email Of Subject And Text Function
subject = subject_txt()
main = main_txt()


# Send Subscribe Emails
def send_emails_to_users():

    with open(send_emails, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        emails = [row[0] for row in reader]

    msg = MIMEMultipart()
    msg['From'] = user_email
    msg['Subject'] = subject
    body = main

    msg.attach(MIMEText(body, _subtype='plain', _charset='utf-8'))

    for email in emails:
        msg['To'] = email
        email_server.sendmail(msg['From'], email, msg.as_string())
        print(f"ایمیل به {email} ارسال شد.")
        del msg['To']


# Give Users Email For Send Main Email
def collect_emails():

    while True:
        user_email = input("لطفاً ایمیل های خود را برای ارسال ایمیل وارد کنید\n"
                           " (برای خروج 'خروج' را وارد کنید):\n"
                           "Please Enter Your List Email Address\n"
                           "For Exit Type 'Exit':\n")
        if user_email.casefold() == 'خروج':
            break
        add_email_to_csv(user_email)


# Run All Functions
collect_emails()
clean_emails()
send_emails_to_users()
email_server.quit()