from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QMessageBox
import sys

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Admin Login")

        self.admin_username = "admin"
        self.admin_password = "password"

        self.username_label = QLabel("Username")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Password")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_credentials)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)

    def check_credentials(self):
        if self.username_input.text() == self.admin_username and self.password_input.text() == self.admin_password:
            self.login_success()
        else:
            self.login_failure()

    def login_success(self):
        app = QApplication([])
        main_window = MainWindow()
        main_window.show()
        app.exec()
    def login_failure(self):
        QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to the Main Window!")
        layout.addWidget(welcome_label)

        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = LoginWindow()
    login_window.show()

    app.exec()
