from customtkinter import *
from PIL import Image
import subprocess

class Home:
        def __init__(self, win):
                self.win = win
                win.geometry('1560x988')
                win.configure(fg_color = "#B48989")
                self.frame1 = CTkLabel(win, fg_color="#FBFBFB", width = 1515, height = 858, text = '')
                self.frame1.place(x = 23, y = 113)

                self.iconWelcome = CTkImage(light_image = Image.open('asset/iconWelcome.png'), size = (1515, 858))
                self.tabWelcome = CTkLabel(win, text = '',image=self.iconWelcome, fg_color = "#51BF56", width = 1302, height = 577)
                self.tabWelcome.place(x = 23, y = 113)

                self.iconExit = CTkImage(light_image = Image.open('asset/iconExit.png'), size = (83, 77))
                self.left = CTkButton(win, image = self.iconExit, corner_radius = 3, text = "", command = self.Exit, font = ('Times new roman', 25), fg_color = "#d5ecf8", 
                                        width = 82, height = 76, hover = True, hover_color='#96F2E7', border_color = '#37a4de', border_width = 3)
                self.left.place(x = 1422, y = 18)

                self.iconHelp = CTkImage(light_image = Image.open('asset/iconHelp.png'), size = (83, 77))
                self.Help = CTkButton(win, image = self.iconHelp, corner_radius = 3, text = "", command = self.help, font = ('Times new roman', 25), fg_color = "#d5ecf8", 
                                        width = 82, height = 76, hover = True, hover_color='#96F2E7', border_color = '#37a4de', border_width = 3)
                self.Help.place(x = 1300, y = 18)
        def Exit(self):
                if  os.path.exists("calLimit/expression.txt") == True:
                        os.remove("calLimit/expression.txt")
                if  os.path.exists("calLimit/resultLimit.txt") == True:
                        os.remove("calLimit/resultLimit.txt")
                if  os.path.exists("calLimit/destiValue.txt") == True:
                        os.remove("calLimit/destiValue.txt")
                if  os.path.exists('calLimit/fileStore.txt') == True:
                        os.remove('calLimit/fileStore.txt')
                if  os.path.exists('calLimit/dothi.png') == True:
                        os.remove('calLimit/dothi.png')

                if  os.path.exists("calIntegral/expression1.txt") == True:
                        os.remove('calIntegral/expression1.txt')
                if  os.path.exists("calIntegral/resultIntegral.txt") == True:
                        os.remove('calIntegral/resultIntegral.txt')
                if  os.path.exists("calIntegral/resultDerivative.txt") == True:
                        os.remove('calIntegral/resultDerivative.txt')
                if  os.path.exists("calIntegral/upperEdge.txt") == True:
                        os.remove("calIntegral/upperEdge.txt")
                if  os.path.exists("calIntegral/lowerEdge.txt") == True:
                        os.remove("calIntegral/lowerEdge.txt")
                if  os.path.exists('calIntegral/fileStore.txt') == True:
                        os.remove('calIntegral/fileStore.txt')

                if  os.path.exists('calEquation/expression.txt') == True:
                        os.remove('calEquation/expression.txt')
                if  os.path.exists('calEquation/resultEquation.txt') == True:
                        os.remove('calEquation/resultEquation.txt')
                if  os.path.exists('calEquation/dothi.png') == True:
                        os.remove('calEquation/dothi.png')
                if  os.path.exists('calEquation/fileStore.txt') == True:
                        os.remove('calEquation/fileStore.txt')
                exit()
        def help(self):
                file = "Help/HelpHome/helpHome.py"
                subprocess.call(['python', file])
     
if __name__ == "__main__":
    win = CTk()
    app = Home(win)
    win.mainloop()