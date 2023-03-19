__author__ = 'wolfenfeld'
from tkinter import Tk
from tkinter import ttk
import tkinter
from svm_handler import SVMHandler
from mail import sendemail
import threading


def run_gui():
    root = Tk()
    root.title("SVM GUI")
    mainframe = tkinter.Frame(root)
    mainframe.pack()

    svm_handler = SVMHandler()


    # Here you need to start the training of the svm. Remember, the other actions (testing/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def activate_train():
        #start the training function on a new thread
        thread = threading.Thread(target=svm_handler.train)
        thread.start()

    # Here you need to start the testing with the svm. Remember, the other actions (training/sending mail) must be
    # responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def activate_test(showMessage):
        test_error_result = svm_handler.test(showMessage = showMessage)
        return test_error_result
        

    def handle_test_result():
        #start the testing function on a new thread
        thread = threading.Thread(target=activate_test(True))
        thread.start()

    # Here you need to send an email with the svm testing result. Remember, the other actions (training/testing)
    # must be responsive to users actions (i.e. hitting their button)- How can this be achieved?
    def send_mail():
        #start the email sending function on a new thread
        message  = 'The error percentage is: ' + str(activate_test(False))
        thread = threading.Thread(target=sendemail(message))
        thread.start()

    # Here you need to implement three buttons, one for each action.

    train_button = ttk.Button(root, text="Train", command=activate_train)
    train_button.pack()

    test_button = ttk.Button(root, text="Test", command=handle_test_result)
    test_button.pack()

    email_button = ttk.Button(root, text="Send Email", command=send_mail)
    email_button.pack()

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
