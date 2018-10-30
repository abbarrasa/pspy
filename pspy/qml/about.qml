pragma Singleton
import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Dialogs 1.2

Dialog {
    id: aboutDialog
    width: 400
    height: 400
    title: qsTr("About")
    standardButtons: StandardButton.Ok

    contentItem: TabView {
        Tab {
            title: "Red"
            Rectangle { color: "red" }
        }
        Tab {
            title: "Blue"
            Rectangle { color: "blue" }
        }
        Tab {
            title: "Green"
            Rectangle { color: "green" }
        }
    }
}
