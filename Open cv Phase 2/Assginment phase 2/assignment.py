import cv2

# 1️⃣ Take image path from user
image_path = input("Enter image path: ")

image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

print("\nChoose an option:")
print("1 - Draw Line")
print("2 - Draw Circle")
print("3 - Draw Rectangle")
print("4 - Write Text")

choice = input("Enter your choice (1/2/3/4): ")

# 2️⃣ Draw Line
if choice == "1":
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 3️⃣ Draw Circle
elif choice == "2":
    x = int(input("Enter center x: "))
    y = int(input("Enter center y: "))
    radius = int(input("Enter radius: "))

    cv2.circle(image, (x, y), radius, (255, 0, 0), 2)

# 4️⃣ Draw Rectangle
elif choice == "3":
    x1 = int(input("Enter top-left x: "))
    y1 = int(input("Enter top-left y: "))
    x2 = int(input("Enter bottom-right x: "))
    y2 = int(input("Enter bottom-right y: "))

    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 5️⃣ Write Text
elif choice == "4":
    text = input("Enter text: ")
    x = int(input("Enter x position: "))
    y = int(input("Enter y position: "))

    cv2.putText(image, text, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2)

else:
    print("Invalid choice")
    exit()

# Show result
cv2.imshow("Modified Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6️⃣ Ask to save
save = input("Do you want to save the image? (yes/no): ")

if save.lower() == "yes":
    cv2.imwrite("assignment_tiger_image.png", image)
    print("Image saved as assignment_tiger_image.png")