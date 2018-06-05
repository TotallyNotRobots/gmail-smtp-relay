import email
import fileinput
from smtplib import SMTP


def parse_message():
    with fileinput.input() as f:
        return email.message_from_string("".join(f))


def send_message(message):
    with SMTP("smtp-relay.gmail.com", port=587) as smtp:
        smtp.starttls()
        smtp.send_message(message)


def main():
    message = parse_message()
    send_message(message)


if __name__ == '__main__':
    main()
