import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.1

Item {
    id: statusBar
    visible: true
    property string msg0: "Some text"
    property string msg1: "Some more text"

    StatusBar {
        RowLayout {
            anchors.fill: parent
            Label { text: statusBar.msg0 }
        }
    }
}

