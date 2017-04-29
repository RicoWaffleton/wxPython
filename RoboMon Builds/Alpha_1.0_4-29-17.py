import wx

class HubWindow(wx.Frame):
	def __init__(self, parent, id):
		#Initialize Hub Frame
		wx.Frame.__init__(self, parent, id, 'Monitoring System - Alpha 1.0', size=(1000, 500))
		#The rest of the entries in this class are modifiers for HubWindow
		#Makes X button close the hub window
		self.Bind(wx.EVT_CLOSE, self.checkIfSure)
		#Panel = Workspace to put txt, buttons, etc
		panel = wx.Panel(self)
		#MenuBar = The thing at the top of window with menus like File, Edit, etc
		menubar = wx.MenuBar()
		#Create First entry in menubar Ex: File option in default menu
		goto = wx.Menu()
		#Add Locations to go to the goto menu entry
		goto.Append(wx.NewId(), "Sensor 1", "Open Sensor 1 GUI")
		goto.Append(wx.NewId(), "Sensor 2", "Open Sensor 2 GUI")
		goto.Append(wx.NewId(), "Sensor 3", "Open Sensor 3 GUI")
		goto.Append(wx.NewId(), "Sensor 4", "Open Sensor 4 GUI")
		#Places GoTo in the menubar
		menubar.Append(goto, "GoTo")
		self.SetMenuBar(menubar)

	def checkIfSure(self, event):
		#Popup to check if user intends to close system
		checkClose = wx.MessageDialog(None, 'You are exiting the Monitoring system, Do you wish to proceed?', 'Exit?', wx.YES_NO)
		checkClose_ans = checkClose.ShowModal()
		#If yes, rip window
		if checkClose_ans == 5103:
			self.Destroy()
		#Close popup
		checkClose.Destroy()






#!!!ACTUAL RUN COMMANDS DO NOT REMOVE!!!
if __name__=='__main__':
	#Create application
	app = wx.App()
	#Create frame
	frame = HubWindow(parent=None, id=-1)
	#Display frame
	frame.Show()
	#Run Code for objects
	app.MainLoop()
