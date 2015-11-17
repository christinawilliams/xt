import numpy as np


def read_fits(file_path):
    """
    Reads in a fits image
    """
    print "READING FITS IMAGE"
    return True


def write_fits(arr, file_path):
    """
    Write out a fits image
    """
    print "WRITING OUT A FITS IMAGE"
    return True
    

def make_region(ra,dec,fn,label="",radius=".75",color="green",fontsize="10"):
    """ Make a DS9 region file

    Make DS9 region file called fn from a list of ra,dec coordinates.
    Optionally add a label or change the radius, color and fontsize. Adapted 
    from IDL code make_region.pro on 2/9/15.
    """
    file = open(fn,"w")
    file.write('global color=white dashlist=8 3 width=1 font="helvetica '+
               fontsize+' normal" select=1 highlite=1 dash=0 fixed=0 edit=1'+ 
               ' move=1 delete=1 include=1 source=1\n')
    file.write('fk5\n')
    print "length of label is",len(label)
    print label[0]
    for i in range(len(ra)):
        print label[i]
        format = 'circle(%f,%f,%s")# color=%s width=1 text={%s}\n'
        values=(ra[i],dec[i],radius,color,label[i])
        file.write(format % values)
        
    file.close()
