```diff

```

### This is a branch from PyMARL framework

```

```

## Python MARL framework

PyMARL is [WhiRL](http://whirl.cs.ox.ac.uk)'s framework for deep multi-agent reinforcement learning and includes implementations of the following algorithms:

- [**QMIX**: QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1803.11485)
- [**COMA**: Counterfactual Multi-Agent Policy Gradients](https://arxiv.org/abs/1705.08926)
- [**VDN**: Value-Decomposition Networks For Cooperative Multi-Agent Learning](https://arxiv.org/abs/1706.05296) 
- [**IQL**: Independent Q-Learning](https://arxiv.org/abs/1511.08779)
- [**QTRAN**: QTRAN: Learning to Factorize with Transformation for Cooperative Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1905.05408)

PyMARL is written in PyTorch and uses [SMAC](https://github.com/oxwhirl/smac) as its environment.

---

## About this Project

This project used PyMARL framework to setup environment **Matrix Game** and **Predator Prey**, allows multi-agent play games in these environments, to demonstrate the patholog. 

Here is a structure diagram for better understanding PyMARL

![]

- The environment setup in [envs](https://github.com/han-ziqi/PyMARL/tree/main/src/envs)

- Agent is controled in [learners](https://github.com/han-ziqi/PyMARL/tree/main/src/learners)

## What does this experiment looks like

A complete experiment takes about two hours. After one experiment has been completed. The results of the experiment are automatically generated in the [sacred folder](https://github.com/han-ziqi/PyMARL/tree/main/results/sacred). I only uploaded five results for display use, while my complete project generated more than two hundred folders. 

I need to extract the test_ep_lenth_mean and test_return_mean from each run to know the effect of this experiment. So I coded my own [plot.py](https://github.com/han-ziqi/PyMARL/blob/main/Plot.py) program to extract these results, calculate them and plot them as a diagram for display.

Here is a demo to show the diagram that used in the experiment.

![]

##  What the experiment has done for me

1. At the time of the experiments started, PyTorch had just released support for Apple Silicon, and I was actively exploring solutions to various adaptation problems to finalize the experiments.
2. A valuable experience about getting familiar with a new framework from zero and understanding it.

