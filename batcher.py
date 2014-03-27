# convertscript

import pyddf2mat

# import os
import os
import sys



inpath = 'F:\\Work\\Data\\Bat\\BatRestrainedData\\BatSorted\\866_Sorted'
outpath = 'F:\\Work\\Data\\Bat\\BatRestrainedData\\TextData'

filelist = os.listdir(inpath)

nprocessed = 0;
for afile in filelist:
    if afile.endswith('.ddf'):

        # split extension and base name
        filebase, fileext = os.path.splitext(afile)
        
        # generate output filename
        outname = filebase + '.txt'
        # append paths
        infile = os.path.join(inpath, afile)
        outfile = os.path.join(outpath, outname)
        
        print "reading from:\n\t", infile
        print "writing to:\n\t", outfile
        print "\n"
        
        argv = ['-i ' + infile, '-o ' + outfile]
        
        print argv
        
        pyddf2mat.main(argv)
        
        nprocessed = nprocessed + 1
        
        if nprocessed == 1:
            sys.exit()
        
