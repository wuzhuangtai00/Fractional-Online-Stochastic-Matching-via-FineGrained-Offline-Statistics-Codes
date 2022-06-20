# Intro

This is the code that generate all numerical results of our paper [(Fractional) Online Stochastic Matching via Fine-Grained Offline
Statistics](https://dl.acm.org/doi/pdf/10.1145/3519935.3519994).

There are two parameters in the code.  n  denotes the number of vertices and $\mathrm{ratio}$ denotes the accuracy of the result. This means that w.h.p. the numerical result has a multiplicative error of at most $1 - \mathrm{ratio}$. Such accuracy is guaranteed by Chernoff bound.

For the numerical results in our paper, we choose  n = 1000  and $\mathrm{ratio} = 0.99$. It takes roughly several hours to run on my laptop.
