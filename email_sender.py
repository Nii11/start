# %%
def get_Contacts(filename):
    name=[]
    email_id=[]
    with open (filename, mode='r', encoding='utf-8') as contact_file:
        for a in contact_file:
            name.append(a.split()[0])
            email_id.append(a.split()[1])
        return name, email_id
    
    

# %%
from string import Template

# %%
def read_template(filename):
    with open(filename,mode='r',encoding='utf-8') as template_file:
        template_file_content=template_file.read()
    return Template(template_file_content)

# %%
import smtplib

# %%
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

# %%


def main():

    names, email_id=get_Contacts('contacts.txt') # read contacts

    message_template = read_template('message.txt')



    # set up the SMTP server

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)

    s.starttls()

    s.login("greedp1234@gmail.com", "Greedp11234")



    # For each contact, send the email:

    for name, email in zip(names, email_id):

        msg = MIMEMultipart()       # create a message



        # add in the actual person name to the message template

        message = message_template.substitute(PERSON_NAME=name.title())



        # Prints out the message body for our sake

        print(message)



        # setup the parameters of the message

        msg['From']='greedp1234@gmail.com'

        msg['To']=email
        
        msg['Subject']="This is TEST"
        
        msg['Bcc']='greedp1234@gmail.com'
        

        # add in the message body

        msg.attach(MIMEText(message, 'plain'))

        

        # send the message via the server set up earlier.

        s.send_message(msg)

        del msg

        

    # Terminate the SMTP session and close the connection

    s.quit()

# %%
