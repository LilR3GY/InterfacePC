import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import *


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

class RootGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        #configure window
        self.title("Commande pour la balance")
        self.geometry(f"{1100}x{580}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        '''# configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        '''
        
        '''self.root = customtkinter.CTk()
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.root.resizable(True, True)
        frame = CTkFrame(self.root)
        frame.pack(pady=5, padx=10, fill="both", expand=True)
        '''
        
class ComGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        #Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=5)
        self.commanager_label = customtkinter.CTkLabel(self.sidebar_frame, text="Com Manager", font=customtkinter.CTkFont(size=10, weight="bold"))
        
        #Frame
        #self.root = root
        #self.frame = CTkFrame(root, text="com Manger", pady=5, padx=5, bg="white")
        #self.label_com = CTkLabel(
        #    self.frame, text="Available Port(s):", bg="white", wight=15, anchor="w"
        #)
        self.publish()
        
    def publish(self):
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.commanager_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    
    

if __name__ == "__main__":
    RootGUI()
    ComGUI()