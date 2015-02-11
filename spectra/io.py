import numpy as np
import pyfits

def read_fits(file_path):
    """
    Read in a fits spectrum
    """
    print "READING IN SPECTRUM {f}".format(f=file_path)
    return True


def write_fits(arr, file_path):
    """
    Write out a numpy array as a fits file
    """
    print "WRITING FITS SPECTRUM {f}".format(f=file_path)
    return True


def closest(array,value):
    """ Return array index closest to value """
    idx = (np.abs(array-value)).argmin()
    return idx



def specread(filename, wlmin, wlmax):
    """ Read in 1-D fits spectrum, return wavelengths and fluxes """
    print 'opening stuff'
    x = pyfits.open(filename)
    # get header info, to calculate wavelength array
    crval = x[0].header['CRVAL1']
    cdelt = x[0].header['CDELT1']
    bunit = x[0].header['BUNIT']
    flux = x[0].data
    x.close()
    
    wl = np.zeros(len(flux))
    
    for i in range(len(flux)):
        if i == 0:
            wl[i] = crval
        else:
            wl[i] = wl[i-1]+cdelt

    indmin = closest(wl, wlmin) # 1270
    indmax = closest(wl, wlmax) # 1330
    wl= wl[indmin:indmax]
    flux=flux[indmin:indmax]
    return wl, flux 
   
def hello():
    print "hello world"


def get_lims(filename):
    """ Return min and max wavelength of a 1-D spectrum """
    x = pyfits.open(filename,memmap=False)
    crval = x[0].header['CRVAL1']
    cdelt = x[0].header['CDELT1']
    flux = x[0].data
    x.close(closed=True,verbose=True)
    wl = np.zeros(len(flux))
    for i in range(len(flux)):
        if i == 0:
            wl[i] = crval
        else:
            wl[i] = wl[i-1]+cdelt
            
    wlmin = wl[0]
    wlmax = wl[len(wl)-1]
    return wlmin, wlmax
            
