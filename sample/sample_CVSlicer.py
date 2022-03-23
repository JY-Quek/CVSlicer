import cvslicer
import numpy as np
import cv2

# Any Object Detection function that gives you the coordinates of contours
def object_detection_function(input_img):
    edged = cv2.Canny(input_img, 30, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours
  
if __name__ == "__main__":
    '''
    Part 1: Load the Image & Specify our specifications
    '''
    img_path = ".\img\sample500x500.png"
    
    # 100, 100: Image CutOff Height and Width
    # 40, 40: Object Maximum Height and Width
    img_slicer = cvslicer.CVSlicer(img_path, 100, 100, 40, 40)  
    
    '''
    Part 2: Use your image algorithm on each of the sliced images. After that convert the coordinates you got from the sliced images to the original coordinates on the original image by shifting x and y coordiantes.
    - Here our image algorithm is represented by the function object_detection_function which will gives the contour cooridnates as output
    '''
    adjusted_contours = []
    for output_img in img_slicer.slice_img(): 
    # .slice_img() gives you a 2D array with the below elements 
    # [ image file path, [x-coordinate to shift, y-coordinate to shift]  ]
        img_loaded = cv2.imread(output_img[0])
        contours = object_detection_function(img_loaded)
        for ctn in contours:
            for points in ctn:
                coordinates = points[0]
                
                x_coordinate = coordinates[0]
                y_coordinate = coordinates[1]
                
                x_adjustment = output_img[1][0] # x-coordinate to shift
                y_adjustment = output_img[1][1] # y-coordinate to shift
                
                adjusted_coordinates = [x_coordinate+x_adjustment, y_coordinate+y_adjustment]
                adjusted_contours.append([adjusted_coordinates])
    
    # Convert back to numpy array    
    adjusted_contours = np.array(adjusted_contours).astype('int32')
    
    '''
    Part 3: Use the coorinates we obtained in Part 2 and put them to use
    '''
    # Show the results
    try:
        # Draw and show
        image = cv2.imread(img_path)
        cv2.drawContours(image, adjusted_contours, -1, (255, 255, 0), 3)
        cv2.imshow('Contours', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        # If image exceeds OPENCV limit
        print("-- Your Original image is too large for OpenCV to draw the contours on. --")
        print("Coordinates for the contours: \n")
        print(adjusted_contours)