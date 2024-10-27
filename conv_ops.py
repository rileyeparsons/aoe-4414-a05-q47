# conv_ops.py

# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p

# Test Case: py conv_ops.py 2054 4 29 11 29 03.3 6778.136999646678 -0.030015095972430572 3838.027968
# Converting from ecef to eci positions

# Parameters:
#  c_in : int 
#   input channel count
#  h_in : int 
#   input height count
#  w_in : int 
#   input width count
#  n_filt : int 
#    number of filters in the convolution layer
#  h_filt : int 
#   filter height count
#  w_filt : float
#   filter width count
#  s : int | float | str
#   stride of convolution filters
#  p : int | float | str
#   amount of padding on each of the four input map sides

# Output:
#  c_out : list
#  output channel count
#  h_out : list
#  output height count
#  w_out : list
#  output width count
#  adds : list
#  number of additions performed
#  muls : list
#  number of multiplications performed
#  divs : list
#  number of divisions performed

# Written by Riley Parsons

import sys
import math

# "constants"
w = 7.292115e-5

# helper functions  
def output_map_h(h_in, p, h_filt, s):
  h_out = ((h_in + 2*p - h_filt)/s) +  1
  return h_out

def output_map_w(w_in, p, w_filt, s):
  w_out = ((w_in + 2*p - w_filt)/s) +  1
  return w_out

def get_muls(n_filt, h_out, w_out, c_in, h_filt, w_filt):
  muls = n_filt*h_out*w_out*c_in*h_filt*w_filt
  return muls

def get_adds(n_filt, h_out, w_out, c_in, h_filt, w_filt):
  adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
  return adds

def get_divs(c_in, h_out, w_out):
  divs = c_in*h_out*w_out
  return divs

# main function
def conv_ops(c_in, h_in, w_in, n_filt, h_filt, w_filt, s, p):
  
  c_out = c_in
  h_out = output_map_h(h_in, p, h_filt, s)
  w_out = output_map_w(w_in, p, w_filt, s)
  adds = get_adds(n_filt, h_out, w_out, c_in, h_filt, w_filt)
  muls = get_muls(n_filt, h_out, w_out, c_in, h_filt, w_filt)
  divs = get_divs(c_in, h_out, w_out)

  print(c_out)
  print(h_out)
  print(w_out)
  print(adds)
  print(muls)
  print(divs)

  return c_out, h_out, w_out, adds, muls, divs
  
# initialize script arguments
year = None
month = None
day = None
hour = None
min = None
sec = None
ecef_x_km = None
ecef_y_km = None
ecef_z_km = None

# parse script arguments
if len(sys.argv)==10:
  year = int(sys.argv[1])
  month = int(sys.argv[2])
  day = int(sys.argv[3])
  hour = int(sys.argv[4])
  min = int(sys.argv[5])
  sec = float(sys.argv[6])
  ecef_x_km = float(sys.argv[7])
  ecef_y_km = float(sys.argv[8])
  ecef_z_km = float(sys.argv[9])

else:
  print('Usage: python3 conv_ops.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km')
  exit()

# write script below this line
if __name__ == '__main__':
  conv_ops(year, month, day, hour, min, sec, ecef_x_km, ecef_y_km, ecef_z_km)
else:
  conv_ops(year, month, day, hour, min, sec, ecef_x_km, ecef_y_km, ecef_z_km)