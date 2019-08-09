import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as am
import ctypes

class ScreenSave(object):
    """ DocString for ScreenSave"""

    def __init__(self, ):
        #@todo: to be defined.
        lib = ctypes.cdll.LoadLibrary('ss.dylib')
        self.func = lib.changeStat
        self.func.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32, ndim=3, flags='C_CONTIGUOUS'),
                              np.ctypeslib.ndpointer(dtype=np.int32, ndim=3, flags='C_CONTIGUOUS'),
                              ctypes.c_int]
        shape = (9, 16, 3)
        self.length = shape[0] * shape[1] * shape[2]
        self.data_pic = 128*np.ones(shape, dtype=np.int32)
        self.data_res = self.data_pic.copy()
        self.fig = plt.figure(tight_layout=True)
        self.img = plt.imshow(self.data_pic/255)

    def update_fig(self, num):
        """DocString for update_fig"""
        self.func(self.data_pic, self.data_res, self.length)
        self.img.set_data(self.data_res / 255)
        return self.img,

    def run(self):
        """DocString for runrun"""
        #@todo: to be defined.
        ani = am.FuncAnimation(self.fig, self.update_fig, np.arange(100), interval=10, blit=True)
        plt.show()


if __name__ == '__main__':
    ss = ScreenSave()
    ss.run()
