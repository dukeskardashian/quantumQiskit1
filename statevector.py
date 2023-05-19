from qiskit import QuantumCircuit, Aer, execute

# Erstellen eines Quanten-Schaltkreises
qc = QuantumCircuit(2, 2)
qc.h(0)  # Anwenden der Hadamard-Operation auf Qubit 0
qc.cx(0, 1)  # Anwenden der CNOT-Operation zwischen Qubit 0 (Kontroll-Qubit) und Qubit 1 (Ziel-Qubit)

# Simulation der Quantenverschränkung
simulator = Aer.get_backend('statevector_simulator')
job = execute(qc, simulator)
result = job.result()
statevector = result.get_statevector()

# Ausgabe des Zustandsvektors
print('Zustandsvektor:', statevector)
