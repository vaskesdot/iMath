import json
from pprint import pprint
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas


class Log:
    def __init__(self, startLogX: float, stopLogX: float, startLogY: float, stopLogY: float, iters: int):
        self.startLogX = startLogX
        self.stopLogX = stopLogX
        self.startLogY = startLogY
        self.stopLogY = stopLogY
        self.iters = iters

    @property
    def x(self):
        return np.logspace(start=self.startLogX, stop=self.stopLogX, num=self.iters)

    @property
    def y(self):
        return np.logspace(start=self.startLogY, stop=self.stopLogY, num=self.iters)

    def getInfo(self) -> dict:

        GrowthRateX = 1 + (1 - self.x[0] / self.x[1])
        GrowthRateY = 1 + (1 - self.y[0] / self.y[1])
        iterationsNumber = len(self.x)
        differenceYXstart = self.y[0] / self.x[0]
        differenceYXfinal = self.y[-1] / self.x[-1]
        info = {
                "data": {
                    "X": {
                        "IterationNumber": iterationsNumber,
                        "GrowthRate": GrowthRateX,
                        "ScaleRateIter": math.log(self.x[1], self.x[0]),
                        "FirstIteration": self.x[0],
                        "FinalIteration": self.x[-1],
                        "TotalGrowthAllIterations": self.x[-1] / self.x[0],
                        "TotalScaleAllIterations": math.log(self.x[-1], self.x[0]),
                            },
                    "Y": {
                        "IterationNumber": iterationsNumber,
                        "GrowthRateIter": GrowthRateY,
                        "ScaleRateIter": math.log(self.y[1], self.y[0]),
                        "FirstIteration": self.y[0],
                        "FinalIteration": self.y[-1],
                        "TotalGrowthAllIterations": self.y[-1] / self.y[0],
                        "TotalScaleAllIterations": math.log(self.y[-1], self.y[0]),
                            },
                        },

                "_more_data": {
                        "GrowthRateSlopeYX": GrowthRateY / GrowthRateX,
                        "differenceYX_start": differenceYXstart,
                        "differenceYX_final": differenceYXfinal,
                            }
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



log = Log(startLogX=1, stopLogX=5.1, startLogY=1, stopLogY=2.6, iters=10)
log_info = log.getInfo()
log_df = log.getDataFrame()
#log.showGraph()

pprint(log_info)

True