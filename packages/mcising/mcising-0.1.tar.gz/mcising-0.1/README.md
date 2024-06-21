# mcising

mcising is a Python package for generating Ising model data using Monte Carlo simulations.

## Installation

You can install the package using pip:

`pip install mcising`

## Usage

You can generate Ising model data from the command line:

`generate_ising_data <seed> <lattice_size> <num_configs> <j1> <j2> [--T_init <T_init>] [--T_final <T_final>] [--T_step <T_step>] [--sweep_steps <sweep_steps>] [--thermalization_scans <thermalization_scans>] [--calculate_correlation]`

An example usage:

`generate_ising_data 42 10 100 1.0 0.5 --T_init 4.0 --T_final 0.1 --T_step 0.05 --sweep_steps 10 --thermalization_scans 5 --calculate_correlation`

## Licence

This project is licensed under the MIT License.
