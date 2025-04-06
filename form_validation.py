import sys
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QTextEdit, QComboBox,
    QPushButton, QFormLayout, QMessageBox, QShortcut
)
from PyQt5.QtGui import QKeySequence

class FormValidationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation")
        self.setup_ui()

    def setup_ui(self):
        layout = QFormLayout()

        self.name_input = QLineEdit()
        layout.addRow("Name:", self.name_input)

        self.email_input = QLineEdit()
        layout.addRow("Email:", self.email_input)

        self.age_input = QLineEdit()
        layout.addRow("Age:", self.age_input)

        self.phone_input = QLineEdit()
        self.phone_input.setInputMask("+62 000 0000 0000;_")
        layout.addRow("Phone Number:", self.phone_input)

        self.address_input = QTextEdit()
        layout.addRow("Address:", self.address_input)

        self.gender_input = QComboBox()
        self.gender_input.addItems(["", "Male", "Female"])
        layout.addRow("Gender:", self.gender_input)

        self.education_input = QComboBox()
        self.education_input.addItems(["","Elementary School", "Junior High School","Senior High School" "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral Degree"])
        layout.addRow("Education:", self.education_input)

        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.validate_form)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_fields)

        layout.addRow(self.save_button, self.clear_button)

        # Shortcut to quit
        quit_shortcut = QShortcut(QKeySequence("Q"), self)
        quit_shortcut.activated.connect(self.close)

        self.setLayout(layout)

    def validate_form(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.toPlainText().strip()
        gender = self.gender_input.currentText()
        education = self.education_input.currentText()

        if not all([name, email, age, phone, address, gender, education]):
            self.show_warning("All fields are required.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_warning("Invalid email format.")
            return
        if not age.isdigit():
            self.show_warning("Age must be numeric.")
            return
        if not (17 <= int(age) <= 100):
            self.show_warning("Age must be between 17 and 100.")
            return
        if not re.fullmatch(r"\+62 \d{3} \d{4} \d{4}", phone):
            self.show_warning("Phone number must follow +62 XXX XXXX XXXX format.")
            return

        QMessageBox.information(self, "Success", "Form submitted successfully!")
        self.clear_fields()

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_input.setCurrentIndex(0)
        self.education_input.setCurrentIndex(0)

    def show_warning(self, message):
        QMessageBox.warning(self, "Validation Error", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
