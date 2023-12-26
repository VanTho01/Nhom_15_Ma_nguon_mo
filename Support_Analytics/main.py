from customtkinter import *
from PIL import Image
import Home.screenHome as screenHome
import calLimit.screenLimit as screenLimit
import calIntegral.screenIntegral as screenIntegral
import calEquation.screenEquation as screenEquation

class Home:
    def __init__(self, win):
        self.win = win
        
        win.geometry('1560x988')
        win.configure(fg_color = "#B48989")
    
        self.tabview1 = CTkLabel(win, corner_radius=10, text = '', fg_color = "#A56666", width = 1560, height = 113)
        self.tabview1.place(x = 0, y = 0)
        screenHome.Home(win)
        self.tabview2 = CTkLabel(win, corner_radius=10, text = '', bg_color = '#A56666', fg_color = "#54AFC3", width = 1083, height = 86)
        self.tabview2.place(x = 36, y = 14)

        self.iconHome = CTkImage(light_image = Image.open('asset/iconHome.png'), size = (48, 48))
        self.buttonHome = CTkButton(win, image=self.iconHome, compound='left', command = self.fctHome, text = '   Home', width = 256, font = ('Times New Roman', 25), 
                                    text_color='black', height = 60, corner_radius=3, bg_color = '#54AFC3', fg_color="#5FE4DC", hover_color="#e82c90")
        self.buttonHome.place(x = 64, y = 26)

        self.iconIntegral = CTkImage(light_image = Image.open('asset/iconIntegral.png'), size = (48, 48))
        self.buttonIntegral = CTkButton(win, image=self.iconIntegral, compound='left', command = self.fctIntegral, text = '  Integral', width = 256, font = ('Times New Roman', 25), 
                                        text_color='black', height = 60, corner_radius=3, bg_color = '#54AFC3', fg_color="#5FE4DC", hover_color="#e82c90")
        self.buttonIntegral.place(x = 318, y = 26)

        self.iconLimit = CTkImage(light_image = Image.open('asset/iconLimit.png'), size = (48, 48))
        self.buttonLimit = CTkButton(win, image=self.iconLimit, compound='left', command=self.fctLimit, text = '  Limit', width = 256, font = ('Times New Roman', 25), 
                                     text_color='black', height = 60, corner_radius=3, bg_color = '#54AFC3', fg_color="#5FE4DC", hover_color="#e82c90")
        self.buttonLimit.place(x = 574, y = 26)

        self.iconEquation = CTkImage(light_image = Image.open('asset/iconEquation.png'), size = (48, 48))
        self.buttonEquation = CTkButton(win, image=self.iconEquation, compound='left', command=self.fctEquation, text = 'Equation', width = 256, font = ('Times New Roman', 25), text_color='black', 
                                        height = 60, corner_radius=3, bg_color = '#54AFC3', fg_color="#5FE4DC", hover_color="#e82c90")
        self.buttonEquation.place(x = 830, y = 26)

    def fctHome(self):
        self.buttonHome.configure(fg_color = "#B48989")
        self.buttonIntegral.configure(fg_color = '#5FE4DC')
        self.buttonEquation.configure(fg_color = '#5FE4DC')
        self.buttonLimit.configure(fg_color = '#5FE4DC')
        screenHome.Home(win)

    def fctLimit(self):
        self.buttonHome.configure(fg_color = "#5FE4DC")
        self.buttonIntegral.configure(fg_color = '#5FE4DC')
        self.buttonEquation.configure(fg_color = '#5FE4DC')
        self.buttonLimit.configure(fg_color = '#B48989')
        screenLimit.calLimit(win)

    def fctIntegral(self):
        self.buttonHome.configure(fg_color = "#5FE4DC")
        self.buttonIntegral.configure(fg_color = '#B48989')
        self.buttonEquation.configure(fg_color = '#5FE4DC')
        self.buttonLimit.configure(fg_color = '#5FE4DC')
        screenIntegral.calIntegral(win)

    def fctEquation(self):
        self.buttonHome.configure(fg_color = "#5FE4DC")
        self.buttonIntegral.configure(fg_color = '#5FE4DC')
        self.buttonEquation.configure(fg_color = '#B48989')
        self.buttonLimit.configure(fg_color = '#5FE4DC')
        screenEquation.calEquation(win)

if __name__ == "__main__":
    win = CTk()
    app = Home(win)
    win.mainloop()