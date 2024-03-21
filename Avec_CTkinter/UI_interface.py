from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkOptionMenu
import customtkinter

class RootGUI():
    def init(self, root):
        self.root = customtkinter.CTk()
        self.root.title("Serial communication")
        self.root.geometry("360x120")
        self.root.config(bg="white")

class ComGUI():
    def init(self, root):
        self.root = root
        self.frame = CTkFrame(root, text="Com Manager",
                              padx=5, pady=5, bg="white")
        self.label_com = CTkLabel(
            self.frame, text="Available Port(s): ", bg="white", width=15, anchor="w")
        self.label_bd = CTkLabel(
            self.frame, text="Baude Rate: ", bg="white", width=15, anchor="w")
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
        self.frame.grid(row=0, column=0, rowspan=3,
                        columnspan=3, padx=5, pady=5)
        self.label_com.grid(column=1, row=2)
        self.label_bd.grid(column=1, row=3)
        self.drop_baud.grid(column=2, row=3, padx=self.padx, pady=self.pady)
        self.drop_com.grid(column=2, row=2, padx=self.padx)
        self.btn_refresh.grid(column=3, row=2)
        self.btn_connect.grid(column=3, row=3)

    def ComOptionMenu(self):
        coms = ["-", "COM3"]
        self.clicked_com = CTk.StringVar()
        self.clicked_com.set(coms[0])
        self.drop_com = CTkOptionMenu(
            self.frame, self.clicked_com, *coms, command=self.connect_ctrl)
        self.drop_com.config(width=10)

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
        self.clicked_bd = CTk.StringVar()
        self.clicked_bd.set(bds[0])
        self.drop_baud = CTkOptionMenu(
            self.frame, self.clicked_bd, *bds, command=self.connect_ctrl)
        self.drop_baud.config(width=10)

    def connect_ctrl(self, widget):
        print("Connect ctrl")

    def com_refresh(self):
        print("Refresh")

    def serial_connect(self):
        print("Connect")

if __name__ == "main":
    RootGUI()
    ComGUI()