import cv2
import numpy as np

# Load the image from the file
image = cv2.imread('image drawing function/tiger_image.jpg')

# Check if the image loaded properly
if image is None:
    print('Image could not be loaded')

else:
    print('Image loaded successfully')

    # Create three points for the triangle
    # First point: x=100, y=50
    # Second point: x=250, y=200  
    # Third point: x=50, y=200
    pts = np.array([[100, 50], [250, 200], [50, 200]], np.int32)
    
    # Reshape the points in the format needed for drawing
    pts = pts.reshape((-1, 1, 2))
    
    # Set the color of the triangle (in BGR format - Blue, Green, Red)
    # This is green color: B=0, G=255, R=0
    color = (0, 255, 0)
    
    # Set how thick the line of triangle should be (in pixels)
    thickness = 3
    
    # Draw the triangle on the image
    # isClosed=True means connect the last point back to the first point
    cv2.polylines(image, [pts], isClosed=True, color=color, thickness=thickness)

    # Show the image with triangle in a window
    cv2.imshow('Triangle Drawing', image)
    
    # Wait for the user to press a key
    cv2.waitKey(0)
    
    # Close the image window
    cv2.destroyAllWindows()
