import numpy as np
from pylab import *


############################################################
# NAME
############################################################

def gauss_variate(x,xerr):
   xerr = np.array(xerr)
   
   if len(xerr) == 1:
      newerr = np.zeros(len(x))
      newerr[:] = xerr
      xerr = newerr

   if len(x) > 1:
      variate = np.zeros(len(x))
      for jj in range(len(x)):
         yy = np.sqrt(-2.*log(np.random.random()))*cos(2.*pi*np.random.random())

         perturb = yy
         variate[jj] = x[jj] + (perturb*xerr[jj])
   else:
      print " i am in the len(x) = 1 loop"
      yy =np.sqrt(-2.*log(np.random.random()))*cos(2.*pi*np.random.random())
      perturb = yy
      variate = x + perturb*xerr

   return variate



def calc_stddev(arrinp):
   
   stddev = np.std(arrinp,axis=0)
   print stddev
   return stddev
