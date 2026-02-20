import cv2

image = cv2.imread('Image drawing function/tiger_image.jpg')
print(image.shape)

if image is None:
    print('Could not load the image')

else:
    print('Image Loaded Successfully')

    # pt1 = (50, 50)
    # pt2 = (150, 150)
    # color = (0,0,255)
    # thickness = 3
    cv2.rectangle(image,  pt1=(50, 30), pt2=(200, 150), color=(0,0,255), thickness=3)
    cv2.imshow('tiger image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()