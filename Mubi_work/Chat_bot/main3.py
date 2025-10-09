import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QFont, QColor, QTextCharFormat, QTextCursor
from PyQt5.QtCore import Qt
import google.generativeai as genai

API_KEY = "AIzaSyAg_h2eXPZ9fweAf2cmwCJls0amsEV5PLc"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite')

def load_data():
    try:
        with open('university_data.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: university_data.txt not found. Please create it."

data = load_data()

def get_gemini_response(user_query):
    system_prompt = f"""
    You are a helpful university assistant for My University. Respond only to university-related queries in natural language.
    Use English, Urdu, or Roman Urdu based on the user's query language:

    * If user writes in English → respond in English.
    * If user writes in Urdu (Arabic script) → respond in Urdu.
    * If user writes in Roman Urdu (Latin script, e.g. "mjhe result btao") → respond in Roman Urdu.
      Be polite and natural, like a human helper.

    Use this data to answer: {data}
    If the query is not related to university and computer science department info, say "Sorry, I can only help with university and computer science department questions."

    Example:
    If user asks "Sir Ahmed ka subject batao" → respond "Sir Ahmed khan Physics padhate hain, class 12 PM Section A mein hai."

    Keep responses short and direct—no deep reasoning or extra analysis.
    """

    full_prompt = f"{system_prompt}\nUser: {user_query}"
    try:
        response = model.generate_content(full_prompt)
        return response.text if response.text else "No response generated."
    except Exception as e:
        return f"Error generating response: {str(e)}"

class UniversityApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Uni_Assistant")
        self.setGeometry(100, 100, 700, 550)
        self.setStyleSheet("background-color: #fffbea;")  # soft yellow

        # Main widget
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Header
        header = QLabel("🎓 Uni_Assistant – University Chatbot")
        header.setFont(QFont("Arial", 16, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("background-color: maroon; color: white; padding: 12px; border-radius: 5px;")
        main_layout.addWidget(header)

        # Chat display
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setFont(QFont("Arial", 12))
        self.chat_display.setStyleSheet("background-color: #ffffff; border: 2px solid maroon; padding: 10px;")
        main_layout.addWidget(self.chat_display)

        # Input field
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 11))
        self.input_field.setStyleSheet("border: 2px solid maroon; padding: 6px;")
        self.input_field.returnPressed.connect(self.send_message)
        main_layout.addWidget(self.input_field)

        # Send button
        send_button = QPushButton("Send")
        send_button.setFont(QFont("Arial", 11, QFont.Bold))
        send_button.setStyleSheet("background-color: maroon; color: white; padding: 6px; border-radius: 5px;")
        send_button.clicked.connect(self.send_message)
        main_layout.addWidget(send_button)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def append_message(self, sender, message, sender_type="user"):
        cursor = self.chat_display.textCursor()
        cursor.movePosition(QTextCursor.End)

        fmt = QTextCharFormat()
        if sender_type == "user":
            fmt.setBackground(QColor("#dbefff"))  # light blue
            fmt.setForeground(QColor("black"))
        else:
            fmt.setBackground(QColor("#f7dada"))  # light maroon-pink
            fmt.setForeground(QColor("black"))

        cursor.insertBlock()
        cursor.setBlockFormat(cursor.blockFormat())
        cursor.insertText(f"{sender}: {message}", fmt)
        cursor.insertBlock()

        self.chat_display.setTextCursor(cursor)
        self.chat_display.ensureCursorVisible()

    def send_message(self):
        user_query = self.input_field.text().strip()
        if user_query:
            self.append_message("You", user_query, sender_type="user")
            response = get_gemini_response(user_query)
            self.append_message("Uni_Assistant", response, sender_type="bot")
            self.input_field.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UniversityApp()
    window.show()
    sys.exit(app.exec_())
