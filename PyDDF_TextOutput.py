#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# PyDDF_TextOutput.py
#------------------------------------------------------------------------------
#   functions to write DDF data (accessed via Neuroshare-Python library)
#   as text
#------------------------------------------------------------------------------
# Sharad J. Shanbhag
# sshanbhag@neomed.edu
#------------------------------------------------------------------------------
# Created 26 March, 2014
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

import sys
import numpy as np

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Function to write main NS information to text file
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def writeMetadataText(nsobj, outfilename, mode):
    metadata_keys = [
    'AppName',
    'FileType',
    'FileComment',
    'EntityCount',
    'Time_Year',
    'Time_Month',
    'Time_Day',
    'Time_Hour',
    'Time_Min',
    'Time_Sec',
    'Time_MilliSec',
    'TimeStampResolution',
    'TimeSpan'
    ]
    if outfilename == 'stdout':
        sys.stdout.write('SourceFile:{0}\n'.format(nsobj._filename))
        for keystr in metadata_keys:
            keydata = nsobj.metadata_raw[keystr]
            sys.stdout.write('{0}:{1}\n'.format(keystr, keydata))
    else:
        with open(outfilename, mode) as fp:
            # metadata tag
            fp.write('METADATA\n')
            # source file name
            fp.write('SourceFile:{0}\n'.format(nsobj._filename))
            for keystr in metadata_keys:
                keydata = nsobj.metadata_raw[keystr]
                fp.write('{0}:{1}\n'.format(keystr, keydata))
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Function to write entity information
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def writeEntityInfoText(nsobj, outfilename, mode) :
    "print entity info"
    # simple list of Entity types , indexed from 1:5
    EntityNames = ['', 'Event', 'Analog', 'Segment', 'Neural', 'Unknown']
    
    # loop through entities, print label
    with open(outfilename, mode) as fp:
        # Entity info tag
        fp.write('ENTITY_INFO\n')
        fp.write('Nentities:{0}\n'.format(nsobj.entity_count))
        for index, entity in enumerate(nsobj.list_entities()):
            fp.write('Entity{0}:{2}:{3}:{1}\n'.format(index, 
                                                    entity.label, 
                                                    entity.entity_type,
                                                    EntityNames[entity.entity_type]))

    return
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Function to write segment entity 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def writeSegmentToText(seg, outfilename, mode):
    """
    segment is written as:
        <segment ID tag>
        EntityLabel:<entity label for tag>
        Nsegments:<# of segments>
    then, for each segment:
        spiketime,spikeid,spikepoints,spike[0],...,spike[spikepoints-1]
        
    for example:
        SEGMENT
        EntityLabel:/ch3_spikes
        MaxSampleCount:130
        MinSampleCount:130
        SampleRate:40000.0
        Units:mV
        Nsegments:2
        42.7828367488,1,140,9.765625,...,4.8828125,4.8828125
        60.7066778762,1,140,-19.53125,...,-19.53125,-24.4140625,
    """
    print '%d total spikes' % seg.item_count
    
    if outfilename == '':
        # loop through segments and extract/store data
        for spikeindx in range(0, seg.item_count):
            # store values
            spike = seg.get_data(spikeindx)
            spiketrace = spike[0][0]
            spiketime = spike[1]
            spikepoints = spike[2]
            spikeid = spike[3]
            print '{0},{1},{2},'.format(spiketime, spikeid, spikepoints),
            for j in range(0, spiketrace.size):
                print '{0},'.format(spiketrace[j]),
            print '\n',
    else:
        with open(outfilename, mode) as fp:
            # write segment tag
            fp.write('SEGMENT\n')
            # write entity label
            fp.write('EntityLabel:{0}\n'.format(
                                        seg.metadata_raw['EntityLabel']))
            # write man, min sample count
            fp.write('MaxSampleCount:{0}\n'.format(
                                    seg.metadata_raw['MaxSampleCount']))
            fp.write('MinSampleCount:{0}\n'.format(
                                    seg.metadata_raw['MinSampleCount']))
            fp.write('SampleRate:{0}\n'.format(
                                    seg.metadata_raw['SampleRate']))
            fp.write('Units:{0}\n'.format(
                                    seg.metadata_raw['Units']))
           # write # of segments
            fp.write('Nsegments:{0}\n'.format(seg.item_count))
            # loop through segments and extract/store data
            for spikeindx in range(0, seg.item_count):
                # store values
                spike = seg.get_data(spikeindx)
                spiketrace = spike[0][0]
                spiketime = spike[1]
                spikepoints = spike[2]
                spikeid = spike[3]
                fp.write('{0},{1},{2},'.format(spiketime, spikeid, spikepoints))
                for j in range(0, spiketrace.size):
                    fp.write('{0},'.format(spiketrace[j]))
                fp.write('\n')            
    return
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Function to write marker entity 
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def writeMarkerToText(marker, outfilename, mode):
    count = marker.item_count
    label = marker.label
    
    if outfilename == '':
        print 'EntityLabel:{0}'.format(label)
        print 'Nmarkers:{0}'.format(count)
        print 'CSVDesc:{0}\n'.format(marker.csv_desc)
        #mdata, mtimes, mcount = marker.get_data(1)
        for m in range(0, count):
            M = marker.get_data(m)
            print '{0},{1},'.format(M[0], M[1])            
    else:
        with open(outfilename, mode) as fp:
            fp.write('MARKER\n')
            fp.write('EntityLabel:{0}\n'.format(label))
            fp.write('Nmarkers:{0}\n'.format(count))
            fp.write('CSVDesc:{0}\n'.format(marker.csv_desc))
            #mdataR, mtimesR, mcountR = markerR.get_data(1)
            for m in range(0, count):
                M = marker.get_data(m)
                fp.write('{0},{1},\n'.format(M[0], M[1]))
                           
    return
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def writeAnalogToText(analogobj, outfilename, mode):
    # get data for analog object
    analogdata = analogobj.get_data()
    # take action depending on outfilename
    if outfilename == 0:
        # if empty, write to screen
        for n in range(0, analogdata.size):
            print analogdata[n]
    else:
        # otherwise, write to file
        with open(outfilename, mode) as fp:
            # ANALOG id tag
            fp.write('ANALOG\n')
            # probe information
            fp.write('ProbeInfo:{0}\n'.format(analogobj.probe_info))
            # sample rate (samples/sec)
            fp.write('SampleRate:{0}\n'.format(analogobj.sample_rate))
            # number of samples
            fp.write('Nsamples:{0}\n'.format(analogdata.size))
            for n in range(0, analogdata.size):
                fp.write('{0},\n'.format(analogdata[n]))

    return
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
    


















#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# routines to write NumPy objects to binary file (to be compatible with
# Matlab BinaryFileToolbox)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def writeString(fileobj, outstring):
    "writes string to binary file fileobj in manner compatible with bintbx"
    typechar = np.array(['T'], dtype = 'str')
    # need length of outstring, in uint8 format
    nchar = np.array(len(outstring), dtype = 'uint8')
    outarray = np.array(outstring)
    typechar.tofile(fileobj)
    nchar.tofile(fileobj)
    outarray.tofile(fileobj)
#------------------------------------------------------------------------------    
def writeVector(fileobj, outvec, fmt):
    "writes string to binary file fileobj in manner compatible with bintbx"
    # ID char for vector = V
    typechar = np.array(['V'], dtype = 'str')
    # need length of outvec, in uint32 format
    nvals = np.array(len(outvec), dtype = 'uint32')
    # generate output array of proper format
    outarray = np.array(outvec, dtype = fmt)
    # write type character to file
    typechar.tofile(fileobj)
    # write the vector data format to file as string
    writeString(fileobj, fmt)
    # write # of values in array
    nvals.tofile(fileobj)
    # write array data
    outarray.tofile(fileobj)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------



