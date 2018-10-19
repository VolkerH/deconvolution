'''
test on fft and ifft for image
'''
'''
command groups:
1) 

'''





import numpy as np

def fft_result(image):
    xd, yd = image.shape
    fft_value = np.fft.fft2(image)
    return fft_value, xd, yd

def ifft_result(fft_image):
