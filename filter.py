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

    #iterate over the directory for images
    for filename in os.listdir(directory_path):
        #TODO: find out what the image format is
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            image = cv.imread(os.path.join(directory_path, filename), 0)
            if check_img(image):
                #this image has passed the check and can be moved to the usable directory 
                os.rename(os.path.join(directory_path, filename),
                          os.path.join(usable_dir_path, filename))
            else:
                #this image is not usable, and therefore must be moved
                os.rename(os.path.join(directory_path, filename),
                          os.path.join(unusable_dir_path, filename))
    
    #iterate over the directory for videos
    for filename in os.listdir(directory_path):
        if filename.endswith(".mp4"):
            cap = cv.VideoCapture(os.path.join(directory_path, filename))
            frame_count = cap.get(7) # i think 7 is the correct property id TODO: verify this
            cap.set(1, 0)
            ret, first_frame = cap.read()
            cap.set(1, frame_count/2)
            ret, middle_frame = cap.read()
            cap.set(1, frame_count - 1)
            ret, last_frame = cap.read()
            video_usable = check_img(first_frame) and check_img(middle_frame) and check_img(last_frame)
            if video_usable:
                #this image has passed the check and can be moved to the usable directory 
                os.rename(os.path.join(directory_path, filename),
                          os.path.join(usable_dir_path, filename))
            else:
                #this image is not usable, and therefore must be moved
                os.rename(os.path.join(directory_path, filename),
                          os.path.join(unusable_dir_path, filename))

                

def check_img(image): #this image check function is incomplete TODO: implement further image scrutiny
    
    if cv.countNonZero(image) == 0:
        #this image is all black 
        return False
    elif np.mean(image) == 255: #the average can only be 255 if all the pixels are white
        #this image is all white
        return False
    #validate the image using opencv to see if the image is completely white or black

    #to determine if the image is blurry see it it is a gaussian blur or laplacian blur
    return True



if __name__ == "__main__":
    main()
