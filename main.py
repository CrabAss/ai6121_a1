import numpy as np
import matplotlib.pyplot as plt

from convert_color import rgb_to_hsl, hsl_to_rgb
from he import hist_equalize


def zero_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    func = lambda x: float('nan') if x == 0.0 else x
    vfunc = np.vectorize(func)
    return vfunc(values)


def he_image_demo(img_dir):
    img = plt.imread(img_dir)

    hsl_img = np.zeros_like(img, dtype=float)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hsl_img[i, j] = rgb_to_hsl(img[i, j, 0], img[i, j, 1], img[i, j, 2])

    img_brightness = np.uint8(hsl_img[:, :, 2] * 255)

    new_img_brightness, histogram, new_histogram, sk = hist_equalize(img_brightness)

    new_img_brightness = np.true_divide(new_img_brightness, 255.0)
    new_img = np.zeros_like(img, dtype=int)
    for i in range(hsl_img.shape[0]):
        for j in range(hsl_img.shape[1]):
            hsl_img[i, j, 2] = new_img_brightness[i, j]
            new_img[i, j] = hsl_to_rgb(hsl_img[i, j, 0], hsl_img[i, j, 1], hsl_img[i, j, 2])

    # show original image
    fig1 = plt.figure()
    fig1.add_subplot(121)
    plt.imshow(img)
    plt.title('Original Image')
    # show new image
    fig1.add_subplot(122)
    plt.imshow(new_img)
    plt.title('Histogram Equalized Image')

    plt.show()

    # plot histograms and transfer function
    fig2 = plt.figure()
    fig2.add_subplot(221)
    plt.plot(histogram)
    plt.title('Original Histogram')  # original histogram

    fig2.add_subplot(222)
    plt.plot(sk)
    plt.title('Transfer Function')

    fig2.add_subplot(223)
    nan_new_histogram = zero_to_nan(new_histogram)
    xs = np.arange(256)
    mask = np.isfinite(nan_new_histogram)
    plt.plot(xs[mask], nan_new_histogram[mask])
    plt.title('Equalized Histogram (Zeros ignored)')

    fig2.add_subplot(224)
    plt.plot(new_histogram)
    plt.title('Equalized Histogram')

    plt.show()


if __name__ == '__main__':
    he_image_demo('data/sample02.jpg')
