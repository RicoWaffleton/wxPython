#Base Imported from 3
import wx

class window(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, 'Buttons Galore', size=(300,200))
		panel = wx.Panel(self)
		button = wx.Button(panel, label='Exit', pos=(110, 50), size=(60, 60))
		self.Bind(wx.EVT_BUTTON, self.exitButton, button)
		self.Bind(wx.EVT_CLOSE, self.closeWindow)
		status = self.CreateStatusBar()
		menubar = wx.MenuBar()
		first_menu = wx.Menu()
		second_menu = wx.Menu()
		first_menu.Append(wx.NewId(), "Title1", "This is the first menu")
		second_menu.Append(wx.NewId(), "Title2", "This is the second menu")
		menubar.Append(first_menu, "Menu 1")
		menubar.Append(second_menu, "Menu 2")
		self.SetMenuBar(menubar)


	def exitButton(self, event):
		self.Close(True)

	def closeWindow(self, event):
		self.Destroy()





#Startup script to show frame and start loop
if __name__=='__main__':
	app = wx.App()
	frame = window(parent=None, id=-1)
	frame.Show()
	app.MainLoop()