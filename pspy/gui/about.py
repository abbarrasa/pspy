# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
import resources


class Ui_About(QObject):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(389, 294)
        about.setWindowIcon(QtGui.QIcon.fromTheme('help-about'))
        self.verticalLayout = QtWidgets.QVBoxLayout(about)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(about)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setMinimumSize(QtCore.QSize(71, 71))
        self.label.setMaximumSize(QtCore.QSize(71, 71))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/resources/icons/pspy.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.version_label = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.version_label.setFont(font)
        self.version_label.setText("PSPy 0.0.1")
        self.version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.version_label.setObjectName("version_label")
        self.verticalLayout_6.addWidget(self.version_label)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.website_label = QtWidgets.QLabel(self.page)
        self.website_label.setToolTip("melloristudio.com")
        self.website_label.setText("")
        self.website_label.setAlignment(QtCore.Qt.AlignCenter)
        self.website_label.setObjectName("website_label")
        self.verticalLayout_6.addWidget(self.website_label)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.page_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.writtenBy = QtWidgets.QTextBrowser(self.tab)
        self.writtenBy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p></body></html>")
        self.writtenBy.setOpenExternalLinks(True)
        self.writtenBy.setOpenLinks(True)
        self.writtenBy.setObjectName("writtenBy")
        self.verticalLayout_3.addWidget(self.writtenBy)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.translatedBy = QtWidgets.QTextBrowser(self.tab_2)
        self.translatedBy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p></body></html>")
        self.translatedBy.setOpenExternalLinks(True)
        self.translatedBy.setObjectName("translatedBy")
        self.verticalLayout_4.addWidget(self.translatedBy)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.artworkBy = QtWidgets.QTextBrowser(self.tab_3)
        self.artworkBy.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p></body></html>")
        self.artworkBy.setOpenExternalLinks(True)
        self.artworkBy.setObjectName("artworkBy")
        self.horizontalLayout_3.addWidget(self.artworkBy)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.plain = QtWidgets.QPlainTextEdit(self.page_3)
        self.plain.setReadOnly(True)
        self.plain.setPlainText("PSPy is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.\n"
"\n"
"PSPy is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.\n"
"\n"
"You should have received a copy of the GNU General Public License along with PSPy; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.\n"
"\n"
"For further information you can also visit http://www.gnu.org/licenses/gpl.html")
        self.plain.setObjectName("plain")
        self.verticalLayout_5.addWidget(self.plain)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.about_button = QtWidgets.QPushButton(about)
        self.about_button.setCheckable(True)
        self.about_button.setChecked(True)
        self.about_button.setAutoDefault(False)
        self.about_button.setObjectName("about_button")
        self.about_button.clicked.connect(self.aboutAction)
        self.buttonGroup = QtWidgets.QButtonGroup(about)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.about_button)
        self.horizontalLayout.addWidget(self.about_button)
        self.credits_button = QtWidgets.QPushButton(about)
        self.credits_button.setCheckable(True)
        self.credits_button.setAutoDefault(False)
        self.credits_button.setObjectName("credits_button")
        self.credits_button.clicked.connect(self.creditsAction)
        self.buttonGroup.addButton(self.credits_button)
        self.horizontalLayout.addWidget(self.credits_button)
        self.license_button = QtWidgets.QPushButton(about)
        self.license_button.setCheckable(True)
        self.license_button.setAutoDefault(False)
        self.license_button.setObjectName("license_button")
        self.license_button.clicked.connect(self.licenseAction)
        self.buttonGroup.addButton(self.license_button)
        self.horizontalLayout.addWidget(self.license_button)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.closeButton = QtWidgets.QPushButton(about)
        self.closeButton.setCheckable(True)
        self.closeButton.setAutoDefault(False)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.clicked.connect(
            lambda checked, dialog=about: self.closeAction(dialog))
        self.buttonGroup.addButton(self.closeButton)
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(about)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "About PSPy"))
        self.label_3.setText(_translate("about", "PSPy allows you to manage your games"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("about", "Written by"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("about", "Translated by"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("about", "Artwork by"))
        self.about_button.setText(_translate("about", "About"))
        self.credits_button.setText(_translate("about", "Credits"))
        self.license_button.setText(_translate("about", "Licence"))
        self.closeButton.setText(_translate("about", "Close"))

    @pyqtSlot()
    def aboutAction(self):
        print("About panel")
        self.stackedWidget.setCurrentIndex(0)

    @pyqtSlot()
    def creditsAction(self):
        self.stackedWidget.setCurrentIndex(1)

    @pyqtSlot()
    def licenseAction(self):
        self.stackedWidget.setCurrentIndex(2)

    @pyqtSlot()
    def closeAction(self, dialog):
        print("Close dialog")
        dialog.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(about)
    about.show()
    sys.exit(app.exec_())
