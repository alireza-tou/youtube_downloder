from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import *
from final import Ui_secondWindow
from pytube.cli import on_progress



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        global d
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wetr = QtWidgets.QLabel(self.centralwidget)
        self.wetr.setGeometry(QtCore.QRect(10, 80, 691, 51))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        self.wetr.setFont(font)
        self.wetr.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.wetr.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.wetr.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wetr.setLineWidth(3)
        self.wetr.setMidLineWidth(0)
        self.wetr.setObjectName("wetr")
        self.zx = QtWidgets.QLineEdit(self.centralwidget)
        self.zx.setGeometry(QtCore.QRect(60, 130, 641, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zx.sizePolicy().hasHeightForWidth())
        self.zx.setSizePolicy(sizePolicy)
        self.zx.setInputMask("")
        self.zx.setText("")
        self.zx.setObjectName("zx")
        self.dfaafda = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.start())
        self.dfaafda.setGeometry(QtCore.QRect(230, 190, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dfaafda.setFont(font)
        self.dfaafda.setObjectName("dfaafda")
        self.qw = QtWidgets.QLabel(self.centralwidget)
        self.qw.setGeometry(QtCore.QRect(10, 130, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qw.setFont(font)
        self.qw.setObjectName("qw")
        self.wretrte = QtWidgets.QLabel(self.centralwidget)
        self.wretrte.setGeometry(QtCore.QRect(10, 10, 691, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wretrte.setFont(font)
        self.wretrte.setFrameShape(QtWidgets.QFrame.Box)
        self.wretrte.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wretrte.setLineWidth(2)
        self.wretrte.setMidLineWidth(1)
        self.wretrte.setAlignment(QtCore.Qt.AlignCenter)
        self.wretrte.setObjectName("wretrte")
        self.rwwret = QtWidgets.QLabel(self.centralwidget)
        self.rwwret.setGeometry(QtCore.QRect(10, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rwwret.setFont(font)
        self.rwwret.setObjectName("rwwret")
        self.wear = QtWidgets.QLabel(self.centralwidget)
        self.wear.setGeometry(QtCore.QRect(130, 250, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        font.setUnderline(True)
        self.wear.setFont(font)
        self.wear.setObjectName("wear")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    # def for start button
    def start(self):
        try:
            global yt
            #create youtube query
            yt=YouTube(self.zx.text(),on_progress)
            self.wear.setText("Url VALID")
            #load second window
            self.window= QtWidgets.QMainWindow()
            self.ui=Ui_secondWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            self.ui.label_8.setText(self.zx.text())
            MainWindow.hide()
            #add title description view
            self.ui.label_8.setText(self.zx.text())
            self.ui.label.setText(self.ui.label.text()+yt.title)
            self.ui.label_2.setText(self.ui.label_2.text()+str(yt.views))
            self.ui.label_3.setText(self.ui.label_3.text()+str(yt.publish_date)[:11])
            self.ui.textBrowser.setText(yt.description)
            #add item to combo
            self.ui.comboBox_2.addItem("choose pls")
            if len(yt.streams.filter(mime_type="video/webm"))>0:
            
                self.ui.comboBox_2.addItem("WEBM")
            if len(yt.streams.filter(only_audio=True))>0:
                self.ui.comboBox_2.addItem("AUDIO")

            if len(yt.streams.filter(progressive=True))>0:
                self.ui.comboBox_2.addItem("MP4")
            #run func after changind combo item
            self.ui.comboBox_2.activated.connect(lambda:self.choose())
            self.ui.comboBox.activated.connect(lambda:self.cho())
            self.ui.yt=yt

        except:
            self.zx.setText("")
            self.wear.setText("Url UNVALID")





    #add item to quality combo
    def choose(self):
        global d
        d=dict()
        if self.ui.comboBox_2.currentText()=="WEBM":
            
            self.ui.comboBox.clear()
            self.ui.comboBox.addItem("choose pls")
            a=yt.streams.filter(mime_type="video/webm")
            
            for i in a:
                self.ui.comboBox.addItem(i.resolution)
                d[i.resolution]=i.itag


        if self.ui.comboBox_2.currentText()=="MP4":

            self.ui.comboBox.clear()
            a=yt.streams.filter(progressive=True)
            self.ui.comboBox.addItem("choose pls")
            for i in a:
                self.ui.comboBox.addItem(i.resolution+".")
                d[i.resolution+"."]=i.itag
            

        if self.ui.comboBox_2.currentText()=="AUDIO":

            self.ui.comboBox.clear()
            self.ui.comboBox.addItem("choose pls")
            for i in yt.streams.filter(only_audio=True):
                self.ui.comboBox.addItem(i.abr)
                d[i.abr]=i.itag



    #connct data between windows  
    def cho(self):
        self.ui.label_11.setText(str(d[self.ui.comboBox.currentText()]))
        self.ui.label_5.setText("File size : "+str(self.ui.yt.streams.get_by_itag(d[self.ui.comboBox.currentText()]).filesize)+" bytes")
        



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloder"))
        self.wetr.setText(_translate("MainWindow", "Enter Url to start : "))
        self.dfaafda.setText(_translate("MainWindow", "start"))
        self.qw.setText(_translate("MainWindow", "Url :"))
        self.wretrte.setText(_translate("MainWindow", "YouTube Downloder"))
        self.rwwret.setText(_translate("MainWindow", "Url status :"))
        self.wear.setText(_translate("MainWindow", "NOT ENTERED"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
