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

During the multi-agent Reinforcement Learning Process, it might be affected by a pathology called relative overgeneralization (RO). In joint action space, when sub-optimal Nash equilibrium are more preferred than optimal Nash equilibrium, the pathology of RO may occur.

This project used PyMARL framework to setup environment **Matrix Game** and **Predator Prey**, allows multi-agent play games in these environments, to demonstrate the patholog. 

In the experiments, I demonstrated that the two algorithms, VDN and QMIX, were indeed affected by RO. I then made modifications to the two algorithms within this project. Finally relieved the RO pathology.

Here is a structure diagram for better understanding PyMARL

![Pymarl structure](https://github.com/han-ziqi/PyMARL/raw/main/demo/PYMARL.jpg)

- The environment setup in [envs](https://github.com/han-ziqi/PyMARL/tree/main/src/envs)

- Agent is controled in [learners](https://github.com/han-ziqi/PyMARL/tree/main/src/learners)

## What does this experiment looks like

A complete experiment takes about two hours. After one experiment has been completed. The results of the experiment are automatically generated in the [sacred folder](https://github.com/han-ziqi/PyMARL/tree/main/results/sacred). I only uploaded five results for display use, while my complete project generated more than two hundred folders. 

The generated data is saved in a file named **info.json**, the raw data is difficult to measure, here is a demo.
![raw data](https://github.com/han-ziqi/PyMARL/raw/main/demo/Result%20data.png)

I need to extract the test_ep_lenth_mean and test_return_mean from each run to know the effect of this experiment. So I coded my own [plot.py](https://github.com/han-ziqi/PyMARL/blob/main/Plot.py) program to extract these results, calculate them and plot them as a diagram for display.

Here is a demo to show the diagram that used in the experiment.

![Relative overgeneralisation pathology](https://github.com/han-ziqi/PyMARL/raw/main/demo/RO%20happend.jpg)

##  What I learned from this experiment

1. At the time of the experiments started, PyTorch had just released support for Apple Silicon, and I was actively exploring solutions to various adaptation problems to finalize the experiments.
2. A valuable experience about getting familiar with a new framework from zero and understanding it.
3. Experience for development of a plotting program that can extract 5000 data at the same time, adding a 95% confidence interval, and draw them in a diagram

