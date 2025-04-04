import sys
from PyQt6.QtWidgets import QApplication 

app = QApplication(sys.argv)

from main_gui import main_window

main_window.show()

sys.exit(app.exec())


# if __name__ == "__main__":
#     Menu.saudacao()
#     menu = Menu()
#     menu.ver_menu_principal()

