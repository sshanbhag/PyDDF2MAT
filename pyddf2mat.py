#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# pyddf2mat.py
#------------------------------------------------------------------------------
'''
takes ddf file, writes segment and marker data to text file
'''
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# path for neuroshare package: this is where the setup.py script for
# neuroshare installs the compiled/bundled neuroshare-python package
nspath = "c:\\users\\sshanbhag\\appdata\\local\\enthought\\canopy32\\user\\lib\\site-packages"
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# import needed modules (neuroshare, Tkinter, etc)
#------------------------------------------------------------------------------
# import sys (for exit, checking path)
import sys
# import os methods
import os
# import getopt
import getopt
# import sjs_utils
from sjs_utils import *
# import PyDDF_Info
from PyDDF_Info import *
# import PyDDF_TextOutput
from PyDDF_TextOutput import *

# before loading neuroshare module, check that it can be found!
if nspath not in sys.path: 
    sys.path.append(nspath)
    print "Appending " + nspath + " to path"
# import neuroshare module
import neuroshare as ns
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# guts!
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def main(argv):
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    # some constants
    #--------------------------------------------------------------------------
    # files
    fullfile = ''
    filepath = ''
    filename = ''
    #outpath = 'F:\\Work\\Code\\Python\\neuroshare-python\\test\\'
    outfile = ''
    outpath = ''
    
    # other things
    sepstr = '--------------------------------------------------------------------'
        
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    # parse input args
    #--------------------------------------------------------------------------
    if len(argv) > 1:
        helpstr = 'ddf2text.py -i <input .ddf file> -o <output .txt file>'
        try:
            opts, args = getopt.getopt(argv, 'hi:o:', ['ifile=', 'ofile='])
            print 'opts: ', opts
            print 'args: ',args
        except getopt.GetoptError as err:
            print str(err)
            print helpstr
            sys.exit(2)
    
        for opt, arg in opts:
            if opt in ('-h', '-help'):
                print helpstr
                sys.exit()
            elif opt in ('-i'):
                fullfile = arg
            elif opt in ('-o'):
                outfile = arg
                
        print "Reading data from:", fullfile
        print "Writing data to:", outfile
    
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    # Get File names
    #--------------------------------------------------------------------------
    # check if fullfile is set or if file in fullfile doesn't exist
    if fullfile != '':
        if os.path.isfile(fullfile) == False:
            warn_dialog(None, "file {0} not found!".format(fullfile))
            fullfile = ''
    # is fullfile set?        
    if fullfile == '':
        # Select a file for opening (uses wx API)
        fullfile_ucode = get_filename('*.ddf')
        # if no file was selected, exit
        if fullfile_ucode == None:
            print('Cancelled...')
            sys.exit()
        else:
            # convert to plain string
            fullfile = str(fullfile_ucode);
            print('fullfile = %s' % fullfile)
        
    # split file into path and name, first "normalizing" path
    filepath, filename = os.path.split(os.path.normpath(fullfile))
    # split extension and base name
    filebase, fileext = os.path.splitext(filename)
    
    # check status of outfile
    if outfile == '':
        # build output file name and path
        outname = filebase + '.txt'
        # select output path
        outpath = get_directory(filepath)
        if outpath == None:
            print('Cancelled...')
            sys.exit()
        else:
            outfile = os.path.join(outpath, outname)
    else:
        outpath, outname = os.path.splitext(outfile)
    
    print sepstr
    print 'Input File:'
    print '\tfile path: %s' % filepath
    print '\tfile name: %s' % filename
    print '\tfile base: %s' % filebase
    print '\tfile ext: %s\n' % fileext
    print 'Output File:'
    print '\toutput path: %s' % outpath
    print '\toutput name: %s' % outname
    print sepstr
    print('\n')
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    
    #--------------------------------------------------------------------------
    # use ns (neuroshare) library to open ddf file
    #--------------------------------------------------------------------------
    # example using hard-coded filename
    #    fd = ns.File("06-25-2013--853_2649_freqscan1_Sorted.ddf")
    # example using filename stored in string "filename":
    #    fd = ns.File(filename)
    F = ns.File(fullfile)
    
    
    #--------------------------------------------------------------------------
    # write metadata to text file - since this is first write to file, open in
    # 'w' mode (no append)
    #--------------------------------------------------------------------------
    writeMetadataText(F, outfile, 'w')
    # write to screen
    writeMetadataText(F, 'stdout', None)
    
    # display entity information
    entity_info(F)
    # get entity information
    entlabels, enttypes, entnames = get_entity_info(F)
    # write entity information to text file
    writeEntityInfoText(F, outfile, 'a')
    
    #--------------------------------------------------------------------------
    # find and load event for R channel (Marker - from DataWave) data
    #--------------------------------------------------------------------------
    # !!!!!!!ASSUME that right channel marker is entity 5!!!!!!!!!!!
    markerR = F.entities[5]
    writeMarkerToText(markerR, outfile, 'a')
    
    #--------------------------------------------------------------------------
    # find and load event for L channel (Marker - from DataWave) data
    #--------------------------------------------------------------------------
    # !!!!!!!ASSUME that left channel marker is entity 6!!!!!!!!!!!
    markerL = F.entities[6]
    writeMarkerToText(markerL, outfile, 'a')
    
    #--------------------------------------------------------------------------
    # find, load, write, plot segment (spike snippet) data
    #--------------------------------------------------------------------------
    isseg, segment_indices = find_segment_entities(F)
    
    # check if any segment entities were found
    if len(segment_indices) == 0:
        # none found, quit script
        print "No Segments Found in file ", fullfile 
    else:
        for s in segment_indices:
            # need to convert to int
            segindx = int(s)
            # get the entity corresponding to segindx
            segment = F.entities[segindx]
            writeSegmentToText(segment, outfile, 'a')    
        # plot segment data
        plot_segments(segment_indices, F)
            
    #--------------------------------------------------------------------------
    # Access analog signal data::
    #--------------------------------------------------------------------------
    '''
    # select analog signal entity
    analog0 = F.entities[0]
    # load data from entity
    analogdata, times, count = analog0.get_data()
    '''
    
    #--------------------------------------------------------------------------
    # Close neuroshare object/interface
    #--------------------------------------------------------------------------
    F.close()
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
if __name__ == "__main__":
#    print "IN PYDD2MAT __main__"
#    print sys.argv
    print "\nNow executing main function"
    main(sys.argv[1:])
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
    
