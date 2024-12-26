file = 'D:\Python\home.ui'
import os
import sys
import file # Тут ваш файл
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from home.ui import Ui_MainWindow  # Импортируем сгенерированный файл

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Подключаем действия меню к методам
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.close)

    def open_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.ui.textEdit.setPlainText(content)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not open file: {e}")

    def save_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    content = self.ui.textEdit.toPlainText()
                    file.write(content)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Could not save file: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = TextEditor()
    editor.show()
    sys.exit(app.exec())
