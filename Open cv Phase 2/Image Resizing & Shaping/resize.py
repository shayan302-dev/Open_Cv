import cv2
image = cv2.imread("Image Resizing & Shaping/tiger_image.jpg")

if image is None:
    print('Image Not found')
else:
    print('Image Loaded')
    # first width than height
    resized = cv2.resize(image, (300,300))

    cv2.imshow("Original Image", image)
    cv2.imshow('Resized Image', resized)

    cv2.imwrite('resized_output.png', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
