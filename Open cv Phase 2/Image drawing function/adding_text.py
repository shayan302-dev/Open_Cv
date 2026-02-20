import cv2

image = cv2.imread('Image drawing function/tiger_image.jpg')

if image is None:
    print('Image could not be loaded')

else:
    print('Image Loaded Successfully')

    # Define the text to write on the image
    text = 'this is tiger'
    
    # Define the position where text will be placed (x=30, y=50)
    pt1 = (30, 50)
    
    # Choose the font for the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # Set the size of the text
    fontScale = 1
    
    # Color of the text in BGR format
    # White color: B=255, G=255, R=255
    color = (255, 255, 255)
    
    # Thickness of the text strokes
    thickness = 2
    
    # Put text on the image
    cv2.putText(image, text, pt1, font, fontScale, color, thickness)
    
    # Show the image with text in a window
    cv2.imshow('Text on Image', image)
    
    # Wait for user to press a key
    cv2.waitKey(0)
    
    # Close all windows
    cv2.destroyAllWindows()