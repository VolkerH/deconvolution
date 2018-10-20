'''
test on fft and ifft for image
'''
import numpy as np
import skimage.external.tifffile as tf
from matplotlib import pyplot as plt


def fft_result(image):
    image_fft = np.fft.fftn(image)

    return image_fft

def fft_mask(image_fft):
    image_fft_trans = np.fft.fftshift(image_fft)
    #plt.imshow(converted_fft, vmin= , vmax= .)

def ifft_result(image_fft):
    image_restore = np.fft.ifftn(image_fft)

    return np.array(image_restore.real, dtype = np.uint16)

# in the fft_mask part, could manually tune the fft_mask to remove artifical effects.
