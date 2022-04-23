import sys
from PyQt5 import QtWidgets
from ui_code import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QtWidgets.QMainWindow() # Call the inherited classes __init__ method
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # PAGES
        # Set main widget
        self.ui.stackedWidget.setCurrentWidget(self.ui.raw)

        # Set links for buttons on side menu
        self.ui.btn_menu1.clicked.connect(self.show_raw_page)
        self.ui.btn_menu2.clicked.connect(self.show_preprocess_page)
        self.ui.btn_menu3.clicked.connect(self.show_events_page)
        self.ui.btn_menu4.clicked.connect(self.show_epochs_page)
        self.ui.btn_menu5.clicked.connect(self.show_tfa_page)
        self.ui.btn_menu6.clicked.connect(self.show_evoked_page)

        # Set links for buttons on main pages
        self.ui.btn_preprocess.clicked.connect(self.show_preprocess_page)
        self.ui.btn_detectevents.clicked.connect(self.show_events_page)
        self.ui.btn_epoch.clicked.connect(self.show_epochs_page)
        self.ui.btn_tfa.clicked.connect(self.show_tfa_page)
        self.ui.btn_evoked.clicked.connect(self.show_evoked_page)

    def show(self):
        self.main_win.show()
    
    def show_raw_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.raw)

    def show_preprocess_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.preprocess)
    
    def show_events_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.events)

    def show_epochs_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.epoch)

    def show_tfa_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.tfa)

    def show_evoked_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.evoked)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())