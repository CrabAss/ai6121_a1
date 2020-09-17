def rgb_to_hsl(r, g, b):
    """
    Convert an RGB color to HSL colorspace.
    :param r: Red color value (int between 0 and 255)
    :param g: Green color value (int between 0 and 255)
    :param b: Blue color value (int between 0 and 255)
    :return: float values of HSL between 0 and 1
    """
    r = float(r) / 255.0
    g = float(g) / 255.0
    b = float(b) / 255.0
    high = max(r, g, b)
    low = min(r, g, b)

    l = (high + low) / 2.0

    c = high - low  # chroma
    if c == 0.0:
        h = 0.0
        s = 0.0
    else:
        h = {
                r: (g - b) / c + (6 if g < b else 0),
                g: (b - r) / c + 2,
                b: (r - g) / c + 4,
            }[high] / 6
        s = c / (2 - high - low) if l > 0.5 else c / (high + low)

    return h, s, l


def saturate(value):
    """
    Return the nearest boundary value (0 or 1) if the input value is out of boundary.
    Otherwise, return the input value itself.
    :param value: input value
    """
    return max(0.0, min(1.0, value))


def hue_to_rgb(h):
    r = abs(h * 6.0 - 3.0) - 1.0
    g = 2.0 - abs(h * 6.0 - 2.0)
    b = 2.0 - abs(h * 6.0 - 4.0)
    return saturate(r), saturate(g), saturate(b)


def hsl_to_rgb(h, s, l):
    """
    Convert an HSL color to RGB colorspace.
    :param h: Hue value (float between 0 and 1)
    :param s: Saturation value (float between 0 and 1)
    :param l: Lightness value (float between 0 and 1)
    :return: int values of RGB between 0 and 255
    """
    r, g, b = hue_to_rgb(h)
    c = (1.0 - abs(2.0 * l - 1.0)) * s
    r = (r - 0.5) * c + l
    g = (g - 0.5) * c + l
    b = (b - 0.5) * c + l

    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)
    return r, g, b
