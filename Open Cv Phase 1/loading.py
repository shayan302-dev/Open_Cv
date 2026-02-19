import cv2
# Loading the image or reading the image
image = cv2.imread('python_logo.jpg')

if image is not None:
    # print('Error: Image not found')
    cv2.imshow("python_logo_image", image) #  open the window
    cv2.waitKey(0) # wait for key
    cv2.destroyAllWindows() # close the window
else:
    print('Image loaded successfully')

# displaying the image
# so we have three functions to display the image 
# 1. imshow()
# 2. waitKey()
# 3. destroyAllWindows()

#imshow()
# it is a function which open the window in your machine  and show the image which you load if you want to run the function so it is neccessary you have to use the waitKey() it is for pausing the window and than destroyAllWindows() help us the successfully close the window 

# for saving the edited image or image we can use imwrite(image_name_you_want_to_store, image_var_in_which_image_is_stored)
cv2.imwrite('output.jpg', image)