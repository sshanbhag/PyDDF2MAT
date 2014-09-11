#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# PyDDF_Info.py
#------------------------------------------------------------------------------
#   functions to obtain entity information from Neuroshare API
#------------------------------------------------------------------------------
# Sharad J. Shanbhag
# sshanbhag@neomed.edu
#------------------------------------------------------------------------------
# Created 26 March, 2014
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# import plotting methods from matplotlib
import matplotlib.pyplot as plt
# need numpy for array manipulation
import numpy as np

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Function to list entities
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def entity_info( nsobj ) :
    "print entity info"
    sepstr = '----------------------------------------------------------------'
    # simple list of Entity types , indexed from 1:5
    EntityNames = ['', 'Event', 'Analog', 'Segment', 'Neural', 'Unknown'] 
    # loop through entities, print label
    print(sepstr)
    print('Entities in:\n  {0}'.format(nsobj._filename))
    print(sepstr)
    for index, entity in enumerate(nsobj.list_entities()):
        print 'Entity {0:2}: {1:35} {2}\t{3}'.format(index, 
                                                entity.label, 
                                                entity.entity_type,
                                                EntityNames[entity.entity_type])
    print(sepstr)
    #for index, entity in enumerate(nsobj.list_entities()):
    #    print entity
    return
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Function to return entity information
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def get_entity_info( nsobj ) :
    """
        return entity info
        entity_label    {list}
        entity_type     {list}
        entity_name     {list}
    """
    # simple list of Entity types , indexed from 1:5
    EntityNames = ['', 'Event', 'Analog', 'Segment', 'Neural', 'Unknown']
    # initialize storage lists
    entity_label = list()
    entity_type = list()
    entity_name = list()
    # loop through entities, store label information
    for index, entity in enumerate(nsobj.list_entities()):
        entity_label.append(entity.label)
        entity_type.append(entity.entity_type)
        entity_name.append(EntityNames[entity.entity_type])

    return (entity_label, entity_type, entity_name)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# find segment (spike snippet) data
#------------------------------------------------------------------------------
def find_segment_entities(nsobj):
    isseg = []
    
    # get entity information
    entlabels, enttypes, entnames = get_entity_info(nsobj)

    # loop through entity names list and check for 'Segment'
    for n in entnames:
        if n is 'Segment':
            isseg.append('True')
        else:
            isseg.append('False')
            
    # convert isseg to NumPy array - this will allow use of np array's "where"
    # method while looking for segment
    isseg = np.array(isseg)

    # find segments
    segment_indices = np.where(isseg == 'True')[0]
    
    return (isseg, segment_indices)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# plot segments
#------------------------------------------------------------------------------
def plot_segments(segment_indices, nsobj):
    # loop through segment entities
    pltindex = 0;
    for s in segment_indices:
        # need to convert to int
        segindx = int(s)
        # get the entity corresponding to segindx
        segment = nsobj.entities[segindx]
        # retrieve all data elements... first initialize some list variables
        spiketraces = [];
        spiketimes = [];
        spikepoints = [];
        spikeids = [];
        # total number of spikes
        nspikes_total = segment.item_count;
        print '%d total spikes' % segment.item_count
        # loop through segments and extract/store data
        for spikeindx in range(0, segment.item_count):
            # store values
            spike = segment.get_data(spikeindx)
            spiketraces.append(spike[0][0])
            spiketimes.append(spike[1])
            spikepoints.append(spike[2])
            spikeids.append(spike[3])
        # plot traces
        plt.figure(pltindex)
        for spikeindx in range(0, nspikes_total):
            plt.plot(spiketraces[spikeindx])
        print spikeids
        print len(spikeids)
        pltindex = pltindex + 1;
#------------------------------------------------------------------------------

