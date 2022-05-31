import random
import sys
import threading
import time

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QIcon


class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.stone = QPushButton("", self)
        self.paper = QPushButton("", self)
        self.scissors = QPushButton("", self)
        self.computer = QPushButton("", self)
        self.label = QLabel()

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

        self.computer.setFixedSize(490, 160)
        self.stone.setFixedSize(140, 100)
        self.paper.setFixedSize(140, 100)
        self.scissors.setFixedSize(140, 100)

        self.computer.setEnabled(False)

        self.label.setText(f"PLAYER: 0 ║ COMPUTER: 0")

        self.label.setStyleSheet("""color:white; font-size:20px; background:#5dba32; padding: 7px; border-radius:5px""")

        self.computer.setStyleSheet(
            """
            QPushButton{
                border-image: url(icons/start_game.png); 
            }
            """
        )

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

        h_lab_box = QHBoxLayout()
        h_lab_box.addWidget(self.label)

        h_comp_box = QHBoxLayout()
        h_comp_box.addWidget(self.computer)

        h_box = QHBoxLayout()
        h_box.addWidget(self.stone)
        h_box.addWidget(self.paper)
        h_box.addWidget(self.scissors)

        v_box = QVBoxLayout()
        v_box.addStretch(1)
        v_box.addLayout(h_lab_box)
        v_box.addStretch(2)
        v_box.addLayout(h_comp_box)
        v_box.addStretch(3)
        v_box.addLayout(h_box)
        v_box.addStretch(4)

        self.setLayout(v_box)
        self.show()


    @staticmethod
    def checkWhoWin(self, object_name):
        self.stone.setEnabled(False)
        self.paper.setEnabled(False)
        self.scissors.setEnabled(False)

        n = random.randrange(0, 3)
        options = ["Stein", "Papier", "Schere"]
        self.computer.setFixedSize(230, 160)
        self.computer.setStyleSheet(f"border-image: url(icons/{options[n]}.png);")
        state = 0

        scores = self.label.text().split("║")
        player_score = int((scores[0].strip().split(":")[1]).strip())
        computer_score = int((scores[1].strip().split(":")[1]).strip())

        if object_name == "Stone" and options[n] == "Schere":
            player_score += 1
            state = 1
        elif object_name == "Stone" and options[n] == "Papier":
            computer_score += 1
            state = 0
        elif object_name == "Paper" and options[n] == "Stein":
            player_score += 1
            state = 1
        elif object_name == "Paper" and options[n] == "Schere":
            computer_score += 1
            state = 0
        elif object_name == "Scissors" and options[n] == "Papier":
            player_score += 1
            state = 1
        elif object_name == "Scissors" and options[n] == "Stein":
            computer_score += 1
            state = 0
        else:
            state = 2

        x = threading.Thread(target=self.setWinner, args=(state, player_score, computer_score, ))
        x.start()

    def setWinner(self, state, player_score, computer_score):
        time.sleep(1)
        self.computer.setFixedSize(490, 160)

        if state == 1:
            self.computer.setStyleSheet(f"border:2px solid black; border-image: url(icons/win.png);")
            time.sleep(1)
            self.computer.setStyleSheet(f"border:2px solid black; border-image: url(icons/try_again.png);")
        elif state == 0:
            self.computer.setStyleSheet(f"border:2px solid black; border-image: url(icons/lose.png);")
            time.sleep(1)
            self.computer.setStyleSheet(f"border:2px solid black; border-image: url(icons/try_again.png);")
        else:
            self.computer.setStyleSheet(f"border:2px solid black; border-image: url(icons/draw.png);")
            time.sleep(1)
            self.computer.setStyleSheet(f"border:2px solid black; border-image: url(icons/try_again.png);")

        self.stone.setEnabled(True)
        self.paper.setEnabled(True)
        self.scissors.setEnabled(True)
        self.label.setText(f"PLAYER: {player_score} ║ COMPUTER: {computer_score}")


def main():
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()