from pprint import pprint
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas



class LogXY:
    def __init__(self, startLogX: float, stopLogX: float, startLogY: float,
                 stopLogY: float, startValueXLog1: float, startValueYLog1: float,  iters: int):
        self.startLogX = startLogX
        self.stopLogX = stopLogX
        self.startLogY = startLogY
        self.stopLogY = stopLogY
        self.startValueXLog1 = startValueXLog1
        self.startValueYLog1 = startValueYLog1
        self.iters = iters

    @property
    def x(self):
        return np.logspace(start=self.startLogX, stop=self.stopLogX,
                           base=self.startValueXLog1, num=self.iters)

    @property
    def y(self):
        return np.logspace(start=self.startLogY, stop=self.stopLogY,
                           base=self.startValueYLog1, num=self.iters,)

    @property
    def xy(self) -> list:
        xy = []
        for xIndex, yIndex in zip(self.x, self.y):
            xyIndex = xIndex * yIndex
            xy.append(xyIndex)
        return xy

    def getInfo(self) -> dict:

        GrowthRateX = self.x[1] / self.x[0]
        GrowthRateY = self.y[1] / self.y[0]
        iterationsNumber = len(self.x)
        differenceYXstart = self.y[0] / self.x[0]
        differenceYXfinal = self.y[-1] / self.x[-1]
        info = {

                "Overall": {
                    "IterationNumber": iterationsNumber,
                            },
                "X": {
                    "GrowthOverIter1": self.x[1] / self.x[0],
                    "GrowthOverIter2": self.x[2] / self.x[1],
                    "ScaleRateIter": math.log(self.x[1], self.x[0]),
                    "FirstIteration": self.x[0],
                    "FinalIteration": self.x[-1],
                    "TotalGrowthAllIterations": self.x[-1] / self.x[0],
                    "TotalScaleAllIterations": math.log(self.x[-1], self.x[0]),
                    },
                "Y": {
                    "GrowthOverIter1": self.y[1] / self.y[0],
                    "GrowthOverIter2": self.y[2] / self.y[1],
                    "ScaleRateIter": math.log(self.y[2], self.y[1]),
                    "FirstIteration": self.y[0],
                    "FinalIteration": self.y[-1],
                    "TotalGrowthAllIterations": self.y[-1] / self.y[0],
                    "TotalScaleAllIterations": math.log(self.y[-1], self.y[0]),
                    },
                "XY": {
                    "GrowthOverIter1": self.xy[1] / self.xy[0],
                    "GrowthOverIter2": self.xy[2] / self.xy[1],
                    "ScaleRateIter": math.log(self.xy[2], self.xy[1]),
                    "FirstIteration": self.xy[0],
                    "FinalIteration": self.xy[-1],
                    "TotalGrowthAllIterations": self.xy[-1] / self.xy[0],
                    "TotalScaleAllIterations": math.log(self.xy[-1], self.xy[0]),
            },
        }
        return info

    def getDataFrame(self):
        df = pandas.DataFrame(self.x, columns=['x'])
        df['y'] = self.y

        def xy(x: list, y: list):
            xy = []
            for index in range(len(x)):
                xy_value = x[index] / y[index]
                xy.append(xy_value)
            return xy

        df['xy'] = xy(x=self.x, y=self.y)
        return df

    def showGraph(self):
        plt.loglog(self.x, self.y)
        plt.title('Логарифмический график')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

    @staticmethod
    def _multiplyXY(x: np.array, y: np.array):
        return x * y

    @staticmethod
    def _divideXY(x: np.array, y: np.array):
        return x / y

    @staticmethod
    def _divideYX(x: np.array, y: np.array):
        return y / x

    @staticmethod
    def _plusYX(x: np.array, y: np.array):
        return y + x

    @staticmethod
    def _minusYX(x: np.array, y: np.array):
        return y - x

    @staticmethod
    def _minusXY(x: np.array, y: np.array):
        return x - y

    @staticmethod
    def _log(stop: float, start: float):
        return math.log(112.5, 25)

