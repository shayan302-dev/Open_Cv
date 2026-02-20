import cv2

image = cv2.imread('Image drawing function/tiger_image.jpg')

if image is None:
    print("Image could no be loaded ")

else:
    print('Image Loaded Successfully')
    print('Image shape:', image.shape)
    
    # pt1 is the center point of the circle (x=91, y=92)
    pt1 = (91, 92)
    
    # pt2 defines the radius of the circle (in pixels)
    pt2 = 50
    
    # Color of the circle (in BGR format)
    # This is red: B=0, G=0, R=255
    color = (0, 0, 255)
    
    # Thickness of the circle line
    # Use -1 for filled circle, or positive number for outline only
    thickness = 3
    
    # Draw the circle on the image using cv2.circle()
    # Parameters: image, center point, radius, color, thickness
    cv2.circle(image, pt1, pt2, color, thickness)
    
    # Show the image with circle in a window
    cv2.imshow('Circle Drawing', image)
    
    # Wait for user to press a key
    cv2.waitKey(0)
    
    # Close all windows
    cv2.destroyAllWindows()
    