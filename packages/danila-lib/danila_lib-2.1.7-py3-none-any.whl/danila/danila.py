# import os
#
# import cv2
#
# from danila.danila_v1 import Danila_v1
# from danila.danila_v2 import Danila_v2
# from danila.danila_v3 import Danila_v3
from danila.danila_v10 import Danila_v10
from danila.danila_v4 import Danila_v4
from danila.danila_v5 import Danila_v5
from danila.danila_v6 import Danila_v6
from danila.danila_v7 import Danila_v7
from danila.danila_v8 import Danila_v8
from danila.danila_v9 import Danila_v9

"""main module for user"""


class Danila:
    """main class for user"""
    def __init__(self, version, yolov5_dir):
        if (version == 4):
            self.danila = Danila_v4(yolov5_dir)
        elif (version == 5):
            self.danila = Danila_v5(yolov5_dir)
        elif (version == 6):
            self.danila = Danila_v6(yolov5_dir)
        elif (version == 7):
            self.danila = Danila_v7(yolov5_dir)
        elif (version == 8):
            self.danila = Danila_v8(yolov5_dir)
        elif (version == 9):
            self.danila = Danila_v9(yolov5_dir)
        elif (version == 10):
            self.danila = Danila_v10(yolov5_dir)
        else:
            self.danila = Danila_v4(yolov5_dir)
    # returns string - class of rama using CNN network
    # img - openCV frame

    def detail_classify(self, img, size = 256):
        return self.danila.detail_classify(img, size)

    def detail_text_detect(self, img, size = 256):
        return self.danila.detail_text_detect(img, size)

    def detail_text_recognize(self, img, size = 256):
        return self.danila.detail_text_recognize(img, size)

    def rama_classify(self, img, size = 256):
        """rama_classify(Img : openCv frame): String - returns class of rama using CNN network"""
        """rama_classify uses Rama_classify_class method - classify(Img)"""
        return self.danila.rama_classify(img, size)

    # returns openCV frame with rama from openCV frame\
    # def rama_detect(self, img, size = 256):
    #     """rama_detect(img : openCV img) -> openCV image with drawn rama rectangle"""
    #     return self.danila.rama_detect(img, size)
    #
    # # returns openCV image with cut_rama
    # def rama_cut(self, img, size = 256):
    #     """rama_cut(img : openCV img) -> openCV image of rama rectangle"""
    #     return self.danila.rama_cut(img, size)

    #
    # returns openCV cut rama with drawn text areas
    def rama_text_detect_cut(self, img, size = 256):
        """returns openCV cut rama with drawn text areas"""
        return self.danila.rama_text_detect_cut(img, size)

    # returns openCV img with drawn text areas
    # def rama_text_detect(self, img, size = 256):
    #     """returns openCV img with drawn text areas"""
    #     return self.danila.text_detect(img, size)
    # returns dict {'number', 'prod', 'year'} for openCV rama img or 'no_rama'
    def rama_text_recognize(self, img, size = 256):
        """returns dict {'number', 'prod', 'year'} for openCV rama img or 'no_rama'"""
        return self.danila.rama_text_recognize(img, size)

    # returns openCV img with drawn number areas
    def vagon_number_detect(self, img, size = 256):
        """returns openCV img with drawn number areas"""
        return self.danila.vagon_number_detect(img, size)

    def vagon_number_recognize(self, img, size = 256, size_number_h = 128, size_number_w = 320):
        return self.danila.vagon_number_recognize(img, size,  size_number_h=size_number_h, size_number_w=size_number_w)