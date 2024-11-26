#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: src/config.py

""" Configuration file for the project """

import os

# Get the directory of this file (i.e., PyTorchNLPBook/src/)
PKG_DIR = os.path.dirname(os.path.abspath(__file__))

# REPO_ROOT is one level up from PKG_DIR (i.e., PyTorchNLPBook/)
REPO_ROOT = os.path.abspath(os.path.join(PKG_DIR, '..'))

# Paths to the data and model directories
data_dir = os.path.join(REPO_ROOT, 'data')
model_dir = os.path.join(REPO_ROOT, 'model_storage')
image_dir = os.path.join(REPO_ROOT, 'assets/images')

# Path for NLTK data
nltk_data_dir = os.path.join(os.path.expanduser('~'), 'nltk_data')
