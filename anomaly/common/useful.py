from os.path import exists
WELCOMEMSG = "Simple Anomaly"

DARKMODE = """QTextEdit {
        border: 2px solid #585858;
        border-radius: 4px;}

        QPushButton {
        font-size: 18px; 
        background-color: transparent; 
        outline: none; 
        border: 2px solid #585858;
        border-radius: 4px; 
        margin: 4px;
        padding: 4px;}

        QPushButton:hover {
        border:2px solid red;
        }

        QWidget {
        background-color: #1c1c1c;
        color: #d0d0d0;
        }"""

LIGHTMODE = """QTextEdit {
        border: 2px solid #878787;
        border-radius: 4px;}

        QPushButton {
        font-size: 18px; 
        background-color: transparent; 
        outline: none; 
        border: 2px solid #878787;
        border-radius:4px;
        margin: 4px;
        padding: 4px;}

        QPushButton:hover {
        border: 2px solid red;
        }

        QWidget {
        background-color: #eeeeee;
        color: #444444;
        }"""

BUTTONDICT = {
    "1":{
    "name":"1",
    "function":"number",
    "value":1,
    "shortcut":"1"
    },
    "2":{
    "name":"1",
    "function":"number",
    "value":1,
    "shortcut":"1"
    },
    "3":{
    "name":"1",
    "function":"number",
    "value":1,
    "shortcut":"1"
    },
    "4":{
    "name":"1",
    "function":"number",
    "value":1,
    "shortcut":"1"
    },
    "5":{
    "name":"1",
    "function":"number",
    "value":1,
    "shortcut":""
    },
    "6":{
    "name":"6",
    "function":"number",
    "value":6,
    "shortcut":"6"
    },
    "7":{
    "name":"7",
    "function":"number",
    "value":7,
    "shortcut":"7"
    },
    "8":{
    "name":"1",
    "function":"number",
    "value":1,
    "shortcut":"8"
    },
    "9":{
    "name":"9",
    "function":"number",
    "value":9,
    "shortcut":"9"
    },    
}

