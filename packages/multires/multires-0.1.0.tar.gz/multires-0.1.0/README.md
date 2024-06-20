# Multiresolution Algorithm

This package is an implementation of the standard and hybrid multiresolution algorithm as proposed in "Analytic and Monte Carlo Approximations to the Distribution of the First Passage Time of the Drifted Diffusion with Stochastic Resetting and Mixed Boundary Conditions" by J. Magalang, R. Turin, et. al. 

# Installation

Install the package from TestPyPI:
```
pip install -i https://test.pypi.org/simple/ multires
```
# Usage
To run a simulation, begin by first choosing the scheme that you want:
1.  `smra` for the standard MRA
2. `hmra` for the hybrid MRA

By default, either simulation scheme will produce a first passage time, rather than a full trajectory.

## SMRA
The `smra` function has the following syntax:
```
smra(v, D, r, x0, eps, kmax = 30, kmin = 25, trajectory = False)
```
Here is a description of each argument:
- `v` : Float. Drift constant.
- `D` : Float. Diffusion constant. Must be positive.
- `r` : Float. Resetting constant. Must be non-negative.
- `x0` : Float. Initial position. Must be from $0 \leq x_0 < 1$
- `eps` : Float. Error threshold. Must be positive.
- `kmax` : Integer, optional. Simulation parameter to determine the maximum resolution $k$ considered before stopping the simulation. The default is 30.
- `kmin` : Integer, optional. Simulation parameter to determine the minimum resolution $k$ considered before computing the next resetting interval given that the stopping condition has not been reached prior. The default is 25.
- `trajectory` : Boolean, optional. If `True`, function returns the full arrays of position and time of the trajectory. If `False`, function returns only the first passage time. The default is `False`.

Running the function will yield either three or four outputs, depending on the argument `trajectory`:

If `trajectory` is `False` (by default):
- `T` : Float. First passage time.
- `k` : Integer. Resolution at end of simulation
- `has_reached_eps` : Boolean. If `False`, simulation has failed to reach the error threshold before reaching `k = kmax`

If `trajectory` is `True`:
- `x_arr` : Array. Positions of the Brownian trajectory at the end of the simulation.
- `t_arr` : Array. Times of the Brownian trajectory at the end of the simulation.
- `k` : Integer. Resolution at end of simulation
- `has_reached_eps` : Boolean. If `False`, simulation has failed to reach the error threshold before reaching `k = kmax`

This is an example of the usage of the `smra` function:

For a single first passage time:
```
import multires as mra

T, k, has_reached_eps = mra.smra(-10**(-3), 10**(-4), (1/3)*(1/365), 0.8, 10**(-4))
```
Sample output:
```
>>> T
np.float64(370.1612953761)
>>> k
24
>>> has_reached_eps
True
```
For a trajectory:
```
import multires as mra

xvalues, tvalues, k, has_reached_eps = mra.smra(-10**(-3), 10**(-4), (1/3)*(1/365), 0.8, 10**(-4), trajectory = True)
```
Sample output:
```
>>> xvalues
array([ 0.8       ,  0.80002268,  0.8000829 , ..., -0.03714226, -0.03716605, -0.03718239])
>>> tvalues
 array([0.00000000e+00, 5.02717020e-05, 1.00543404e-04, ..., 8.43419103e+02, 8.43419153e+02, 8.43419204e+02]),
>>> k
24
>>> has_reached_eps
True
```
## HMRA
The `hmra` function has the following syntax:
```
hmra(v, D, r, x0, eps, eul_dt, mul_thresh = 0.1, kmax = 30, trajectory = False)
```
Here is a description of each argument:
- `v` : Float. Drift constant.
- `D` : Float. Diffusion constant. Must be positive.
- `r` : Float. Resetting constant. Must be non-negative.
- `x0` : Float. Initial position. Must be from $0 \leq x_0 < 1$
- `eps` : Float. Error threshold. Must be positive.
- `eul_dt` : Float. Euler-Maruyama simulation timestep.
- `mul_thresh` : Float, optional. Position threshold, the multiresolution algorithm will begin to compute if the Euler trajectory is below this threshold. The default is 0.1.
- `kmax` : Integer, optional. Simulation parameter to determine the maximum resolution $k$ considered before stopping the simulation. The default is 30.
- `trajectory` : Boolean, optional. If `True`, function returns the full arrays of position and time of the trajectory. If `False`, function returns only the first passage time. The default is `False`.

Running the function will yield either three or four outputs, depending on the argument `trajectory`:

If `trajectory` is `False` (by default):
- `T` : Float. First passage time.
- `k` : Integer. Resolution at end of simulation
- `has_reached_eps` : Boolean. If `False`, simulation has failed to reach the error threshold before reaching `k = kmax`

If `trajectory` is `True`:
- `x_arr` : Array. Positions of the Brownian trajectory at the end of the simulation.
- `t_arr` : Array. Times of the Brownian trajectory at the end of the simulation.
- `k` : Integer. Resolution at end of simulation
- `has_reached_eps` : Boolean. If `False`, simulation has failed to reach the error threshold before reaching `k = kmax`

This is an example of the usage of the `smra` function:

For a single first passage time:
```
import multires as mra

T, k, has_reached_eps = mra.hmra(-10**(-3), 10**(-4), (1/3)*(1/365), 0.8, 10**(-4), 0.1)
```
Sample output:
```
>>> T
np.float64(638.0523437500765)
>>> k
10
>>> has_reached_eps
True
```
For a trajectory:
```
import multires as mra

xvalues, tvalues, k, has_reached_eps = mra.hmra(-10**(-3), 10**(-4), (1/3)*(1/365), 0.8, 10**(-4), 0.1, trajectory = True)
```
Sample output:
```
>>> xvalues
array([ 0.8       ,  0.79679549,  0.80113966, ..., -0.00413409, -0.0042602 , -0.00409163])
>>> tvalues
 array([0.00000000e+00, 1.00000000e-01, 2.00000000e-01, ..., 7.48199805e+02, 7.48199902e+02, 7.48200000e+02]),
>>> k
10
>>> has_reached_eps
True
```
## Auxiliary Functions

This package also contains auxiliary functions:
1. `increase_resolution` increases the resolution of a trajectory from level $k-1$ to $k$ given that the input array has length $2^{k-1}+1$, following Equation 4.3 of Magalang, Turin, et. al.
2. `euler` is an implementation of the Euler-Maruyama algorithm which outputs a full trajectory and is required for the HMRA.

> Written with [StackEdit](https://stackedit.io/).
