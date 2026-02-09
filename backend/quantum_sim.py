try:
    from qiskit import QuantumCircuit
    from qiskit_aer import Aer
    from qiskit import transpile
    from qiskit.visualization import plot_histogram
except ImportError:
    # Fallback/Mock if Qiskit not installed in environment
    print("Qiskit not found. Using mock simulation.")

import random

def run_quantum_simulation():
    """
    Runs a simple Bell State simulation to test entanglement.
    Returns a dictionary with measurement counts.
    """
    try:
        # Create a Quantum Circuit acting on the q register
        circuit = QuantumCircuit(2, 2)
        
        # Add a H gate on qubit 0
        circuit.h(0)
        
        # Add a CX (CNOT) gate on control qubit 0 and target qubit 1
        circuit.cx(0, 1)
        
        # Map the quantum measurement to the classical bits
        circuit.measure([0, 1], [0, 1])
        
        # Use Aer's qasm_simulator
        simulator = Aer.get_backend('qasm_simulator')
        
        # Transpile the circuit for the simulator
        compiled_circuit = transpile(circuit, simulator)
        
        # Run the simulation
        job = simulator.run(compiled_circuit, shots=1000)
        
        # Get the result
        result = job.result()
        
        # Returns counts, e.g., {'00': 500, '11': 500}
        counts = result.get_counts(compiled_circuit)
        
        # Calculate a 'coherence' score based on how close it is to ideal Bell state
        total_shots = sum(counts.values())
        ideal_states = counts.get('00', 0) + counts.get('11', 0)
        coherence_score = ideal_states / total_shots
        
        return {
            "counts": counts,
            "coherence_score": coherence_score,
            "status": "Success"
        }

    except Exception as e:
        # Mock result if actual simulation fails or libraries missing
        print(f"Quantum simulation failed: {e}. Returning mock data.")
        return {
            "counts": {'00': 490, '11': 510},
            "coherence_score": 0.98,
            "status": "Simulated (Fallback)"
        }
