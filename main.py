from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import os
import json

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_note)
        self.ui.pushButton_2.clicked.connect(self.save_note)

        if os.path.exists("note.json") and os.path.getsize("note.json"):
            with open("note.json", 'r') as file:
                self.notes = json.load(file)
                self.ui.listWidget.addItem(self.notes.keys())
        else:
            self.notes = {}


    def add_note(self):
        text, ok = QInputDialog.getText(self, 'Додати замітку', 'введіть текст')
        if ok:
            self.ui.listWidget.addItem(text)
            self.notes[text] = {"текст":""}

    def save_note(self):
        if self.ui.listWidget.selectedItems():
            key = self.ui.listWidget.selectedItems()[0].text()
            self.notes[key]["текст"] = self.ui.textEdit.toPlainText()
            with open("notes.json", "w") as file:
                json.dump(self.notes,file,sort_keys=True,ensure_ascii=False)
                print('Збережено')
        else:
            print('Замітка не обрана')


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()