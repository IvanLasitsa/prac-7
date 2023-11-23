# python -m PyQt5.uic.pyuic -x untitled.ui -o ui.py
import random
import string
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_generate.clicked.connect(self.result)
        self.ui.quit.clicked.connect(self.quit)

    def value(self):
        value = self.ui.value.value()
        return value
            
    def checkbox_numbers(self, count):
        if self.ui.cb_numbers.isChecked():
            numbers = [str(random.randint(1, 100)) for _ in range(count)]
            return ''.join(numbers)
        else:
            return ''
        
    def checkbox_alphabet(self, count):
        if self.ui.cb_alphabet.isChecked():
            alphabet = string.ascii_letters
            checkbox_alphabet = ''.join(random.choice(alphabet) for _ in range(count))
            return ''.join(checkbox_alphabet)
        else:
            return ''
                 
    def checkbox_password(self):
        count = self.value()
        text_numbers = self.checkbox_numbers(count)
        text_alphabet = self.checkbox_alphabet(count)
        combined = list (text_alphabet + text_numbers)
        
        if not text_numbers and not text_alphabet:
            return ""
    
        result_password = ''.join(random.choice(combined) for _ in range(count))
        return ''.join(result_password)

    def result(self):
        password = self.checkbox_password()
        self.ui.result.setText(password)
        
    def quit(self):
        sys.exit()
          
app = QApplication([])
ex = Widget()
ex.show()
app.exec_()

