# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from game import Game
from cover import Cover
#from settings import Settings
from util import Util


class Ui_EditDialog(QObject):
    def setupUi(self, EditDialog):
        EditDialog.setObjectName("EditDialog")
        EditDialog.resize(448, 360)
        EditDialog.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(EditDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.titleLabel = QtWidgets.QLabel(EditDialog)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.titleEdit = QtWidgets.QLineEdit(EditDialog)
        self.titleEdit.setObjectName("titleEdit")
        self.gridLayout.addWidget(self.titleEdit, 0, 1, 1, 2)
        self.descriptionLabel = QtWidgets.QLabel(EditDialog)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridLayout.addWidget(self.descriptionLabel, 1, 0, 1, 1)
        self.formatLabel = QtWidgets.QLabel(EditDialog)
        self.formatLabel.setObjectName("formatLabel")
        self.gridLayout.addWidget(self.formatLabel, 2, 0, 1, 1)
        self.formatCombo = QtWidgets.QComboBox(EditDialog)
        self.formatCombo.addItems(['ISO', 'CSO', 'Eboot'])
        self.formatCombo.setObjectName("formatCombo")
        self.gridLayout.addWidget(self.formatCombo, 2, 1, 1, 2)
        self.descriptionEdit = QtWidgets.QLineEdit(EditDialog)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout.addWidget(self.descriptionEdit, 1, 1, 1, 2)
        self.commentEdit = QtWidgets.QTextEdit(EditDialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(9)
        self.commentEdit.setFont(font)
        self.commentEdit.setWhatsThis("")
        self.commentEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.commentEdit.setAcceptRichText(False)
        self.commentEdit.setObjectName("commentEdit")
        self.gridLayout.addWidget(self.commentEdit, 5, 1, 2, 2)
        self.sizeLabel = QtWidgets.QLabel(EditDialog)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 3, 0, 1, 1)
        self.sizeSpin = QtWidgets.QSpinBox(EditDialog)
        self.sizeSpin.setRange(0, 10000)
        self.sizeSpin.setObjectName("sizeSpin")
        self.gridLayout.addWidget(self.sizeSpin, 3, 1, 1, 1)
        self.unitCombo = QtWidgets.QComboBox(EditDialog)
        self.unitCombo.addItems(['MiB', 'GiB'])
        self.unitCombo.setObjectName("unitCombo")
        self.gridLayout.addWidget(self.unitCombo, 3, 2, 1, 1)
        self.commentLabel = QtWidgets.QLabel(EditDialog)
        self.commentLabel.setAlignment(QtCore.Qt.AlignTop)
        self.commentLabel.setObjectName("commentLabel")
        self.gridLayout.addWidget(self.commentLabel, 5, 0, 1, 2)
        self.pathLabel = QtWidgets.QLabel(EditDialog)
        self.pathLabel.setObjectName("pathLabel")
        self.gridLayout.addWidget(self.pathLabel, 7, 0, 1, 1)
        self.pathEdit = QtWidgets.QLineEdit(EditDialog)
        self.pathEdit.setObjectName("pathEdit")
        self.gridLayout.addWidget(self.pathEdit, 7, 1, 1, 2)
        self.coverLabel = QtWidgets.QLabel(EditDialog)
        self.coverLabel.setObjectName("coverLabel")
        self.gridLayout.addWidget(self.coverLabel, 8, 0, 1, 1)
        self.coverEdit = QtWidgets.QLineEdit(EditDialog)
        self.coverEdit.setObjectName("coverEdit")
        self.gridLayout.addWidget(self.coverEdit, 8, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(EditDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.msg = QtWidgets.QMessageBox(EditDialog)
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setWindowTitle("Error")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        self.retranslateUi(EditDialog)
        self.buttonBox.rejected.connect(EditDialog.reject)
        self.buttonBox.accepted.connect(
            lambda dialog=EditDialog: self.saveCall(dialog))
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
        self.sizeLabel.setText(_translate("edit", "Size:"))
        self.commentLabel.setText(_translate("edit", "Comment:"))
        self.pathLabel.setText(_translate("edit", "Path:"))
        self.coverLabel.setText(_translate("edit", "Cover:"))

    @pyqtSlot()
    def saveCall(self, dialog):
        try:
            title = self.titleEdit.text().strip()
            description = self.descriptionEdit.text().strip()
            comment = self.commentEdit.toPlainText().strip()
            path = self.pathEdit.text().strip()
            filename = self.coverEdit.text().strip()
            format = str(self.formatCombo.currentText())
            size = Util.toBytes("{0}{1}".format(str(self.sizeSpin.value()), str(self.unitCombo.currentText())))
            g = Game(title=title, description=description, size=size, format=format, path=path, comment=comment)
            if filename:
                Cover().generateThumbnail(filename, str(id(g.id)))


            #generator2 = Cover(raw=g.cover)
            #settings = Settings()
            #directory = settings.read().get('General', 'thumbnail_directory')
            #generator2.save(str(id(g.id)), '.')

            print("Save")
            dialog.close()
        except ValueError as err:
            print(str(err))
            self.msg.setText(str(err))
            self.msg.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditDialog = QtWidgets.QDialog()
    ui = Ui_EditDialog()
    ui.setupUi(EditDialog)
    EditDialog.show()
    sys.exit(app.exec_())
