# quantumQiskit1
Simulation of quantum entanglement of two qubits using the Qiskit framework.

Here we use the Qiskit framework to create a quantum circuit with two qubits. We apply the Hadamard operation (qc.h(0)) to the first qubit to put it in a state of superposition, and then the CNOT operation (qc.cx(0, 1)) between the first and second qubits to create entanglement.

The simulation is performed using the statevector_simulator of Qiskit. The state vector of the system after quantum entanglement is retrieved and output via result.get_statevector()
