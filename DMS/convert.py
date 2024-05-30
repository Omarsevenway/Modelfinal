import keras
import tensorflow as tf


model = keras.models.load_model("C:/Users/aymane/Desktop/DMS/full_model.keras")


converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()


with open('model.tflite', 'wb') as f:
    f.write(tflite_model)

print("Model converted to TensorFlow Lite and saved successfully.")