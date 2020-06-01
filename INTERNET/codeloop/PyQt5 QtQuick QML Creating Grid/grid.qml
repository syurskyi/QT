import QtQuick.Window 2.2
import QtQuick 2.3



Window {
visible:true
id:root
width:360
height:360


Grid {
spacing:15
columns:4
rows:4

Repeater {
model:16

Rectangle {
color:"red"
width:360/4
height:360/4




}



}

}




}