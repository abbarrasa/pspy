# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot


class Ui_EditDialog(QObject):
    def setupUi(self, EditDialog):
        EditDialog.setObjectName("EditDialog")
        EditDialog.resize(448, 360)
        EditDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.titleLabel = QtWidgets.QLabel(EditDialog)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.titleEdit = QtWidgets.QLineEdit(EditDialog)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout.addWidget(self.titleEdit, 0, 1, 1, 1)
        self.descriptionLabel = QtWidgets.QLabel(EditDialog)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridLayout.addWidget(self.descriptionLabel, 1, 0, 1, 1)
        self.formatLabel = QtWidgets.QLabel(EditDialog)
        self.formatLabel.setObjectName("formatLabel")
        self.gridLayout.addWidget(self.formatLabel, 2, 0, 1, 1)
        self.formatCombo = QtWidgets.QComboBox(EditDialog)
        self.formatCombo.addItem("ISO", "ISO")
        self.formatCombo.addItem("CSO", "CSO")
        self.formatCombo.addItem("Eboot", "Eboot")        
        self.formatCombo.setMaxVisibleItems(3)
        self.formatCombo.setMaxCount(3)
        self.formatCombo.setObjectName("formatCombo")
        self.gridLayout.addWidget(self.formatCombo, 2, 1, 1, 1)
        self.descriptionEdit = QtWidgets.QLineEdit(EditDialog)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout.addWidget(self.descriptionEdit, 1, 1, 1, 1)
        self.commentEdit = QtWidgets.QTextEdit(EditDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.commentEdit.setFont(font)
        self.commentEdit.setWhatsThis("")
        self.commentEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.commentEdit.setAcceptRichText(False)
        self.commentEdit.setObjectName("commentEdit")
        self.gridLayout.addWidget(self.commentEdit, 5, 1, 2, 1)
        self.sizeLabel = QtWidgets.QLabel(EditDialog)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 3, 0, 1, 1)
        self.sizeSpin = QtWidgets.QSpinBox(EditDialog)
        self.sizeSpin.setMaximum(99)
        self.sizeSpin.setObjectName("sizeSpin")
        self.gridLayout.addWidget(self.sizeSpin, 3, 1, 1, 1)
        self.commentLabel = QtWidgets.QLabel(EditDialog)
        self.commentLabel.setAlignment(QtCore.Qt.AlignTop)
        self.commentLabel.setObjectName("commentLabel")
        self.gridLayout.addWidget(self.commentLabel, 5, 0, 1, 1)
        self.pathLabel = QtWidgets.QLabel(EditDialog)
        self.pathLabel.setObjectName("pathLabel")
        self.gridLayout.addWidget(self.pathLabel, 7, 0, 1, 1)
        self.pathEdit = QtWidgets.QLineEdit(EditDialog)
        self.pathEdit.setObjectName("pathEdit")
        self.gridLayout.addWidget(self.pathEdit, 7, 1, 1, 1)
        self.coverLabel = QtWidgets.QLabel(EditDialog)
        self.coverLabel.setObjectName("coverLabel")
        self.gridLayout.addWidget(self.coverLabel, 8, 0, 1, 1)
        self.coverEdit = QtWidgets.QLineEdit(EditDialog)
        self.coverEdit.setObjectName("coverEdit")
        self.gridLayout.addWidget(self.coverEdit, 8, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(EditDialog)
        self.buttonBox.rejected.connect(EditDialog.reject)
        self.buttonBox.accepted.connect(EditDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(EditDialog)

    def retranslateUi(self, EditDialog):
        _translate = QtCore.QCoreApplication.translate
        EditDialog.setWindowTitle(_translate("edit", "Add New Game"))
        self.titleLabel.setText(_translate("edit", "Title:"))
        self.titleEdit.setToolTip(_translate("edit", "Enter the name of the game"))
        self.descriptionLabel.setText(_translate("edit", "Description:"))
        self.formatLabel.setText(_translate("edit", "Format:"))
        self.formatCombo.setToolTip(_translate("edit", "Select the format of the backup game (ISO, CSO or Eboot)"))
        self.descriptionEdit.setToolTip(_translate("edit", "Enter a description for the game"))
        self.commentEdit.setToolTip(_translate("edit", "Enter the text of the comment"))
        self.sizeLabel.setText(_translate("edit", "Size"))
        self.sizeSpin.setSuffix(_translate("edit", " bytes"))
        self.commentLabel.setText(_translate("edit", "Comment:"))
        self.pathLabel.setText(_translate("edit", "Path"))
        self.coverLabel.setText(_translate("edit", "Cover"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditDialog = QtWidgets.QDialog()
    ui = Ui_EditDialog()
    ui.setupUi(EditDialog)
    EditDialog.show()
    sys.exit(app.exec_())

