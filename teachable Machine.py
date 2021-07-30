import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# load label file
label_file = open('labels.txt','r')
list_labels = []
for line in label_file:
    line1 = line.strip()
    list_labels.append(line1)
label_file.close()

print(list_labels)
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
#image = Image.open('test_photo.jpg')

cap = cv2.VideoCapture(0)
while (True):
    ret, image1 = cap.read()

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    #size = (224, 224)
    #image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image = cv2.resize(image1,(224,224))
    #turn the image into a numpy array
    image_array = np.asarray(image)

    # display the resized image
    #image.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    #print(prediction)
    index = np.argmax(prediction)
    print(index)
    cv2.putText(image,str(list_labels[index]),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow('image',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()