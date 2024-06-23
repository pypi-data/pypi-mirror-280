from skimage import color, exposure
from skimage.feature import hog


def hog_feature_extraction(image):
    image = color.rgb2gray(image)
    # Вычисление HOG-гистограммы
    fd, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8),
                        cells_per_block=(2, 2), visualize=False)
    return fd
