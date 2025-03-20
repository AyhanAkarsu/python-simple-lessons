import cv2

def increase_image_quality(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Apply Gaussian Blur to the image
    image = cv2.GaussianBlur(image, (5, 5), 0)

    # Increase the resolution of the image by 2x using bicubic interpolation
    height, width = image.shape[:2]
    image = cv2.resize(image, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

    # Save the processed image
    cv2.imwrite("improved_quality_image.jpg", image)

    return "improved_quality_image.jpg"

# Example usage

# Path to the image
image_path = "C:/Users/Ayhan/Desktop/IMG_20210908_145318.jpg"

# Call the function
result = increase_image_quality(image_path)

print("Improved image saved at:", result)
