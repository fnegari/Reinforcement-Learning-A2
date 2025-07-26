# Reinforcement-Learning-A2
# Assignment 2 – Reinforcement Learning

This repository contains the full implementation and reports for **Assignment 2** of Reinforcement Learning.  
The assignment is divided into two main parts:

- **Part 1:** Value function estimation using Bellman Equations, Policy Iteration, and Value Iteration in a 5×5 Gridworld.
- **Part 2:** Monte Carlo methods and behaviour policies for a modified gridworld environment with terminal states.

---

## **1. Part 1 – Dynamic Programming Methods**

### **1.1 Overview**
In **Part 1**, we work with a **5×5 Gridworld environment** where:
- The agent can move **up, down, left, or right**.
- Rewards:
  - **+5** for reaching a high-value square (blue).
  - **+2.5** for a medium-value square (green).
  - **−0.5** penalty for hitting grid borders.
  - **0** for valid moves elsewhere.

The goal is to compute the **state-value function \( V(s) \)** and **optimal policy \( \pi(s) \)**.

We implement:
1. **Bellman Equations (explicit solution)**  
2. **Iterative Policy Evaluation (Policy Iteration)**  
3. **Value Iteration**

---

### **1.2 Results**
- **Value Functions:**  
  We visualize the value functions using heatmaps (Bellman, Policy Iteration, Value Iteration).  
- **Optimal Policies:**  
  Policies are displayed as arrows (↑, ↓, ←, →) for each grid cell.

**Sample Output (Value Iteration):**


---

## **2. Part 2 – Monte Carlo Methods**

### **2.1 Overview**
In **Part 2**, we use Monte Carlo methods to evaluate and improve policies in a modified gridworld environment:
- Certain cells are **terminal states** (black squares).
- Rewards:
  - **−0.2** for valid moves,
  - **−0.5** for attempts to move outside the grid,
  - **0** for terminal states.

We implement:
1. **Monte Carlo with Exploring Starts (MC-ES)**  
2. **Monte Carlo with ϵ-soft Policy (ε = 0.1)**  
3. **Behaviour Policy with Importance Sampling**

The discount factor:
\[
\gamma = 0.95
\]

---

### **2.2 Sample Output (MC-ES Value Function)**

