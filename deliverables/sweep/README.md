# How to use

The recommended way is to install all the dependencies using **poetry**. Make sure you have `jupyter`, `matplotlib`, `tqdm`, `pandas`, and `numpy` installed (via poetry, Anaconda, Miniconda, or pip). For more information about how to install poetry see https://python-poetry.org/.

Extract all files to a folder of your choice (e.g. C:/multiprocessors/python_sweep/)

# Poetry + VS Code

If you use poetry, from a command line, go to the folder where the `pyproject.toml` is located and type:

    poetry install

This will install all dependencies. Then using the Jupyter and Python extensions of VS Code select the proper python installation to the one created by poetry. You can find it by running

    poetry env info --path

# Usage from the command line

From a command line, run the following command:

    poetry run jupyter notebook --notebook-dir=<path_to_notebook>
 
for the example directory given above, the full command is: 

    poetry run jupyter notebook --notebook-dir=C:/multiprocessors/python_sweep/


## Jupyter

After some time, a new browser window will appear. Open the `analysis.ipynb` notebook, and select <kbd>Cell</kbd> ➞ <kbd>Run All</kbd> to run the experiment and generate the output graphs.

Check the [jupyter documentation](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html) on  for an introduction of how to use Jupyter notebooks.

# Rotalumis Runner

The Rotalumis runner is used to run POOSL models. It is used in the `run_network_model.py` module, which creates system instances by replacing parameters.

The replacement occurs on a text-basis. The template contains references to e.g. `{params[numberOfNodes]}` which are replaced in the script by the actual value.

The files `bus_template.poosl` and `analysis.ipynb` show an example of how this mechanism can be used to automate experiments.