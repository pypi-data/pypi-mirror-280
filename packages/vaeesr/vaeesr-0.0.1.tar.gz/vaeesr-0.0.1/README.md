# Variational Autoencoder Embeddings Symbolic Regression (VAEESR)

This python package performs Symbolic Regression by creating an Embedding where semantically similar equations are close to each other and it uses MCMC sampling to find the equation that is the closest to the oberved data. Therefore, is uses three main functions: 

1. `create_dataset` which creates a customizable dataset that can be ajusted for the specific problem at hand. The main parameters are: The x_values for which the functions are evaluated, the range of constants, the maximum tree depth, the possible operators and functions and the total number of equations in the dataset.

2. `create_autoencoder` which trains an autoencoder with the dataset. The some hyperparameters can be ajdusted as well. 

3. `perform_MCMC` which performs the symbolic regression by sampling equations from the autoencoder embedding. 

## Install 
`pip install vaeesr`

## Tutorial
There are three main function:
1. create_dataset()
2. create_autoencoder()
3. perform_MCMC()

### 1. Create Dataset
The dataset is customizable and can be tuned to the problem and create an antoencoder that fits the problem at hand. `create_dataset` takes the follwing arguments with their default values. 

### 2. Create Autoencoder
The created dataset can be used to train the autoencoder. 