from customtkinter import *
from PIL import Image

win = CTk()
win.geometry("691x824")
win.title("Hướng dẫn sử dụng")
win.configure(fg_color = "#d8fdff")
win.resizable(False, False)

image1 = CTkImage(light_image=Image.open("Help/HelpHome/buttonHome.png"), size = (134, 87))
label1 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image1, width = 134, height = 87)
label1.place(x = 136, y = 85)
text1 = 'Hiển thị màn hình chính, \nchứa phím Exit và Help!'
content1 = CTkLabel(win, corner_radius = 10, fg_color="#d3cff9", font = ("Times New Roman", 18),  text_color='black', text = text1, width = 268, height = 86)
content1.place(x = 287, y = 86)

image2 = CTkImage(light_image=Image.open("Help/HelpHome/buttonIntegral.png"), size = (134, 87))
label2 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image2, width = 134, height = 87)
label2.place(x = 136, y = 192)
text2 = 'Đi đến màn hình tính tích phân,\n đạo hàm'
content2 = CTkLabel(win, corner_radius = 10, fg_color="#d3cff9", font = ("Times New Roman", 18),  text_color='black', text = text2, width = 268, height = 86)
content2.place(x = 287, y = 192)

image3 = CTkImage(light_image=Image.open("Help/HelpHome/buttonLimit.png"), size = (134, 87))
label3 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image3, width = 134, height = 87)
label3.place(x = 136, y = 299)
text3 = 'Đi đến màn hình tính giới hạn'
content3 = CTkLabel(win, corner_radius = 10, fg_color="#d3cff9", font = ("Times New Roman", 18),  text_color='black', text = text3, width = 268, height = 86)
content3.place(x = 287, y = 299)

image4 = CTkImage(light_image=Image.open("Help/HelpHome/buttonEquation.png"), size = (134, 87))
label4 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image4, width = 134, height = 87)
label4.place(x = 136, y = 406)
text4 = 'Đi đến màn hình giải phương trình'
content4 = CTkLabel(win, corner_radius = 10, fg_color="#d3cff9", font = ("Times New Roman", 18),  text_color='black', text = text4, width = 268, height = 86)
content4.place(x = 287, y = 406)

image5 = CTkImage(light_image=Image.open("Help/HelpHome/buttonExit.png"), size = (134, 87))
label5 = CTkLabel(win, corner_radius = 10, fg_color = "#796fe4", text = "", image=image5, width = 134, height = 87)
label5.place(x = 136, y = 513)
text5 = 'thoát khỏi giải đấu!'
content5 = CTkLabel(win, corner_radius = 10, fg_color="#d3cff9", font = ("Times New Roman", 18),  text_color='black', text = text5, width = 268, height = 86)
content5.place(x = 287, y = 513)

button = CTkButton(win, corner_radius=10, border_width = 2, command = exit, border_color = '#f0bf10', fg_color="#796fe4", text = "OK", font = ("Times New Roman", 30), 
                   hover_color='#c6e8b1', height = 111)
button.place(x = 256, y = 659)
win.mainloop()
