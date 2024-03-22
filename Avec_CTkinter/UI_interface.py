from customtkinter import *

class RootGUI():
    def __init__(self):
        self.root = CTk()
        self.root.title("Serial communication")
        self.root.geometry("1100x580")
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure((2, 3), weight=0)
        self.root.grid_rowconfigure((0, 1, 2), weight=1)
        self.root.config(bg="white")

class ComGUI():
    def __init__(self, root):
        self.root = root
        self.frame = CTkFrame(root, width=140, corner_radius=0)
        self.frame_title = CTkLabel(self.frame, text="Com Manager", 
                                    font=CTkFont("Arial", size=20, weight='bold'))
        self.label_com = CTkLabel(
            self.frame, text="Available Port(s): ", width=15)
        self.label_bd = CTkLabel(
            self.frame, text="Baude Rate: ", width=15)
        self.ComOptionMenu()
        self.baudOptionMenu()
        self.btn_refresh = CTkButton(self.frame, text="Refresh",
                                    width=10,  command=self.com_refresh)
        self.btn_connect = CTkButton(self.frame, text="Connect",
                                    width=10, state="disabled",  command=self.serial_connect)
        self.padx = 20
        self.pady = 5
        self.publish()

    def publish(self):
        self.frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame_title.grid(row=0, column=0, padx=20, pady=(10, 5))
        self.label_com.grid(column=0, row=2)
        self.label_bd.grid(column=0, row=3)
        self.drop_baud.grid(column=2, row=3, padx=self.padx, pady=self.pady)
        self.drop_com.grid(column=2, row=2, padx=self.padx)
        self.btn_refresh.grid(column=3, row=2)
        self.btn_connect.grid(column=3, row=3)

    def ComOptionMenu(self):
        coms = ["-", "COM3"]
        self.clicked_com = StringVar()
        self.clicked_com.set(coms[0])
        self.drop_com = CTkOptionMenu(
            self.frame, values=coms, width=10, command=self.connect_ctrl)

    def baudOptionMenu(self):
        bds = ["-",
               "300",
               "600",
               "1200",
               "2400",
               "4800",
               "9600",
               "14400",
               "19200",
               "28800",
               "38400",
               "56000",
               "57600",
               "115200",
               "128000",
               "256000"]
        self.clicked_bd = StringVar()
        self.clicked_bd.set(bds[0])
        self.drop_baud = CTkOptionMenu(
            self.frame, values=bds, width=10, command=self.connect_ctrl)

    def connect_ctrl(self, widget):
        print("Connect ctrl")

    def com_refresh(self):
        print("Refresh")

    def serial_connect(self):
        print("Connect")

if __name__ == "main":
    RootGUI()
    ComGUI()