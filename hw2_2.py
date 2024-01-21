import contextlib
from doctest import master
import logging
import os
import sys
import cv2
import torch
from torch.autograd import Variable
import numpy as np


with open(os.devnull, 'w') as devnull:
    with contextlib.redirect_stderr(devnull):
        model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt', force_reload=True)
        pass

if len(sys.argv) > 1:
    filename = sys.argv[1]
img = cv2.imread(filename)

results = model(filename)
results = results.xyxy[0]

# empire state building class index = 3
filtered_empire = results[results[:, -1] == 3]
for building in filtered_empire:
    x1, y1, x2, y2, conf, cls = building
    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 20)
cv2.imshow('Empire state building', img)
cv2.waitKey()
cv2.destroyAllWindows()
