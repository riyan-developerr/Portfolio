"""  
intro to PyQt5 for making gui
"""

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Billionaire Training")
        self.setGeometry(0,0,700,700)
        self.setWindowIcon(QIcon("icon.png"))
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # by default the window is hidden so to show it
    window.show()
    # but it closes quickly to keep it open we use
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()