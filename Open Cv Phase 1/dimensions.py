import cv2
image = cv2.imread('python_logo.jpg')

if image is not None:
    height, width, channel = image.shape
    print(f'Image Loaded: \n Height: {height} \n Width: {width} \n Channel: {channel}')

else:
    print('could not load image')