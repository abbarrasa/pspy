from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QTextCursor
from PyQt5.QtWidgets import (QDialog, QDialogButtonBox, QLabel,
    QTabWidget, QTextBrowser, QHBoxLayout, QVBoxLayout)
import base64
    
    
class About(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        aboutText = self.tr("""<p>A simple weather information applet.</p>
            <p>Website: <a href="https://github.com/abbarrasa/openbox">
            https://github.com/abbarrasa/openbox</a></p>
            <p>Data source: <a href="https://www.yahoo.com/news/weather">
            Yahoo! News</a>.</p>
            <p>Based in <a href="https://github.com/decayofmind/weatherboy">Weatherboy</a>.</p>
            <p>If you want to report a dysfunction or a suggestion,
            feel free to open an issue in <a href="https://github.com/abbarrasa/openbox/issues">
            github</a>.""")
        creditsText = self.tr("""(c) 2018 Alberto Buitrago <%s>""") % base64.b64decode('YWJiYXJyYXNhQGdtYWlsLmNvbQ==').decode('utf-8')
        licenseText = self.tr("""<p>This program is free software; you can
            redistribute it and/or modify it under the terms of the GNU
            General Public License as published by the free Software
            Foundation, either version 3 of the License, or (at your option)
            any later version.</p>
            <p>This program is distributed in the hope that it will be useful,
            but WITHOUT ANY WARRANTY; without even the implied warranty of
            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
            General Public License for more details.</p>
            <p>You should have received a copy of the GNU General Public
            License along with this program. If not, see
            <a href="http://www.gnu.org/licenses/gpl-3.0.html">GNU General Public
            License version 3</a>.</p>""")

        layout = QVBoxLayout()
        titleLayout = QHBoxLayout()
        titleLabel = QLabel('<font size="4"><b>{0} {1}</b></font>'.format('PSPy', '0.0.1'))

        contentsLayout = QHBoxLayout()
        aboutBrowser = QTextBrowser()
        aboutBrowser.append(aboutText)
        aboutBrowser.setOpenExternalLinks(True)

        creditsBrowser = QTextBrowser()
        creditsBrowser.append(creditsText)
        creditsBrowser.setOpenExternalLinks(True)

        licenseBrowser = QTextBrowser()
        licenseBrowser.append(licenseText)
        licenseBrowser.setOpenExternalLinks(True)

        TabWidget = QTabWidget()
        TabWidget.addTab(aboutBrowser, self.tr('About'))
        TabWidget.addTab(creditsBrowser, self.tr('Contributors'))
        TabWidget.addTab(licenseBrowser, self.tr('License'))

        aboutBrowser.moveCursor(QTextCursor.Start)
        creditsBrowser.moveCursor(QTextCursor.Start)
        licenseBrowser.moveCursor(QTextCursor.Start)

        icon = QIcon.fromTheme('indicator-weather')
        pixmap = icon.pixmap(QSize(64, 64))
        imageLabel = QLabel()
        imageLabel.setPixmap(pixmap)
        titleLayout.addWidget(imageLabel)
        titleLayout.addWidget(titleLabel)
        titleLayout.addStretch()
        contentsLayout.addWidget(TabWidget)
        buttonLayout = QHBoxLayout()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
        buttonLayout.addWidget(buttonBox)
        layout.addLayout(titleLayout)
        layout.addLayout(contentsLayout)
        layout.addLayout(buttonLayout)
        buttonBox.clicked.connect(dialog.accept)

        self.setLayout(layout)
        self.setMinimumSize(QSize(480, 400))
        self.setWindowTitle(self.tr('About PSPy'))
        self.setWindowIcon(QIcon.fromTheme('help-about'))
        self.show()
