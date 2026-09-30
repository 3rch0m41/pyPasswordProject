"""Main window: connects the widgets designed in Qt Designer to the core logic."""

from PySide6.QtGui import QFontDatabase, QGuiApplication
from PySide6.QtWidgets import QHeaderView, QMainWindow, QTableWidgetItem

from core.password_tools import evaluate_password, generate_passwords
from ui.ui_main_window import Ui_MainWindow

# Progress bar colour for each strength level
STRENGTH_COLORS = {
    "compromised": "#8b0000",
    "very_weak": "#d9534f",
    "weak": "#f0ad4e",
    "fair": "#5bc0de",
    "strong": "#5cb85c",
}


def _color_for(result) -> str:
    if result.is_common:
        return STRENGTH_COLORS["compromised"]
    if result.score < 4:
        return STRENGTH_COLORS["very_weak"]
    if result.score == 4:
        return STRENGTH_COLORS["weak"]
    if result.score == 5:
        return STRENGTH_COLORS["fair"]
    return STRENGTH_COLORS["strong"]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._setup_table()
        self._connect_signals()

    # ---------- setup ----------

    def _setup_table(self):
        header = self.ui.tblResults.horizontalHeader()
        header.setStretchLastSection(False)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tblResults.setToolTip("Double-click a row to copy the password")

    def _connect_signals(self):
        # Evaluate tab: button click or Enter in the text field
        self.ui.btnEvaluate.clicked.connect(self.on_evaluate)
        self.ui.txtPasswordEvaluate.returnPressed.connect(self.on_evaluate)
        # Generate tab
        self.ui.btnGenerate.clicked.connect(self.on_generate)
        self.ui.tblResults.cellDoubleClicked.connect(self.on_copy_password)

    # ---------- Evaluate tab ----------

    def on_evaluate(self):
        password = self.ui.txtPasswordEvaluate.text()
        if not password:
            self.ui.statusbar.showMessage("Type a password first.", 3000)
            return

        result = evaluate_password(password)
        self.ui.pbarEvaluationBar.setMaximum(result.max_score)
        self.ui.pbarEvaluationBar.setValue(result.score)
        self.ui.pbarEvaluationBar.setStyleSheet(
            f"QProgressBar::chunk {{ background-color: {_color_for(result)}; }}"
        )
        self.ui.lblEvaluationResult.setText(
            f"<b>{result.label}</b><br>"
            f"{result.length} characters, {result.char_types}/4 character types"
        )

    # ---------- Generate tab ----------

    def on_generate(self):
        try:
            results = generate_passwords(
                min_len=self.ui.spbMinLen.value(),
                max_len=self.ui.spbMaxLen.value(),
                amount=self.ui.spbQty.value(),
                upper=self.ui.chkUpper.isChecked(),
                lower=self.ui.chkLower.isChecked(),
                digit=self.ui.chkDigit.isChecked(),
                special=self.ui.chkSpecial.isChecked(),
            )
        except ValueError as err:
            self.ui.statusbar.showMessage(str(err), 5000)
            return

        mono = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        table = self.ui.tblResults
        table.setRowCount(len(results))
        for row, (password, result) in enumerate(results):
            pwd_item = QTableWidgetItem(password)
            pwd_item.setFont(mono)
            table.setItem(row, 0, pwd_item)
            table.setItem(row, 1, QTableWidgetItem(f"{result.score}/{result.max_score}"))
            table.setItem(row, 2, QTableWidgetItem(result.label))

        self.ui.statusbar.showMessage(f"Generated {len(results)} passwords.", 3000)

    def on_copy_password(self, row, _column):
        password = self.ui.tblResults.item(row, 0).text()
        QGuiApplication.clipboard().setText(password)
        self.ui.statusbar.showMessage("Password copied to clipboard.", 3000)
