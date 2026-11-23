import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QGridLayout, QMessageBox
)

def calc(op):
    try:
        val = float(a.text().strip())
        val2 = float(b.text().strip())
        if op == "+":
            ans = val + val2
        elif op == "-":
            ans = val - val2
        elif op == "*":
            ans = val * val2
        elif op == "/":
            ans = val / val2
        anss.setText(f"計算結果：{ans:.2f}")
    except (ValueError, ZeroDivisionError):
        QMessageBox.critical(win, "WA", "WA")


def clear():
    a.clear()
    b.clear()
    anss.setText("計算結果：")

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("簡易計算機")
win.resize(320, 210)
grid = QGridLayout()
win.setLayout(grid)
grid.addWidget(QLabel("第一個數字:"), 0, 0)
a = QLineEdit()
grid.addWidget(a, 0, 1, 1, 3)

grid.addWidget(QLabel("第二個數字:"), 1, 0)
b = QLineEdit()
grid.addWidget(b, 1, 1, 1, 3)

for col, sym in enumerate(["+", "-", "*", "/"]):
    btn = QPushButton(sym)
    btn.clicked.connect(lambda checked, s=sym: calc(s))
    grid.addWidget(btn, 2, col)

anss = QLabel("計算結果：")
grid.addWidget(anss, 3, 0, 1, 4)

clr_btn = QPushButton("清除")
clr_btn.clicked.connect(clear)
grid.addWidget(clr_btn, 4, 0, 1, 4)




win.show()
sys.exit(app.exec())