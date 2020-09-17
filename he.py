import numpy as np


def get_histogram(img):
    # calculates normalized histogram of an image
    x, y = img.shape
    h = [0] * 256
    for i in range(x):
        for j in range(y):
            h[img[i, j]] += 1
    return np.array(h) / (x * y)


def cumulative_sum(h):
    # finds cumulative sum of a numpy array, list
    return [sum(h[:i + 1]) for i in range(len(h))]


def hist_equalize(img):
    histogram = get_histogram(img)
    cdf = np.array(cumulative_sum(histogram))  # cumulative distribution function
    sk = np.uint8(255 * cdf)  # finding transfer function values
    x, y = img.shape
    equalized_img = np.zeros_like(img)
    # applying transferred values for each pixels
    for i in range(x):
        for j in range(y):
            equalized_img[i, j] = sk[img[i, j]]
    equalized_histogram = get_histogram(equalized_img)
    # return transformed image, original and new histogram,
    # and transform function
    return equalized_img, histogram, equalized_histogram, sk
