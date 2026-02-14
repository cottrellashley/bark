---
title: "Quantum Simulator"
tags: [python, physics]
description: "A lightweight quantum circuit simulator for educational use. Simulates qubit operations, entanglement, and measurement on up to 12 qubits."
---

# Quantum Simulator

A Python-based quantum circuit simulator built for learning and experimentation.

## Overview

This simulator models quantum circuits using state vectors and matrix operations. It supports common gates (Hadamard, CNOT, Pauli, Toffoli) and provides visualisation of quantum states.

## Example

```python
from qsim import Circuit

c = Circuit(2)
c.h(0)       # Hadamard on qubit 0
c.cnot(0, 1) # Entangle qubits 0 and 1
result = c.measure()
print(result) # {'00': 512, '11': 488}
```

## Key Design Decisions

- State vector representation (not density matrix) for speed
- Sparse matrix gates for memory efficiency
- NumPy backend with optional GPU acceleration
