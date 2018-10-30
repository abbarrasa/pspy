import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Window 2.2
import QtQuick.Layouts 1.1
import "."

//window containing the application
ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    property string status0: "Some text"
    property string status1: "Some more text"

    //menu containing two menu items
    menuBar: MenuBar {
        Menu {
            title: qsTr("File")
            MenuItem {
                text: qsTr("&Open")
                onTriggered: console.log("Open action triggered");
            }
            MenuItem {
                text: qsTr("E&xit")
                iconName: "application-exit"
                onTriggered: Qt.quit();
            }
        }
        Menu {
            title: qsTr("Help")
            MenuItem {
                action: Action {
                    id: aboutAction
                    text: qsTr("&About")
                    iconName: "help-about"
                    onTriggered: {
                        AboutDialog.visible = true
                        AboutDialog.open()
                    }
                }
            }
        }
    }

    //Content Area

    //a button in the middle of the content area
    Button {
        text: qsTr("Hello World")
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }

    statusBar: StatusBar {
        RowLayout {
            anchors.fill: parent
            Label { text: status0 }
        }
    }
}

