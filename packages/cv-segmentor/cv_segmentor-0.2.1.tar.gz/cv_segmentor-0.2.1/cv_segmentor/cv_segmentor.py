class CV_Segmentor(object):

    def __init__(self, name):
        self.name = name

    # Params
    # @image: numpy.ndarray((height, width, channels=3))
    # Return
    # @masks: numpy.ndarray((height * width))
    # @time_records: numpy.ndarray((n))
    def segment(self, image):
        raise NotImplementedError()
    
    # Parans:
    # @file_name: str
    # Return
    # @file_path: str
    # Comment: use this method when getting the path to any file such as .pth or .mdl
    # Otherwise loading the file may fail on submission.
    def get_file_path(self, file_path):
        return file_path