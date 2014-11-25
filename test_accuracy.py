import os
from ImageHistogram import ImageHistogram
import cv2

#creates histograms of images in test folder and saves each to disk through cpickle
valid_image_extensions = ['.jpg', '.jpeg', '.png']


class TestImage:

    def __init__(self, image_name,hist, color):
        self.image_name = image_name
        self.hist = hist
        self.color = color

#runs through folders in test_folder and creates TestImage objects for each, saving them to disk with cpickle
#format for finding color: test_folder/COLOR/image_name.extension
def save_histograms_to_disk(test_folder="testimages", cpickle_file = "testimages.pickle"):
    
    test_images_list = []
    image_hist = ImageHistogram()
    #find all images in test folder
    for root, directories, filenames in os.walk(test_folder):

        for filename in filenames: 
            file_path = os.path.join(root,filename)
            file_base, file_extension = os.path.splitext(file_path)

            #if file and valid extension and isn't mask:
            if file_extension in valid_image_extensions and "mask" not in file_path:

                mask_name = file_base + "_MASK.png" 
                mask = cv2.imread(mask_name, 0)
                hist = image_hist.create_hist(file_path, mask=mask)
                color = file_base.split("/")[-2]
                test_images_list.append(TestImage(file_path, hist, color))
    import pdb; pdb.set_trace()
    #save test_image objects to disk


