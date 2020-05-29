#usage "filter [directory path]" where [directory path] is replaced by the path of the directory you want to iterate over

import cv2 as cv
import sys
import os
import numpy as np

def main():
    # set up the necessary directories/ housekeeping stuff

    #debugging for shane
    print("argc: ")
    print(sys.argc)
    if sys.argc != 2:
        print("Usage: python")

    directory_path = sys.argv[1]
    usable_dir_path = os.path.join(directory_path + "usable_data") #using os.path.join so the trailing / doesn't matter 
    unusable_dir_path = os.path.join(directory_path + "unusable_data")
    os.mkdir(usable_dir_path)
    os.mkdir(unusable_dir_path)
    #make sure the amount of images and videos are above 50%

    #iterate over the directory
    for filename in os.listdir(directory_path):
        #TODO: find out what the image format is
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            image = cv.imread(directory_path + filename, 0)
            if cv.countNonZero(image) == 0:
                #this image is all black and not usable, and therefore must be moved
                os.rename(directory_path + filename, unusable_dir_path + filename)
            elif np.mean(image) == 255: #the average can only be 255 if all the pixels are white
                #this image is all white and not usable, so it must be moved to the unusable directory
                os.rename(directory_path + filename, unusable_dir_path + filename)
            else:
                continue #we can't say its usable quite yet
            








            
    #validate the image using opencv to see if the image is completely white or black

    #to determine if the image is blurry see it it is a gaussian blur or laplacian blur






if __name__ == "__main__":
    main()
