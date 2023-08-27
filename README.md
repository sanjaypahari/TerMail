# TerMail - Terminal Email Sender

TerMail is a Python program that allows you to send emails directly from the terminal. It utilizes the `smtplib` library to establish a secure connection with Gmail's SMTP server and send emails. With TerMail, you can quickly send emails without needing a graphical email client.

## Features

- Send emails using a simple command-line interface.
- Securely sends emails via Gmail's SMTP server.
- Uses SSL encryption for secure communication.

## Prerequisites

Before you start using TerMail, make sure you have the following:

1. Python 3 installed on your system.
2. Gmail account and app password (saved in a file named `pass.txt` in the same directory as the script).

## Usage

1. Open your terminal.
2. Navigate to the directory containing the `TerMail.py` script.
3. Run the script using the following command:

   ```bash
   python TerMail.py
   ```

4. You'll be prompted to enter your name. This is a one-time setup.

5. Choose an option:
   - **1**: Send email
   - **2**: Exit

6. If you choose to send an email:
   - Enter the sender's email address.
   - Enter the recipient's email address.
   - Your Gmail app password will be used for authentication.
   - Enter the email subject.
   - Enter the email body.

7. TerMail will display an emoji-based progress message while sending the email.

8. Once sent, TerMail will notify you of the successful email transmission or display an error if something goes wrong.

## Note

- Make sure to enable "Less secure app access" for your Gmail account if you encounter authentication issues.
- For security reasons, do not hardcode your Gmail password in the script; use an app password stored in `pass.txt`.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to contribute to this project by adding more features or improving its functionality. If you encounter any issues or have suggestions, please create an issue on the GitHub repository.
```
