#Creates, names, and resizes a window, thats it

import wx

class garbo(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Frame/Window', size=(300,200))

#Startup script to show frame and start loop
if __name__=='__main__':
	app = wx.App()
	frame = garbo(parent=None, id=-1)
	frame.Show()
	app.MainLoop()