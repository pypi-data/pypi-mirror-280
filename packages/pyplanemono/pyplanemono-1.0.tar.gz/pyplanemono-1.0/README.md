# pyplanemono

[TOC]

Welcome to the PyPlaneMono repository!

This repo contains the code for the PyPlaneMono python package, which is capable of calculating geometrical quantities of a plane grating monochromator (PGM). Colloquially known as the plane mono, PGMs are widely used at synchrotron and free-electron laser facilities which require monochromatic soft X-ray light (50-3000 eV) worldwide. 

To install, we recommend you use PyPi installation:

``` console
$ python -m pip install pyplanemono
```
You should take extra care when you wish to use PyPlaneMono's API with *SHADOW* to perform raytracing; you must use *SHADOW*'s own python environment to do so. (usually a miniconda 3.8 installation)

You can also install from source should you wish to develop PyPlaneMono yourself:
``` console
$ git clone https://github.com/patrickwang27/pyplanemono pyplanemono
$ cd $! && python -m pip install -e .
```
## References
If you have found this library useful, please consider citing the following:

Wang, Y. P., Walters, A. C., Bazan da Silva, M., *et al*., PGMweb: An Online Simulation Tool for Plane Grating Monochromators, *In Preparation*.

A web based version of this library with a GUI is also available on the [Diamond server][1].

[1]:https://pgmtool.diamond.ac.uk
