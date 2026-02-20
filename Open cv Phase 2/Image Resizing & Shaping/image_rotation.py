# Import the OpenCV library for image processing
import cv2 

# Load the image from the specified file path
# The image is returned as a NumPy array in BGR color format
image = cv2.imread('Image Resizing & Shaping/tiger_image.jpg')

# Check if the image was successfully loaded
if image is None:
    # Print error message if the image file could not be found or loaded
    print('could not load the image')

else:
    # Get the height and width of the image from its shape attribute
    # image.shape returns (height, width, channels) for color images
    # [:2] extracts only the height and width, ignoring the number of channels
    (h, w) = image.shape[:2]

    # Calculate the center point of the image
    # Center coordinates are (width/2, height/2)
    # Using integer division (//) to get pixel coordinates
    center = (w//2, h//2)
    
    # Create a rotation matrix for rotating the image 90 degrees around its center
    # cv2.getRotationMatrix2D parameters:
    #   - center: the point of rotation (x, y)
    #   - 90: rotation angle in degrees (counter-clockwise for positive values)
    #   - 1.0: scaling factor (1.0 means no scaling, size remains the same)
    # Returns a 2x3 affine transformation matrix
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    
    # Apply the rotation transformation to the image
    # cv2.warpAffine parameters:
    #   - image: the source image
    #   - M: the 2x3 transformation matrix
    #   - (w, h): the output image size (same as original)
    rotated = cv2.warpAffine(image, M, (w, h))

    # Display the original image in a window
    cv2.imshow('original Image', image)
    
    # Display the rotated image in a separate window
    cv2.imshow('Rotated 90 degree' , rotated)

    # Wait indefinitely for a key press (0 means wait until user presses a key)
    cv2.waitKey(0)
    
    # Close all image display windows
    cv2.destroyAllWindows()

