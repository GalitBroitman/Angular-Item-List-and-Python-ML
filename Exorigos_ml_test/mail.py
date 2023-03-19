import smtplib
import tkinter
import tkinter.messagebox as tkMessageBox

# A function that sends the email of the result to hadas.c@velismedia.com.
def sendemail(message):
    from_addr = 'hopetoworkforyou@gmail.com'
    subject = 'Finished The Program'
    login = 'hopetoworkforyou'
    password = 'velismedia'
    to = 'hadas.c@velismedia.com'

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(login, password)

        email_message = f"Subject: {subject}\n\n{message}"

        # Send the email
        server.sendmail(from_addr, to, email_message)

        tkMessageBox.showinfo("Email Sent ", 'sent message to {to}')
        print(F'sent message to {to}')

        # Close the SMTP server connection
        server.quit()

    except smtplib.SMTPException as error:
        tkMessageBox.showerror("Error ", error)
        print(F'An error occurred: {error}')



