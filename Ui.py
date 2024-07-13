import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QFormLayout, QDesktopWidget
)
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon, QCursor
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMessageBox

class InstagramBotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Manchan\'s IG Bot')
        self.setGeometry(100, 100, 800, 600)  # Default size
        self.setMinimumSize(600, 400)  # Set minimum size for the window
        self.setStyleSheet("background-color: #f0f0f0;")
        self.center()

        # Create palette for modern lighting effect
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))
        palette.setColor(QPalette.WindowText, Qt.black)
        self.setPalette(palette)

        # Heading label
        self.label_heading = QLabel('Manchan\'s Instagram Bot')
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_heading.setFont(font)
        self.label_heading.setAlignment(Qt.AlignCenter)
        self.label_heading.setStyleSheet("color: #333;")

        # Introduction label
        self.label_intro = QLabel(
            'Welcome to Manchan\'s Instagram Bot. '
            'This bot helps you automate interactions on Instagram, such as liking posts, commenting, and messaging.'
        )
        self.label_intro.setAlignment(Qt.AlignCenter)
        self.label_intro.setStyleSheet("font-size: 16px; color: #666;")

        # Goal label
        self.label_goal = QLabel(
            'Our goal is to simplify your Instagram experience by automating routine interactions.'
        )
        self.label_goal.setAlignment(Qt.AlignCenter)
        self.label_goal.setStyleSheet("font-size: 16px; color: #666;")

        # Security note label
        self.label_security = QLabel(
            'Please enter your Instagram credentials to log in. Your credentials are used only to log in and perform actions on Instagram. '
            'We do not store your credentials.'
        )
        self.label_security.setAlignment(Qt.AlignCenter)
        self.label_security.setStyleSheet("font-size: 12px; color: #888;")

        # View security agreement button
        self.button_view_security = QPushButton('View Security Agreement')
        self.button_view_security.clicked.connect(self.open_security_agreement)
        self.button_view_security.setStyleSheet(self.button_style("#1E90FF"))

        # Username and password fields
        self.label_username = QLabel('Username:')
        self.label_password = QLabel('Password:')
        self.input_username = QLineEdit()
        self.input_username.setPlaceholderText('Enter your Instagram username')
        self.input_username.setStyleSheet(self.input_style())
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.setPlaceholderText('Enter your Instagram password')
        self.input_password.setStyleSheet(self.input_style())

        # Login button
        self.button_login = QPushButton('Login')
        self.button_login.clicked.connect(self.login)
        self.button_login.setToolTip('Click to log in to Instagram')
        self.button_login.setStyleSheet(self.button_style("#4CAF50"))

        # Form layout for login fields
        form_layout = QFormLayout()
        form_layout.addRow(self.label_username, self.input_username)
        form_layout.addRow(self.label_password, self.input_password)
        form_layout.addRow(self.button_login)

        # Adding more functionality
        self.label_like = QLabel('Enter user to like their posts:')
        self.input_like = QLineEdit()
        self.input_like.setPlaceholderText('Enter the username')
        self.input_like.setStyleSheet(self.input_style())
        self.button_like = QPushButton('Like Posts')
        self.button_like.clicked.connect(self.like_posts)
        self.button_like.setToolTip('Click to like posts of the specified user')
        self.button_like.setStyleSheet(self.button_style("#2196F3"))

        self.label_comment = QLabel('Enter user to comment on their posts:')
        self.input_comment_user = QLineEdit()
        self.input_comment_user.setPlaceholderText('Enter the username')
        self.input_comment_user.setStyleSheet(self.input_style())
        self.label_comment_text = QLabel('Enter comment text:')
        self.input_comment_text = QTextEdit()
        self.input_comment_text.setPlaceholderText('Enter your comment')
        self.input_comment_text.setStyleSheet(self.input_style())
        self.button_comment = QPushButton('Comment on Posts')
        self.button_comment.clicked.connect(self.comment_on_posts)
        self.button_comment.setToolTip('Click to comment on posts of the specified user')
        self.button_comment.setStyleSheet(self.button_style("#FF5722"))

        self.label_message_user = QLabel('Enter user to message:')
        self.input_message_user = QLineEdit()
        self.input_message_user.setPlaceholderText('Enter the username')
        self.input_message_user.setStyleSheet(self.input_style())
        self.label_message_text = QLabel('Enter message text:')
        self.input_message_text = QTextEdit()
        self.input_message_text.setPlaceholderText('Enter your message')
        self.input_message_text.setStyleSheet(self.input_style())
        self.label_message_time = QLabel('Enter time to send the message (HH:MM):')
        self.input_message_time = QLineEdit()
        self.input_message_time.setPlaceholderText('Enter the time')
        self.input_message_time.setStyleSheet(self.input_style())
        self.button_message = QPushButton('Send Message')
        self.button_message.clicked.connect(self.send_message)
        self.button_message.setToolTip('Click to send a message to the specified user at the specified time')
        self.button_message.setStyleSheet(self.button_style("#9C27B0"))

        # Layout for functionalities
        vbox_like = QVBoxLayout()
        vbox_like.addWidget(self.label_like)
        vbox_like.addWidget(self.input_like)
        vbox_like.addWidget(self.button_like)

        vbox_comment = QVBoxLayout()
        vbox_comment.addWidget(self.label_comment)
        vbox_comment.addWidget(self.input_comment_user)
        vbox_comment.addWidget(self.label_comment_text)
        vbox_comment.addWidget(self.input_comment_text)
        vbox_comment.addWidget(self.button_comment)

        vbox_message = QVBoxLayout()
        vbox_message.addWidget(self.label_message_user)
        vbox_message.addWidget(self.input_message_user)
        vbox_message.addWidget(self.label_message_text)
        vbox_message.addWidget(self.input_message_text)
        vbox_message.addWidget(self.label_message_time)
        vbox_message.addWidget(self.input_message_time)
        vbox_message.addWidget(self.button_message)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox_like)
        hbox.addLayout(vbox_comment)
        hbox.addLayout(vbox_message)
        hbox.setSpacing(20)  # Add spacing between vertical boxes

        vbox_main = QVBoxLayout()
        vbox_main.addWidget(self.label_heading)
        vbox_main.addWidget(self.label_intro)
        vbox_main.addWidget(self.label_goal)
        vbox_main.addWidget(self.label_security)
        vbox_main.addWidget(self.button_view_security)
        vbox_main.addLayout(form_layout)
        vbox_main.addLayout(hbox)
        vbox_main.setSpacing(10)  # Adjust spacing between elements

        self.setLayout(vbox_main)

    def input_style(self):
        return """
            QLineEdit, QTextEdit {
                border: 2px solid #ccc;
                border-radius: 8px;
                padding: 6px;
                font-size: 14px;
                color: #333;
            }
            QLineEdit:focus, QTextEdit:focus {
                border: 2px solid #4CAF50;
            }
        """

    def button_style(self, color):
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                font-size: 14px;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
            }}
            QPushButton:hover {{
                background-color: {color}CC;
            }}
            QPushButton:pressed {{
                background-color: {color}99;
            }}
        """

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def open_security_agreement(self):
        # Show the security agreement widget
        self.agreement_widget = SecurityAgreementWidget()
        self.agreement_widget.show()

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()
        # Implement your login logic here using pyinsta or instapy
        print(f"Logging in with Username: {username}, Password: {password}")

    def like_posts(self):
        user_to_like = self.input_like.text()
        # Implement the logic to like posts here using instapy
        print(f"Liking posts for User: {user_to_like}")

    def comment_on_posts(self):
        user_to_comment = self.input_comment_user.text()
        comment_text = self.input_comment_text.toPlainText()
        # Implement the logic to comment on posts here using instapy
        print(f"Commenting '{comment_text}' on posts for User: {user_to_comment}")

    def send_message(self):
        user_to_message = self.input_message_user.text()
        message_text = self.input_message_text.toPlainText()
        message_time = self.input_message_time.text()
        # Implement the logic to send message here using pyinsta
        print(f"Sending message '{message_text}' to User: {user_to_message} at {message_time}")

class SecurityAgreementWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Security Promise and Agreement")
        self.setStyleSheet("background-color: #fff;")

        # Create your UI components for the security agreement widget
        label_title = QLabel("Security Promise and Agreement")
        label_title.setAlignment(Qt.AlignCenter)
        label_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #333;")

        # Example text for the agreement
        agreement_text = QTextEdit()
        agreement_text.setPlainText(
            "we are committed to safeguarding your privacy and ensuring the security of your personal information. This Security Promise outlines our dedication to protecting your data and maintaining your trust.\n\n"
            "1. **Data Protection**: We employ industry-standard security measures to protect your information from unauthorized access, alteration, disclosure, or destruction.\n\n"
            "2. **Use of Information**: Your Instagram credentials are used solely for logging into your account and performing automated interactions as requested by you. We do not store your credentials beyond what is necessary for these purposes.\n\n"
            "3. **Transparency**: We are transparent about our data practices and will notify you promptly if there are any changes that may affect your privacy rights.\n\n"
            "4. **Legal Compliance**: We adhere to applicable data protection laws and regulations to ensure that your information is handled lawfully and ethically.\n\n"
            "5. **Third-Party Services**: When necessary, we may use third-party services for authentication or interaction automation. These services adhere to strict security and privacy standards.\n\n"
            "6. **User Control**: You have the right to access, correct, or delete your personal information stored within our application. You can manage these settings directly through your account.\n\n"
            "By using our Instagram Bot application, you agree to abide by this Security Promise and Agreement. If you have any questions or concerns about our practices, please contact us at [Your Contact Information]."
        )
        agreement_text.setStyleSheet("""
            font-size: 14px;
            color: #555;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
        """)
        agreement_text.setReadOnly(True)

        # Close button to return to the main application
        button_close = QPushButton("Close")
        button_close.clicked.connect(self.close_agreement)
        button_close.setStyleSheet("""
            QPushButton {
                background-color: #FF5722;
                color: white;
                font-size: 14px;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #FF5722CC;
            }
            QPushButton:pressed {
                background-color: #FF572299;
            }
        """)

        # Layout for security agreement widget
        vbox = QVBoxLayout()
        vbox.addWidget(label_title)
        vbox.addWidget(agreement_text)
        vbox.addWidget(button_close)
        vbox.setAlignment(Qt.AlignCenter)

        self.setLayout(vbox)

    def close_agreement(self):
        self.hide()  # Hide the agreement widget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InstagramBotApp()
    window.show()
    sys.exit(app.exec_())
