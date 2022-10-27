import cv2


class ImageLoader:

    def _get_image(self, path_to_image: str):
        img = cv2.imread(path_to_image)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)