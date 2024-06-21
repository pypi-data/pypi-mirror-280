import numpy as np

from educelab.imgproc.properties import dynamic_range


def as_dtype(image, dtype) -> np.ndarray:
    """Convert an image to a specific fundamental dtype. Automatically performs
    dynamic range adjustment.

    :param image: Input image.
    :param dtype: Numpy dtype. Must be one of: :code:`np.uint8`,
           :code:`np.uint16`, :code:`np.float32`.
    :return: Converted image.
    """
    if image.dtype == dtype:
        return image

    in_min, in_max = (float(x) for x in dynamic_range(image))
    out_min, out_max = (float(x) for x in dynamic_range(dtype))

    if image.dtype in (np.float32, np.float64):
        image = np.clip(image, a_min=0., a_max=1.)

    image = out_min + (image - in_min) * (out_max - out_min) / (in_max - in_min)
    return image.astype(dtype)
