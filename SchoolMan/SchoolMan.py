import wpf
import datetime

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'SchoolMan.xaml')
        
    def PswBox_TextChanged(self, sender, e):
        pass

    
    def Try_Click(self, sender, e):
       
        pass

if __name__ == '__main__':
    Application().Run(MyWindow())
