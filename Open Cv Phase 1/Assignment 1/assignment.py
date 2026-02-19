import cv2

# 1️⃣ Take image path from user
path = input("Enter image path: ")

# 2️⃣ Load image
image = cv2.imread(path)

if image is None:
    print("Could not load the image.")
else:
    # 3️⃣ Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 4️⃣ Ask user what to do
    choice = input("Type 'show' to display image or 'save' to save image: ").lower()

    if choice == "show":
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "save":
        filename = input("Enter name to save image (example: output.jpg): ")
        cv2.imwrite(filename, gray)
        print("Image saved successfully.")

    else:
        print("Invalid option.")