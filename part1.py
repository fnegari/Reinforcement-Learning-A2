# -*- coding: utf-8 -*-
"""Part1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/196L8yQQg-Cs1ezVARxuhbG-jg1N89m_i
"""

import numpy as np

# Environment dimensions
env_size = 5
state_space = [(row, col) for row in range(env_size) for col in range(env_size)]
action_list = ['up', 'down', 'left', 'right']

# Initialize rewards and transition probabilities
reward_matrix = np.zeros((env_size, env_size))
transition_model = {}

for row in range(env_size):
    for col in range(env_size):
        transition_model[(row, col)] = {}
        for move in action_list:
            # Compute the next state based on the action
            if move == 'up':
                next_pos = (max(row - 1, 0), col)
            elif move == 'down':
                next_pos = (min(row + 1, env_size - 1), col)
            elif move == 'left':
                next_pos = (row, max(col - 1, 0))
            elif move == 'right':
                next_pos = (row, min(col + 1, env_size - 1))

            # Special squares and rewards
            if (row, col) == (0, 1):  # Blue square
                transition_model[(row, col)][move] = [(3, 2)], 5
            elif (row, col) == (0, 4):  # Green square
                transition_model[(row, col)][move] = [(3, 2), (4, 4)], 2.5
            elif (row, col) == next_pos:  # Border of the grid
                transition_model[(row, col)][move] = [next_pos], -0.5
            else:
                transition_model[(row, col)][move] = [next_pos], 0

def bellman_solver(state_space, transition_model, gamma=0.95):
    """
    Solve the Bellman equations for the given gridworld.
    :param state_space: List of all states
    :param transition_model: Transition model dict
    :param gamma: Discount factor
    :return: Value function matrix
    """
    n_states = len(state_space)
    A = np.zeros((n_states, n_states))
    b = np.zeros(n_states)

    for idx, s in enumerate(state_space):
        A[idx, idx] = 1  # Set diagonal element
        for move in action_list:
            next_states, r = transition_model[s][move]
            # Check if multiple next states exist
            prob = 1 / len(next_states)
            for nxt in next_states:
                nxt_idx = state_space.index(nxt)
                A[idx, nxt_idx] -= prob * gamma / len(action_list)
                b[idx] += prob * r / len(action_list)

    value_vector = np.linalg.solve(A, b)
    return value_vector.reshape((env_size, env_size))

v_function = bellman_solver(state_space, transition_model)
print(v_function)

def iterative_policy_evaluation(states, transitions, gamma=0.95, theta=0.01):
    V = np.zeros((grid_size, grid_size))
    delta = float('inf')

    while delta > theta:
        delta = 0
        for state in states:
            i, j = state
            old_value = V[i, j]
            new_value = 0

            for action in actions:
                next_states, reward = transitions[state][action]

                # Calculate expected value for this action
                expected_v = 0
                for ns in next_states:
                    expected_v += V[ns]  # ns is a tuple (i,j)
                expected_v /= len(next_states)  # Average over possible next states

                # Add contribution from this action
                new_value += 0.25 * (reward + gamma * expected_v)

            # Update value and track maximum change
            V[i, j] = new_value
            delta = max(delta, abs(old_value - new_value))

    return V

value_function_2 = iterative_policy_evaluation(states, transitions)
print(value_function_2)

def evaluate_policy_iteratively(state_space, transition_model, gamma=0.95, epsilon=0.01):
    """
    Iterative policy evaluation for a uniform random policy.
    :param state_space: List of all states in the grid
    :param transition_model: Transition probabilities and rewards
    :param gamma: Discount factor
    :param epsilon: Convergence threshold
    :return: Value function matrix
    """
    value_grid = np.zeros((env_size, env_size))  # Initialize all state values to zero
    max_change = float('inf')

    while max_change > epsilon:
        max_change = 0
        for s in state_space:
            old_value = value_grid[s]
            value_grid[s] = 0  # Reset current value to recalculate

            # Evaluate all possible actions (equiprobable policy)
            for move in action_list:
                next_states, reward = transition_model[s][move]

                # Compute expected value based on next states
                if isinstance(next_states, list):
                    avg_val = sum(value_grid[ns] for ns in next_states) / len(next_states)
                else:
                    avg_val = value_grid[next_states]

                value_grid[s] += 0.25 * (reward + gamma * avg_val)

            max_change = max(max_change, abs(old_value - value_grid[s]))
    return value_grid

v_function_2 = evaluate_policy_iteratively(state_space, transition_model)
print(v_function_2)

def compute_value_iteration(state_space, transition_model, gamma=0.95, epsilon=0.01):
    """
    Value Iteration algorithm to compute the optimal value function.
    :param state_space: List of all states in the gridworld
    :param transition_model: Transition probabilities and rewards
    :param gamma: Discount factor
    :param epsilon: Threshold for convergence
    :return: Optimal value function matrix
    """
    value_grid = np.zeros((env_size, env_size))  # Start with zero values
    max_change = float('inf')

    while max_change > epsilon:
        max_change = 0
        for s in state_space:
            prev_val = value_grid[s]
            q_values = []  # Store action values for the current state

            # Evaluate all possible actions
            for move in action_list:
                next_states, reward = transition_model[s][move]

                # If multiple next states, calculate expected value
                if isinstance(next_states, list):
                    exp_val = sum(reward + gamma * value_grid[ns] for ns in next_states) / len(next_states)
                else:
                    exp_val = reward + gamma * value_grid[next_states]

                q_values.append(exp_val)

            # Choose the best action value
            value_grid[s] = max(q_values)
            max_change = max(max_change, abs(prev_val - value_grid[s]))
    return value_grid

v_function_3 = compute_value_iteration(state_space, transition_model)
print(v_function_3)

import matplotlib.pyplot as plt
import seaborn as sns

# Initialize figure and axes
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Heatmap for Bellman solution
sns.heatmap(v_function, ax=axes[0], annot=True, cmap='viridis', fmt=".2f")
axes[0].set_title('Bellman Solution (Explicit)')

# Heatmap for Iterative Policy Evaluation
sns.heatmap(v_function_2, ax=axes[1], annot=True, cmap='viridis', fmt=".2f")
axes[1].set_title('Iterative Policy Evaluation')

# Heatmap for Value Iteration
sns.heatmap(v_function_3, ax=axes[2], annot=True, cmap='viridis', fmt=".2f")
axes[2].set_title('Value Iteration Results')

# Display all plots
plt.tight_layout()
plt.show()

# Find the highest value in the Bellman value function
max_val_bellman = np.max(v_function)
best_states_bellman = np.argwhere(v_function == max_val_bellman)

print("Maximum Value (Bellman):", max_val_bellman)
print("States with Maximum Value (Bellman):", best_states_bellman)

# Find the maximum value in the Iterative Policy Evaluation result
max_val_iterative = np.max(v_function_2)
best_states_iterative = np.argwhere(v_function_2 == max_val_iterative)

print("Maximum Value (Iterative):", max_val_iterative)
print("States with Maximum Value (Iterative):", best_states_iterative)

# Find the maximum value in the Value Iteration result
max_val_vi = np.max(v_function_3)
best_states_vi = np.argwhere(v_function_3 == max_val_vi)

print("Maximum Value (Value Iteration):", max_val_vi)
print("States with Maximum Value (Value Iteration):", best_states_vi)

def derive_policy_from_values_with_arrows(state_space, transition_model, V, gamma=0.95):
    """
    Derive an optimal policy represented with arrows instead of action names.
    """
    arrow_map = {'up': '↑', 'down': '↓', 'left': '←', 'right': '→'}
    policy = np.full((env_size, env_size), '', dtype=object)

    for r in range(env_size):
        for c in range(env_size):
            state = (r, c)
            best_action = None
            best_value = -float('inf')

            for move in action_list:
                next_states, reward = transition_model[state][move]

                if len(next_states) > 1:  # Probabilistic outcomes
                    avg_val = sum(V[ns] for ns in next_states) / len(next_states)
                    action_val = reward + gamma * avg_val
                else:
                    ns = next_states[0]
                    action_val = reward + gamma * V[ns]

                if action_val > best_value:
                    best_value = action_val
                    best_action = move

            policy[r, c] = arrow_map[best_action]

    return policy

# Derive and display the policy with arrows
policy_with_arrows = derive_policy_from_values_with_arrows(state_space, transition_model, v_function)
print(policy_with_arrows)

def value_iteration_and_policy_improvement(states, transitions, gamma=0.95, theta=0.01):
    """
    Value Iteration combined with Policy Improvement.
    Returns optimal policy and value function.
    """
    V = np.zeros((grid_size, grid_size))
    policy = np.full((grid_size, grid_size), '', dtype=object)
    arrow_map = {'up': '↑', 'down': '↓', 'left': '←', 'right': '→'}

    while True:
        delta = 0
        for state in states:
            current_val = V[state]
            best_action = None
            best_value = -float('inf')

            # Evaluate all possible actions
            for action in actions:
                action_val = 0
                next_states, reward = transitions[state][action]
                prob = 1 / len(next_states)
                action_val = sum(prob * (reward + gamma * V[ns]) for ns in next_states)

                if action_val > best_value:
                    best_value = action_val
                    best_action = action

            V[state] = best_value
            policy[state] = arrow_map[best_action]  # Store arrow instead of action text
            delta = max(delta, abs(current_val - best_value))

        if delta < theta:
            break

    return policy, V


# Run Value Iteration + Policy Improvement
vi_optimal_policy, optimal_values_vi = value_iteration_and_policy_improvement(states, transitions)
print(vi_optimal_policy)

def value_iteration_with_policy(states_list, transition_map, gamma=0.95, epsilon=0.01):
    """
    Value Iteration combined with policy extraction.
    Finds the optimal value function and policy.
    """
    value_grid = np.zeros((grid_size, grid_size))
    policy_grid = np.zeros((grid_size, grid_size), dtype=object)

    while True:
        max_delta = 0
        for s in states_list:
            prev_val = value_grid[s]
            best_val = -float('inf')
            best_action = None

            # Check all actions for current state
            for act in actions:
                total_val = 0
                next_states, reward = transition_map[s][act]
                for ns in next_states:
                    prob = 1 / len(next_states)
                    total_val += prob * (reward + gamma * value_grid[ns])

                if total_val > best_val:
                    best_val = total_val
                    best_action = act

            value_grid[s] = best_val
            policy_grid[s] = best_action
            max_delta = max(max_delta, abs(prev_val - best_val))

        # Stop when value updates are small enough
        if max_delta < epsilon:
            break

    return policy_grid, value_grid


# اجرای Value Iteration
vi_policy, vi_values = value_iteration_with_policy(states, transitions)
print(vi_policy)

import matplotlib.pyplot as plt
import numpy as np

def show_policy(policy_matrix, title="Optimal Policy"):
    """
    Display a policy grid (5x5) as arrows.
    Supports both action names ('up','down','left','right')
    and arrow symbols ('↑','↓','←','→').
    """
    grid_size = policy_matrix.shape[0]

    # Action directions
    directions = {
        'up': (0, 1),
        'down': (0, -1),
        'left': (-1, 0),
        'right': (1, 0),
        '↑': (0, 1),
        '↓': (0, -1),
        '←': (-1, 0),
        '→': (1, 0)
    }

    # Create figure
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-0.5, grid_size - 0.5)
    ax.set_ylim(-0.5, grid_size - 0.5)
    ax.grid(which='major', color='black', linestyle='-', linewidth=2)

    # Configure grid
    ax.set_xticks(np.arange(0, grid_size, 1))
    ax.set_yticks(np.arange(0, grid_size, 1))
    ax.xaxis.tick_top()
    ax.invert_yaxis()
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Plot arrows
    for row in range(grid_size):
        for col in range(grid_size):
            act = policy_matrix[row][col]
            if act in directions:
                dx, dy = directions[act]
                ax.arrow(col, row, dx * 0.3, dy * 0.3,
                         color='blue', head_width=0.2, head_length=0.2)

    plt.title(title)
    plt.show()


# Visualizing each policy
show_policy(bellman_optimal_policy, "Policy 1: Bellman Optimality Equation")
show_policy(pi_policy, "Policy 2: Policy Iteration")
show_policy(vi_policy, "Policy 3: Value Iteration")