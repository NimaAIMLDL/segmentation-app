"""Michael Bauer Werkhof e.V., Schulze-Delitzsch-Straße, 70565 Stuttgart (160 Module)"""

import cv2
import numpy as np
import glob
import math

pix_treshold = 155

def sollar_cell_pixel_counter(pred_img_np):
	counter = 0		
	for i in range(pred_img_np.shape[0]): # (255,255,3)
		for j in range(255):
			if (pred_img_np[i,j,0]> pix_treshold): # assuming all 3 channels are always equall
				counter = counter + 1
				#print(counter)
			else:
				pass
	return counter

