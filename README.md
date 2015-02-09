# xt
example python module for xtina

Make sure that PYTHONPATH includes the folder where this is located

try this:
import xt.spectra (or .imaging)
xt.spectra.io.readfits("some_file.fits")
xt.imaging.io.readfits("some_file.fits")


# CCWs notes:
# xt is the parent directory, spectra is a sub directory, io is a .py file that contains a def called readfits. spectra needs a blank __init__.py file.
# note you 