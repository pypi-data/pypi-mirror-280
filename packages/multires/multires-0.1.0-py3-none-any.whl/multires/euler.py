import numpy as np

def euler(v,D,r,eul_dt,x0,t0):
    """
    Generate a trajectory with resetting using the Euler-Maruyama algorithm

    Parameters
    ----------
    v : Float
        Drift constant.
    D : Float
        Diffusion constant. Must be positive.
    r : Float
        Resetting constant. Must be non-negative.
    eul_dt : Float
        Simulation timestep.
    x0 : Float
        Initial position. Must be from 0 <= x0 < 1
    t0 : Float
        Initial time.

    Returns
    -------
    eul_x : Array
        Positions of the Brownian trajectory.
    eul_t : Array
        Times of the Brownian trajectory.

    """
    current_x = x0
    current_t = t0
    
    eul_x = [x0]
    eul_t = [t0]
    
    #Generate the first resetting itme
    if r == 0:
        tmax = 10**100
    else:
        tmax = np.random.exponential(1/r)
    
    while current_x >= 0:
        
        if current_t < tmax:
            #Check if next time increment will go over tmax
            if current_t+eul_dt > tmax:
                current_t = tmax
            else:
                current_t += eul_dt
            
            #Generate the next position increment using the SDE
            B = np.random.normal() #Generate random number B ~ N(0,1)
            d_x = v*eul_dt + np.sqrt(2*D*eul_dt)*B
            
            if current_x + d_x > 1:
                #Reflection condition
                current_x = 2-(current_x + d_x)
            else:
                current_x += d_x
        
        else:
            #If process does not reach absorbing boundary by the resetting time, generate a new resetting time and start the process again
            current_t = tmax
            current_x = x0
            tmax += np.random.exponential(1/r)
       
        eul_x.append(current_x)
        eul_t.append(current_t)            
    
    return eul_x, eul_t