# Quantum computing resources

- [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning) — guided introductions to quantum circuits, superposition and entanglement.
- [Official Qiskit quickstart](https://quantum.cloud.ibm.com/docs/en/guides/quick-start) — create and execute your first circuit.
- [Construct circuits in Qiskit](https://quantum.cloud.ibm.com/docs/en/guides/construct-circuits) — gates, measurement and classical registers.
- [Qiskit programming guides](https://quantum.cloud.ibm.com/docs/en/guides) — documented APIs.
- [Qiskit Aer simulation](https://quantum.cloud.ibm.com/docs/en/guides/simulate-with-qiskit-aer) — exact and noisy simulation.
- [Noise models](https://quantum.cloud.ibm.com/docs/en/qiskit/build-noise-models) — advanced material for Level 3.
- [Google Colab](https://colab.research.google.com/) — browser-based notebook execution.

You do **not** need an IBM Quantum account to solve these challenges. All tasks use local simulation. 

## Concept reminders

- **Qubit:** a quantum two-level system; here represented by a vector of two complex amplitudes.
- **Gate:** a unitary transformation of quantum state amplitudes.
- **Measurement:** turns amplitudes into sampled classical outcomes according to probabilities.
- **Relative phase:** can affect interference even when immediate Z-basis probabilities look unchanged.
- **Entanglement:** correlations in a joint quantum state not expressible as independent states for each qubit.
- **Oracle:** a reversible phase marking operation in Grover search.
- **Noise:** a model of errors in gates and measurements; simulation parameters are not automatically hardware measurements.

## Bitstring notation
Qiskit displays qubit 0 as the **rightmost** bit in printed bitstrings. The label `01` corresponds to qubit 1 = 0, qubit 0 = 1.
