# Import the OpenCV library for image processing
import cv2

# Read the image from the specified file path and store it in the 'image' variable
# The image is loaded as a NumPy array with BGR color format
image = cv2.imread('Image Resizing & Shaping/tiger_image.jpg')

# Check if the image was successfully loaded (not None)
if image is not None:
    # Crop the image using array slicing: [rows_start:rows_end, cols_start:cols_end]
    # This extracts pixels from row 100 to 200 and column 50 to 150
    # NumPy array slicing works on rows first (height), then columns (width)
    cropped = image[100:200 , 50:150]
    
    # Display the original image in a window titled 'Original Image'
    cv2.imshow('Original Image', image)
    
    # Display the cropped image in a window titled 'Cropped'
    cv2.imshow("Cropped", cropped)
    
    # Wait indefinitely for a key press (0 means wait forever until a key is pressed)
    cv2.waitKey(0)
    
    # Close all the image display windows that were created
    cv2.destroyAllWindows()
else:
    # If the image file could not be found or loaded, print an error message
    print('image not found')