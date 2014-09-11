===========================================================================
===========================================================================

This is a small bit of code I have written to convert DataWave Technologies’
.ddf format files to a text format that can then be imported into other
analysis programs (in my case, Matlab).

Note that SciWorks from DataWave must be installed on your system in order for
the dll information to be used properly on Windows.  The hardlock USB key is, however, not necessary to use this code.  

I am running this code in a virtual environment installation of Windows 7
(32 bit) in a Mac OS X host.

Sharad J. Shanbhag
sshanbhag@neomed.edu
===========================================================================
===========================================================================



===========================================================================
===========================================================================
Some other bits of info from code that is used in this project:
===========================================================================
===========================================================================


Python Bindings for Neuroshare
==============================

The Neuroshare API is a standardized interface to access
electrophysiology data stored in various different file
formats. To do so, it uses format- specific shared libraries.
Refer to the official website
     		    http://neuroshare.org
for more information.

The aim of this library is to provide a high level interface
to the Neuroshare API, i.e. it focuses on API usability more
then being a mere python version of the C API. Thus none of
the original Neuroshare API calls are directly exposed but
the interface is through python objects that resemble (more
or less) the Neuroshare Entities.


Installation
------------

The compile-time requirements for python-neuroshare are the
'setuptools' and the Python development files and a working
C compiler (clang or gcc) and NumPy. For Debian based
distributions, e.g. Ubuntu, this can easily be done with:

	$ sudo apt-get install clang python-setuptools \
                               python-dev python-numpy

After that, python-neuroshare is installed with the following
command:

	$ sudo python setup.py install

Additional runtime dependencies:
	* The Neuroshare vendor DLLs for the specific data file(s)!
	  Please refer to the following section for more information.

##################
FOR WINDOWS:
##################
assumptions: 
	1. Canopy python distribution is installed):
	2. you have a copy of the neuroshare .egg file, 
		e.g., neuroshare-0.8.5-py2.7-win32.egg

Step 1: launch the command prompt from windows start menu
	Start->AllPrograms->command

Step 2: make sure you have the full path to the neuroshare .egg
file
	C:\Users\steveballmer\neuroshare-0.8.5-py2.7-win32.egg

Step 3: install using the egginst command:

> egginst C:\Users\steveballmer\neuroshare-0.8.5-py2.7-win32.egg

you should get something that looks like this:

C:\> egginst C:\Users\steveballmer\neuroshare-0.8.5-py2.7-win32.egg

neuroshare-0.8.5-py2.7-win32.egg         [installing]
    82 KB[.............................................]

C:\>

you can test installation:

C:\>python
Enthought Canopy Python 2.7.6 | 32-bit | 
Type "help", "copyright", "credits" or "license" for more information.
>>> import neuroshare
>>>

if no errors... it's installed!

- - - - - - - - - - - - - -
- - - - - - - - - - - - - -


- - - - - - - - - - - - - -
Installation of vendor DLLs
- - - - - - - - - - - - - -

Python-neuroshare relies on the vendor specific DLLs to
access data failes. Therefore the specific DLLs for each
type of file must be downloaded and installed into one of
the following locations:
	/usr/local/lib/neuroshare
	/usr/lib/neuroshare
	~/.neuroshare
----> windows:  C:\Apps\NeuroshareDLLs

A (possibly incomplete) list of the vendor specific DLLs
can be obtained be obtained from the neuroshare website:
  http://neuroshare.sourceforge.net/DLLLinks.shtml

Please note that you need the corresponding DLLs for your
platform (e.g. Linux, 64-bit). If you find yourself in the
situation that there is no DLL for your specific platform
and you are either on a UNIX-like system you can use G-Node's
very one nswineproxy component to use the Windows 32 bit
DLLs. Please refer to the nswineproxy homepage for more
information:
	https://github.com/G-Node/nswineproxy

Usage
-----

   Opening a file:

	>> import neuroshare as ns
	>> fd = ns.File ("NeuroshareExample.mcd")

   Iterate over the entities in the file:

   	>> for entity in fd.list_entities():
        >>    print entity.label, entity.entity_type
	>>    ... do something else with entity ...


Reporting Bugs & Submitting Patches
-----------------------------------
Any bugs can and should be filed to the project's issue
tracker at github:
	https://github.com/G-Node/python-neuroshare/issues
