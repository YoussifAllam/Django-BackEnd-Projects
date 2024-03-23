import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.conf import settings
import os
from PIL import Image as PilImage
import io


model_path = os.path.join(settings.BASE_DIR, 'models/model_Ar_Signal.h5')
model = load_model(model_path)

def load_and_prepare_image(image_field):
    img_bytes = image_field.read()
    img = PilImage.open(io.BytesIO(img_bytes))
    img = img.resize((128, 128))
    img = img.convert('RGB')  
    img_array = np.asarray(img) / 255.0  
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array


# Predict the class of an image
def classify_image(image_path):
    img = load_and_prepare_image(image_path)
    prediction = model.predict(img)
    class_id = np.argmax(prediction, axis=1)[0]
    return class_id  # Or map this ID to a class name if you have a mapping available

# Example usage
# image_path = r"D:\Graduate Dtaset\ArASL_Database_54K_Final\nun\Nun (51).JPG"    
# class_id = predict_image_class(image_path)
# print(f'Class ID of the image: {class_id}')


