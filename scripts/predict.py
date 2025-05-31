import tensorflow as tf
import numpy as np
from PIL import Image
import json
import sys

# تحميل النموذج المدرب
model_path = "../models/model_final.h5"
model = tf.keras.models.load_model(model_path)

# تحميل تصنيفات الأنواع
label_map_path = "../data/label_map.json"
with open(label_map_path, "r") as file:
    label_map = json.load(file)

def predict_image(image_path):
    image = Image.open(image_path).resize((224, 224))
    img_array = np.expand_dims(np.array(image) / 255.0, axis=0)
    
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)

    return label_map[str(predicted_class)]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ الرجاء إدخال مسار الصورة.")
    else:
        image_path = sys.argv[1]
        print("🚀 التصنيف:", predict_image(image_path))
