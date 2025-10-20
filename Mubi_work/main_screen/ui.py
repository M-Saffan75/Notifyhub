import os
from PyQt5.QtWidgets import (
    QWidget, QMainWindow, QLabel, QPushButton, QFrame,
    QHBoxLayout, QVBoxLayout, QGridLayout, QGraphicsDropShadowEffect,
    QTableWidget, QTableWidgetItem, QTextEdit, QSizePolicy
)
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtGui import QFont, QFontDatabase, QPixmap


def try_load_font(path):
    try:
        if os.path.exists(path):
            QFontDatabase.addApplicationFont(path)
            return True
    except Exception:
        pass
    return False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow):
        # window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 780)
        MainWindow.setMinimumSize(1024, 600)

        # try load fonts if present
        fonts_dir = os.path.join(os.path.abspath("."), "assets", "fonts")
        try_load_font(os.path.join(fonts_dir, "Montserrat-Bold.ttf"))
        try_load_font(os.path.join(fonts_dir, "Montserrat-Regular.ttf"))
        try_load_font(os.path.join(fonts_dir, "Roboto-Regular.ttf"))
        try_load_font(os.path.join(fonts_dir, "Roboto-Bold.ttf"))

        # Root widget and layout
        self.centralwidget = QWidget(MainWindow)
        self.root_layout = QVBoxLayout(self.centralwidget)
        self.root_layout.setContentsMargins(12, 12, 12, 12)
        self.root_layout.setSpacing(12)

        #  Header
        self.header = QFrame()
        self.header.setObjectName("header")
        self.header.setFixedHeight(72)
        header_layout = QHBoxLayout(self.header)
        header_layout.setContentsMargins(20, 6, 20, 6)

        self.univ_label = QLabel("GC UNIVERSITY HYDERABAD")
        self.univ_label.setObjectName("univLabel")
        self.univ_label.setFont(QFont("Montserrat", 18, QFont.Bold))
        self.univ_label.setStyleSheet("background: transparent;")  # ensure transparent

        self.datetime_label = QLabel()
        self.datetime_label.setObjectName("datetimeLabel")
        self.datetime_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.datetime_label.setFont(QFont("Roboto", 12, QFont.Bold))
        self.datetime_label.setStyleSheet("background: transparent;")  # ensure transparent

        header_layout.addWidget(self.univ_label, 1)
        header_layout.addWidget(self.datetime_label, 0, Qt.AlignRight)
        self.root_layout.addWidget(self.header)

        # ---------- Main Grid (2 columns) ----------
        main_grid = QHBoxLayout()
        main_grid.setSpacing(12)

        # ---------- Left Column ----------
        left_col = QVBoxLayout()
        left_col.setSpacing(12)

        # Alerts card (left)
        self.alerts_card = QFrame()
        self.alerts_card.setObjectName("alertsCard")
        alerts_layout = QVBoxLayout(self.alerts_card)
        alerts_layout.setContentsMargins(16, 16, 16, 16)

        self.alerts_title = QLabel("IMPORTANT ALERTS")
        self.alerts_title.setObjectName("sectionTitle")
        self.alerts_title.setFont(QFont("Montserrat", 14, QFont.Bold))

        self.alerts_text = QLabel(
            "We have updated our academic notices section. Please check & if you have any query feel free to visit Computer Science Department."
        )
        self.alerts_text.setWordWrap(True)
        self.alerts_text.setFont(QFont("Roboto", 11))

        alerts_layout.addWidget(self.alerts_title)
        alerts_layout.addWidget(self.alerts_text)
        self._add_shadow(self.alerts_card)
        left_col.addWidget(self.alerts_card)

        # Academic Notices (left)
        self.notices_card = QFrame()
        self.notices_card.setObjectName("noticesCard")
        notices_outer = QVBoxLayout(self.notices_card)
        notices_outer.setContentsMargins(16, 16, 16, 16)

        self.notices_title = QLabel("ACADEMIC NOTICES")
        self.notices_title.setObjectName("sectionTitle")
        self.notices_title.setFont(QFont("Montserrat", 14, QFont.Bold))
        notices_outer.addWidget(self.notices_title, 0, Qt.AlignLeft)

        images_row = QHBoxLayout()
        images_row.setSpacing(12)
        self.notice_boxes = []
        # store expected notice box size so we can scale images reliably
        self._notice_box_size = (160, 200)
        for i in range(4):
            box = QFrame()
            box.setObjectName("noticeBox")
            box.setFixedSize(self._notice_box_size[0], self._notice_box_size[1])
            inner = QVBoxLayout(box)
            inner.setContentsMargins(6, 6, 6, 6)
            lbl = QLabel("Image Placeholder")
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("color:#999; font-size:12px; background: transparent;")
            # keep a reference to the label (we will set pixmap later)
            self.notice_boxes.append(lbl)
            inner.addWidget(lbl, 1)
            images_row.addWidget(box)
        notices_outer.addLayout(images_row)

        self._add_shadow(self.notices_card)
        left_col.addWidget(self.notices_card)

        # Department Time Tables (3x2 grid) - left column
        self.dept_card = QFrame()
        self.dept_card.setObjectName("deptCard")
        dept_layout = QVBoxLayout(self.dept_card)
        dept_layout.setContentsMargins(16, 16, 16, 16)

        self.dept_title = QLabel("DEPARTMENT TIME TABLES")
        self.dept_title.setObjectName("sectionTitle")
        self.dept_title.setFont(QFont("Montserrat", 14, QFont.Bold))
        dept_layout.addWidget(self.dept_title, 0, Qt.AlignLeft)

        grid = QGridLayout()
        grid.setSpacing(20)
        self.dept_boxes = []
        # use a comfortable size for A4 landscape previews
        self._dept_box_size = (260, 180)
        for r in range(2):
            for c in range(3):
                box = QFrame()
                box.setObjectName("deptBox")
                box.setFixedSize(self._dept_box_size[0], self._dept_box_size[1])
                inner = QVBoxLayout(box)
                inner.setContentsMargins(6, 6, 6, 6)
                label = QLabel("Table Placeholder")
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet("color:#999; font-size:12px; background: transparent;")
                self.dept_boxes.append(label)
                inner.addWidget(label, 1)
                grid.addWidget(box, r, c)
        dept_layout.addLayout(grid)
        self._add_shadow(self.dept_card)
        left_col.addWidget(self.dept_card)

        main_grid.addLayout(left_col, 2)

        # ---------- Right Column ----------
        right_col = QVBoxLayout()
        right_col.setSpacing(12)

        # Department Timetable (right)
        self.tt_card = QFrame()
        self.tt_card.setObjectName("ttCard")
        tt_layout = QVBoxLayout(self.tt_card)
        tt_layout.setContentsMargins(16, 16, 16, 16)

        self.tt_title = QLabel("DEPARTMENT TIME TABLE")
        self.tt_title.setObjectName("sectionTitle")
        self.tt_title.setFont(QFont("Montserrat", 14, QFont.Bold))
        tt_layout.addWidget(self.tt_title)

        self.table = QTableWidget(5, 3)
        self.table.setHorizontalHeaderLabels(["Class", "Time", "Room"])
        self.table.verticalHeader().setVisible(False)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        classes = [
            ("Physics", "8:45-9:30", "Four"),
            ("Chemistry", "9:30-10:20", "Three"),
            ("Algebra", "10:30-11:10", "Four"),
            ("Islamiyat", "11:30-12:20", "Four"),
            ("Statics", "12:20-1:10", "Two"),
        ]
        for r, row in enumerate(classes):
            for c, val in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(val))
        tt_layout.addWidget(self.table)
        self._add_shadow(self.tt_card)
        right_col.addWidget(self.tt_card)

        # Exam Updates (right)
        self.exam_card = QFrame()
        self.exam_card.setObjectName("examCard")
        exam_layout = QVBoxLayout(self.exam_card)
        exam_layout.setContentsMargins(16, 16, 16, 16)

        self.exam_title = QLabel("EXAM UPDATES")
        self.exam_title.setObjectName("sectionTitle")
        self.exam_title.setFont(QFont("Montserrat", 14, QFont.Bold))
        self.exam_text = QLabel("Mid Term: September - October")
        self.exam_text.setFont(QFont("Roboto", 11))
        exam_layout.addWidget(self.exam_title)
        exam_layout.addWidget(self.exam_text)
        self._add_shadow(self.exam_card)
        right_col.addWidget(self.exam_card)

        # AI Assistant (right, expanded)
        self.ai_card = QFrame()
        self.ai_card.setObjectName("aiCard")
        ai_layout = QVBoxLayout(self.ai_card)
        ai_layout.setContentsMargins(16, 16, 16, 16)

        self.ai_title = QLabel("AI ASSISTANT")
        self.ai_title.setObjectName("sectionTitle")
        self.ai_title.setFont(QFont("Montserrat", 14, QFont.Bold))

        self.ai_desc = QTextEdit()
        self.ai_desc.setReadOnly(True)
        self.ai_desc.setText("This AI is built for providing answers under given context only.")
        self.ai_desc.setFont(QFont("Roboto", 11))
        self.ai_desc.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.ai_button = QPushButton("PRESS DOWN BUTTON TO SPEAK")
        self.ai_button.setObjectName("aiButton")
        self.ai_button.setMinimumHeight(50)

        ai_layout.addWidget(self.ai_title)
        ai_layout.addWidget(self.ai_desc, 3)
        ai_layout.addWidget(self.ai_button, 0, Qt.AlignCenter)
        self._add_shadow(self.ai_card)
        right_col.addWidget(self.ai_card, 2)

        main_grid.addLayout(right_col, 1)

        # Add main grid to root
        self.root_layout.addLayout(main_grid)

        # Footer
        self.footer = QLabel("GC University Hyderabad, Kali Mori Hyderabad Sindh, Pakistan - Phone: 022-2111856")
        self.footer.setObjectName("footer")
        self.footer.setAlignment(Qt.AlignCenter)
        self.root_layout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        # start clock
        self._setup_clock()

        # ---------------------------
        # Auto-load images (if present)
        # images folder should be: ./images/
        # ---------------------------
        try:
            images_dir = os.path.join(os.path.abspath("."), "images")
            # notification images (4)
            notice_files = ["noti1.jpg", "noti2.jpg", "noti3.jpg", "noti4.jpg"]
            for idx, fname in enumerate(notice_files):
                path = os.path.join(images_dir, fname)
                if os.path.exists(path) and idx < len(self.notice_boxes):
                    self.set_notice_image(idx, path)
            # dept timetable image (use same image for all 6)
            dept_img = os.path.join(images_dir, "timetab1.jpeg")
            for idx in range(len(self.dept_boxes)):
                if os.path.exists(dept_img):
                    self.set_dept_image(idx, dept_img)
        except Exception:
            # don't crash if image loading fails
            pass

    def _setup_clock(self):
        def update():
            now = QDateTime.currentDateTime()
            self.datetime_label.setText(now.toString("dddd, MMMM d  |  hh:mm AP"))
        update()
        timer = QTimer()
        timer.timeout.connect(update)
        timer.start(1000)
        self._clock_timer = timer

    def _add_shadow(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 4)
        widget.setGraphicsEffect(shadow)

    # helpers to set images later
    def set_notice_image(self, index, path):
        """
        Set an image into the notice_boxes[index].
        Uses known notice box size for scaling.
        """
        try:
            if 0 <= index < len(self.notice_boxes) and os.path.exists(path):
                pix = QPixmap(path)
                if not pix.isNull():
                    lbl = self.notice_boxes[index]
                    target_w, target_h = self._notice_box_size
                    # scale to fit box while keeping aspect ratio
                    scaled = pix.scaled(target_w - 12, target_h - 12, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    lbl.setPixmap(scaled)
                    lbl.setScaledContents(False)
        except Exception:
            pass

    def set_dept_image(self, index, path):
        """
        Set an image into the dept_boxes[index].
        Uses known dept box size for scaling.
        """
        try:
            if 0 <= index < len(self.dept_boxes) and os.path.exists(path):
                pix = QPixmap(path)
                if not pix.isNull():
                    lbl = self.dept_boxes[index]
                    target_w, target_h = self._dept_box_size
                    scaled = pix.scaled(target_w - 12, target_h - 12, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    lbl.setPixmap(scaled)
                    lbl.setScaledContents(False)
        except Exception:
            pass
