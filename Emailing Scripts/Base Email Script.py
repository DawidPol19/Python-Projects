# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:04:11 2020

@author: Dawid
"""
#Library Import
#!/usr/bin/python

#Login Details
send_from = 'examplemail@gmail.com'
password = '*******'

#Mailing List File
email_list_name = 'TemplateCSV.xlsx'

#Email Text Content
def content(salutation, first_name, area, area_content):
    email_content = """\
Hi {}. {},
    
I hope you are doing great. I heard that you have a strong background in {}.
    
{}
    
I have attached a pdf that I think would be of most interest to you.
    
Kind Regards,
    
Dawid Polanski
+44 (0) 07777 777 777
dawidpolanski4869@gmail.com""".format(salutation, first_name, area, area_content)
    
    return email_content

#Email Attachments
files = ['Example PDF.pdf']
files_list = [files]

#Importing Libraries
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import pandas as pd

#Mail Backend
#email_file = pd.read_csv(email_list_name)        #For CSV export from CRMs when using a csv file.
email_file = pd.read_excel(email_list_name)

def send_mail(send_to, send_from, password, email_subject, salutation, first_name, last_name, area, area_content, list_number):
    msg = MIMEMultipart()
    msg['Subject'] = email_subject
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)

    msg.attach(MIMEText(content(salutation, first_name, area, area_content), 'plain'))
    
    #Attaching Files
    for f in files_list[list_number]:
        with open(f, "rb") as opened:
            openedfile = opened.read()
        attachedfile = MIMEApplication(openedfile, _subtype = "pdf")
        attachedfile.add_header('content-disposition', 'attachment', filename = f)
        msg.attach(attachedfile)  
    
    #Creating SMTP Session for Gmail Email
    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.login(send_from, password)
    session.sendmail(send_from, send_to, msg.as_string())
    session.quit()

#Function repeat for all emails
for i in range(email_file.shape[0]):
    send_to = email_file['E-mail'][i]
    salutation = email_file['Salutation'][i]
    first_name = email_file['First Name'][i]
    last_name = email_file['Last Name'][i]
    email_subject = email_file['Email Subject'][i]
    area = email_file['Area'][i].lower()
    area_content = email_file['Area Content'][i]
    list_number = int(email_file['List Number'][i])-1
    send_mail(send_to, send_from, password, email_subject, salutation, first_name, last_name, area, area_content, list_number)