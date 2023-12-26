from customtkinter import *
from PIL import Image

win = CTk()
win.geometry("1068x824")
win.title("Hướng dẫn sử dụng")
win.configure(fg_color = "#d8fdff")
win.resizable(False, False)

image1 = CTkImage(light_image=Image.open("Help/HelpEquation/buttonHelp.png"), size = (134, 87))
label1 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image1, width = 134, height = 87)
label1.place(x = 50, y = 22)
text1 = 'Hướng dẫn sử dụng'
content1 = CTkLabel(win, corner_radius = 10, fg_color="#d3cff9", font = ("Times New Roman", 18),  text_color='black', text = text1, width = 268, height = 86)
content1.place(x = 201, y = 22)

image2 = CTkImage(light_image=Image.open("Help/HelpEquation/buttonSave.png"), size = (134, 87))
label2 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image2, width = 134, height = 87)
label2.place(x = 50, y = 127)
text2 = 'Lưu kết quả'
content2 = CTkLabel(win, corner_radius = 10, fg_color="#d3cff9", font = ("Times New Roman", 18),  text_color='black', text = text2, width = 268, height = 86)
content2.place(x = 201, y = 127)

image3 = CTkImage(light_image=Image.open("Help/HelpEquation/buttonUpload.png"), size = (134, 87))
label3 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image3, width = 134, height = 87)
label3.place(x = 50, y = 232)
text3 = 'Tải file lên'
content3 = CTkLabel(win, corner_radius = 10, fg_color="#d3cff9", font = ("Times New Roman", 18),  text_color='black', text = text3, width = 268, height = 86)
content3.place(x = 201, y = 232)

image4 = CTkImage(light_image=Image.open("Help/HelpEquation/writeFunction.png"), size = (477, 576))
label4 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image4, width = 477, height = 576)
label4.place(x = 488, y = 22)

image5 = CTkImage(light_image=Image.open("Help/HelpEquation/note.png"), size = (410, 455))
label5 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image5, width = 419, height = 455)
label5.place(x = 50, y = 336)


button = CTkButton(win, corner_radius=10, border_width = 2, command = exit, border_color = '#f0bf10', fg_color="#796fe4", text = "OK", font = ("Times New Roman", 30), 
                   hover_color='#c6e8b1', height = 111)
button.place(x = 499, y = 670)
win.mainloop()
