#usage "filter [directory path]" where [directory path] is replaced by the path of the directory you want to iterate over

import cv2 as cv
import sys
import os
import numpy as np

def main():
    # make sure that the user included a directory when calling the script
    if len(sys.argv) != 2:
        print("Usage: python [directory path]")
        quit()
    
    # set up the necessary directories/ housekeeping stuff
    directory_path = sys.argv[1]
    usable_dir_path = os.path.join(directory_path, "usable_data") #using os.path.join so the trailing / doesn't matter 
    unusable_dir_path = os.path.join(directory_path, "unusable_data")
    if not os.path.isdir(usable_dir_path):
        os.mkdir(usable_dir_path)
    if not os.path.isdir(unusable_dir_path):
        os.mkdir(unusable_dir_path)
    #make sure the amount of images and videos are above 50%

    #iterate over the directory
    for filename in os.listdir(directory_path):
        #TODO: find out what the image format is
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            image = cv.imread(os.path.join(directory_path, filename), 0)
            if cv.countNonZero(image) == 0:
                #this image is all black and not usable, and therefore must be moved
                os.rename(os.path.join(directory_path, filename),
                          os.path.join(unusable_dir_path, filename))
            elif np.mean(image) == 255: #the average can only be 255 if all the pixels are white
                #this image is all white and not usable, so it must be moved to the unusable directory
                os.rename(os.path.join(directory_path, filename),
                          os.path.join(unusable_dir_path, filename))
            else:
                continue #we can't say its usable quite yet
            








            
    #validate the image using opencv to see if the image is completely white or black

    #to determine if the image is blurry see it it is a gaussian blur or laplacian blur






if __name__ == "__main__":
    main()
