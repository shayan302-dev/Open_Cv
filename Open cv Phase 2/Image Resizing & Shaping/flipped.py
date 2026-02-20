# Import the OpenCV library for image processing and manipulation
import cv2

# Load an image from the specified file path and store it as a NumPy array
# The image is loaded in BGR color format (Blue, Green, Red) by default
image = cv2.imread('Image Resizing & Shaping/tiger_image.jpg')

# Check if the image was successfully loaded (returns None if file not found or cannot be read)
if image is None:
    # Display an error message if the image file could not be loaded
    print('Could not load the image')

else:
    # Flip the image horizontally (left-right flip)
    # cv2.flip() parameters: (image, flipCode)
    # flipCode = 1: flip horizontally around the vertical axis
    flipped_horizontal = cv2.flip(image, 1)
    
    # Flip the image vertically (top-bottom flip)
    # flipCode = 0: flip vertically around the horizontal axis
    flipped_vertical = cv2.flip(image, 0) 
    
    # Flip the image both horizontally and vertically (180 degree rotation)
    # flipCode = -1: flip both horizontally and vertically
    flipped_both = cv2.flip(image, -1)

    # Display the original image in a window titled 'Original'
    cv2.imshow("Original", image)
    
    # Display the horizontally flipped image in a window
    cv2.imshow('Flipped Horizontal', flipped_horizontal)
    
    # Display the vertically flipped image in a window
    cv2.imshow('Flipped Vertical', flipped_vertical)
    
    # Display the image flipped both horizontally and vertically in a window
    cv2.imshow('Flipped Both Horizontal and vertical', flipped_both)

    # Wait indefinitely for a key press (0 means wait until a key is pressed)
    cv2.waitKey(0)
    
    # Close all opened image display windows
    cv2.destroyAllWindows() 