import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, transpile
from qiskit.tools.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi
from qiskit_textbook.games import hello_quantum

"""
Here's what we should attempt: implement a simulation of
a surface code.
"""

sim = Aer.get_backend('qasm_simulator')

initialize = []
success_condition = {}
allowed_gates = {'0': {'NOT': 3}, '1': {}, 'both': {}}
vi = [[1], False, False]
qubit_names = {'0':'the only bit', '1':None}
puzzle = hello_quantum.run_game(initialize, success_condition, allowed_gates, vi, qubit_names)