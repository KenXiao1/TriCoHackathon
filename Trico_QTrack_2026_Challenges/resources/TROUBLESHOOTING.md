# Quick troubleshooting

- **`ModuleNotFoundError: qiskit` / `qiskit_aer`:** run the installation cell; restart runtime if needed. A connection is required for first-time installs.
- **`ValueError` about parameters:** use the required bitstring (`00`, `01`, `10`, `11`), integer shots, or supported n=3/4.
- **Can't draw circuits:** use `.draw(output='text')` (no optional drawing packages needed).
- **Probabilities seem reversed:** qubit 0 is the rightmost bit of an output bitstring.
- **Measurement results vary:** shot counts are random; use the specified `seed_simulator` for a repeatable example. Statistical checks allow tolerance.
- **A self-check says unfinished:** replace the `return None` placeholder in the relevant task.
- **Noise mitigation gives negatives before clipping:** finite-sample estimates can do this; the Level 3 algorithm clips and renormalizes, which is a simplification you should acknowledge.
- **Colab session disconnects:** download your notebook regularly; save a copy to Drive if you want persistence.
- **No credit card / hardware:** none is needed for the required challenges. All required exercises use local simulation.

Documentation: https://quantum.cloud.ibm.com/docs/en/guides
