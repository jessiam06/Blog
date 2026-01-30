---
title: What is a Neural Network?
date: 2026-01-15
description: Lorem ipsum dolor sit amet consectetur adipiscing elit. Consectetur adipiscing elit quisque faucibus ex sapien vitae.
thumbnail:/Assets/nn thumbnail.png
tags: web, static-sites, programming
readtime: 6 min
---
# Neural Networks: A Gentle Overview

*Neural networks* are a class of **machine learning models** inspired by the structure of the human brain. They are especially powerful for tasks like image recognition, natural language processing, and function approximation.

---

## What Is a Neural Network?

A **neural network** is composed of layers of interconnected nodes (called *neurons*). Each neuron:
- Receives inputs  
- Applies a weighted sum  
- Passes the result through an *activation function*

> In short: **inputs → computation → output**

---

## Basic Architecture

### 1. Input Layer
The input layer receives raw data, such as pixel values or numerical features.

### 2. Hidden Layers
Hidden layers perform most of the computation. Adding more hidden layers leads to a *deep* neural network.

### 3. Output Layer
The output layer produces the final prediction, such as a class label or a number.

---

## The Math Behind a Neuron

A single neuron computes:

$$
z = \sum_{i=1}^{n} w_i x_i + b
$$

and then applies an activation function:

$$
a = \sigma(z)
$$

where:
- \( w_i \) are weights  
- \( x_i \) are inputs  
- \( b \) is a bias  
- \( \sigma \) might be *ReLU*, *sigmoid*, or *tanh*

---

## Example Code (Python)

Below is a **very small example** using NumPy:

```python
import numpy as np

def relu(x):
    return np.maximum(0, x)

x = np.array([1.0, -2.0, 3.0])
w = np.array([0.5, 0.2, -0.1])
b = 0.1

z = np.dot(w, x) + b
a = relu(z)

print(a)