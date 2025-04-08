import sys
from PyQt6.QtWidgets import QApplication
from UI.main_gui import criar_main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = criar_main_window()
    main_window.show()
    sys.exit(app.exec())



