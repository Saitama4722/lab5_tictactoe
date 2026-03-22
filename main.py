import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox
from PyQt5.QtCore import Qt


class TicTacToeGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Крестики-нолики на PyQt5")
        self.setGeometry(100, 100, 300, 370)
        self.buttons = []
        self.current_player = "X"
        self.move_count = 0
        self.create_buttons()

    def create_buttons(self):
        cw = QLabel(self)
        self.setCentralWidget(cw)
        self.buttons = []
        for row in range(3):
            row_buttons = []
            for col in range(3):
                btn = QPushButton("", cw)
                btn.setGeometry(col * 100, row * 100, 100, 100)
                btn.clicked.connect(self.on_click)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)
        self.status_label = QLabel("", cw)
        self.status_label.setGeometry(0, 300, 300, 20)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.new_game_btn = QPushButton("Новая игра", cw)
        self.new_game_btn.setGeometry(50, 330, 200, 30)
        self.new_game_btn.clicked.connect(self.reset_game)

    def on_click(self):
        sender = self.sender()
        if sender.text() != "":
            return
        sender.setText(self.current_player)
        self.move_count += 1
        if self.check_winner():
            return
        self.switch_player()

    def check_winner(self):
        for row in range(3):
            t = self.buttons[row][0].text()
            if t != "" and t == self.buttons[row][1].text() == self.buttons[row][2].text():
                self.end_game("Победил " + t)
                return True
        for col in range(3):
            t = self.buttons[0][col].text()
            if t != "" and t == self.buttons[1][col].text() == self.buttons[2][col].text():
                self.end_game("Победил " + t)
                return True
        t = self.buttons[1][1].text()
        if t != "" and t == self.buttons[0][0].text() == self.buttons[2][2].text():
            self.end_game("Победил " + t)
            return True
        if t != "" and t == self.buttons[0][2].text() == self.buttons[2][0].text():
            self.end_game("Победил " + t)
            return True
        if self.move_count == 9:
            self.end_game("Ничья")
            return True
        return False

    def end_game(self, message):
        self.status_label.setText(message)
        for row in self.buttons:
            for btn in row:
                btn.setEnabled(False)

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def reset_game(self):
        self.current_player = "X"
        self.move_count = 0
        self.status_label.setText("")
        for row in self.buttons:
            for btn in row:
                btn.setText("")
                btn.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToeGame()
    window.show()
    sys.exit(app.exec_())
