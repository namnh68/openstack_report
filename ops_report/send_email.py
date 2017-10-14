import config
from email.mime import application
from email.mime import multipart
from email.mime import text as tx
from email.utils import formatdate
from os.path import basename
import smtplib


def send_mail(send_from=None, password=None, send_to=None, subject=None,
              text=None, file=None, server=None):
    """This function is to send a notify email to Admin.
    :param send_from: Email of dispatcher.
    :param password: Password of dispatcher.
    :param send_to: Email of receiver.
    :param subject: A subject of this email
    :param text: Content of email
    :param file: File attachment.
    :param server: Email server. If no input then gmail is a default server.
    Form server: ip_server:port_server
    :return:
    """
    # Set default options
    server = "smtp.gmail.com:587" if server is None else server
    send_from = config.email_dispatcher if send_from is None else send_from
    password = config.password_email_dis if password is None else password
    send_to = config.email_receiver if send_to is None else send_to
    subject = "Report OpenStack status" if subject is None else subject
    text = "Dear Admin \n," \
           "I would like to send an email to report the status of Openstack" \
        if text is None else text

    hostname, port = server.split(':')
    msg = multipart.MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(tx.MIMEText(text))

    with open(file, "rb") as fil:
        part = application.MIMEApplication(fil.read(), Name=basename(file))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
        msg.attach(part)

    smtp = smtplib.SMTP(host=hostname, port=port)
    smtp.starttls()
    smtp.login(user=send_from, password=password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()
