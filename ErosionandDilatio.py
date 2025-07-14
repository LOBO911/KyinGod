import cv2
import numpy as np

# Original image (binary)
A = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,0,0,0,0,0,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,0,0,0,0,0,1,1,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    
], dtype=np.uint8)

# Structuring element
B = np.array([
    [0,1,0],
    [1,1,1],
    [0,1,0]
], dtype=np.uint8)

# Apply Opening
opening = cv2.morphologyEx(A, cv2.MORPH_OPEN, B)

# Apply Closing
closing = cv2.morphologyEx(A, cv2.MORPH_CLOSE, B)

print("Opening:\n", opening)
print("Closing:\n", closing)
