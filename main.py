import kivy 

from logo_text import add_logo
from basecon import Base_converter
from basecon import Binary_calculator
from floating import Floating_calculator
from floation_base import FloatingBaseConverter
from complement import Complement



from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

        
class HomeScreen(Screen):
    def __init__(self,**kwargs):
        super(HomeScreen,self).__init__(**kwargs)
        Boxlayout = BoxLayout(orientation='horizontal',height=300,padding=10 , spacing=10)
        boxlayout1 = BoxLayout(orientation='vertical',height=300,padding=10 , spacing=8)
        
        button1 = Button(text = "Floating Calculator ",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        button1.background_color = (1,1,1,1)
        button1.bind(on_press=self.Scientific)

        button2 = Button(text = "MultiBase Calculator",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 60,pos_hint={'center_x':0.5, 'center_y': 1})
        button2.background_color = (1,1,1,1)
        button2.bind(on_press=self.MultiBase)

        button3 = Button(text = "BaseChanger",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        button3.background_color = (1,1,1,1)
        button3.bind(on_press=self.Base)

        button4 = Button(text = "Complexify",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        button4.background_color = (1,1,1,1)
        button4.bind(on_press=self.Complex)

        button5= Button(text = "History",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        button5.background_color = (1,1,1,1)
        button5.bind(on_press=self.History)

        

        
        add_logo(Boxlayout)
        boxlayout1.add_widget(button1)
        boxlayout1.add_widget(button2)
        boxlayout1.add_widget(button3)
        boxlayout1.add_widget(button4)
        boxlayout1.add_widget(button5)
        self.add_widget(Boxlayout)
        
        self.add_widget(boxlayout1)

    def Scientific(self,instance):
        self.manager.current = 'scientificCalc'

    def MultiBase(self,instance):
        self.manager.current = 'BinaryCalc'

    def Base(self,instance):
        self.manager.current = 'Basecon'
    
    def Complex(self,instance):
        self.manager.current = 'Complex'

    def History(self,instance):
        self.manager.current = 'History'

class BaseConScreen(Screen):
    def __init__(self, **kwargs):
        super(BaseConScreen,self).__init__(**kwargs)

        Boxlayout = BoxLayout(orientation='horizontal',height=300,padding=10 , spacing=10)
        boxlayout1 = BoxLayout(orientation='vertical',height=300,padding=10 , spacing=8)
        anchorlayout=AnchorLayout(anchor_x = 'right',anchor_y = 'top')

        button = Button(text = "Home ",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        button.background_color = (1,1,1,1)
        button.bind(on_press=self.Home)

        self.label2 = Label(text = "BaseChanger",color=(1,1,1,1),font_size="20sp",size=(240,50),size_hint = (None,0.3),height = 50,pos_hint={'center_x': 0.1, 'center_y': 1})
        boxlayout1.add_widget(self.label2)

        self.label1 = Label(text = "_______________________________________________________________________________________________________________________________________________",color=(1,0,0,1),font_size="12sp",size=(200,50),size_hint = (None,0.1),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        boxlayout1.add_widget(self.label1)

        
        self.label = Label(text = "0",color=(1,1,1,1),font_size="20sp",size=(240,50),size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        boxlayout1.add_widget(self.label)
        

        self.numer1= None
        self.number2 = None
        self.current_value  = ""

        
        
        gridlayout = GridLayout(cols=4, spacing=10, padding=10, size_hint=(1, 1))
        for i in range(0, 10):  # Create buttons from 1 to 10
            btn = Button(text=str(i),size_hint =(50,50))
            btn.bind(on_press=self.update_label)
            gridlayout.add_widget(btn)

        for char in"ABCDEF":  # Create buttons from 1 to 10
            btn = Button(text=char,size_hint =(50,50))
            btn.bind(on_press=self.update_label)
            gridlayout.add_widget(btn)

        # sin_btn= Button(text = "Button",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        # sin_btn.background_color = (1,1,1,1)
        # sin_btn.bind(on_press=self.updat)
        # gridlayout.add_widget(sin_btn)

        Back_btn= Button(text = "back",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        Back_btn.background_color = (1,1,1,1)
        Back_btn.bind(on_press=self.Back_space)
        #gridlayout.add_widget(Back_btn)


        cleanbutton= Button(text = "C",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        cleanbutton.background_color = (1,1,1,1)
        cleanbutton.bind(on_press=self.Clean)
        gridlayout.add_widget(cleanbutton)
        
        eq_button= Button(text = "=",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        eq_button.background_color = (1,1,1,1)
        eq_button.bind(on_press=self.equal)
        gridlayout.add_widget(eq_button)

        num1button= Button(text = "Num1",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        num1button.background_color = (1,1,1,1)
        num1button.bind(on_press=self.num1)
        gridlayout.add_widget(num1button)
        
        num2button= Button(text = "Base",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        num2button.background_color = (1,1,1,1)
        num2button.bind(on_press=self.num2)
        gridlayout.add_widget(num2button)


        to_binary= Button(text = "B",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        to_binary.background_color = (1,1,1,1)
        to_binary.bind(on_press=self.binary)
        gridlayout.add_widget(to_binary)
        
        to_octal= Button(text = "O",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        to_octal.background_color = (1,1,1,1)
        to_octal.bind(on_press=self.octal)
        gridlayout.add_widget(to_octal)

        to_decimal= Button(text = "D",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        to_decimal.background_color = (1,1,1,1)
        to_decimal.bind(on_press=self.decimal)
        gridlayout.add_widget(to_decimal)
        
        to_hexa= Button(text = "H",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        to_hexa.background_color = (1,1,1,1)
        to_hexa.bind(on_press=self.hexa)
        gridlayout.add_widget(to_hexa)

        to_excess= Button(text = "Excess3",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        to_excess.background_color = (1,1,1,1)
        to_excess.bind(on_press=self.excess3)
        gridlayout.add_widget(to_excess)

        to_r= Button(text = "R-1",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        to_r.background_color = (1,1,1,1)
        to_r.bind(on_press=self.r_s_com)
        gridlayout.add_widget(to_r)

        to_r_1= Button(text = "R",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        to_r_1.background_color = (1,1,1,1)
        to_r_1.bind(on_press=self.r_1_com)
        gridlayout.add_widget(to_r_1)

        to_gray= Button(text = "Gray",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        to_gray.background_color = (1,1,1,1)
        to_gray.bind(on_press=self.Graycode)
        gridlayout.add_widget(to_gray)
        
        add_logo(Boxlayout)
        anchorlayout.add_widget(button)
        Boxlayout.add_widget(anchorlayout)
        
        boxlayout1.add_widget(gridlayout)
        self.add_widget(Boxlayout)
        self.add_widget(boxlayout1)  
        
        
    def Back_space(self, instance):
        if self.label.text:  # Check if there is text left
            # Remove the last character from the label's text
            self.label.text = self.label.text[:-1]   

    def Home(self,instance):
        self.manager.current = 'Home'

    def update_label(self, instance):
        self.current_value += instance.text
        self.label.text = f"{self.current_value}"

            
    def Clean(self,instance):
        self.label.text = ""
        self.numer1= None
        self.number2 = None
        self.current_value = ""

    def equal(self,instance):

        try:
            if self.current_value == "":
                raise ValueError("No input to save!")

            # Convert current input to integer
            current_input = self.current_value
            
            if self.numer1 is None:
                self.numer1 = current_input
            elif self.number2 is None:
                self.number2 = current_input
            self.current_value=""
        except ValueError as e:
            self.label.text = f"Error: {str(e)}"

    def num1(self,instance):
        self.label.text = self.numer1

    def num2(self,instance):
        self.label.text = self.number2


    def binary(self, instance):
        try:
            
            converter = Base_converter(self.numer1, int(self.number2))
            result = converter.convert_to_specific_base(2)
            self.label.text = f"Binary: {result}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

    def octal(self, instance):
        try:
            converter = Base_converter(self.numer1, int(self.number2))
            result = converter.convert_to_specific_base(8)
            self.label.text = f"octal: {result}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

    def decimal(self, instance):
        try:
            converter = Base_converter(self.numer1, int(self.number2))
            result = converter.convert_to_specific_base(10)
            self.label.text = f"decimal: {result}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"
            

    def hexa(self, instance):
        try:
            converter = Base_converter(self.numer1, int(self.number2))
            result = converter.convert_to_specific_base(16)
            self.label.text = f"hexa: {result}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

    def excess3(self, instance):
        try:
            converter = Base_converter(self.numer1,int(self.number2))
            result = converter.convert_to_specific_base(3)
            self.label.text = f"Excess3: {result}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

    def r_s_com(self, instance):
        try:
            converter = Complement(self.numer1,int(self.number2))
            result = converter.decimal_complement()
            self.label.text = f"R-1 : {result}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

    def r_1_com(self, instance):
        try:
            converter = Complement(self.numer1,int(self.number2))
            result = converter.r_complement()
            self.label.text = f"R: {result}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

    def Graycode(self, instance):
        try:
            converter = Base_converter(self.numer1,2)
            result = converter.convert_to_specific_base("Gray")
            self.label.text = f"Gray Code: {result}"
        except Exception as e:
            self.label.text = f"Error: {str(e)}"

class BinaryCalcScreen(Screen):
    def __init__(self, **kwargs):
        super(BinaryCalcScreen,self).__init__(**kwargs)

        Boxlayout = BoxLayout(orientation='horizontal',height=300,padding=10 , spacing=10)
        boxlayout1 = BoxLayout(orientation='vertical',height=300,padding=10 , spacing=8)
        anchorlayout=AnchorLayout(anchor_x = 'right',anchor_y = 'top')
        
        button1 = Button(text = "Home ",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        button1.background_color = (1,1,1,1)
        button1.bind(on_press=self.Home)

        self.label2 = Label(text = "MultiBase Calculator",color=(1,1,1,1),font_size="20sp",size=(240,50),size_hint = (None,0.2),height = 50,pos_hint={'center_x': 0.15, 'center_y': 1})
        boxlayout1.add_widget(self.label2)

        self.label1 = Label(text = "_______________________________________________________________________________________________________________________________________________",color=(1,0,0,1),font_size="12sp",size=(200,50),size_hint = (None,0.002),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        boxlayout1.add_widget(self.label1)


        self.l = Label(text = "0",color=(1,1,1,1),font_size="20sp",size=(240,50),size_hint = (None,0.16),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        boxlayout1.add_widget(self.l)
        
        
        gridlayout = GridLayout(cols=4, spacing=10, padding=10, size_hint=(1, 1))
        for i in range(0, 10):  # Create buttons from 1 to 10
            btn = Button(text=str(i),size_hint =(50,50))
            btn.bind(on_press=self.update_label)
            gridlayout.add_widget(btn)

        for char in"ABCDEF":  # Create buttons from 1 to 10
            btn = Button(text=char,size_hint =(50,50))   
            btn.bind(on_press=self.update_label)
            gridlayout.add_widget(btn)

        bace_btn= Button(text = "Base",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        bace_btn.background_color = (1,1,1,1)
        bace_btn.bind(on_press=self.Base_Base)
        gridlayout.add_widget(bace_btn)


        cleanbutton= Button(text = "C",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        cleanbutton.background_color = (1,1,1,1)
        cleanbutton.bind(on_press=self.Clean)
        gridlayout.add_widget(cleanbutton)

        eq_button= Button(text = "=",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        eq_button.background_color = (1,1,1,1)
        eq_button.bind(on_press=self.equal1)
        gridlayout.add_widget(eq_button)

        add_btn= Button(text = "+",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        add_btn.background_color = (1,1,1,1)
        add_btn.bind(on_press=self.add)
        gridlayout.add_widget(add_btn)

        sub_btn= Button(text = "-",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        sub_btn.background_color = (1,1,1,1)
        sub_btn.bind(on_press=self.sub)
        gridlayout.add_widget(sub_btn)

        mul_btn= Button(text = "*",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        mul_btn.background_color = (1,1,1,1)
        mul_btn.bind(on_press=self.mul)
        gridlayout.add_widget(mul_btn)

        div_btn= Button(text = "/",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        div_btn.background_color = (1,1,1,1)
        div_btn.bind(on_press=self.div)
        gridlayout.add_widget(div_btn)

        base =  Button(text = "B1",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        base.background_color = (1,1,1,1)
        base.bind(on_press=self.base_btn)
        gridlayout.add_widget(base)

        base1 =  Button(text = "B2",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        base1.background_color = (1,1,1,1)
        base1.bind(on_press=self.base_btn1)
        gridlayout.add_widget(base1)

        num1_btn =  Button(text = "N1",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        num1_btn.background_color = (1,1,1,1)
        num1_btn.bind(on_press=self.Num1_btn)
        gridlayout.add_widget(num1_btn)

        num2_btn =  Button(text = "N2",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        num2_btn.background_color = (1,1,1,1)
        num2_btn.bind(on_press=self.Num2_btn)
        gridlayout.add_widget(num2_btn)


        bin_btn =  Button(text = "Binary",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        bin_btn.background_color = (1,1,1,1)
        bin_btn.bind(on_press=self.binary_btn)
        gridlayout.add_widget(bin_btn)

        octal_btn=  Button(text = "octal",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        octal_btn.background_color = (1,1,1,1)
        octal_btn.bind(on_press=self.oct_btn)
        gridlayout.add_widget(octal_btn)


        deci_btn=  Button(text = "Deci",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        deci_btn.background_color = (1,1,1,1)
        deci_btn.bind(on_press=self.decimal_btn)
        gridlayout.add_widget(deci_btn)

        hexa_btn =  Button(text = "Hexa",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        hexa_btn.background_color = (1,1,1,1)
        hexa_btn.bind(on_press=self.hexadeci_btn)
        gridlayout.add_widget(hexa_btn)

    
    

        add_logo(Boxlayout)
        anchorlayout.add_widget(button1)
        Boxlayout.add_widget(anchorlayout)
        boxlayout1.add_widget(gridlayout)
        self.add_widget(Boxlayout)
        self.add_widget(boxlayout1)

        self.nu1= None
        self.nu2= None
        self.Bas1=None
        self.Bas2 =None
        self.current_value2 = ""
        self.counter = 0
        self.Answer = ""

        

    def base_btn(self,instance):
        self.l.text = str(self.Bas1)

    def base_btn1(self,instance):
        self.l.text = str(self.Bas2)

    def Num1_btn(self,instance):
        self.l.text = str(self.nu1)

    def Num2_btn(self,instance):
        self.l.text = str(self.nu2)

    def Home(self,instance):
        self.manager.current = 'Home'  

    def update_label(self, instance):
        # Append button text to the label
        self.current_value2 += instance.text
        self.l.text = f"{self.current_value2}"

    def Clean(self,instance):
        self.l.text = ""
        self.nu1= None
        self.nu2= None
        self.Bas1=None
        self.Bas2 =None
        self.current_value2 = ""

    def binary_btn(self, base):
        if self.Bas1 is None:
            self.Bas1 = 2
            
        elif self.Bas2 is None:
            self.Bas2 = 2
            

    def oct_btn(self, base):
        if self.Bas1 is None:
            self.Bas1 = 8
            
        elif self.Bas2 is None:
            self.Bas2 = 8

    def decimal_btn(self, base):
        if self.Bas1 is None:
            self.Bas1 = 10
            
        elif self.Bas2 is None:
            self.Bas2 = 10


    def hexadeci_btn(self, base):
        if self.Bas1 is None:
            self.Bas1 = 16
            
        elif self.Bas2 is None:
            self.Bas2 = 16

    def equal1(self,instance):
        if self.nu1 is None:
            self.nu1 = self.current_value2
            self.current_value2 = ""
            self.l.text = "Enter second number."
        elif self.nu2 is None:
            self.nu2 = self.current_value2
            self.current_value2 = ""


    def Base_Base(self,instance):
        binary = FloatingBaseConverter(self.Answer,10)
        self.counter += 1

        if self.counter == 1:
            result = binary.convert_to_base(2)
            self.l.text = f"Binary :  {result}"     
        elif self.counter == 2:
            result = binary.convert_to_base(8)
            self.l.text = f"octal :  {result}"
        elif self.counter == 3:
            result = binary.convert_to_base(10)
            self.l.text = f"Decimal :  {result}"
        elif self.counter == 4:
            result = binary.convert_to_base(16)
            self.l.text = f"Hexa :  {result}"
            self.counter = 0  
        

    def add (self,instance):
        calc = Binary_calculator(self.nu1,self.Bas1,self.nu2,self.Bas2)
        self.l.text = f"{calc.__add__()}"
        self.Answer = calc.__add__()

    def sub (self,instance):
        if self.nu1 is None or self.nu2 is None:
            self.current_value2 += instance.text
            self.l.text = f"{self.current_value2}"
        else:
            calc = Binary_calculator(self.nu1,self.Bas1,self.nu2,self.Bas2)
            self.l.text = f"{calc.__sub__()}"
            self.Answer = calc.__sub__()
    
    def mul (self,instance):
        calc = Binary_calculator(self.nu1,self.Bas1,self.nu2,self.Bas2)
        self.l.text = f"{calc.__mul__()}"
        self.Answer = calc.__mul__()

    def div (self,instance):
        num1 = Floating_calculator(self.nu1,self.Bas1)
        num2 = Floating_calculator(self.nu2,self.Bas2)
        res= num1/num2
        # self.l.text  = f"{f.convert_to_base(10)}"
        f = FloatingBaseConverter(res,2)

        self.Answer = f.convert_to_base(10)
        self.l.text  = f"{f.convert_to_base(10)}"
        

        

    
class ScientificCalcScreen(Screen):
    def __init__(self, **kwargs):
        super(ScientificCalcScreen,self).__init__(**kwargs)

        Boxlayout = BoxLayout(orientation='horizontal',height=300,padding=10 , spacing=10)
        boxlayout1 = BoxLayout(orientation='vertical',height=300,padding=10 , spacing=8)
        anchorlayout=AnchorLayout(anchor_x = 'right',anchor_y = 'top')
        

        button1 = Button(text = "Home ",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        button1.background_color = (1,1,1,1)
        button1.bind(on_press=self.Home)

        self.label2 = Label(text = "Floating Calculator",color=(1,1,1,1),font_size="20sp",size=(240,50),size_hint = (None,0.2),height = 50,pos_hint={'center_x': 0.15, 'center_y': 1})
        boxlayout1.add_widget(self.label2)

        self.label1 = Label(text = "_______________________________________________________________________________________________________________________________________________",color=(1,0,0,1),font_size="12sp",size=(200,50),size_hint = (None,0.002),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        boxlayout1.add_widget(self.label1)

        self.label_f = Label(text = "0",color=(1,1,1,1),font_size="20sp",size=(240,50),size_hint = (None,0.16),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        boxlayout1.add_widget(self.label_f)
        
        
        gridlayout = GridLayout(cols=4, spacing=10, padding=10, size_hint=(1, 1))
        for i in range(0, 10):  # Create buttons from 1 to 10
            btn = Button(text=str(i),size_hint =(50,50))
            btn.bind(on_press=self.update_label)
            gridlayout.add_widget(btn)

        

        point_btn= Button(text = ".",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        point_btn.background_color = (1,1,1,1)
        point_btn.bind(on_press=self.update_label)
        gridlayout.add_widget(point_btn)

        bace_btn= Button(text = "Base",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        bace_btn.background_color = (1,1,1,1)
        bace_btn.bind(on_press=self.Base_Base)
        gridlayout.add_widget(bace_btn)

        cleanbutton= Button(text = "C",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        cleanbutton.background_color = (1,1,1,1)
        cleanbutton.bind(on_press=self.Clean)
        gridlayout.add_widget(cleanbutton)

        num1button= Button(text = "Num1",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        num1button.background_color = (1,1,1,1)
        num1button.bind(on_press=self.num1)
        gridlayout.add_widget(num1button)
        
        num2button= Button(text = "Num2",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        num2button.background_color = (1,1,1,1)
        num2button.bind(on_press=self.num2)
        gridlayout.add_widget(num2button)

        base =  Button(text = "B1",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        base.background_color = (1,1,1,1)
        base.bind(on_press=self.base_btn)
        gridlayout.add_widget(base)

        base1 =  Button(text = "B2",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        base1.background_color = (1,1,1,1)
        base1.bind(on_press=self.base_btn1)
        gridlayout.add_widget(base1)

        add_btn= Button(text = "+",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        add_btn.background_color = (1,1,1,1)
        add_btn.bind(on_press=self.add1)
        gridlayout.add_widget(add_btn)

        sub_btn= Button(text = "-",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        sub_btn.background_color = (1,1,1,1)
        sub_btn.bind(on_press=self.sub1)
        gridlayout.add_widget(sub_btn)

        mul_btn= Button(text = "*",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        mul_btn.background_color = (1,1,1,1)
        mul_btn.bind(on_press=self.mul1)
        gridlayout.add_widget(mul_btn)

        div_btn= Button(text = "/",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        div_btn.background_color = (1,1,1,1)
        div_btn.bind(on_press=self.div1)
        gridlayout.add_widget(div_btn)

        eq_button= Button(text = "=",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        eq_button.background_color = (1,1,1,1)
        eq_button.bind(on_press=self.equal2)
        gridlayout.add_widget(eq_button)

        bin_btn =  Button(text = "Binary",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        bin_btn.background_color = (1,1,1,1)
        bin_btn.bind(on_press=self.binary_btn1)
        gridlayout.add_widget(bin_btn)

        octal_btn=  Button(text = "octal",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        octal_btn.background_color = (1,1,1,1)
        octal_btn.bind(on_press=self.oct_btn1)
        gridlayout.add_widget(octal_btn)


        deci_btn=  Button(text = "Deci",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        deci_btn.background_color = (1,1,1,1)
        deci_btn.bind(on_press=self.decimal_btn1)
        gridlayout.add_widget(deci_btn)

        hexa_btn =  Button(text = "Hexa",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        hexa_btn.background_color = (1,1,1,1)
        hexa_btn.bind(on_press=self.hexadeci_btn1)
        gridlayout.add_widget(hexa_btn)

        
        add_logo(Boxlayout)
        anchorlayout.add_widget(button1)
        Boxlayout.add_widget(anchorlayout)
        boxlayout1.add_widget(gridlayout)
        self.add_widget(Boxlayout)
        self.add_widget(boxlayout1)

        self.flo1= None
        self.flo2= None
        self.f1=None
        self.Fl2 =None
        self.current_value3 = ""
        self.counter = 0
        self.Answer = ""

    def Home(self,instance):
        self.manager.current = 'Home'

    def update_label(self, instance):
         # Append button text to the label
        self.current_value3 += instance.text
        self.label_f.text = f"{self.current_value3}"

    def Clean(self,instance):
        self.label_f.text = ""
        self.flo1= None
        self.flo2= None
        self.f1=None
        self.Fl2 =None
        self.current_value3 = ""

    def equal2(self,instance):
        if self.flo1 is None:
            self.flo1 = self.current_value3
            self.current_value3 = ""
            self.label_f.text = "Enter second number."
        elif self.flo2 is None:
            self.flo2 = self.current_value3
            self.current_value3 = ""

    def binary_btn1(self, base):
        if self.f1 is None:
            self.f1 = 2
            
        elif self.Fl2 is None:
            self.Fl2 = 2
            

    def oct_btn1(self, base):
        if self.f1 is None:
            self.f1 = 8
            
        elif self.Fl2 is None:
            self.Fl2 = 8

    def decimal_btn1(self, base):
        if self.f1 is None:
            self.f1 = 10
            
        elif self.Fl2 is None:
            self.Fl2 = 10


    def hexadeci_btn1(self, base):
        if self.f1 is None:
            self.f1 = 16
            
        elif self.Fl2 is None:
            self.Fl2 = 16

    def num1(self,instance):
        self.label_f.text = self.flo1
    def num2(self,instance):
        self.label_f.text =self.flo2

    def base_btn(self,instance):
        self.label_f.text = str(self.f1)
    

    def base_btn1(self,instance):
        self.label_f.text =str(self.Fl2)

    def Base_Base(self,instance):
        binary = FloatingBaseConverter(self.Answer,2)
        self.counter += 1

        if self.counter == 1:
            result = binary.convert_to_base(2)
            self.label_f.text = f"Binary :  {result}"     
        elif self.counter == 2:
            result = binary.convert_to_base(8)
            self.label_f.text  = f"octal :  {result}"
        elif self.counter == 3:
            result = binary.convert_to_base(10)
            self.label_f.text  = f"Decimal :  {result}"
        elif self.counter == 4:
            result = binary.convert_to_base(16)
            self.label_f.text  = f"Hexa :  {result}"
            self.counter = 0  

    def add1 (self,instance):
        num1 = Floating_calculator(self.flo1,self.f1)
        num2 = Floating_calculator(self.flo2,self.Fl2)
        self.label_f.text = f"{num1+num2}"
        self.Answer = num1+num2

    def sub1 (self,instance):
        if self.flo1 is None or self.flo2 is None :
            self.current_value3 += instance.text
            self.label_f.text = f"{self.current_value3}"
        else:
            num1 = Floating_calculator(self.flo1,self.f1)
            num2 = Floating_calculator(self.flo2,self.Fl2)
            self.label_f.text = f"{num1-num2}"
            self.Answer = num1-num2

    def mul1 (self,instance):
        num1 = Floating_calculator(self.flo1,self.f1)
        num2 = Floating_calculator(self.flo2,self.Fl2)
        self.Answer = num1*num2
        self.label_f.text = f"{num1*num2}"
        # self.Answer = num1*num2

    def div1 (self,instance):
        num1 = Floating_calculator(self.flo1,self.f1)
        num2 = Floating_calculator(self.flo2,self.Fl2)
        self.label_f.text = f"{num1/num2}"
        self.Answer = num1/num2

    
    


class ComplexCalcScreen(Screen):
    def __init__(self, **kwargs):
        super(ComplexCalcScreen,self).__init__(**kwargs)

        Boxlayout = BoxLayout(orientation='horizontal',height=300,padding=10 , spacing=10)
        boxlayout1 = BoxLayout(orientation='vertical',height=300,padding=10 , spacing=8)
        anchorlayout=AnchorLayout(anchor_x = 'right',anchor_y = 'top')
        

        button1 = Button(text = "Home ",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        button1.background_color = (1,1,1,1)
        button1.bind(on_press=self.Home)

        self.label = Label(text = "",color=(1,1,1,1),font_size = '20')
        boxlayout1.add_widget(self.label)
        
        
        gridlayout = GridLayout(cols=5, spacing=10, padding=10, size_hint=(1, 0.6))
        for i in range(0, 10):  # Create buttons from 1 to 10
            btn = Button(text=str(i))
            btn.bind(on_press=self.update_label)
            gridlayout.add_widget(btn)

        cleanbutton= Button(text = "C",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        cleanbutton.background_color = (1,1,1,1)
        cleanbutton.bind(on_press=self.Clean)
        gridlayout.add_widget(cleanbutton)

        add_logo(Boxlayout)
        anchorlayout.add_widget(button1)
        Boxlayout.add_widget(anchorlayout)
        boxlayout1.add_widget(gridlayout)
        self.add_widget(Boxlayout)
        self.add_widget(boxlayout1)

    def Home(self,instance):
        self.manager.current = 'Home'

    def update_label(self, instance):
        # Append button text to the label
        if self.label.text == "Press a button":
            self.label.text = instance.text  # Replace default text
        else:
            self.label.text += f"{instance.text}"
    def Clean(self,instance):
        self.label.text = ""


class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super(HistoryScreen,self).__init__(**kwargs)

        Boxlayout = BoxLayout(orientation='horizontal',height=300,padding=10 , spacing=10)
        boxlayout1 = BoxLayout(orientation='vertical',height=300,padding=10 , spacing=8)
        anchorlayout=AnchorLayout(anchor_x = 'right',anchor_y = 'top')
        

        button1 = Button(text = "Home ",size=(200,50),font_size = "20",color=(0,0,0,1) ,size_hint = (None,None),height = 50,pos_hint={'center_x': 0.5, 'center_y': 1})
        button1.background_color = (1,1,1,1)
        button1.bind(on_press=self.Home)

        add_logo(Boxlayout)
        anchorlayout.add_widget(button1)
        Boxlayout.add_widget(anchorlayout)
        
        self.add_widget(Boxlayout)
        self.add_widget(boxlayout1)

    def Home(self,instance):
        self.manager.current = 'Home'

    

class MyScreenManager(ScreenManager):
    pass


class BinaryCalculatorApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(HomeScreen(name='Home'))
        sm.add_widget(BaseConScreen(name='Basecon'))
        sm.add_widget(BinaryCalcScreen(name='BinaryCalc'))
        sm.add_widget(ScientificCalcScreen(name='scientificCalc'))
        sm.add_widget(ComplexCalcScreen(name='Complex'))
        sm.add_widget(HistoryScreen(name='History'))
        return sm
    
if __name__ == "__main__":
    BinaryCalculatorApp().run()