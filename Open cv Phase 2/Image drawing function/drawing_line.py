import cv2
# Import OpenCV library for image processing

# Load an image from file
image = cv2.imread('image drawing function/tiger_image.jpg')
# print(image.shape)

# Check if image loaded successfully
if image is None:
    print('Your image is not working')

# If image is loaded, proceed with drawing
else:
    print('Image Loaded Successfully')

    # Define starting point of the line (x=50, y=100)
    pt1 = (50, 100)
    # Define ending point of the line (x=180, y=100)
    pt2 = (180, 100)
    # Define color in BGR format: (Blue=255, Green=0, Red=0) = BLUE
    color = (255,0,0)
    # Set line thickness in pixels
    thickness = 4

    # Draw a line from pt1 to pt2 with specified color and thickness
    cv2.line(image, pt1, pt2, color, thickness)

    # Display the image with the drawn line
    cv2.imshow('Line Drawing', image)
    # Wait for any key press (0 = wait indefinitely)
    cv2.waitKey(0)
    # Close all display windows
    cv2.destroyAllWindows()