# Interconnect-Analysis-5LIE0
Analysis of multiple interconnect forms, namely the bus, mesh, torus and fat-tree

## Project Summary

This project explores how different Network-on-Chip (NoC) topologies behave under varying traffic conditions. Specifically, it looks at how send rate and latency change when we adjust the link load and buffer sizes.

The main focus is on simulating and comparing several common NoC topologies:

* Bus
* Mesh
* Fat-Tree (multiple variants: by degree, buffer, and layers)

Some support for Torus is outlined but not yet implemented.



## What This Notebook Does

The Jupyter notebook runs a batch of POOSL simulations using parameterized models. It:

* Varies model parameters like topology, buffer size, and link load
* Runs the simulations in parallel
* Collects output data (from `.log` files)
* Extracts send rate and latency numbers from each run
* Organizes the results using Pandas
* Generates plots showing performance trends
* Saves everything for later


## How to Use It

1. Choose a topology
   Inside the notebook, set the `template_name` to one of:

   ```python
   template_name = "bus"
   # or: "mesh", "tree_buffers", "tree_layers", "tree_degrees"
   ```

2. Set your model path
   Make sure the `model_path` points to where your POOSL models are located:

   ```python
   model_path = Path("../model").resolve()
   ```

3. Run the notebook
   It will:

   * Launch all simulations
   * Store logs in the `output/` folder
   * Create graphs (e.g. latency vs link load)



## Dependencies

This project requires:

* Python 3.x
* Rotalumis
* Python packages:

  * `numpy`
  * `pandas`
  * `matplotlib`
  * `tqdm`

## Background

This project is based on simulations and findings described in the accompanying report:


## Notes and Limitations

* The mesh and fat-tree models are more complex and may run into deadlocks.
* The torus topology is described in the paper but wasn’t implemented in time.
* The experiments focus on synthetic traffic and parameter sweeps—not real workloads.
