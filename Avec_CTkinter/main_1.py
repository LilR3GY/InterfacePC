from UI_interface import RootGUI, ComGUI


RootMaster = RootGUI()

ComMaster = ComGUI(RootMaster.root)

RootMaster.root.mainloop()