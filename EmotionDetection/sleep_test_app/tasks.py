from django.conf import settings
from PIL import Image
import os
import numpy as np
from tensorflow.keras.models import load_model




def Classfiy_Image(image_path):
    model_path = os.path.join(settings.BASE_DIR, 'models/model.h5')
    model = load_model(model_path ,  compile=False  )
    # print( '-------------------/-----------------------------------', model_path)
    img = Image.open(image_path)
    resized_frame_rgb = img.resize((256, 256)).convert('RGB')
    image_array = np.array(resized_frame_rgb) / 255.0
    image_array_expanded = np.expand_dims(image_array, axis=0)

    # Explicitly set the loss function to 'binary_crossentropy'
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    prediction = model.predict(image_array_expanded)

    if prediction > 0.5:
        result = "Sad Face"
    else:
        result = "Happy Face"

    return result

# print(Classfiy_Image(r"C:\Users\youss\OneDrive\Pictures\Screenshots 1\Screenshot 2024-05-05 201125.png"))


