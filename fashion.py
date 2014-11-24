import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import cv2


image_name = 'black.jpg'

#creates 3d histogram of image and plots to screen
def create_lab_hist(image_name):
    
    image = cv2.imread(image_name)
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    hist = cv2.calcHist([lab_image], [1, 2], None, [8, 8], [0, 256, 0, 256])
    return hist

#creates proper x and y floor values for 3d histogram to user later
def create_3d_floor(histogram):
    x_data, y_data = np.meshgrid( np.arange(histogram.shape[1]),np.arange(histogram.shape[0]) )
    return (x_data, y_data)

#searches np array of arrays and finds top k valued indexes, and returns list of indexes
#TODO figure out way that doesnt alter data structure passed in
def find_top_val_postitions(hist, k=4):
    new_struct = np.copy(hist)
    indices_list = []
    for index in range(k):
        i,j = np.unravel_index(new_struct.argmax(), new_struct.shape)
        indices_list.append((i,j))
        new_struct[i,j] = 0
    return indices_list

#computes distance between two images based off of the 4 most dominant bins in their a and b LAB histograms
def compute_distance(image_name_1, image_name_2):
    distance = 0
    hist1 = create_lab_hist(image_name_1)
    hist2 = create_lab_hist(image_name_2)
    top_indexes_1 = find_top_val_postitions(hist1, 4)
    top_indexes_2 = find_top_val_postitions(hist2, 4)
    return distance

#takes in two images and plots their 3d lab histograms side by side
def create_3d_hist_plots(image_name_1, image_name_2):
    
    fig = plt.figure()
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122, projection='3d')
    
    if not os.path.exists(image_name_1):
        raise Exception("Image:" , image_name_1 , "cannot be found, please enter valid image")
    if not os.path.exists(image_name_2):
        raise Exception("Image:" , image_name_2 , "cannot be found, please enter valid image")
    
    lab_hist_1 = create_lab_hist(image_name_1)
    lab_hist_2 = create_lab_hist(image_name_2)
    image_1 = cv2.imread(image_name_1)
    image_2 = cv2.imread(image_name_2)
    
    x_data_1, y_data_1 = create_3d_floor(lab_hist_1)
    x_data_2, y_data_2 = create_3d_floor(lab_hist_2)
    x_data_1 = x_data_1.flatten(); y_data_1 = y_data_1.flatten(); z_data_1 = lab_hist_1.flatten()
    x_data_2 = x_data_2.flatten(); y_data_2 = y_data_2.flatten(); z_data_2 = lab_hist_2.flatten()
    
    ax1.bar3d( x_data_1,y_data_1,np.zeros(len(z_data_1)),1, 1, z_data )
    ax2.bar3d( x_data,y_data,np.zeros(len(z_data)),1, 1, z_data )
    plt.show()

def print_lab_values(image_name):
    
    image = cv2.imread(image_name)
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l_channel,a_channel,b_channel = cv2.split(lab_image)
    
    # Print the minimum and maximum of lightness.
    print "Min of L channel: " + str(np.min(l_channel)) 
    print "Max of L channel: " + str(np.max(l_channel)) 

    # Print the minimum and maximum of a.
    print "Min of a channel: " + str(np.min(a_channel)) 
    print "Max of a channel: " + str(np.max(a_channel)) 

    # Print the minimum and maximum of b.
    print "Min of b channel: " + str(np.min(b_channel)) 
    print "Max of b channel: " + str(np.max(b_channel)) 

def db():
    import pdb
    pdb.set_trace()

