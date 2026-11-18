import numpy as np

# Creating an image as a matrix
image = np.array([
    [50, 100, 150],
    [100, 150, 200],
    [150, 200, 250]
])

print("Original Image:")
print(image)

# 1. Reshaping the image
reshaped = image.reshape(1, 9)
print("\nReshaped Image:")
print(reshaped)

# 2. Slicing a specific region
sliced = image[0:2, 0:2]
print("\nSliced Image:")
print(sliced)

# 3. Brightness adjustment using broadcasting
bright = image + 30
bright = np.clip(bright, 0, 255)
print("\nBrightness Adjusted Image:")
print(bright)

# 4. Matrix multiplication for transformation
transform = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

result = np.dot(image, transform)
print("\nTransformed Image:")
print(result)