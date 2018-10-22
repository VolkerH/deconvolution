"""
pipeline for normal psf deconvolution, with known or measured psf:
1. determine the psf in 3d or 2d. this would determine whether if the method could be applicable to 3d or 2d. following is based on 3d algorithm
2. fit or mimic the 3d pdf from experimental result;
3. use the psf, and 3d stack images, to deconvolute each plane. for 3d, the deconvoluted plane procedure will differ by using a different order of zstack.
4. got the deconvoluted result
"""
