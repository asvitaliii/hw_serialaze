from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from drivers import XMLDrive


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('gui.ui')
        self.__win.setWindowTitle(XMLDrive().get_title())
        self.__win.question1.setText(XMLDrive().get_questions(0))
        self.__win.question1.adjustSize()
        self.__win.question2.setText(XMLDrive().get_questions(1))
        self.__win.question2.adjustSize()
        self.__win.question3.setText(XMLDrive().get_questions(2))
        self.__win.question3.adjustSize()
        self.__driver = XMLDrive()

    def __set_slots(self):
        self.__win.ok.clicked.connect(self.finish_test)

    def show(self):
        self.__set_slots()
        self.__win.show()

    def finish_test(self):
        mark = 0
        if self.__driver.get_answers(0) == self.__win.answer1.text():
            mark += 1
        if self.__driver.get_answers(1) == self.__win.answer2.text():
            mark += 1
        if self.__driver.get_answers(2) == self.__win.answer3.text():
            mark += 1
        QMessageBox.information(self, 'Ваш результат:', f'{mark} бал(а).')
