import numpy as np
import cv2

img = cv2.imread('/Volumes/My Passport/wdrface/WDR_face_dataset/WDR_tiff/scene1/01/Scene1_One-Face0.tif', flags=cv2.IMREAD_ANYDEPTH)
print(np.min(img), np.max(img))
img = np.expand_dims(img, axis=2)
img = np.concatenate([img, img, img], axis=2)
print(img.shape)
tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
ldrDrago = tonemapDrago.process(img)
ldrDrago = 3 * ldrDrago
cv2.imwrite("ldr-Drago.jpg", ldrDrago * 255)
