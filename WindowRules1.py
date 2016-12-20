# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WindowRules.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RuleEditorWidget(object):
    def setupUi(self, RuleEditorWidget):
        RuleEditorWidget.setObjectName(_fromUtf8("RuleEditorWidget"))
        RuleEditorWidget.resize(400, 340)
        font = QtGui.QFont()
        font.setPointSize(12)
        RuleEditorWidget.setFont(font)
        RuleEditorWidget.setAcceptDrops(False)
        self.gridLayoutWidget = QtGui.QWidget(RuleEditorWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 201))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.LCellBorn = QtGui.QLabel(self.gridLayoutWidget)
        self.LCellBorn.setAlignment(QtCore.Qt.AlignCenter)
        self.LCellBorn.setObjectName(_fromUtf8("LCellBorn"))
        self.gridLayout.addWidget(self.LCellBorn, 5, 0, 1, 1)
        self.CellDiesLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.CellDiesLineEdit.setMaxLength(50)
        self.CellDiesLineEdit.setObjectName(_fromUtf8("CellDiesLineEdit"))
        self.gridLayout.addWidget(self.CellDiesLineEdit, 3, 1, 1, 1)
        self.LRulePresets = QtGui.QLabel(self.gridLayoutWidget)
        self.LRulePresets.setMaximumSize(QtCore.QSize(16777215, 50))
        self.LRulePresets.setFrameShape(QtGui.QFrame.NoFrame)
        self.LRulePresets.setAlignment(QtCore.Qt.AlignCenter)
        self.LRulePresets.setObjectName(_fromUtf8("LRulePresets"))
        self.gridLayout.addWidget(self.LRulePresets, 0, 0, 1, 1)
        self.RemovePreset = QtGui.QPushButton(self.gridLayoutWidget)
        self.RemovePreset.setObjectName(_fromUtf8("RemovePreset"))
        self.gridLayout.addWidget(self.RemovePreset, 1, 1, 1, 1)
        self.LCellDies = QtGui.QLabel(self.gridLayoutWidget)
        self.LCellDies.setFrameShape(QtGui.QFrame.NoFrame)
        self.LCellDies.setAlignment(QtCore.Qt.AlignCenter)
        self.LCellDies.setObjectName(_fromUtf8("LCellDies"))
        self.gridLayout.addWidget(self.LCellDies, 3, 0, 1, 1)
        self.RulePresetnComboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.RulePresetnComboBox.setEditable(False)
        self.RulePresetnComboBox.setObjectName(_fromUtf8("RulePresetnComboBox"))
        self.gridLayout.addWidget(self.RulePresetnComboBox, 0, 1, 1, 1)
        self.CellBornLineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.CellBornLineEdit.setMaxLength(50)
        self.CellBornLineEdit.setObjectName(_fromUtf8("CellBornLineEdit"))
        self.gridLayout.addWidget(self.CellBornLineEdit, 5, 1, 1, 1)
        self.AddPreset = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddPreset.sizePolicy().hasHeightForWidth())
        self.AddPreset.setSizePolicy(sizePolicy)
        self.AddPreset.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.AddPreset.setObjectName(_fromUtf8("AddPreset"))
        self.gridLayout.addWidget(self.AddPreset, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(RuleEditorWidget)
        self.groupBox.setGeometry(QtCore.QRect(19, 9, 371, 221))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget.raise_()
        self.LCellBorn_2 = QtGui.QLabel(RuleEditorWidget)
        self.LCellBorn_2.setGeometry(QtCore.QRect(20, 230, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LCellBorn_2.setFont(font)
        self.LCellBorn_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.LCellBorn_2.setObjectName(_fromUtf8("LCellBorn_2"))
        self.groupBox.raise_()
        self.gridLayoutWidget.raise_()
        self.LCellBorn_2.raise_()
        self.LCellBorn.setBuddy(self.CellBornLineEdit)
        self.LRulePresets.setBuddy(self.RulePresetnComboBox)
        self.LCellDies.setBuddy(self.CellDiesLineEdit)
        self.LCellBorn_2.setBuddy(self.CellBornLineEdit)

        self.retranslateUi(RuleEditorWidget)
        QtCore.QMetaObject.connectSlotsByName(RuleEditorWidget)

    def retranslateUi(self, RuleEditorWidget):
        RuleEditorWidget.setWindowTitle(_translate("RuleEditorWidget", "Edit Rules", None))
        self.LCellBorn.setToolTip(_translate("RuleEditorWidget", "total number does not have to cover all number 0 to 7.\n"
"Not listed states will just stay allive", None))
        self.LCellBorn.setText(_translate("RuleEditorWidget", "New cell is born at: ", None))
        self.CellDiesLineEdit.setStatusTip(_translate("RuleEditorWidget", "1,2,3,4", None))
        self.CellDiesLineEdit.setText(_translate("RuleEditorWidget", "0,1,4,5,6,7", None))
        self.LRulePresets.setText(_translate("RuleEditorWidget", "Rule Presets", None))
        self.RemovePreset.setToolTip(_translate("RuleEditorWidget", "Removes current preset", None))
        self.RemovePreset.setText(_translate("RuleEditorWidget", "Remove Preset", None))
        self.LCellDies.setToolTip(_translate("RuleEditorWidget", "Use numbers 0 to 7. You can write for exsample:\n"
"1,2,3,4\n"
"1 6 7\n"
" 532", None))
        self.LCellDies.setText(_translate("RuleEditorWidget", "Cell dies when at:", None))
        self.CellBornLineEdit.setText(_translate("RuleEditorWidget", "3", None))
        self.AddPreset.setToolTip(_translate("RuleEditorWidget", "Saves current settings", None))
        self.AddPreset.setText(_translate("RuleEditorWidget", "Add Preset", None))
        self.LCellBorn_2.setToolTip(_translate("RuleEditorWidget", "total number does not have to cover all number 0 to 7.\n"
"Not listed states will just stay allive", None))
        self.LCellBorn_2.setText(_translate("RuleEditorWidget", "*See some exsamples:\n"
" 1,2,5 cell dies when surrounded by 1,2,5 neighours\n"
" 7 ,4,2- cell dies when surrounded by 2,4 or 7 neighours\n"
" 4a5t - invalid input", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    RuleEditorWidget = QtGui.QWidget()
    ui = Ui_RuleEditorWidget()
    ui.setupUi(RuleEditorWidget)
    RuleEditorWidget.show()
    sys.exit(app.exec_())

