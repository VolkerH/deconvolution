"""
This function generate the point-spread function for a widefield microscope using a scalar diffraction-limited model (Stokseth refer to [1] and [3] below)
----------------
Input parameters:
lambdaEx: Excitation Wavelength (in nm)
lambdaEm: Emission wavelegnth (in nm)
numAper: Numerical aperture of the objective
magObj: Objective total magnification
rindexObj: Refractive index of the objective immersion medium
ccdSize: Pixel dimension of the CCD (in the plane of the camera)
rindex_sp: Refractive index of the specimen medium
xysize: Size of the desired image (specimen view size/pixel dimension)
nslices: Number of slices desired (Depth view/Z axis sampling)
depth: depth of the specimen under the cover-slip in nm
dxy: CCD pixel size (in nm)
dz: Optical axis Z sampling or defocusing (in nm)
nor: Normalization on the PSF (default: no normalization)
0: L-infinity normalization
1: L-1 normalization
-------------
Example usage:
Note that for large z sections, the algorithms speed is dependent on the 2D fFTs
Without spherical aberration, and normalized to l-infinity:
Microscope objective: 63X/1.4, oil immersion
CCD camera pixel size: 6.45 microns
Fluorophore is GFP and excited in blue
>> psf = wfmpsf(488, 520, 1.4, 63, 1.518, 6450, 300, 128, 64, 1.518, 0, 0);
With spherical aberration:
Microscope objective: 63X/1.4, oil immersion
CCD camera pixel size: 6.45 microns
Specimen immersed has a buffer index of 1.45
and imaged at 15 microns in depth
Fluorophore is GFP and excited in blue
>> psf = wfmpsf(488, 520, 1.2, 40, 1.33, 6450, 300, 256, 128, 1.45, 15000, 0);
To plot the PSFs:
>> load cmap_fire;
Remove any errors due to the Fourier transform
>> psf(psf<5.7e-06) = 5.7e-06;
>> figure, imagesc(maxintensityproj(log(psfl), 1)');
>> colormap(cmap_fire); colorbar;
---------------
References:
----------
[1] P. A. Stokseth (1969). `Properties of a defocused optical system'. J. Opt. Soc. Am. A 59:1314?1321.
[2] P. Pankajakshan, et al. (2010). `Point-spread function model for fluorescence macroscopy imaging'. In Proc. of Asilomar Conference on Signals, Systems and Computers.
[3] P. Pankajakshan (2009). Blind Deconvolution for Confocal Laser Scanning Microscopy. Ph.D. thesis, Universite de Nice Sophia-Antipolis.
"""
