"""-------------------------------------------------------
Computer Vision: Module Description Here
-------------------------------------------------------
Author:  JD
ID:      91786
Uses:    numpy,openCV,matplotlib,pandas,OpenCV
Version:  1.0.8
__updated__ = Sat Dec 28 2024
-------------------------------------------------------
"""

import os
import numpy as np
import pandas as pd
import random

# import cv2 as cv
from matplotlib import pyplot as plt

x = np.arange(1, 100, dtype=np.int32)

plt.figure(figsize=(12, 5))
plt.style.use("bmh")
plt.plot(x, x, label="x")
plt.plot(x, np.log(x), label="log(x)")
plt.plot(x, x / 2, label="x/2")

plt.title("Log Functions", fontsize=16)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.legend()
plt.show()
