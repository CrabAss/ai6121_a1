import numpy as np


def cumulative_sum(h):
    """find cumulative sum of a numpy array or a list"""
    return [sum(h[:i + 1]) for i in range(len(h))]


def get_histogram(img):
    # calculates normalized histogram of an image
    x, y = img.shape
    h = [0] * 256
    for i in range(x):
        for j in range(y):
            h[img[i, j]] += 1
    return np.array(h) / (x * y)


def hist_equalize(img):
    histogram = get_histogram(img)
    cdf = np.array(cumulative_sum(histogram))  # cumulative distribution function
    sk = np.uint8(255 * cdf)  # get the transfer function values
    x, y = img.shape
    equalized_img = np.zeros_like(img)
    # apply transferred values for each pixel
    for i in range(x):
        for j in range(y):
            equalized_img[i, j] = sk[img[i, j]]
    equalized_histogram = get_histogram(equalized_img)
    # return transformed image, original and new histogram,
    # and transform function
    return equalized_img, histogram, equalized_histogram, sk
