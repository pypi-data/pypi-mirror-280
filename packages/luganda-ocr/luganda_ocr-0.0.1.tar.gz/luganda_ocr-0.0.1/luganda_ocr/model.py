import numpy as np
import os
import pandas as pd
import tensorflow as tf
import tensorflow.data as tfd
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model, load_model
from luganda_ocr.models.basepath import get_base_path
class CTCLayer(Layer):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.loss_function = tf.keras.backend.ctc_batch_cost
    def call(self, y_true, y_hat):
        batch_len = tf.cast(tf.shape(y_true)[0], dtype="int64")
        input_len = tf.cast(tf.shape(y_hat)[1], dtype='int64') * tf.ones(shape=(batch_len, 1), dtype='int64')
        label_len = tf.cast(tf.shape(y_true)[1], dtype='int64') * tf.ones(shape=(batch_len, 1), dtype='int64')
        loss = self.loss_function(y_true, y_hat, input_len, label_len)
        self.add_loss(loss)
        return y_hat

        
IMG_WIDTH = 1500
IMG_HEIGHT = 100
MAX_LABEL_LENGTH=100

unique_characters=[' ', '!', '"', "'", '(', ')', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '?', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ÿ', 'Ŋ', 'ŋ', '‘', '’', '“', '”', '…']

char_to_num = StringLookup(vocabulary=list(unique_characters), mask_token=None)
num_to_char = StringLookup(vocabulary = char_to_num.get_vocabulary(), mask_token = None, invert = True)
model_path = "luganda_ocr/models/sentenceModel.h5"
def load_pretrained_model(model_path):
    pretrained_model = load_model(model_path, custom_objects={'CTCLayer': CTCLayer})
    pred_model = tf.keras.Model(inputs=pretrained_model.get_layer(name="image").input, outputs=pretrained_model.get_layer(name='output_dense').output)

    return pred_model

def decoder_prediction(pred_label, num_to_char, MAX_LABEL_LENGTH):
    input_len = np.ones(shape=pred_label.shape[0]) * pred_label.shape[1]
    decode = tf.keras.backend.ctc_decode(pred_label, input_length=input_len, greedy=True)[0][0][:, :MAX_LABEL_LENGTH]
    chars = num_to_char(decode)
    texts = [tf.strings.reduce_join(inputs=char).numpy().decode('UTF-8') for char in chars]
    filtered_texts = [text.replace('[UNK]', " ").strip() for text in texts]
    return filtered_texts

def single_sample_prediction(model, image_path, IMG_WIDTH, IMG_HEIGHT, num_to_char, MAX_LABEL_LENGTH):
    image_loading = tf.io.read_file(image_path)
    decoded_image = tf.image.decode_jpeg(contents=image_loading, channels=1)
    convert_image = tf.image.convert_image_dtype(image=decoded_image, dtype=tf.float32)
    resized_image = tf.image.resize(images=convert_image, size=(IMG_HEIGHT, IMG_WIDTH))
    resized_image = tf.transpose(resized_image, perm=[1, 0, 2])
    image_array = tf.cast(resized_image, dtype=tf.float32)
    single_image_data_with_batch = np.expand_dims(image_array, axis=0)
    prediction = decoder_prediction(model.predict(single_image_data_with_batch), num_to_char, MAX_LABEL_LENGTH)
    return prediction
    
def batch_prediction(folder_path):
    model_path = f"{get_base_path()}/models/sentenceModel.h5"
    model_path = model_path.replace("\\", "/")
    pred_model = load_model(model_path, custom_objects={'CTCLayer': CTCLayer})
    model = tf.keras.Model(inputs=pred_model.get_layer(name="image").input, outputs=pred_model.get_layer(name='output_dense').output)
    image_files = sorted([filename for filename in os.listdir(folder_path) if filename.endswith(".png")])
    predictions = []
    for filename in image_files:
        image_path = os.path.join(folder_path, filename)
        prediction = single_sample_prediction(model, image_path)
        predictions.append(prediction[0])
    
    return predictions
    
    

