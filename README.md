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

[[ 3.42 4.15 4.88 5.12 6.73]
[ 2.89 3.52 3.94 4.02 4.88]
[ 2.21 2.88 3.12 3.22 3.55]
[ 1.72 2.11 2.32 2.42 2.63]
[ 1.42 1.92 2.11 2.19 2.37]]
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
[[-1.64 -1.79 -1.91 -1.83 -1.67]
[-0.87 -1.31 -1.49 -1.33 -0.87]
[ 0.00 -0.71 -1.12 -0.80 0.00]
[-0.16 -0.72 -1.15 -1.14 -0.77]
[ 0.00 -0.62 -1.22 -1.45 -1.44]]

---

## **3. Repository Structure**


Assignment2/
├── part1.py # Code for Part 1 (Bellman, Policy Iteration, Value Iteration)
├── part2.py # Code for Part 2 (MC-ES, ϵ-soft, Behaviour Policy)
├── figures/ # Saved heatmaps and policy plots
│ ├── policy1.png
│ ├── policy2.png
│ ├── policy3.png
│ ├── value_bellman.png
│ ├── value_policy_iteration.png
│ └── value_value_iteration.png
├── report/
│ ├── main.tex # LaTeX source of the final report
│ └── Reinforcement-Learning-A2.pdf # Compiled report (PDF)
└── README.md # Project documentation

---

## **4. Setup Instructions**

### **4.1 Install Dependencies**
```bash
pip install numpy matplotlib seaborn
4.2 Run the Code
For Part 1:

python part1.py
For Part 2:
python part2.py
6. Reports
Full details of the methods, results, and analysis are provided in report/Reinforcement-Learning-A2.pdf.

The LaTeX source is included for reproducibility.


7. Authors
Fatemeh Negari

Saba Tamizi

8. License
This repository is part of Reinforcement Learning: Assignment 2 (2025) and is intended solely for educational purposes.


