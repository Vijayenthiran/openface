<<<<<<< HEAD
#!/usr/bin/env python
#
# Example to classify faces.
# Brandon Amos
# 2015/10/11
=======
#!/usr/bin/env python2
#
# Example to run classifier on webcam stream.
# Brandon Amos & Vijayenthiran
# 2016/06/21
>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b
#
# Copyright 2015-2016 Carnegie Mellon University
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

<<<<<<< HEAD
=======
# Contrib: Vijayenthiran
# This example file shows to run a classifier on webcam stream. You need to
# run the classifier.py to generate classifier with your own dataset.
# To run this file from the openface home dir:
# ./demo/classifier_webcam.py <path-to-your-classifier>


>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b
import time

start = time.time()

import argparse
import cv2
import os
import pickle
<<<<<<< HEAD
import sys

from operator import itemgetter

import numpy as np
np.set_printoptions(precision=2)
import pandas as pd

import openface

from sklearn.pipeline import Pipeline
from sklearn.lda import LDA
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.mixture import GMM
=======

import numpy as np
np.set_printoptions(precision=2)
from sklearn.mixture import GMM
import openface
>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b

fileDir = os.path.dirname(os.path.realpath(__file__))
modelDir = os.path.join(fileDir, '..', 'models')
dlibModelDir = os.path.join(modelDir, 'dlib')
openfaceModelDir = os.path.join(modelDir, 'openface')


def getRep(bgrImg):
    start = time.time()
    if bgrImg is None:
<<<<<<< HEAD
        raise Exception("Unable to load image: {}".format(imgPath))
=======
        raise Exception("Unable to load image/frame")
>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b

    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    if args.verbose:
        print("  + Original size: {}".format(rgbImg.shape))
    if args.verbose:
        print("Loading the image took {} seconds.".format(time.time() - start))

    start = time.time()

<<<<<<< HEAD
    #Get the largest face bounding box
    #bb = align.getLargestFaceBoundingBox(rgbImg) #Bounding box

    #Get all bounding boxes
    bb = align.getAllFaceBoundingBoxes(rgbImg)
    
    if bb is None:
        #raise Exception("Unable to find a face: {}".format(imgPath))
=======
    # Get the largest face bounding box
    # bb = align.getLargestFaceBoundingBox(rgbImg) #Bounding box

    # Get all bounding boxes
    bb = align.getAllFaceBoundingBoxes(rgbImg)

    if bb is None:
        # raise Exception("Unable to find a face: {}".format(imgPath))
>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b
        return None
    if args.verbose:
        print("Face detection took {} seconds.".format(time.time() - start))

    start = time.time()

    alignedFaces = []
    for box in bb:
<<<<<<< HEAD
        alignedFaces.append (align.align_v1(args.imgDim, rgbImg, box, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE))

    if alignedFaces is None:
        raise Exception("Unable to align image: {}".format(imgPath))
=======
        alignedFaces.append(
            align.align(
                args.imgDim,
                rgbImg,
                box,
                landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE))

    if alignedFaces is None:
        raise Exception("Unable to align the frame")
>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b
    if args.verbose:
        print("Alignment took {} seconds.".format(time.time() - start))

    start = time.time()

    reps = []
    for alignedFace in alignedFaces:
<<<<<<< HEAD
        reps.append (net.forward(alignedFace))
=======
        reps.append(net.forward(alignedFace))
>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b

    if args.verbose:
        print("Neural network forward pass took {} seconds.".format(
            time.time() - start))

<<<<<<< HEAD
    #print reps
    return reps


def infer(img,args):
    with open(args.classifierModel, 'r') as f:
        (le, clf) = pickle.load(f) #le - label and clf - classifer
    
=======
    # print reps
    return reps


def infer(img, args):
    with open(args.classifierModel, 'r') as f:
        (le, clf) = pickle.load(f)  # le - label and clf - classifer

>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b
    reps = getRep(img)
    persons = []
    confidences = []
    for rep in reps:
        try:
            rep = rep.reshape(1, -1)
        except:
            print "No Face detected"
            return (None, None)
        start = time.time()
        predictions = clf.predict_proba(rep).ravel()
<<<<<<< HEAD
        #print predictions
        maxI = np.argmax(predictions)
        max2 = np.argsort(predictions)[-3:][::-1] [1]
        persons.append (le.inverse_transform(maxI))
        print
        print str(le.inverse_transform(max2)) + ": "+str( predictions [max2])
        confidences.append (predictions[maxI])
        if args.verbose:
            print("Prediction took {} seconds.".format(time.time() - start))
            pass
        #print("Predict {} with {:.2f} confidence.".format(person, confidence))
=======
        # print predictions
        maxI = np.argmax(predictions)
        # max2 = np.argsort(predictions)[-3:][::-1][1]
        persons.append(le.inverse_transform(maxI))
        # print str(le.inverse_transform(max2)) + ": "+str( predictions [max2])
        # ^ prints the second prediction
        confidences.append(predictions[maxI])
        if args.verbose:
            print("Prediction took {} seconds.".format(time.time() - start))
            pass
        # print("Predict {} with {:.2f} confidence.".format(person, confidence))
>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b
        if isinstance(clf, GMM):
            dist = np.linalg.norm(rep - clf.means_[maxI])
            print("  + Distance from the mean: {}".format(dist))
            pass
<<<<<<< HEAD
    return (persons,confidences)


if __name__ == '__main__':
    video_capture = cv2.VideoCapture(0)
    video_capture.set(3,320)
    video_capture.set(4,240)
    
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--dlibFacePredictor', type=str,
                        help="Path to dlib's face predictor.",
                        default=os.path.join(dlibModelDir,
                                             "shape_predictor_68_face_landmarks.dat"))
    parser.add_argument('--networkModel', type=str,
                     help="Path to Torch network model.",
                     default=os.path.join(openfaceModelDir, 'nn4.small2.v1.t7'))
    parser.add_argument('--imgDim', type=int,
                        help="Default image dimension.", default=96)
    parser.add_argument('--cuda', action='store_true')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('classifierModel', type=str,
                             help='The Python pickle representing the classifier. This is NOT the Torch network model, which can be set with --networkModel.')
    args = parser.parse_args()
    
    align = openface.AlignDlib(args.dlibFacePredictor)
    net = openface.TorchNeuralNet(args.networkModel, imgDim=args.imgDim, cuda=args.cuda)
    
    confidenceList = []
    beginTime = time.time()
    noOfFrames = 0
    while True:
        ret, frame = video_capture.read()
        noOfFrames += 1
        persons,confidences = infer(frame, args)
        print "P: " + str(persons) + " C: " + str(confidences)
        try:
            confidenceList.append(confidences[0])
        except:
            pass
        if time.time() - beginTime >= 5:
            print "noOfFrames: " + str(noOfFrames)
            print "******* Avg. conf:" + str(np.mean(confidenceList)) + " *******"
            beginTime = time.time()
            #time.sleep(3)
            #sys.exit()
            
        for i,c in enumerate(confidences):
            if c<=0.5:
                persons[i] = "_unknown"
        
        cv2.putText(frame ,"P: " + str(persons) + " C: " + str(confidences) ,(50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),1)
        cv2.imshow('', frame)
=======
    return (persons, confidences)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dlibFacePredictor',
        type=str,
        help="Path to dlib's face predictor.",
        default=os.path.join(
            dlibModelDir,
            "shape_predictor_68_face_landmarks.dat"))
    parser.add_argument(
        '--networkModel',
        type=str,
        help="Path to Torch network model.",
        default=os.path.join(
            openfaceModelDir,
            'nn4.small2.v1.t7'))
    parser.add_argument('--imgDim', type=int,
                        help="Default image dimension.", default=96)
    parser.add_argument(
        '--captureDevice',
        type=int,
        default=0,
        help='Capture device. 0 for latop webcam and 1 for usb webcam')
    parser.add_argument('--width', type=int, default=320)
    parser.add_argument('--height', type=int, default=240)
    parser.add_argument('--threshold', type=float, default=0.5)
    parser.add_argument('--cuda', action='store_true')
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument(
        'classifierModel',
        type=str,
        help='The Python pickle representing the classifier. This is NOT the Torch network model, which can be set with --networkModel.')

    args = parser.parse_args()

    align = openface.AlignDlib(args.dlibFacePredictor)
    net = openface.TorchNeuralNet(
        args.networkModel,
        imgDim=args.imgDim,
        cuda=args.cuda)

    # Capture device. Usually 0 will be webcam and 1 will be usb cam.
    video_capture = cv2.VideoCapture(args.captureDevice)
    video_capture.set(3, args.width)
    video_capture.set(4, args.height)

    confidenceList = []
    while True:
        ret, frame = video_capture.read()
        persons, confidences = infer(frame, args)
        print "P: " + str(persons) + " C: " + str(confidences)
        try:
            # append with two floating point precision
            confidenceList.append('%.2f' % confidences[0])
        except:
            # If there is no face detected, confidences matrix will be empty.
            # We can simply ignore it.
            pass

        for i, c in enumerate(confidences):
            if c <= args.threshold:  # 0.5 is kept as threshold for known face.
                persons[i] = "_unknown"

                # Print the person name and conf value on the frame
        cv2.putText(frame, "P: {} C: {}".format(persons, confidences),
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow('', frame)
        # quit the program on the press of key 'q'
>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
<<<<<<< HEAD


=======
>>>>>>> 3dc4546198e3802e6c4463227dbf537308ae890b
