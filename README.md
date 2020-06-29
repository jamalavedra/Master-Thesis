# Development_of_feature_based_smart_virtual_sensors

This is the implementation of the thesis for the Computer Science Master from the Technical University of Denmark (DTU).

## Table of contents

- [Introduction](#introduction)
- [General info](#general-info)
- [Requirements](#requirements)

## Introduction

This thesis proposes an application of convolutional feature points as smart virtual sensors. The feature descriptors are formed using the feature maps of one of the layers of a VGG-16 network pre-trained on Imagenet.From the extracted and matched features, information is obtained from each of them to create a data-set that describes the sequence of frames under consideration. Different sets of information are extracted from the feature correspondences such as their coordinates with respect the image or their local displacement between frames. Moreover, to compare the robustness of the implemented convolutional features, the same information is obtained using the SIFT descriptor and a brute-force matching technique.
The collected information from the matched feature points is used to train a set of machine learning models that predict physical properties of the environment or body under consideration. The two used applications are: volume prediction on a self-developed sphere simulation and displacement prediction on the [KITTI](http://www.cvlibs.net/datasets/kitti/)benchmark suite.

## General info

This repository shares the implementation of the two main modules in which the thesis is divided.
Additionally, the .csv files containing the gathered data-sets are included.

### Feature extraction and matching

A comparison is made between the implemented convolutional features based methodology and SIFT-based.
For each, three files are presented.

- Applied to the sphere.
- Applied to KITTI city sequences.
- Visualization of specific frames from the above applications.

Additionally, another file is provided to allow for observing the outcome of certain layers of the pre-trained VGG-16 network.

### Machine learning regression models

Two regression models are presented:

- Multi-variable linear model.
- Long short-term memory model.

## Requirements

Project is created with:

- Torch
- Pytorchvis
- numpy
- matplotlib
- OpenCV: 3.4.2.16 (To include SIFT descriptor)
- Jupyter Notebook as experimentation platform

To install all the requirements run

```
pip install -r requirements.txt
```

Prior to doing so, in some Linux distributions, you may need to install software packages such as the following:

- pip
- python3 development package
- python-setup
