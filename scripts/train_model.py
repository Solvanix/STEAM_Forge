 
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

# 🔹 تحميل بيانات الأزهار
dataset_name = "tf_flowers"
(train_data, test_data), dataset_info = tfds.load(
    dataset_name, split=["train[:80%]", "train[80%:]"], as_supervised=True, with_info=True
)

# 🔹 تجهيز البيانات
def preprocess_image(image, label):
    image = tf.image.resize(image, (224, 224)) / 255.0
    return image, label

train_data = train_data.map(preprocess_image).batch(32).shuffle(1000)
test_data = test_data.map(preprocess_image).batch(32)

# 🔹 بناء النموذج باستخدام MobileNet
model = tf.keras.Sequential([
    hub.KerasLayer("https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5", trainable=False),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(dataset_info.features["label"].num_classes, activation="softmax")
])

# 🔹 تجميع النموذج
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# 🔹 إضافة سجل تدريبي
early_stop = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=3, restore_best_weights=True)

# 🔹 تدريب النموذج
model.fit(train_data, epochs=15, validation_data=test_data, callbacks=[early_stop])

# 🔹 حفظ النموذج في المسار الجديد
model_path = "/mnt/c/Users/ali/Desktop/STEAM_Nexus_Hub/Classification_of_flower_structure_TM1/Plant_Recognition_Lab/models/trained_model.h5"
model.save(model_path)

print(f"✅ تم حفظ النموذج المدرب في: {model_path}")
