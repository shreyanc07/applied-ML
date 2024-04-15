# Transfer Learning Assignment

## Overview

This repository contains the Jupyter notebooks for a two-part assignment on transfer learning. The assignment applies advanced machine learning techniques, specifically focusing on fine-tuning pre-trained models for both image and text classification tasks.

## Part 1: Image Classification with CNNs

#### LINK FOR GOOGLE COLAB NOTEBOOK

[Open the Colab Notebook](https://colab.research.google.com/drive/1qyV8xf9r_2dAn6PBi7At9MdwryfTFVgK?usp=sharing)

### Description

Part 1 utilizes a pre-trained convolutional neural network to classify images of ducks and chickens. About 100 images for each class were used, with the model fine-tuned to distinguish between these two bird types.

### Implementation Steps

- Download approximately 100 images each of ducks and chickens.
- Load and preprocess the images to fit the input requirements of the pre-trained model.
- Fine-tune a pre-trained convolutional neural network on the dataset.
- Evaluate the model using a classification report to understand its performance metrics.

## Part 2: Text Classification with Transformers

#### LINK FOR GOOGLE COLAB NOTEBOOK

[Open the Colab Notebook](https://colab.research.google.com/drive/1zV-USI1U2fyeJycM1ea1Gsv_8i0C5sOd?usp=sharing)

### Description

Part 2 focuses on sentiment analysis using a pre-trained transformer model. The task involves classifying sentiments as positive, neutral, or negative by fine-tuning the transformer on relevant text data.

### Implementation Steps

- Prepare or obtain a dataset labeled with sentiments (positive, neutral, negative).
- Preprocess the text data to fit the transformer model's input requirements.
- Fine-tune the pre-trained transformer on the sentiment classification task.
- Generate a classification report to evaluate the performance of the model.

## Requirements

- Python 3.7+
- Jupyter Notebook or Google Colab
- Libraries: `tensorflow` or `pytorch`, `transformers`, `numpy`, `matplotlib`

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/shreyanc07/applied-ML.git
```
