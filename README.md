# NeuNet

---

## History

Before starting this project, gosh I thought neural networks were these weird black magic thing.

But now? Now? NOW IK THEY ARE BLACK MAGIC WITH WEIGHTS!!!

Anyway, Idk why but ive gotten pretty interested in Ml, from that markov chain I built to this.

---

## What

It's s a linear linear linear neural networky thing.

So I made two.

One is a one hidden neuron model.

Basically it takes in 4 inputs and outputs one output.

The other one is a model that takes in 6 input and output's 6.

Let's talk about the one hidden neuron because it is simpler and reverser works basically the same as that just with more neurons and params.

It's in dir calculator/

It's goal: (a + b) - (c + d)

Basically the difference of the sum of two pairs.

A generator generates the training data. 

It generates something that looks like:

```f"{a},{b},{c},{d} = {ans}"```

It gets fed to the model.

The training loop adjusts the weights based on the learn rate.

It adjusts the weights like this:

weights += Loss x Input x Learn Rate (More info on calculator\main.py. just read the extremely long docstring)

and yea.

It does this till your desired target accuracy.

I set it to 100, it hits that in around 80 epochs.

The reverser's goal is to just reverse a 6-letter word.

It hits accuracy 100 in around 110 epochs.

## Project structure

```txt
calculator\
    main.py
    train_gen.py
reverser\
    main.py
    train_gen.py
README.md
```

## Definitions

- Neural network: A collection of simulated neurons
- Epoch: One complete pass through the ```train_data``` dataset
- Weight Update- ```Loss x Input x Learn rate```
- Loss: Determines the error of the model ```target - prediction```