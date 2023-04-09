# Importing necessary libraries
import cv2
import numpy as np 
import pickle

# Loading list of parking space coordinates from a pickle file
with open('car_park_pos', 'rb') as f:
        pos_list = pickle.load(f)

# Dimensions of each parking space
width, height = 27, 15

# Function to check the status of each parking space in the given frame
def check_parking_space(img):
    free_spaces = 0

    # Looping through each parking space coordinate
    for pos in pos_list:
        # Cropping the image to get only the parking space area
        img_crop = img[pos[1]:pos[1] + height, pos[0]:pos[0] + width]                       
        count = cv2.countNonZero(img_crop)

        if count > 110:
            color = (0, 0, 255)
       
        else:
            free_spaces += 1
            color = (0, 255, 0)

        # Drawing a rectangle around the parking space and displaying the count of non-zero pixels inside it
        cv2.rectangle(frame, pos, (pos[0] + width, pos[1] + height), color, 1)
        cv2.putText(frame, str(count), (pos[0], pos[1] + height - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, color, 1)

    # Displaying the total number of free parking spaces out of the total number of parking spaces
    cv2.putText(frame, f'{free_spaces} / {len(pos_list)}', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 3)


cap = cv2.VideoCapture("busy_parking_lot.mp4")

# Getting the dimensions of the video frame
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 30

# Setting up the video writer to write the processed video to a file
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # mp4 codec
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while 1:
        # Reading a frame from the video capture
        ret, frame = cap.read()

        # Converting the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Blurring the grayscale frame using a Gaussian filter
        blurred_frame = cv2.GaussianBlur(gray_frame, (3,3), 1)

        # Applying adaptive thresholding to the blurred frame to binarize it
        threshold_frame = cv2.adaptiveThreshold(blurred_frame, 255,
                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                                cv2.THRESH_BINARY_INV, 25, 16)

        # Applying median filtering to the thresholded frame to remove noise
        frame_median = cv2.medianBlur(threshold_frame, 5)

        # Dilating the filtered frame to fill in gaps in the parking space boundaries
        kernel = np.ones((5, 5), np.uint8)
        dilated_frame = cv2.dilate(frame_median, kernel, iterations=1)
        
        check_parking_space(dilated_frame)

        cv2.imshow('frame', frame)

        if cv2.waitKey(20) & 0xFF == ord("q"):
               break

cap.release()
out.release()
cv2.destroyAllWindows()