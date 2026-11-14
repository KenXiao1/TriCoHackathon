from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Create an entangled Bell state
qc.h(0)


# Measure both qubits and store the results in classical bits
qc.measure([0, 1], [0, 1])

# Display the quantum circuit
print(qc.draw())

# Run the circuit 1000 times using a local quantum simulator
simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()

# Retrieve and display the measurement counts
counts = result.get_counts()
print(counts)
