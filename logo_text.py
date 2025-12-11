import kivy

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

def add_logo(layout):
    anchorlayout=AnchorLayout(anchor_x = 'left',anchor_y = 'top')
    Boxlayout = BoxLayout(orientation='horizontal',height=300,padding=10 , spacing=10)

    logo_path = "C:\\Users\\kumar\\OneDrive\\Documents\\Desktop\\calc_apk\\logo.jpg"
    logo = Image(source=logo_path, size=(100, 100),height=30,allow_stretch=True,size_hint=(None,None))
    label = Label(text = "CALCULATOR",font_size="12sp",size=(240,50),size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
    label.bind(size=label.setter('text_size'))

    anchorlayout.add_widget(logo)
    anchorlayout.add_widget(label)
    layout.add_widget(anchorlayout)

