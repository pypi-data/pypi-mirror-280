import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow.data as tfd
from tensorflow.keras.layers import *
from tensorflow.keras.models import load_model
from model import load_pretrained_model, single_sample_prediction, batch_prediction, num_to_char
from utils import load_and_preprocess_image, load_image_files, save_predictions

model_path = "/home/beijuka/luganda_ocr/luganda_ocr/models/sentenceModel.h5"
IMAGE_FOLDER = "/home/beijuka/luganda_ocr/tests/trial"
OUTPUT_FILE = "/home/beijuka/luganda_ocr/predictions.txt"
IMG_WIDTH = 1500
IMG_HEIGHT = 100
MAX_LABEL_LENGTH = 100

pred_model = load_pretrained_model(model_path)

image_files = load_image_files(IMAGE_FOLDER)
predictions = []
for image_path in image_files:
    image = load_and_preprocess_image(image_path, IMG_WIDTH, IMG_HEIGHT)
    prediction = single_sample_prediction(pred_model, image_path, IMG_WIDTH, IMG_HEIGHT, num_to_char, MAX_LABEL_LENGTH)
    predictions.append(prediction[0])
save_predictions(predictions, OUTPUT_FILE)

