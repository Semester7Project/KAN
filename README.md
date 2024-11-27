# Neural Network Framework

## Project Overview

This project implements a basic neural network framework from scratch. It provides functionalities for building and training feed-forward neural networks with various activation functions and loss functions.  The framework is designed to be modular and extensible, allowing for easy addition of new neuron types and loss functions.

## Features

* **Modular Neuron Implementations:**  Different neuron types are implemented in the `neuron` directory (`neuron_kan.py`, `neuron_nn.py`, `neuron_template.py`).
* **Feed-forward Network Architecture:** A feed-forward network architecture is implemented in the `feed_forward_network` directory.
* **Layer Implementation:** Individual layers of the network are implemented in `feed_forward_network/layer.py`.
* **Activation Functions:** A variety of activation functions are available in `utils/activations.py`.
* **Loss Functions:**  Support for squared loss and cross-entropy loss is provided in the `loss` directory.
* **Gradient Testing:** Unit tests for gradient calculations are included in the `test` directory.


## Installation

This project uses Python and requires the packages listed in `requirements.txt`.  You can install them using pip:

```bash
pip install -r requirements.txt
```

## Usage

The main functionality is demonstrated in `main.ipynb`.  This Jupyter Notebook provides examples of how to create, train, and use the neural network.  To run it, make sure you have Jupyter Notebook installed (`pip install notebook`) and then navigate to the project directory in your terminal and run:

```bash
jupyter notebook main.ipynb
```

You can then follow the instructions within the notebook to experiment with the different components of the framework.  The `neuron`, `feed_forward_network`, `utils`, and `loss` directories contain the core implementation details.  The `test` directory contains unit tests that can be run using a testing framework like `pytest` (install with `pip install pytest`).
