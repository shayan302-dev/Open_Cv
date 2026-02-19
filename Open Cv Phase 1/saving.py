import cv2
image = cv2.imread('python_logo.jpg')
# for saving the edited image or image we can use imwrite(image_name_you_want_to_store, image_var_in_which_image_is_stored)

if image is not None:
    success = cv2.imwrite('output.jpg', image)
    if success:
        print('Image is saved successfully as "output.jpg"')
    else:
        print('Failed to saved an image')

else:
    print('Error: Could not load the image')
    
