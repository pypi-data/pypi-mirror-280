import numpy as np
from .increase_resolution import increase_resolution
from .euler import euler

def hmra(v, D, r, x0, eps, eul_dt, mul_thresh = 0.1, kmax = 30, trajectory = False):
    """
    Function to either generate a first passage time or a Brownian trajectory starting from x0 up to the first crossing below 0 following the hybrid MRA.

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
    eul_dt : Float
        Euler-Maruyama simulation timestep.
    mul_thresh : Float, optional
        Position threshold, the multiresolution algorithm will begin to compute if the Euler trajectory is below this threshold. The default is 0.1.
    kmax : Integer, optional
        Simulation parameter to determine the maximum resolution k considered before stopping the simulation. The default is 30.
    trajectory : Boolean, optional
        If true, function returns the full arrays of position and time of the trajectory. If false, function returns only the first passage time. The default is False.

    Returns
    -------
    If "trajectory" == False (default):
    fpt : Float
        First passage time.
    k : Integer
        Resolution at end of simulation
    has_reached_eps : Boolean
        If False, simulation has failed to reach the error threshold before reaching k = kmax
    
    If "trajectory" == True:
    xtraj_final : Array
        Positions of the Brownian trajectory at the end of the simulation.
    ttraj_final : Array
        Times of the Brownian trajectory at the end of the simulation.
    k : Integer
        Resolution at end of simulation
    has_reached_eps : Boolean
        If False, simulation has failed to reach the error threshold before reaching k = kmax

    """
    
    t0 = 0
    
    #Make an Euler-Maruyama estimate of the first passage time
    eul_x, eul_t = euler(v,D,r,eul_dt,x0,t0)
    eul_fpt = eul_t[-1]
    
    subx_arrs = []
    subt_arrs = []
    thresh_inds = []
    #Obtain all segments of the Euler-Maruyama trajectory that are below the position threshold
    for i in np.arange(0, len(eul_x)-1):
        if eul_x[i+1]<mul_thresh:
            subx_arrs.append([eul_x[i], eul_x[i+1]])
            subt_arrs.append([eul_t[i], eul_t[i+1]])
            thresh_inds.append(i)
    
    x_arrs = [subx_arrs]
    t_arrs = [subt_arrs]
    
    #Begin the multiresolution algorithm for the segments below the threshold
    k = 0
    
    T = eul_fpt
    has_reached_eps = True
    
    while True:
        #Obtain the k-th element of the array of Euler-Maruyama segments
        xk_arr = x_arrs[k]
        tk_arr = t_arrs[k]
        
        k += 1
        
        xk_arrs = []
        tk_arrs = []
        #Iterate over all Euler-Maruyama segments
        for i in np.arange(0, len(xk_arr)):
        
            xi_arr = xk_arr[i]
            ti_arr = tk_arr[i]
            #Increase resolution of each Euler-Maruyama segment
            xi_arr, ti_arr = increase_resolution(xi_arr, ti_arr, D, k, eul_dt)
            
            xk_arrs.append(xi_arr)
            tk_arrs.append(ti_arr)
        
        x_arrs.append(xk_arrs)
        t_arrs.append(tk_arrs)
        
        xktraj = np.array(xk_arrs).ravel()
        tktraj = np.array(tk_arrs).ravel()
        
        #Check if full trajectory has reached the boundary
        abscheck = np.where(xktraj<0)
        
        if np.any(abscheck):
        
            T_ind = abscheck[0][0]
            T = tktraj[T_ind]

            h = eul_dt/(2**(k))
            #Check if reflected trajectory has reached the stopping condition (Equation 4.10)
            if h < eps:
               break
            #If stopping condition has not been reached up until kmax, simulation ends with a failure
            elif k >= kmax:
                has_reached_eps = False
                break
    
    if trajectory:
        
        xtraj = eul_x.copy()
        ttraj = eul_t.copy()
        for ith in range(len(thresh_inds)):
            th_ind = thresh_inds[ith]
            t_insert = tk_arrs[ith][:-1]
            ttraj[th_ind] = t_insert
            
            x_insert = xk_arrs[ith][:-1]
            xtraj[th_ind] = x_insert
        
        x_arr = np.hstack(xtraj)
        t_arr = np.hstack(ttraj)
        
        return x_arr, t_arr, k, has_reached_eps
    else:
        return T, k, has_reached_eps