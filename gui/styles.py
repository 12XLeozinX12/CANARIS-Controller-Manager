DARK_THEME = """

QMainWindow,
QWidget
{
    background:#0F0F12;
    color:#FFFFFF;
    font-family:"Segoe UI";
}



QLabel
{
    color:#FFFFFF;
}



QFrame
{
    background:#17171C;
    border-radius:18px;
}



QPushButton
{
    background:#8B5CF6;
    color:white;
    border:none;
    border-radius:12px;
    padding:10px 16px;
    font-size:14px;
    font-weight:bold;
}



QPushButton:hover
{
    background:#7C3AED;
}



QPushButton:pressed
{
    background:#6D28D9;
}





/* INPUTS */


QComboBox,
QSpinBox
{
    background:#202024;
    color:white;
    border:1px solid #303038;
    border-radius:10px;
    padding:8px;
}



QComboBox:hover,
QSpinBox:hover
{
    border:1px solid #8B5CF6;
}



QComboBox::drop-down
{
    border:none;
}





/* CHECKBOX */


QCheckBox
{
    color:#DDDDDD;
    spacing:10px;
}



QCheckBox::indicator
{
    width:18px;
    height:18px;
    border-radius:5px;
    background:#202024;
    border:1px solid #444;
}



QCheckBox::indicator:checked
{
    background:#8B5CF6;
    border:1px solid #8B5CF6;
}






/* SCROLL */


QScrollBar:vertical
{
    background:#111116;
    width:10px;
    margin:0;
    border-radius:5px;
}



QScrollBar::handle:vertical
{
    background:#8B5CF6;
    border-radius:5px;
}



QScrollBar::handle:vertical:hover
{
    background:#A78BFA;
}






/* LISTAS */


QListWidget,
QTableWidget
{
    background:#17171C;
    color:white;
    border:none;
    border-radius:15px;
}



QListWidget::item:hover
{
    background:#25252D;
}



QListWidget::item:selected
{
    background:#8B5CF6;
    border-radius:8px;
}






/* MENU LATERAL */


QToolButton
{
    background:transparent;
    color:#AAAAAA;
    border:none;
    border-radius:12px;
    padding:12px;
    text-align:left;
}



QToolButton:hover
{
    background:#1E1E24;
    color:white;
}



QToolButton:checked
{
    background:#8B5CF6;
    color:white;
}





/* TITULOS */


QLabel#title
{
    color:#8B5CF6;
    font-size:30px;
    font-weight:bold;
}



QLabel#subtitle
{
    color:#999999;
    font-size:14px;
}


"""