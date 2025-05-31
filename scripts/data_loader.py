 
import tensorflow as tf
import tensorflow_datasets as tfds

#   تحميل بيانات الأزهار
dataset_name = "tf_flowers"
(train_data, test_data), dataset_info = tfds.load(
    dataset_name, split=["train[:80%]", "train[80%:]"], as_supervised=True, with_info=True
)

#   تجهيز البيانات
def preprocess_image(image, label):
    image = tf.image.resize(image, (224, 224)) / 255.0
    return image, label

train_data = train_data.map(preprocess_image).batch(32).shuffle(1000)
test_data = test_data.map(preprocess_image).batch(32)

print("✅ تم تحميل البيانات ومعالجتها بنجاح!")
