import numpy as np
from .increase_resolution import increase_resolution

def smra(v, D, r, x0, eps, kmax = 30, kmin = 25, tmax_in = 10**5, trajectory = False):
    """
    Function to either generate a first passage time or a Brownian trajectory starting from x0 up to the first crossing below 0 following the standard MRA.

    Parameters
    ----------
    v : Float
        Drift constant.
    D : Float
        Diffusion constant. Must be positive.
    r : Float
        Resetting constant. Must be non-negative.
    x0 : Float
        Initial position. Must be from 0 <= x0 < 1
    eps : Float
        Error threshold. Must be positive.
    kmax : Integer, optional
        Simulation parameter to determine the maximum resolution k considered before stopping the simulation. The default is 30.
    kmin : Integer, optional
        Simulation parameter to determine the minimum resolution k considered before computing the next resetting interval given that the stopping condition has not been reached prior. The default is 25.
    tmax_in : Float, optional
        The time at the endpoint of the Brownian trajectory when r = 0. The default is 10**5.
    trajectory : Boolean, optional
        If true, function returns the full arrays of position and time of the trajectory. If false, function returns only the first passage time. The default is False.

    Returns
    -------
    
    If "trajectory" == False (default):
    T : Float
        First passage time.
    k : Integer
        Resolution at end of simulation
    has_reached_eps : Boolean
        If False, simulation has failed to reach the error threshold before reaching k = kmax
    
    If "trajectory" == True:
    x_arr : Array
        Positions of the Brownian trajectory at the end of the simulation.
    t_arr : Array
        Times of the Brownian trajectory at the end of the simulation.
    k : Integer
        Resolution at end of simulation
    has_reached_eps : Boolean
        If False, simulation has failed to reach the error threshold before reaching k = kmax

    """
    
    x00 = x0
    t00 = 0.0
    
    #Generate the first reset time
    if r == 0:
        tmax = tmax_in
    else:
        tmax = np.random.exponential(1/r)
    
    T = np.nan
    
    hit = False
    has_reached_eps = True
    
    while hit == False:
    
        k = 0
        #Generate the end position at the resetting interval biased to the drift constant v
        x01 = np.random.normal(loc = (v*(tmax-t00))+x00, scale= np.sqrt(2*D*(tmax-t00)))
        
        #Generate the resetting interval
        x_arr = [x00, x01]
        t_arr = [t00, tmax]
        
        while True:
            #Increment resolution
            k += 1
            
            #Generate the next resolution given the resetting interval
            x_arr, t_arr = increase_resolution(x_arr, t_arr, D, k, (tmax-t00))
            
            #Generate the reflected trajectory (Section 4.3)
            Xref = np.empty(len(x_arr))
            Xref[0] = x_arr[0]
            for i in range(0, len(x_arr)-1):
                dx = x_arr[i+1]-x_arr[i]
                if Xref[i]+dx > 1:
                    Xref[i+1] = 2-(Xref[i]+dx)
                else:
                    Xref[i+1] = Xref[i]+dx
            
            #Check if any of the reflected trajectory has reached the boundary
            abscheck = np.where(Xref<0)
            
            if np.any(abscheck):
                T_ind = abscheck[0][0]
                T = t_arr[T_ind]
                
                h = (tmax-t00)/(2**k)
                #Check if reflected trajectory has reached the stopping condition (Equation 4.10)
                if h<eps:
                    hit = True
                    break
                #If stopping condition has not been reached up until kmax, simulation ends with a failure
                elif k >= kmax:
                    hit = True
                    has_reached_eps = False
                    break
            #If simulation has not reached the boundary, start the process again with a new resetting interval
            elif k >= kmin:
                t00 = tmax
                tmax += np.random.exponential(1/r)
                break
    
    if trajectory:
        return x_arr, t_arr, k, has_reached_eps
    else:
        return T, k, has_reached_eps