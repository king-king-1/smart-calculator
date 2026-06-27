import sys 


from PyQt5.QtWidgets import ( QMainWindow,QApplication
                ,QPushButton,QLabel,QCheckBox,QRadioButton
                ,QWidget,QHBoxLayout,QVBoxLayout
                ,QButtonGroup,QLineEdit,QGridLayout
)
from PyQt5.QtGui import QIcon , QFont,QPixmap
from PyQt5.QtCore import Qt 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,50,600,600)
        self.label_result=QLabel("1234679",self)  
        self.label_result.setAlignment(Qt.AlignCenter)
        self.button1=QPushButton("1",self)
        self.button2=QPushButton("2",self)
        self.button3=QPushButton("3",self)
        self.button4=QPushButton("4",self)
        self.button5=QPushButton("5",self)
        self.button6=QPushButton("6",self)
        self.button7=QPushButton("7",self)
        self.button8=QPushButton("8",self)
        self.button9=QPushButton("9",self)
        self.button0=QPushButton("0",self)
        self.button_del=QPushButton("del",self)
        self.button_opp1=QPushButton("+",self)
        self.button_opp2=QPushButton("-",self)
        self.button_opp3=QPushButton("*",self)
        self.button_opp4=QPushButton("/",self)
        self.button_opp5=QPushButton("=",self)
        
        self.button1.clicked.connect(self.clic)
        self.button2.clicked.connect(self.clic)
        self.button3.clicked.connect(self.clic)
        self.button4.clicked.connect(self.clic)
        self.button5.clicked.connect(self.clic)
        self.button6.clicked.connect(self.clic)
        self.button7.clicked.connect(self.clic)
        self.button8.clicked.connect(self.clic)
        self.button9.clicked.connect(self.clic)
        self.button0.clicked.connect(self.clic)
        self.button_del.clicked.connect(self.clic)
        self.button_opp1.clicked.connect(self.clic)
        self.button_opp2.clicked.connect(self.clic)
        self.button_opp3.clicked.connect(self.clic)
        self.button_opp4.clicked.connect(self.clic)
        self.button_opp5.clicked.connect(self.clic)
        self.num1=""
        self.num2=""
        self.texte_label=""
        self.number_list=["1","2","3","4","5","6","7","8","9","0"]
        self.number_opr=["/","*","+","-"]
        self.number_opr_real=[self.button_opp1,self.button_opp2,self.button_opp3,self.button_opp4]
        for opr_kined in self.number_opr_real:
            opr_kined.setDisabled(True)
        self.num2_ok=False
        self.styled()
        self.organized()
    def styled(self):
        for opr in [self.button_opp1,self.button_opp2,self.button_opp3,self.button_opp4,self.button_opp5,self.button_del]  :
              opr.setObjectName("opration_button")               
        for opr in [self.button0,self.button1,self.button2,self.button3,self.button4,self.button5,self.button6,self.button7,self.button8,self.button9]  :
              opr.setObjectName("number_button")               
         # QMainWindow{background-color:#c1becf}
        self.setStyleSheet("""

        QMainWindow{background: qlineargradient(
            x1: 0, y1: 0, x2: 1, y2: 1,
            stop: 0 #3498DB,
            stop: 1 #2C3E50
        )}
        
        QPushButton{
                 font-size:30px;
                 color:#1d1d1f;
                 background-color:#414042;
                 border: 2px solid 1e1e1e;
                 margin-top: 10px;
                 margin-bottom: 10px; 
                 height:50px;

        }

        QLabel{
                 background-color:#ffffff;
                 border: 2px solid #000000;
                 text-align: center;
                 font-size:70px;
                font-family=Arial; 
                margin: 15px;
        }
                """)
    def organized(self):
        widget1=QWidget()
        self.setCentralWidget(widget1)
        organiser=QGridLayout()
        widget1.setLayout(organiser)
        organiser.addWidget(self.label_result,0,0,1,4)
        organiser.addWidget(self.button1,1,0)
        organiser.addWidget(self.button2,1,1)
        organiser.addWidget(self.button3,1,2)
        organiser.addWidget(self.button4,2,0)
        organiser.addWidget(self.button5,2,1)
        organiser.addWidget(self.button6,2,2)
        organiser.addWidget(self.button7,3,0)
        organiser.addWidget(self.button8,3,1)
        organiser.addWidget(self.button9,3,2)
        organiser.addWidget(self.button0,4,1)
        organiser.addWidget(self.button_del,4,0)
        organiser.addWidget(self.button_opp1,1,3)
        organiser.addWidget(self.button_opp2,2,3)
        organiser.addWidget(self.button_opp3,3,3)
        organiser.addWidget(self.button_opp4,4,3)
        organiser.addWidget(self.button_opp5,4,2)
   
    def clic(self):
            the_cliced_button=self.sender()
            t=the_cliced_button.text()
            print(f"you clic  :  {t}")
            if str(t) in self.number_list and  self.num2_ok==False  :                 
               self.num1+= t 
               self.texte_label +=t              
               print(self.texte_label)

               print(f" num1  : {self.num1}")
               for opr_kined in self.number_opr_real: 
                    opr_kined.setDisabled(False)                     
               self.label_result.setText(self.texte_label)   
            elif  str(t) in self.number_opr :
                 self.occur_opr=str(t)                
                 print(f"the opration  is   :  {self.occur_opr}")
                 self.num2_ok=True 
                 self.texte_label +=t  
                 print(self.texte_label)
                 self.label_result.setText(self.texte_label)                    
            elif str(t) in self.number_list and  self.num2_ok==True  :                 
               self.num2+= t 
               print(f" num2  : {self.num2}")
               for opr_kined in self.number_opr_real: 
                    opr_kined.setDisabled(True)                     
               self.texte_label +=t  
               print(self.texte_label)
               self.label_result.setText(self.texte_label)                  
            elif str(t) =="="   :
              try :   
                if self.occur_opr=="*":
                    self.result=float(self.num1) * float(self.num2)
                elif  self.occur_opr=="/":
                    self.result=float(self.num1) / float(self.num2)
                elif  self.occur_opr=="+":
                    self.result=float(self.num1) + float(self.num2)
                elif self.occur_opr=="-":
                    self.result=float(self.num1) - float(self.num2)
                self.texte_label =str(self.result)                 
                print(self.result)
                self.num2_ok=False  
                self.num1=""
                self.num2=""    
                print(self.texte_label)
                self.label_result.setText(self.texte_label)                   
                for opr_kined in self.number_opr_real: 
                    opr_kined.setDisabled(True)                   
              except :
                self.num2="0" 
                self.occur_opr="+"                 
                if self.occur_opr=="*":
                    self.result=float(self.num1) * float(self.num2)
                elif  self.occur_opr=="/":
                    self.result=float(self.num1) / float(self.num2)
                elif  self.occur_opr=="+":
                    self.result=float(self.num1) + float(self.num2)
                elif self.occur_opr=="-":
                    self.result=float(self.num1) - float(self.num2)
                
                print(self.result)
                self.num2_ok=False  
                self.num1=""
                self.num2=""    
                for opr_kined in self.number_opr_real: 
                    opr_kined.setDisabled(True)                   
                self.texte_label =str(self.result)        
                print(self.texte_label)
                self.label_result.setText(self.texte_label)                   
              finally:
                  self.texte_label=""
            elif  str(t) =="del"  :
                self.num2_ok=False  
                self.num1=""
                self.num2=""    
                for opr_kined in self.number_opr_real: 
                    opr_kined.setDisabled(True)   
                self.texte_label ="" 
                self.label_result.setText(self.texte_label)   
                print(self.texte_label)
  
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__" :
    main()
    




































