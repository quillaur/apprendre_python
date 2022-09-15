
# I chose skimage because it is made by sci-kit learn contributors 
# and I am gonna be using sci-kit learn all throughout this notebook. 
# Moreover, this module was build on top of OpenCV to make it easier to use.
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray
from skimage.exposure import equalize_hist
# Let's do a random selection of preprocessing parameters
import random
from tqdm.notebook import tqdm
import numpy as np
import pandas as pd
# Always use cross validation to test your models.
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from statistics import mean, stdev
# The time module will help us monitor model trainings.
import time
import os


def preprocessing(img_path: str, grayscale: bool=True, size: tuple=(64,64), equalize: bool=True) -> np.ndarray:
    """
    The image preprocessing steps before fitting the model.

    Args:
        - img_path: image path.
        - grayscale: if true, convert image from RGB to grayscale.
        - size: width and length to resize the image with.
        - equalize: if true then equalize image histogram, else not.
    
    Returns:
        The preprocessed image as a numpy array.
    """
    img = imread(img_path)
    img = resize(img, size)
    
    if grayscale:
        img = rgb2gray(img)
    
    if equalize:
        img = equalize_hist(img)
    return img


def load_preprocess_dataset(data_path: str, img_number: int, grayscale: bool=True, size: tuple=(64,64), equalize: bool=True) -> tuple:
    """
    Load and preprocess the collection of images.

    Args:
        - data_path: path toward the parent directory of the zip file.
        - img_number: number of images to include in the collection. If 0, then the whole collection is loaded.
        - grayscale: if true, convert image from RGB to grayscale.
        - size: width and length to resize the image with.
        - equalize: if true then equalize image histogram, else not.
    
    Returns:
        The collection of preprocess images as a list of numpy arrays and a list of labels.
    """
    cat_dir_path = os.path.join(data_path, "cat")
    dog_dir_path = os.path.join(data_path, "dog")

    cat_img_paths = [os.path.join(root, path) for root, dirs, files in os.walk(cat_dir_path) for path in files]
    dog_img_paths = [os.path.join(root, path) for root, dirs, files in os.walk(dog_dir_path) for path in files]

    if img_number:
        cat_img_paths = cat_img_paths[:img_number]
        dog_img_paths = dog_img_paths[:img_number]

    img_paths = cat_img_paths + dog_img_paths
    labels = [0] * len(cat_img_paths) + [1] * len(dog_img_paths)

    return ([preprocessing(img_path, grayscale, size, equalize) for img_path in img_paths], labels)


def train_test_model(model, images, labels) -> tuple:
    """
    Upon training the model, monitor the training time 
    and test accuracy with cross-validation.
    """
    X = np.array(images).reshape(len(images),-1)
    y = np.array(labels)
    # Split le dataset
    X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.3, 
    shuffle=True,
    random_state=42,
    )
    # Train
    start_time = time.time()
    model.fit(X_train, y_train)
    training_time = time.time() - start_time
    # Test
    accuracies = cross_val_score(model, X_test, y_test, cv=5)
    model_accuracy = mean(accuracies)
    
    return (model, model_accuracy, stdev(accuracies), training_time)



def test_models(models: dict, data_path: str, preprocess_params: list, n_iter: int) -> pd.DataFrame:
    tested_gray = []
    tested_sizes = []
    tested_equal = []
    tested_models = []
    training_times = []
    scores = []
    deviations = []
    for _ in tqdm(range(n_iter)):
        # Select randomly the parameters
        grayscale, size, equalize = [random.choice(params) for params in preprocess_params]
        size = (size, size) # Use same size for width and length
        # Load the data with selected parameters.
        images, labels = load_preprocess_dataset(data_path, 100, grayscale, size, equalize)
        # Train and test the models.
        for name, model in models.items():
            # Keep track of what is being tested
            tested_gray.append(grayscale)
            tested_sizes.append(size)
            tested_equal.append(equalize)
            tested_models.append(name)

            # Train and test
            model, model_accuracy, training_time, deviation = train_test_model(model, images, labels)

            # Track success
            scores.append(model_accuracy)
            deviations.append(deviation)
            training_times.append(training_time)

    return pd.DataFrame({
        "model": tested_models,
        "grayscale": tested_gray,
        "size": tested_sizes,
        "equalize histogram": tested_equal,
        "Accuracy": scores,
        "Stdev": deviations,
        "Training time": training_times
    })