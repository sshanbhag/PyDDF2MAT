#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# sjs_utils.py
#------------------------------------------------------------------------------
# miscellaneous general-purpose code bits
#------------------------------------------------------------------------------
# Sharad J. Shanbhag
# sshanbhag@neomed.edu
#------------------------------------------------------------------------------
# Created 26 March, 2014
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# import wxPython
try:
    import wx
except ImportError:
    raise ImportError, "need wxpython module"

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# utility function to list all members of a class
#------------------------------------------------------------------------------
def all_members(aClass):
    members = {}
    bases = list(aClass.__bases__)
    bases.reverse()
    for base in bases:
        members.update(all_members(base))
    members.update(vars(aClass))
    return members
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def get_filename(wildcard):
    """
    Shows file dialog, wildcard is used to set default types
    """
    # create wx.App instance
    app = wx.App(None)
    # set style to open dialog, file must exist
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    # create dialog
    dialog = wx.FileDialog(None, 'Select DataWave file', 
                            wildcard=wildcard, style=style)
    # get path
    if dialog.ShowModal() == wx.ID_OK:
        filename = dialog.GetPath()
    else:
        # return None if cancelled
        filename = None
    # close dialog
    dialog.Destroy()
    app.Destroy()
    return filename
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def get_directory(defaultpath):
    # check if defaultpath is None
    if defaultpath == None:
        defaultpath = ''
    # create wx.App instance
    app = wx.App(None)
    style = wx.DD_DEFAULT_STYLE
    dialog = wx.DirDialog(None, 'Choose output directory', 
                            style = style, defaultPath = defaultpath)
    if dialog.ShowModal() == wx.ID_OK:
        dirname = dialog.GetPath()
    else:
        dirname = None
    dialog.Destroy()
    app.Destroy()
    return dirname
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def warn_dialog(parent, message, caption = 'Warning!'):
    app = wx.App(None)
    dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_WARNING)
    dlg.ShowModal()
    dlg.Destroy()
    app.Destroy()
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------




'''
#------------------------------------------------------------------------------
# ======== Select a file for opening: using Tk API 
#------------------------------------------------------------------------------
# check if fullfile is set or if file in fullfile doesn't exist
if fullfile != None:
    if os.path.isfile(fullfile) == False:
        fullfile = None
        
if fullfile == None:
    # if not, ask user for file
    # create root window 
    root = Tkinter.Tk()
    #and hide it using withdraw() method
    root.withdraw()
    # bring window to front
    root.lift()
    root.attributes('-topmost', 1)
    
    # define file open options within fileoptions dictionary (denoted by {})
    fileoptions = {}
    fileoptions['parent'] = root
    fileoptions['defaultextension'] = '.ddf'
    # !default filetype extension is listed last!
    fileoptions['filetypes'] = [('all files', '.*'),('ddf files', '.ddf')]
    # title/prompt for window
    fileoptions['title'] = 'Choose a DataWave file...'
    
    # use askopenfilename method of tkFileDialog to get a .ddf file
    """
    Example using wrapped lines:
    fullfile_ucode = tkFileDialog.askopenfilename(  
                                    parent = root, 
                                    defaultextension = '.ddf',
                                    filetypes = [ ('all files', '.*'),
                                                ('ddf files', '.ddf') ],
                                    title='Choose a DataWave data file')
    """
    # use fileoptions with '**' prepended to expand the fileoptions dictionary
    fullfile_ucode = tkFileDialog.askopenfilename(**fileoptions)
    # send window to back
    root.attributes('-topmost', 0)
    
    # convert to plain string
    fullfile = str(fullfile_ucode);
    print('fullfile = %s' % fullfile)
    
    # if no file was selected, exit
    if (len(fullfile) == 0) or (fullfile == None):
        print('Cancelled...')
        sys.exit()
'''

# data = file.read()
# file.close()
# print "I got %d bytes from this file." % len(data)

