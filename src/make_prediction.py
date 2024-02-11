import tensorflow as tf
import numpy as np
from tensorflow import keras
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
# Load the trained model
model_path = r'D:\BSCS\CS7\FYP\modelcode\TrainedModels\cnnNotTrained\accuracy90%'
model = keras.models.load_model(model_path)

# Map class indices to class names if available
class_names = ['glioma', 'meningioma', 'no', 'pituitary']
def predict(img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch
    predictions = model.predict (img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
#     confidence = round(np.max(predictions[0]),2)
    confidence = round(100*(np.max(predictions[0])),2)

    return predicted_class, confidence



def display_image(image_array):
    plt.imshow(image_array)
    plt.axis('off')  # Hide axes
    plt.show()

def process_image(uploaded_file):
    # Perform tumor detection using the loaded model
    img = Image.open(uploaded_file).convert('RGB')
    img = img.resize((256, 256))  # Adjust the size if needed

    # Convert the image to a numpy array
    img_array = np.array(img)
    # display_image(img_array)
    return img_array

