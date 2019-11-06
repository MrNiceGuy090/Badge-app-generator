
import sys
import os
from join import brain
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

inputFolder = "dss"
outputFolder = "as"
nr=0
WidthMin = [0,0,0,0,0,0]
WidthMax = [0,0,0,0,0,0]
Height = [0,0,0,0,0,0]
FontSize= [0,0,0,0,0,0]
FontName = [0,0,0,0,0,0]
TextColor = [0,0,0,0,0,0]
TextAlign = [0,0,0,0,0,0]

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Badge Creator'
        self.left = 10
        self.top = 10
        self.width = 1600
        self.borderRadius = 50
        self.height = 600
        self.initUI()


    def initUI(self):
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setObjectName("MainWindow")

        self.setAutoFillBackground(True)

        self.close = QPushButton("X", self)
        self.close.move(1520,0)
        self.close.clicked.connect(self.closeFunc)


        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #primul buton pt folder
        button1 = QPushButton('Select input folder', self)
        button1.move(10,40)
        button1.clicked.connect(self.on_click1)
        self.label1 = QLabel("                                                                                                                ",self)
        self.label1.move(110,45)
        #al doilea buton pt folder
        button2 = QPushButton('Select output folder', self)
        button2.move(10,80)
        button2.clicked.connect(self.on_click2)
        self.label2 = QLabel("                                                                                                                ",self)
        self.label2.move(110,85)

        #font
        QFontDatabase.addApplicationFont("BebasNeue-Regular.otf")
        self.font = QFont("BebasNeue-Regular", 30)
        #imagine cu badge
        label = QLabel(self)
        badge= QPixmap('badge.jpg')
        pixmap = QPixmap('badge.jpg').scaledToWidth(400)
        self.raport = pixmap.width()/badge.width()
        label.setPixmap(pixmap)
        label.move(1100, 50)
        #coord poza
        self.pozLabel = QLabel("Poza colt stanga sus",self)
        self.pozLabel.move(550,50)

        self.widthPoza1 = QLineEdit(self)
        self.widthPoza1.move(660,50)
        self.heightPoza1 = QLineEdit(self)
        self.heightPoza1.move(800,50)

        self.pozLabel = QLabel("Poza colt dreapta jos",self)
        self.pozLabel.move(550,100)

        self.widthPoza2 = QLineEdit(self)
        self.widthPoza2.move(660,100)
        self.heightPoza2 = QLineEdit(self)
        self.heightPoza2.move(800,100)

        self.showPoza = QPushButton('see',self)
        self.showPoza.move(970,70)
        self.showPoza.clicked.connect(self.putPoza)

        self.poza = QLabel(self)

        # setare numar de label-uri
        self.nrLabels = QLineEdit(self)
        self.nrLabels.move(110,500)
        self.nrLabels.resize(80,20)
        self.nrLabelsLbs = QLabel("number of labels",self)
        self.nrLabelsLbs.move(10,500)

        #head texts
            # widths and height
        self.widthMinLabel =    QLabel("width min",self)
        self.widthMinLabel.move(40,140)
        self.widthMinLabel =    QLabel("width max",self)
        self.widthMinLabel.move(100,140)
        self.widthMinLabel =    QLabel("height",self)
        self.widthMinLabel.move(160,140)
            # text align
        self.textAlignLabel = QLabel("left/center/right",self)
        self.textAlignLabel.move(720,140)
        #text color label
        self.textColorLabel = QLabel("cmyk color",self)
        self.textColorLabel.move(580,140)
        #primul coordonare pt text

        self.labelCoord1 = QLabel("1",self)
        self.labelCoord1.move(10,180)
        self.coordWidth1 = QLineEdit(self)
        self.coordWidth1.resize(40,20)
        self.coordWidth1.move(40,180)
        self.coordWidthMax1 =  QLineEdit(self)
        self.coordWidthMax1.resize(40,20)
        self.coordWidthMax1.move(100,180)
        self.coordHeight1 = QLineEdit(self)
        self.coordHeight1.resize(40,20)
        self.coordHeight1.move(160,180)
        self.coordLabel1 = QLabel(self)
        self.coordLabel1.setFont(self.font)
        self.coordLabel1.move(224,180)
        self.fontLabel1 = QLabel("font size",self)
        self.fontLabel1.move(230,180)
        self.fontSize1 = QLineEdit(self)
        self.fontSize1.setText("20")
        self.fontSize1.resize(50,20)
        self.fontSize1.move(280,180)
        self.fontName1 = QLabel("font name",self)
        self.fontName1.move(350,180)
        self.fontNameBox1 = QLineEdit(self)
        self.fontNameBox1.move(420,180)
        self.pickColor1 = QLineEdit("(0,0,0,0)",self)
        self.pickColor1.move(560,180)
        self.textAlign1  =QLineEdit("left",self)
        self.textAlign1.move(700, 180)
        self.buttonGetCoord1 = QPushButton('see',self)
        self.buttonGetCoord1.move(1000,180)
        self.buttonGetCoord1.clicked.connect(self.showCoord1)

        self.labelCoord2 = QLabel("2",self)
        self.labelCoord2.move(10,230)
        self.coordWidth2 = QLineEdit(self)
        self.coordWidth2.resize(40,20)
        self.coordWidth2.move(40,230)
        self.coordWidthMax2 =  QLineEdit(self)
        self.coordWidthMax2.resize(40,20)
        self.coordWidthMax2.move(100,230)
        self.coordHeight2 = QLineEdit(self)
        self.coordHeight2.resize(40,20)
        self.coordHeight2.move(160,230)
        self.coordLabel2 = QLabel("                                                  ",self)
        self.coordLabel2.setFont(self.font)
        self.coordLabel2.move(224,230)
        self.fontLabel2 = QLabel("font size",self)
        self.fontLabel2.move(230,230)
        self.fontSize2 = QLineEdit(self)
        self.fontSize2.setText("20")
        self.fontSize2.resize(50,20)
        self.fontSize2.move(280,230)
        self.fontName2 = QLabel("font name",self)
        self.fontName2.move(350,230)
        self.fontNameBox2 = QLineEdit(self)
        self.fontNameBox2.move(420,230)
        self.pickColor2 = QLineEdit("(0,0,0,0)",self)
        self.pickColor2.move(560,230)
        self.textAlign2  =QLineEdit("left",self)
        self.textAlign2.move(700, 230)
        self.buttonGetCoord2 = QPushButton('see',self)
        self.buttonGetCoord2.move(1000,230)
        self.buttonGetCoord2.clicked.connect(self.showCoord2)

        self.labelCoord3 = QLabel("3",self)
        self.labelCoord3.move(10,280)
        self.coordWidth3 = QLineEdit(self)
        self.coordWidth3.resize(40,20)
        self.coordWidth3.move(40,280)
        self.coordWidthMax3 =  QLineEdit(self)
        self.coordWidthMax3.resize(40,20)
        self.coordWidthMax3.move(100,280)
        self.coordHeight3 = QLineEdit(self)
        self.coordHeight3.resize(40,20)
        self.coordHeight3.move(160,280)
        self.coordLabel3 = QLabel("                                                  ",self)
        self.coordLabel3.setFont(self.font)
        self.coordLabel3.move(224,280)
        self.fontLabel3 = QLabel("font size",self)
        self.fontLabel3.move(230,280)
        self.fontSize3 = QLineEdit(self)
        self.fontSize3.setText("20")
        self.fontSize3.resize(50,20)
        self.fontSize3.move(280,280)
        self.fontName3 = QLabel("font name",self)
        self.fontName3.move(350,280)
        self.fontNameBox3 = QLineEdit(self)
        self.fontNameBox3.move(420,280)
        self.pickColor3 = QLineEdit("(0,0,0,0)",self)
        self.pickColor3.move(560,280)
        self.textAlign3  =QLineEdit("left",self)
        self.textAlign3.move(700, 280)
        self.buttonGetCoord3 = QPushButton('see',self)
        self.buttonGetCoord3.move(1000,280)
        self.buttonGetCoord3.clicked.connect(self.showCoord3)

        self.labelCoord4 = QLabel("4",self)
        self.labelCoord4.move(10,330)
        self.coordWidth4 = QLineEdit(self)
        self.coordWidth4.resize(40,20)
        self.coordWidth4.move(40,330)
        self.coordWidthMax4 =  QLineEdit(self)
        self.coordWidthMax4.resize(40,20)
        self.coordWidthMax4.move(100,330)
        self.coordHeight4 = QLineEdit(self)
        self.coordHeight4.resize(40,20)
        self.coordHeight4.move(160,330)
        self.coordLabel4 = QLabel("                                                  ",self)
        self.coordLabel4.setFont(self.font)
        self.coordLabel4.move(224,330)
        self.fontLabel4 = QLabel("font size",self)
        self.fontLabel4.move(230,330)
        self.fontSize4 = QLineEdit(self)
        self.fontSize4.setText("20")
        self.fontSize4.resize(50,20)
        self.fontSize4.move(280,330)
        self.fontName4 = QLabel("font name",self)
        self.fontName4.move(350,330)
        self.fontNameBox4 = QLineEdit(self)
        self.fontNameBox4.move(420,330)
        self.pickColor4 = QLineEdit("(0,0,0,0)",self)
        self.pickColor4.move(560,330)
        self.textAlign4  =QLineEdit("left",self)
        self.textAlign4.move(700, 330)
        self.buttonGetCoord4 = QPushButton('see',self)
        self.buttonGetCoord4.move(1000,330)
        self.buttonGetCoord4.clicked.connect(self.showCoord4)

        self.labelCoord5 = QLabel("5",self)
        self.labelCoord5.move(10,380)
        self.coordWidth5 = QLineEdit(self)
        self.coordWidth5.resize(40,20)
        self.coordWidth5.move(40,380)
        self.coordWidthMax5 =  QLineEdit(self)
        self.coordWidthMax5.resize(40,20)
        self.coordWidthMax5.move(100,380)
        self.coordHeight5 = QLineEdit(self)
        self.coordHeight5.resize(40,20)
        self.coordHeight5.move(160,380)
        self.coordLabel5 = QLabel("                                                  ",self)
        self.coordLabel5.setFont(self.font)
        self.coordLabel5.move(224,380)
        self.fontLabel5 = QLabel("font size",self)
        self.fontLabel5.move(230,380)
        self.fontSize5 = QLineEdit(self)
        self.fontSize5.setText("20")
        self.fontSize5.resize(50,20)
        self.fontSize5.move(280,380)
        self.fontName5 = QLabel("font name",self)
        self.fontName5.move(350,380)
        self.fontNameBox5 = QLineEdit(self)
        self.fontNameBox5.move(420,380)
        self.pickColor5 = QLineEdit("(0,0,0,0)",self)
        self.pickColor5.move(560,380)
        self.textAlign5  =QLineEdit("left",self)
        self.textAlign5.move(700, 380)
        self.buttonGetCoord5 = QPushButton('see',self)
        self.buttonGetCoord5.move(1000,380)
        self.buttonGetCoord5.clicked.connect(self.showCoord5)

        self.labelCoord6 = QLabel("6",self)
        self.labelCoord6.move(10,430)
        self.coordWidth6 = QLineEdit(self)
        self.coordWidth6.resize(40,20)
        self.coordWidth6.move(40,430)
        self.coordWidthMax6 =  QLineEdit(self)
        self.coordWidthMax6.resize(40,20)
        self.coordWidthMax6.move(100,430)
        self.coordHeight6 = QLineEdit(self)
        self.coordHeight6.resize(40,20)
        self.coordHeight6.move(160,430)
        self.coordLabel6 = QLabel("                                                  ",self)
        self.coordLabel6.setFont(self.font)
        self.coordLabel6.move(224,430)
        self.fontLabel6 = QLabel("font size",self)
        self.fontLabel6.move(230,430)
        self.fontSize6 = QLineEdit(self)
        self.fontSize6.setText("20")
        self.fontSize6.resize(50,20)
        self.fontSize6.move(280,430)
        self.fontName6 = QLabel("font name",self)
        self.fontName6.move(350,430)
        self.fontNameBox6 = QLineEdit(self)
        self.fontNameBox6.move(420,430)
        self.pickColor6 = QLineEdit("(0,0,0,0)",self)
        self.pickColor6.move(560,430)
        self.textAlign6  =QLineEdit("left",self)
        self.textAlign6.move(700, 430)
        self.buttonGetCoord6 = QPushButton('see',self)
        self.buttonGetCoord6.move(1000,430)
        self.buttonGetCoord6.clicked.connect(self.showCoord6)





        #butonul de merge
        mergeButon = QPushButton('Create badges', self)
        mergeButon.move(100,540)
        mergeButon.clicked.connect(self.merge)

        self.mergeLabel = QLabel("           ",self)
        self.mergeLabel.move(500,560)

        self.show()


    def on_click1(self):
        def pick_new():
            dialog = QFileDialog()
            folder_path = dialog.getExistingDirectory(None, "Select Folder")
            return folder_path
        global inputFolder
        inputFolder = pick_new()
        self.label1.setText(inputFolder)



    def on_click2(self):
        def pick_new():
            dialog = QFileDialog()
            folder_path = dialog.getExistingDirectory(None, "Select Folder")
            return folder_path
        global outputFolder
        outputFolder = pick_new()
        self.label2.setText(outputFolder)

    def putPoza(self):

        placeholder = QPixmap('placeholder.jpg')
        print(int(self.widthPoza2.text()) - int(self.widthPoza1.text()), int(self.heightPoza2.text()) - int(self.heightPoza1.text()))
        self.poza.setPixmap(placeholder)
        self.poza.move( 1100 +int(self.widthPoza1.text())*self.raport , 50+ int(self.heightPoza1.text())*self.raport )
        self.poza.resize(int(self.widthPoza2.text())*self.raport - int(self.widthPoza1.text())*self.raport, int(self.heightPoza2.text())*self.raport - int(self.heightPoza1.text())*self.raport)




    def merge(self):
        global inputFolder, outputFolder, nr, WidthMin, WidthMax, Height, FontSize, FontName, TextAlign, TextColor
        nr = int(self.nrLabels.text())
        Colt1 = [ int(self.widthPoza1.text()) , int(self.heightPoza1.text()) ]
        Colt2 = [ int(self.widthPoza2.text()) , int(self.heightPoza2.text()) ]

        if nr>=1:
            WidthMin[0] = int(self.coordWidth1.text())
            WidthMax[0] = int(self.coordWidthMax1.text())
            Height[0] = int(self.coordHeight1.text())
            FontSize[0] = int(self.fontSize1.text())
            FontName[0] = self.fontNameBox1.text()
            TextColor[0] = eval(self.pickColor1.text())
            TextAlign[0] = self.textAlign1.text()


        if nr>=2:
            WidthMin[1] = int(self.coordWidth2.text())
            WidthMax[1] = int(self.coordWidthMax2.text())
            Height[1] = int(self.coordHeight2.text())
            FontSize[1] = int(self.fontSize2.text())
            FontName[1] = self.fontNameBox2.text()
            TextColor[1] = eval(self.pickColor2.text())
            TextAlign[1] = self.textAlign2.text()

        if nr>=3:
            WidthMin[2] = int(self.coordWidth3.text())
            WidthMax[2] = int(self.coordWidthMax3.text())
            Height[2] = int(self.coordHeight3.text())
            FontSize[2] = int(self.fontSize3.text())
            FontName[2] = self.fontNameBox3.text()
            TextColor[2] = eval(self.pickColor3.text())
            TextAlign[2] = self.textAlign3.text()

        if nr>=4:
            WidthMin[3] = int(self.coordWidth4.text())
            WidthMax[3] = int(self.coordWidthMax4.text())
            Height[3] = int(self.coordHeight4.text())
            FontSize[3] = int(self.fontSize4.text())
            FontName[3] = self.fontNameBox4.text()
            TextColor[3] = eval(self.pickColor4.text())
            TextAlign[3] = self.textAlign4.text()

        if nr>=5:
            WidthMin[4] = int(self.coordWidth5.text())
            WidthMax[4] = int(self.coordWidthMax5.text())
            Height[4] = int(self.coordHeight5.text())
            FontSize[4] = int(self.fontSize5.text())
            FontName[4] = self.fontNameBox5.text()
            TextColor[4] = eval(self.pickColor5.text())
            TextAlign[4] = self.textAlign5.text()

        if nr>=6:
            WidthMin[5] = int(self.coordWidth6.text())
            WidthMax[5] = int(self.coordWidthMax6.text())
            Height[5] = int(self.coordHeight6.text())
            FontSize[5] = int(self.fontSize6.text())
            FontName[5] = self.fontNameBox6.text()
            TextColor[5] = eval(self.pickColor6.text())
            TextAlign[5] = self.textAlign6.text()

        brain(inputFolder, outputFolder, nr, Colt1, Colt2, WidthMin, WidthMax, Height, FontSize, FontName, TextColor, TextAlign )
        self.mergeLabel.setText("Done!")



    def showCoord1(self):
        font = self.fontNameBox1.text()
        QFontDatabase.addApplicationFont(font)
        font = font.split('.')
        self.font1 = QFont(font[0], int(self.fontSize1.text() )*self.raport  )
        self.coordLabel1.setFont(self.font1)
        self.coordLabel1.setText("SAMPLE TEXT1")
        self.coordLabel1.adjustSize()
        if self.textAlign1.text() == "left":
            self.coordLabel1.move(  1100+int(self.coordWidth1.text())*self.raport  , 50+int(self.coordHeight1.text())*self.raport )
        elif self.textAlign1.text() == "center":
            self.coordLabel1.move(  1100+( (int(self.coordWidth1.text())  +int(self.coordWidthMax1.text() ) )/2 )*self.raport - self.coordLabel1.width()/2  , 50+int(self.coordHeight1.text())*self.raport )
        else:
            self.coordLabel1.move(  1100+(int(self.coordWidthMax1.text()) )*self.raport  - int(self.coordLabel1.width()) , 50+int(self.coordHeight1.text())*self.raport )
    def showCoord2(self):
        font = self.fontNameBox2.text()
        QFontDatabase.addApplicationFont(font)
        font = font.split('.')
        self.font2 = QFont(font[0], int( self.fontSize2.text() )*self.raport )
        self.coordLabel2.setFont(self.font2)
        self.coordLabel2.setText("SAMPLE TEXT2")
        self.coordLabel2.adjustSize()
        if self.textAlign2.text() == "left":
            self.coordLabel2.move(  1100+int(self.coordWidth2.text())*self.raport  , 50+int(self.coordHeight2.text())*self.raport )
        elif self.textAlign2.text() == "center":
            self.coordLabel2.move(  1100+( (int(self.coordWidth2.text())  +int(self.coordWidthMax2.text() ) )/2 )*self.raport - self.coordLabel2.width()/2  , 50+int(self.coordHeight2.text())*self.raport )
        else:
            self.coordLabel2.move(  1100+(int(self.coordWidthMax2.text()) )*self.raport  - int(self.coordLabel2.width()) , 50+int(self.coordHeight2.text())*self.raport )
    def showCoord3(self):
        font = self.fontNameBox3.text()
        QFontDatabase.addApplicationFont(font)
        font = font.split('.')
        self.font3 = QFont(font[0],int(self.fontSize3.text() )*self.raport )
        self.coordLabel3.setFont(self.font3)
        self.coordLabel3.setText("SAMPLE TEXT3")
        self.coordLabel3.adjustSize()
        if self.textAlign3.text() == "left":
            self.coordLabel3.move(  1100+int(self.coordWidth3.text())*self.raport  , 50+int(self.coordHeight3.text())*self.raport )
        elif self.textAlign3.text() == "center":
            self.coordLabel3.move(  1100+( (int(self.coordWidth3.text())  +int(self.coordWidthMax3.text() ) )/2 )*self.raport - self.coordLabel3.width()/2  , 50+int(self.coordHeight3.text())*self.raport )
        else:
            self.coordLabel3.move(  1100+(int(self.coordWidthMax3.text()) )*self.raport  - int(self.coordLabel3.width()) , 50+int(self.coordHeight3.text())*self.raport )
    def showCoord4(self):
        font = self.fontNameBox4.text()
        QFontDatabase.addApplicationFont(font)
        font = font.split('.')
        self.font4 = QFont(font[0], int(self.fontSize4.text() )*self.raport )
        self.coordLabel4.setFont(self.font4)
        self.coordLabel4.setText("SAMPLE TEXT4")
        self.coordLabel4.adjustSize()
        if self.textAlign4.text() == "left":
            self.coordLabel4.move(  1100+int(self.coordWidth4.text())*self.raport  , 50+int(self.coordHeight4.text())*self.raport )
        elif self.textAlign4.text() == "center":
            self.coordLabel4.move(  1100+( (int(self.coordWidth4.text())  +int(self.coordWidthMax4.text() ) )/2 )*self.raport - self.coordLabel4.width()/2  , 50+int(self.coordHeight4.text())*self.raport )
        else:
            self.coordLabel4.move(  1100+(int(self.coordWidthMax4.text()) )*self.raport  - int(self.coordLabel4.width()) , 50+int(self.coordHeight4.text())*self.raport )
    def showCoord5(self):
        font = self.fontNameBox5.text()
        QFontDatabase.addApplicationFont(font)
        font = font.split('.')
        self.font5 = QFont(font[0], int(self.fontSize5.text() )*self.raport )
        self.coordLabel5.setFont(self.font5)
        self.coordLabel5.setText("SAMPLE TEXT5")
        self.coordLabel5.adjustSize()
        if self.textAlign5.text() == "left":
            self.coordLabel5.move(  1100+int(self.coordWidth5.text())*self.raport  , 50+int(self.coordHeight5.text())*self.raport )
        elif self.textAlign5.text() == "center":
            self.coordLabel5.move(  1100+( (int(self.coordWidth5.text())  +int(self.coordWidthMax5.text() ) )/2 )*self.raport - self.coordLabel5.width()/2  , 50+int(self.coordHeight5.text())*self.raport )
        else:
            self.coordLabel5.move(  1100+(int(self.coordWidthMax5.text()) )*self.raport  - int(self.coordLabel5.width()) , 50+int(self.coordHeight5.text())*self.raport )
    def showCoord6(self):
        font = self.fontNameBox6.text()
        QFontDatabase.addApplicationFont(font)
        font = font.split('.')
        self.font6 = QFont(font[0], int(self.fontSize6.text() )*self.raport )
        self.coordLabel6.setFont(self.font6)
        self.coordLabel6.setText("SAMPLE TEXT6")
        self.coordLabel6.adjustSize()
        if self.textAlign6.text() == "left":
            self.coordLabel6.move(  1100+int(self.coordWidth6.text())*self.raport  , 50+int(self.coordHeight6.text())*self.raport )
        elif self.textAlign6.text() == "center":
            self.coordLabel6.move(  1100+( (int(self.coordWidth6.text())  +int(self.coordWidthMax6.text() ) )/2 )*self.raport - self.coordLabel6.width()/2  , 50+int(self.coordHeight6.text())*self.raport )
        else:
            self.coordLabel6.move(  1100+(int(self.coordWidthMax6.text()) )*self.raport  - int(self.coordLabel6.width()) , 50+int(self.coordHeight6.text())*self.raport )

    def closeFunc(self):
        QtCore.QCoreApplication.instance().quit()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
