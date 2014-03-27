# convertscript

import pyddf2mat
reload(pyddf2mat)
# import os
import os

inpath = 'F:\\Work\\Data\\Bat\\BatRestrainedData\\BatSorted\\878_Sorted'
outpath = 'F:\\Work\\Data\\Bat\\BatRestrainedData\\TextData'

filelist = os.listdir(inpath)
ddffiles = [];

nprocessed = 0;
for afile in filelist:
    if afile.endswith('.ddf'):
        ddffiles.append(afile)

nfiles = len(ddffiles)
print 'Found {0} ddf files'.format(nfiles)

for findex in range(0, nfiles):
        afile = ddffiles[findex]
        
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
        
        # create list of arguments
        argv = ['-i', infile, '-o', outfile]

        pyddf2mat.main(argv)
        
