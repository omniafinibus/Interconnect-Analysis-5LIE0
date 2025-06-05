# import the convenience utility to run parameterized POOSL models
from Rotalumis import rotalumisrunner
import os

def run_network_model(p):
    """Create a network model by using the elements of a POOSL network library, 
    given a template for the network, the nodes and its channels. The created 
    model is run through the rotalumisrunner.
    Returns True when the model terminated correctly, and False otherwise.
    
    The output of the Rotalumis session is printed to the IPython notebook.
    """
    # convert the given network_model system instance template into a full-fledged system instance with the given system-level parameters
    model_library_paths, network_model, parameters, output_directory = p
    model = network_model.format(params=parameters)

    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)
    
    # write the model to a temporary file
    temp_filename = os.path.join(output_directory, 'model.poosl')
    
    with open(temp_filename, 'w') as output:
        output.write(model)
    
    # run the generated model by running Rotalumis on the generated system instance, with the provided model library paths
    return rotalumisrunner.runrotalumis(os.path.abspath(temp_filename), output_directory, model_library_paths), parameters, output_directory
