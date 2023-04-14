## About this Project

This is my personal research project, utilizes the [PyMARL framework](https://github.com/oxwhirl/pymarl) to setup environment Matrix Game and Predator Prey, allows multi-agent play games in these environments, to demonstrate the patholog.  The project’s technological stack comprises of **Python** and **PyTorch**.

I show the influence of the relative overgeneralization pathology for the VDN and QMIX algorithms, a phenomenon where an agent’s behavior becomes overly influenced by the actions of its teammates, leading to suboptimal decision-making. Then I modified these algorithm to address the pathology.

VDN (Value-Decomposition Networks) is a multi-agent reinforcement learning algorithm that decomposes the centralized value function into a sum of individual value functions, enabling agents to make decentralized decisions.
QMIX (Q-value Mixing) is a variant of VDN that uses a monotonic mixing function to improve the performance of the algorithm.

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

