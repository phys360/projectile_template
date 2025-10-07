from math import radians
import numpy as np

def solver(v0=15,  
           theta = 20,
           m=0.42,  
           beta = 1.3* 0.5 * (0.69**2)/(4*np.pi), 
           dt = 1e-3 ):


  x = [0.]  
  y = [0.]  
  t = [0.]
  g=9.81
  
  # convert speed
  n = 0  
  vx, vy = convert_speed(v0, theta)

  while y[n]>= 0:
    t.append(t[n] + dt)
    ax, ay = dvdt(m,g,beta,vx,vy)
    
    vx.append(vx[n] + ax*dt)
    vy.append(vy[n] + ay*dt)
    
    x.append(x[n] + vx[n+1] * dt)
    y.append(y[n] + vy[n+1] * dt)
    n += 1
      
  return x,y