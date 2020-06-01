import QtQuick.Window 2.2
import QtQuick 2.3



Window {

visible:true
width:600
height:400
color:"yellow"
title: "PyQt5 QML Window"


Rectangle {

id:blueRect
color:"blue"
width:450
height:64
//x:80
//y:80

anchors.centerIn:parent
border.color:"black"
border.width:6
radius:15




}




Text {

id:text1
text:"Hello QtQuick Application"
font.pixelSize:30
font.bold:true
color:"white"
anchors.centerIn:parent

}




Image {

id:image
source:"qml.png"
sourceSize.width:parent.width/2
sourceSize.height:parent.height/2



}






TextInput {
id:te
text:"Hello"
color:"black"

//scale:6
font.pixelSize: 16; font.bold: true
maximumLength: 16
focus: true
x:200
y:50

font.capitalization: Font.AllUppercase




}





}