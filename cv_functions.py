import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------
# load drone images into workspace and display one of them 
def load_drone_imgs(directory, files):
  imgs = []
  for file in files:
    if file.endswith('.JPG'):
      img_path = os.path.join(directory, file)
      img = cv2.imread(img_path)  # Load image in BGR format
      if img is None:
        print(f"Failed to load image: {img_path}")
      else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        imgs.append(img)

  if len(imgs) == 0:
    print("No images loaded.")
    return None
  else:
    # Convert the list of images to numpy array for easier manipulation
    imgs = np.array(imgs)

    # Check the shape of the loaded images array
    print("Shape of loaded images array:", imgs.shape)

    # Display the first image
    if len(imgs) > 0:
      plt.imshow(imgs[0])
      plt.axis('off')  # Hide axis
      plt.show()
    
    return imgs

# --------------------------------------------------------
