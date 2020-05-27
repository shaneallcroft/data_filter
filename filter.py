#usage "filter [directory path] 1" where [directory path] is replaced by the path of the directory you want to iterate over

import cv2 as cv
import sys
import os


def main():
    # set up the necessary directories/ housekeeping stuff
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
            else:
                continue #while the image is not black, we cannot sufficiently place it in the usable directory
    #validate the image using opencv to see if the image is completely white or black

    #to determine if the image is blurry see it it is a gaussian blur or laplacian blur






if __name__ == "__main__":
    main()
