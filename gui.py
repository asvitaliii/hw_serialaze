from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from drivers import XMLDrive


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('gui.ui')
        self.setWindowTitle(XMLDrive().get_title())
        self.question1.setText(XMLDrive().get_questions(0))
        self.question1.adjustSize()
        self.question2.setText(XMLDrive().get_questions(1))
        self.question2.adjustSize()
        self.question3.setText(XMLDrive().get_questions(2))
        self.question3.adjustSize()

    def __set_slots(self):
        self.__win.ok.clicked.connect(self.finish_test)

    def show(self):
        self.__set_slots()
        self.__win.show()

    def finish_test(self):
        mark = 0
        if XMLDrive().get_answers(0) == self.__win.lineEdit.text():
            mark += 1
        if XMLDrive().get_answers(1) == self.__win.lineEdit_2.text():
            mark += 1
        if XMLDrive().get_answers(2) == self.__win.lineEdit_3.text():
            mark += 1
        QMessageBox.information(self, 'Ваш результат:', f'{mark} бал(а).')
