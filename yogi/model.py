################## IMPORTS #################

from tensorflow.keras import utils, optimizers
from tensorflow.keras import models, layers
from tensorflow.keras.applications import densenet
from tensorflow.keras.callbacks import EarlyStopping

################## MODEL #################

def initialize_model():
    base_model = densenet.DenseNet169(
                        include_top=False,
                        weights='imagenet',
                        input_shape=(img_height, img_width, 3),
                        classifier_activation='softmax')

    base_model.trainable = True

    model = models.Sequential([
        base_model,
        layers.Flatten(),
        layers.Dropout(0.4),
        layers.Dense(1000,activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(900, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(800, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(700, activation="relu"),
        layers.Dense(87, activation="softmax")
    ])


    opt = optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=opt,
                loss='categorical_crossentropy',
                metrics=['accuracy'])

    return model

def train_model(model, train_generator, validation_generator, batch_size):

    es = EarlyStopping(patience=5, restore_best_weights=True)

    history = model.fit(
                train_generator,
                steps_per_epoch = train_generator.samples // batch_size,
                validation_data = validation_generator,
                validation_steps = validation_generator.samples // batch_size,
                epochs=500,
                batch_size=batch_size
                callbacks=[es])

    return history
