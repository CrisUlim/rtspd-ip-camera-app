import customtkinter
import cv2

customtkinter.set_appearance_mode('dark')

windows = customtkinter.CTk()
windows.geometry("800x500")
windows.resizable(False, False)
windows.title('Ip Camera')


def cam_1():
    video = cv2.VideoCapture("rtsp://admin:password@ip_address:port/cam/realmonitor?channel=1&subtype=1")
    while(True):
        if cv2.waitKey(1) & 0xFF == 27:
            break
        ret, frame = video.read()
        cv2.imshow('Cam 01', frame)
    cv2.destroyAllWindows()
        
def cam_2():
    video = cv2.VideoCapture("rtsp://admin:password@ip_address:port/cam/realmonitor?channel=1&subtype=1")
    while(True):
        if cv2.waitKey(1) & 0xFF == 27:
            break
        ret, frame = video.read()
        cv2.imshow('Cam 02', frame)
    cv2.destroyAllWindows()
    
def cam_3():
    video = cv2.VideoCapture("rtsp://admin:password@ip_address:port/cam/realmonitor?channel=1&subtype=1")
    while(True):
        if cv2.waitKey(1) & 0xFF == 27:
            break
        ret, frame = video.read()
        cv2.imshow('Cam 03', frame)
    cv2.destroyAllWindows()
    
def cam_4():
    video = cv2.VideoCapture("rtsp://admin:password@ip_address:port/cam/realmonitor?channel=1&subtype=1")
    while(True):
        if cv2.waitKey(1) & 0xFF == 27:
            break
        ret, frame = video.read()
        cv2.imshow('Cam 04', frame)
    cv2.destroyAllWindows()
 
 






label1 = customtkinter.CTkLabel(text='Ip Camere Monitor', text_color='white', text_font=('Italic', 20), height=150).pack()

button1 = customtkinter.CTkButton(text='Cam 01', width=20, command=cam_1 ).place(x= 310, y= 190)
button2 = customtkinter.CTkButton(text='Cam 02', width=20, command=cam_2).place(x= 310, y= 235)
button3 = customtkinter.CTkButton(text='Cam 03', width=20, command=cam_3).place(x= 430, y= 190)
button4 = customtkinter.CTkButton(text='Cam 04', width=20, command=cam_4 ).place(x= 430, y= 235)

button5 = customtkinter.CTkButton(text='Exit', width=80 , command=windows.destroy)
button5.place(x= 360, y=400)





windows.mainloop()

