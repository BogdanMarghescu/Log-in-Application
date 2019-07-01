from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from selenium import webdriver
import sys
import time
import login_ui


class Login(QDialog, login_ui.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        systray_icon = QIcon("login.png")
        systray = QSystemTrayIcon(systray_icon, self)
        menu = QMenu()
        restart = QAction("Restart", self)
        minmax = QAction("Minimize/Maximize", self)
        close = QAction("Close", self)
        menu.addActions([restart, minmax, close])
        systray.setContextMenu(menu)
        systray.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000)
        self.Clock.show()
        restart.triggered.connect(lambda: self.restart(systray))
        minmax.triggered.connect(self.minimize_maximize)
        close.triggered.connect(self.close)
        self.facebook.setContextMenuPolicy(Qt.CustomContextMenu)
        self.facebook.customContextMenuRequested.connect(self.showContextMenuFacebook)
        self.twitter.setContextMenuPolicy(Qt.CustomContextMenu)
        self.twitter.customContextMenuRequested.connect(self.showContextMenuTwitter)
        self.instagram.setContextMenuPolicy(Qt.CustomContextMenu)
        self.instagram.customContextMenuRequested.connect(self.showContextMenuInstagram)
        self.login.clicked.connect(self.log_in)

    def tick(self):
        self.Clock.display(time.strftime('%H:%M:%S'))

    def showContextMenuFacebook(self, position):
        menuFacebook = QMenu(self)
        enable = QAction("Enable", self)
        disable = QAction("Disable", self)
        menuFacebook.addActions([enable, disable])
        enable.triggered.connect(lambda: self.facebook.setChecked(True))
        disable.triggered.connect(lambda: self.facebook.setAutoExclusive(False))
        disable.triggered.connect(lambda: self.facebook.setChecked(False))
        disable.triggered.connect(lambda: self.facebook.setAutoExclusive(True))
        menuFacebook.popup(self.facebook.mapToGlobal(position))

    def showContextMenuTwitter(self, position):
        menuTwitter = QMenu(self)
        enable = QAction("Enable", self)
        disable = QAction("Disable", self)
        menuTwitter.addActions([enable, disable])
        enable.triggered.connect(lambda: self.twitter.setChecked(True))
        disable.triggered.connect(lambda: self.twitter.setAutoExclusive(False))
        disable.triggered.connect(lambda: self.twitter.setChecked(False))
        disable.triggered.connect(lambda: self.twitter.setAutoExclusive(True))
        menuTwitter.popup(self.twitter.mapToGlobal(position))

    def showContextMenuInstagram(self, position):
        menuInstagram = QMenu(self)
        enable = QAction("Enable", self)
        disable = QAction("Disable", self)
        menuInstagram.addActions([enable, disable])
        enable.triggered.connect(lambda: self.instagram.setChecked(True))
        disable.triggered.connect(lambda: self.instagram.setAutoExclusive(False))
        disable.triggered.connect(lambda: self.instagram.setChecked(False))
        disable.triggered.connect(lambda: self.instagram.setAutoExclusive(True))
        menuInstagram.popup(self.instagram.mapToGlobal(position))

    def minimize_maximize(self):
        if self.windowState() == Qt.WindowActive:
            self.setWindowState(Qt.WindowMinimized)
        else:
            self.setWindowState(Qt.WindowActive)

    def restart(self, systray):
        systray.show()
        self.close()
        time.sleep(1)
        systray.showMessage("Application Restarted", "Application has restarted. Please log in again.",
                            QSystemTrayIcon.Information)
        self.username.setText("")
        self.password.setText("")
        self.facebook.setAutoExclusive(False)
        self.twitter.setAutoExclusive(False)
        self.instagram.setAutoExclusive(False)
        self.facebook.setChecked(False)
        self.twitter.setChecked(False)
        self.instagram.setChecked(False)
        self.facebook.setAutoExclusive(True)
        self.twitter.setAutoExclusive(True)
        self.instagram.setAutoExclusive(True)
        self.open()

    def facebook_login(self):
        url = "https://www.facebook.com/"
        driver = webdriver.Chrome("chromedriver")
        driver.get(url)
        time.sleep(0.2)
        driver.find_element_by_id("email").send_keys(self.username.text())
        time.sleep(0.2)
        driver.find_element_by_id("pass").send_keys(self.password.text())
        time.sleep(0.2)
        driver.find_element_by_id("loginbutton").click()

    def twitter_login(self):
        url = "https://twitter.com/login/"
        driver = webdriver.Chrome("chromedriver")
        driver.get(url)
        time.sleep(0.2)
        driver.find_element_by_class_name("js-username-field").send_keys(self.username.text())
        time.sleep(0.2)
        driver.find_element_by_class_name("js-password-field").send_keys(self.password.text())
        time.sleep(0.2)
        driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium").click()

    def instagram_login(self):
        url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
        driver = webdriver.Chrome("chromedriver")
        driver.get(url)
        time.sleep(0.2)
        driver.find_element_by_name("username").send_keys(self.username.text())
        time.sleep(0.2)
        driver.find_element_by_name("password").send_keys(self.password.text())
        time.sleep(0.2)
        driver.find_element_by_css_selector("button[type='submit']").click()

    def log_in(self):
        if self.username.text() == "" and self.password.text() == "":
            QMessageBox.critical(self, "Login Error",
                                 "\"Username\" and \"Password\" fields are empty.\nPlease fill them to continue!")
        elif self.username.text() == "":
            QMessageBox.critical(self, "Login Error", "\"Username\" field is empty.\nPlease fill it to continue!")
        elif self.password.text() == "":
            QMessageBox.critical(self, "Login Error", "\"Password\" field is empty.\nPlease fill it to continue!")
        else:
            if self.facebook.isChecked() == True:
                self.facebook_login()
            elif self.twitter.isChecked() == True:
                self.twitter_login()
            elif self.instagram.isChecked() == True:
                self.instagram_login()
            else:
                QMessageBox.critical(self, "Login Error", "No platform selected.\nPlease select one to continue!")


app = QApplication(sys.argv)
login = Login()
splash_image = QPixmap("welcome.jpg")
splash = QSplashScreen(splash_image)
splash.show()
time.sleep(1)
login.show()
splash.finish(login)
app.exec_()
