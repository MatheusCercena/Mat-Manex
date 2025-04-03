import sys
from PyQt6.QtWidgets import QApplication 
from main_gui import main_window

app = QApplication(sys.argv)

main_window.show()

app.exec()


# if __name__ == "__main__":
#     Menu.saudacao()
#     menu = Menu()
#     menu.ver_menu_principal()

