#Testing Out Buttons
import wx

class window(wx.Frame):
	def __init__(self, parent, id):
		#Creates the frame
		wx.Frame.__init__(self, parent, id, 'Buttons Galore', size=(300,200))
		#Creates panel inside the frame
		panel = wx.Panel(self)
		#Creates a button inside the panel
		button = wx.Button(panel, label='Exit', pos=(110, 50), size=(60, 60))
		#Binds the close script to the button press
		self.Bind(wx.EVT_BUTTON, self.exitButton, button)
		#Binds a destroy close script to the 'X' button in the corner
		self.Bind(wx.EVT_CLOSE, self.closeWindow)
		

	def exitButton(self, event):
		#Script to close window
		self.Close(True)

	def closeWindow(self, event):
		self.Destroy()

#Startup script to show frame and start loop
if __name__=='__main__':
	app = wx.App()
	frame = window(parent=None, id=-1)
	frame.Show()
	app.MainLoop()

