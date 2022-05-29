import random
import sys
import threading
import time

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QPixmap


class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.stone = QPushButton("", self)
        self.paper = QPushButton("", self)
        self.scissors = QPushButton("", self)
        self.computer = QPushButton("", self)

        self.initUI()

    def initUI(self):
        self.setFixedSize(800, 500)
        self.setStyleSheet("Background: white;")
        self.setWindowTitle('Rock, Paper, Scissors')
        self.setWindowIcon(QIcon('icons/icon.png'))

        # creating a push button

        self.stone.setObjectName("Stone")
        self.paper.setObjectName("Paper")
        self.scissors.setObjectName("Scissors")

        self.computer.setFixedSize(190, 160)
        self.stone.setFixedSize(130, 100)
        self.paper.setFixedSize(130, 100)
        self.scissors.setFixedSize(130, 100)

        self.computer.setEnabled(False)
        self.computer.setStyleSheet("border-radius:5px; border:1px solid gray;")

        self.stone.setStyleSheet(
            """
            QPushButton{
                border-image: url(icons/Stein.png); 
            }
            
            QPushButton:hover{
                border:5px solid white;
            }
            """
        )

        self.paper.setStyleSheet(
            """
            QPushButton{
                border-image: url(icons/Papier.png); 
            }
            
            QPushButton:hover{
                border:5px solid white;
            }
            """
        )

        self.scissors.setStyleSheet(
            """
            QPushButton{
                border-image: url(icons/Schere.png); 
            }
            
            QPushButton:hover{
                border:5px solid white;
            }
            """
        )

        self.stone.clicked.connect(lambda: self.checkWhoWin(self, self.stone.objectName()))
        self.paper.clicked.connect(lambda: self.checkWhoWin(self, self.paper.objectName()))
        self.scissors.clicked.connect(lambda: self.checkWhoWin(self, self.scissors.objectName()))

        h_comp_box = QHBoxLayout()
        h_comp_box.addWidget(self.computer)

        h_box = QHBoxLayout()
        h_box.addWidget(self.stone)
        h_box.addWidget(self.paper)
        h_box.addWidget(self.scissors)

        v_box = QVBoxLayout()
        v_box.addLayout(h_comp_box)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.show()


    @staticmethod
    def checkWhoWin(self, object_name):
        n = random.randrange(0, 3)
        options = ["Stein", "Papier", "Schere"]
        self.computer.setStyleSheet(f"border-image: url(icons/{options[n]}.png);")
        state = 0

        if object_name == "Stone" and options[n] == "Schere":
            state = 1
        elif object_name == "Stone" and options[n] == "Papier":
            state = 0
        elif object_name == "Paper" and options[n] == "Stein":
            state = 1
        elif object_name == "Papier" and options[n] == "Schere":
            state = 0
        elif object_name == "Scissors" and options[n] == "Papier":
            state = 1
        elif object_name == "Scissors" and options[n] == "Stein":
            state = 0
        else:
            state = 2

        x = threading.Thread(target=self.clear, args=(state,))
        x.start()

    def clear(self, state):
        time.sleep(1)

        if state == 1:
            self.computer.setStyleSheet(f"border:2px solid black; border-image: url(icons/win.png);")
        elif state == 0:
            self.computer.setStyleSheet(f"border:2px solid black; border-image: url(icons/lose.png);")
        else:
            self.computer.setStyleSheet(f"border:2px solid black; border-image: url(icons/try_again.png);")


def main():
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()