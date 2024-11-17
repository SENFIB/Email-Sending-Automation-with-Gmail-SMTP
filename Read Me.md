# Email Sending Automation Script

This Python script allows users to collect email addresses, manage email lists, and automatically send emails to a list of recipients using Gmail's SMTP server.

## Features
- Collect email addresses from users.
- Store collected emails in a CSV file.
- Allows the user to clean up the email list by deleting certain addresses.
- Automatically send personalized emails to a list of recipients.
- User provides their Gmail email and application-specific password for login.

## Requirements
- Python 3.x
- SMTP access for Gmail
- Internet connection

## Installation

1. Clone or download the repository to your local machine.
2. Ensure that you have Python 3.x installed.
3. Install necessary dependencies (if any):
    ```bash
    pip install smtplib
    ```

## Usage

1. **Set up your Gmail account**:
   - Go to [Google Account Settings](https://myaccount.google.com/) and enable 2-Step Verification.
   - Generate an "App Password" for this script under the "Security" section. You'll use this app password instead of your regular Gmail password.

2. **Run the Script**:
    ```bash
    python script_name.py
    ```
   
3. **Steps in the script**:
    - Enter your Gmail email address.
    - Enter the app-specific password.
    - Provide a subject for the email in the `subject.txt` file.
    - Provide the email content in the `main.txt` file.
    - Enter email addresses that you want to send emails to.
    - The script will send the email to all the addresses in the CSV file.

## Files
- **subject.txt**: The subject line of the email.
- **main.txt**: The main content of the email.
- **emails.csv**: A CSV file containing all collected email addresses.
- **delete.csv**: A CSV file to store the email addresses to be deleted.
- **for_delete.txt**: A text file containing the email addresses that need to be deleted.

## Notes
- This script uses Gmail's SMTP server for sending emails. Ensure that you don't exceed the daily email sending limit (500 emails per day for regular Gmail accounts).
- For larger email campaigns, consider using services like SendGrid, Mailchimp, or Amazon SES to avoid hitting Gmail's limits.

## License
This project is licensed under the MIT License.
