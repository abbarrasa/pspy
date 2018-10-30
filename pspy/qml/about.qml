pragma Singleton
import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Dialogs 1.2

Dialog {
    id: aboutDialog
    modality: Qt.WindowModal
    title: qsTr("About")
    width: 400
    height: 400

    TabView {
        id: frame
        anchors.fill: parent
        anchors.margins: 4

        Tab {
            title: qsTr("Tab 1")
            TextArea {
                text: qsTr("<p>A simple weather information applet.</p>
                        <p>Website: <a href=\"https://github.com/abbarrasa/openbox\">
                        https://github.com/abbarrasa/openbox</a></p>
                        <p>Data source: <a href=\"https://www.yahoo.com/news/weather\">
                        Yahoo! News</a>.</p>
                        <p>Based in <a href=\"https://github.com/decayofmind/weatherboy\">Weatherboy</a>.</p>
                        <p>If you want to report a dysfunction or a suggestion,
                        feel free to open an issue in <a href=\"https://github.com/abbarrasa/openbox/issues\">
                        github</a>.")
            }
        }
        Tab { title: "Tab 2" }
        Tab { title: "Tab 3" }
    }
}
