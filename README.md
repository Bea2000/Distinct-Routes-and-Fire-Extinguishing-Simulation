# Distinct Routes and Fire Extinguishing Simulation

## Context

This project was developed as part of the Design and Analysis of Algorithms course at Pontificia Universidad Católica de Chile during the second semester of 2023. The objective was to solve two algorithmic problems, focusing on route counting and optimal strategies for emergency response in a simulated environment.

## Objectives

1. **Problem 1: Distinct Routes to University**
   - Calculate the number of distinct tram routes Alicia can take from her house to the university, considering multiple tram lines.
  
2. **Problem 2: Fire Extinguishing Simulation**
   - Determine the minimum time required for a team of park rangers to extinguish all fire spots in a national park, using a greedy algorithm approach.

## Requirements

- Python 3.x
- Standard input for testing
- Basic understanding of dynamic programming and greedy algorithms

## Problem Descriptions

### Problem 1: Distinct Routes

- **Input**: 
  - Two integers `N` and `M` where `N` is the block number of the university and `M` is the number of trams.
  - Followed by `M` pairs of integers `(li, ri)` indicating the start and end blocks of each tram.
  
- **Output**: 
  - An integer representing the total number of distinct routes modulo \(10^9 + 9\).
  
- **Constraints**: 
  - \(1 \leq N \leq 10^9\)
  - \(1 \leq M \leq 10^5\)

### Problem 2: Fire Extinguishing Simulation

- **Input**: 
  - Two integers `N` and `M` where `N` is the number of park rangers and `M` is the number of fire spots.
  - The positions of the park rangers and the fire spots in sorted order.
  
- **Output**: 
  - An integer indicating the minimum number of minutes required to extinguish all fires.
  
- **Constraints**: 
  - \(1 \leq N, M \leq 10^5\)

## Running the Project

To run the project, make sure you have Python installed on your machine. You can test the program with the following command, where `input_XX.txt` is the file containing valid input for either problem:

```bash
python pX/pX.py < input_XX.txt
```

## Complexity Analysis

- Problem 1 Complexity: The expected complexity is **O(M⋅log(M))** due to the dynamic programming approach utilized to count distinct routes.
- Problem 2 Complexity: The expected complexity is **O((N+M)⋅log(max(gi,fi)))**, achieved through a greedy algorithm to efficiently match park rangers to fire spots.

## Example Inputs and Outputs

### Problem 1 Example

#### Input

```plaintext
3 3
0 1
1 2
2 3
```

#### Output

```plaintext
1
```

### Problem 2 Example

#### Input

```plaintext
2 2
3 4
1 10
```

#### Output

```plaintext
6
```
