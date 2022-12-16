from statistics import fmean
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
from pytube import *
import pyperclip

class Ui_secondWindow(object):
    def setupUi(self, secondWindow):
        secondWindow.setObjectName("secondWindow")
        secondWindow.resize(538, 496)
        self.centralwidget = QtWidgets.QWidget(secondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(250, 50, 271, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.download())
        self.pushButton_2.setGeometry(QtCore.QRect(140, 350, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.saveinfo())
        self.pushButton_3.setGeometry(QtCore.QRect(280, 390, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.copy())
        self.pushButton_4.setGeometry(QtCore.QRect(10, 390, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 250, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 210, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 300, 351, 31))
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.click())
        self.pushButton_10.setGeometry(QtCore.QRect(440, 300, 93, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 440, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.scrollArea.setFont(font)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 211, 71))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 80, 211, 61))
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 211, 61))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        

        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)

        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        secondWindow.setCentralWidget(self.centralwidget)
        self.label_9.setText(os.getcwd())
        self.fname=os.getcwd()
        self.yt=''
        self.label_8.setText("")

        self.retranslateUi(secondWindow)
        QtCore.QMetaObject.connectSlotsByName(secondWindow)
    def click(self):

        self.fname=QFileDialog.getExistingDirectory( caption="Select Directory",directory="C:\\")
        print(self.fname)
        self.label_9.setText(self.fname)

    def copy(self):
        pyperclip.copy(self.yt.description)

    def saveinfo(self):
        f = open(self.fname+"/info.txt", "a")
        f.writelines(["Title: "+self.yt.title,"'\n'Author: "+self.yt.author
        ,"'\n'Channel_id : "+self.yt.channel_id,"'\n'Channel_url : "+self.yt.channel_url
        ,"'\n'Keywords : "+str(self.yt.keywords),"'\n'Publish_date : "+str(self.yt.publish_date),
        "'\n'Views : "+str(self.yt.views),"'\n'Description : "+self.yt.description])
        
        f.close()




    def download(self):
        try:
            print(self.yt.streams.get_by_itag(int(self.label_11.text())))

            self.yt.streams.get_by_itag(int(self.label_11.text())).download(self.fname)
            print("\nDownload finished !!!")
            self.label_5.setText("Download finished !!!")


        except:
            self.label_5.setText("please enter valid data ")


    def progress_function(self,chunk, file_handle, bytes_remaining):
        global filesize
        current = ((filesize - bytes_remaining)/filesize)
        percent = ('{0:.1f}').format(current*100)
        progress = int(50*current)
        status = '█' * progress + '-' * (50 - progress)
        sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
        sys.stdout.flush()


    def retranslateUi(self, secondWindow):
        _translate = QtCore.QCoreApplication.translate
        secondWindow.setWindowTitle(_translate("secondWindow", "Youtube Downloder"))
        self.label_2.setText(_translate("secondWindow", "Views : "))
        self.label_4.setText(_translate("secondWindow", "description :"))
        self.pushButton_2.setText(_translate("secondWindow", "Download"))
        self.pushButton_3.setText(_translate("secondWindow", "save info to text file"))
        self.pushButton_4.setText(_translate("secondWindow", "copy description"))
        self.label_6.setText(_translate("secondWindow", "quality to download :"))
        self.label_7.setText(_translate("secondWindow", "format to download :"))
        self.label_10.setText(_translate("secondWindow", "save to : "))
        self.pushButton_10.setText(_translate("secondWindow", "browse"))
        self.label.setText(_translate("secondWindow", "Title : "))
        self.label_3.setText(_translate("secondWindow", "Publish Date : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    secondWindow = QtWidgets.QMainWindow()
    ui = Ui_secondWindow()
    ui.setupUi(secondWindow)
    secondWindow.show()
    sys.exit(app.exec_())
