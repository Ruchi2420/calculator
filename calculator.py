#imports
from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QHBoxLayout,QVBoxLayout,QGridLayout
from PyQt5.QtGui import QFont

class CalculatorApp(QWidget):
#App Settings
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator App")
        self.resize(250,300)
        self.init_ui()

    def init_ui(self):
        #creates all objects and widgets
        self.text_box = QLineEdit()
        self.text_box.setReadOnly(True)
        self.text_box.setFont(QFont("Arial", 14))
        self.text_box.setStyleSheet("QLineEdit  { background-colorL:#95b0db ;}")

        self.grid = QGridLayout()

        buttons = [
                "7","8","9","/",
                "4","5","6","*",
                "1","2","3","-",
                "0",".","=","+"
                ]

        self.clear_button = QPushButton("clear")
        self.delete_button = QPushButton("<")

        row=0
        col=0

        for text in buttons:
            button = QPushButton(text)
            button.setFont(QFont("Aria",12))
            button.setStyleSheet("QPushButton { background-color: #95b0db;}")
            button.clicked.connect(lambda ch, t=text:self.on_button_click(t))
            #button.clicked.connect(None)
            self.grid.addWidget(button,row,col)
            col+=1

            if col>3:
                col=0
                row+=1

        #Design
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row  = QHBoxLayout()
        button_row.addWidget(self.clear_button)
        button_row.addWidget(self.delete_button)

        master_layout.addLayout(button_row)

        self.setLayout(master_layout)

        
        # Connect buttons to the event handler
        self.clear_button.setFont(QFont("Arial", 12))
        self.clear_button.setStyleSheet("QPushButton { background-color: red; color: white; }")
        self.clear_button.clicked.connect(lambda: self.on_button_click("clear"))

        self.delete_button.setFont(QFont("Arial", 12))
        self.delete_button.setStyleSheet("QPushButton { background-color: orange; color: white; }")
        self.delete_button.clicked.connect(lambda: self.on_button_click("<"))

    def on_button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.text_box.text()))
                self.text_box.setText(result)
            except Exception as e:
                self.text_box.setText("Error")
        elif text == "clear":
            self.text_box.clear()
        elif text == "<":
            current_text = self.text_box.text()
            self.text_box.setText(current_text[:-1])
        else:
            current_text = self.text_box.text()
            self.text_box.setText(current_text + text)

if __name__ == '__main__':
    app = QApplication([])
    calc = CalculatorApp()
    calc.show()
    app.exec_()
    
        