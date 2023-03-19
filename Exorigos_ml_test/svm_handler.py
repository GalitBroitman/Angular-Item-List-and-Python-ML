from sklearn import svm
from parse_data import parse_data
from calc_error_pct import *
import tkinter
from datetime import datetime
import tkinter.messagebox as tkMessageBox


class SVMHandler:
    """ In this class you will implement the classifier and it's methods. """

    data_file_path = 'data/adult.data'
    test_file_path = 'data/adult.test'
    # Load the training data
    train_data = parse_data(data_file_path)
    global train_X 
    train_X  = train_data[0]  # select the first 13 columns as features
    global train_Y
    train_Y = train_data[1]  # select the 14th column as the label (income)

    # Load the testing data
    test_data = parse_data(test_file_path)
    global test_X 
    test_X  = test_data[0]  # select the first 13 columns as features
    global test_Y
    test_Y = test_data[1]  # select the 14th column as the label (income)
   

    def __init__(self):
        self.clf = svm.SVC(kernel='linear')
    
    def train(self):
        #train the SVM classifier on a given dataset
        self.clf.fit(train_X, train_Y)
        tkMessageBox.showinfo("Training the Learner ", "Training the Learner finished")

        
    def test(self, showMessage):
        try:
            #predict the target values of the test data.
            y_pred = self.clf.predict(test_X)
            #calculates error percentage with the test and prdicted vectors
            error = calculate_error_percentage(test_Y, y_pred)
            if showMessage == True:
                tkMessageBox.showinfo("Testing the Learner ", "Testing the Learner finished and the error is " + str(error))
            return error
        except:
            tkMessageBox.showinfo("Testing the Learner ", "Training the Learner is not finished yet")
