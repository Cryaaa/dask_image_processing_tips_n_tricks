import warnings
import numpy as np
from functools import wraps
from napari_workflows._workflow import is_image
from toolz import curry
from skimage.io import imread
from skimage.io.collection import alphanumeric_key
from dask import delayed
import dask.array as da
from glob import glob
import pyclesperanto_prototype as cle

def make_dask_stack_from_folder(folder: str, prefix: str):
    """
    Returns a dask stack of images oaded from a folder with a prefix 
    before the alphanumeric index. Copied from the napari documentation:
    https://napari.org/tutorials/processing/dask.html
    
    Parameters
    ----------
    folder: str
        path to the folder including slashes before file name
    prefix: str
        filename with is in front of the alphanumeric index
        must be a .tif file
    """
    filenames = sorted(glob(folder + prefix + "*.tif"), key=alphanumeric_key)
    # read the first file to get the shape and dtype
    # ASSUMES THAT ALL FILES SHARE THE SAME SHAPE/TYPE
    sample = imread(filenames[0])

    lazy_imread = delayed(imread)  # lazy reader
    lazy_arrays = [lazy_imread(fn) for fn in filenames]
    dask_arrays = [
        da.from_delayed(delayed_reader, shape=sample.shape, dtype=sample.dtype)
        for delayed_reader in lazy_arrays
    ]
    # Stack into one large dask.array
    return da.stack(dask_arrays, axis=0)

# TODO docstring
# Inspired by notebook by Talley Lambert:
# https://github.com/tlambert03/napari-dask-example/blob/8e41a78b7415ee9e3d4867c68ae3d93314bf1307/dask_napari.ipynb
@curry
def dask_clesperanto_adapter(function):

    @wraps(function)
    def worker_function(*args, **kwargs):
        new_args = []
        new_kwargs = {}
        extras = []
        for arg in args:
            if is_image(arg):
                if arg.ndim >3:
                    modified_array = np.squeeze(arg[...,:,:,:]) 
                    extras.append(arg.ndim - modified_array.ndim)
                    new_args.append(modified_array)
                    continue
            new_args.append(arg)
                    
        for key,value in kwargs.items():    
            if is_image(value):
                if value.ndim >3:
                    modified_array = np.squeeze(value[...,:,:,:]) 
                    extras.append(value.ndim - modified_array.ndim)
                    new_kwargs[key] = modified_array
                    continue
            new_kwargs[key] = value
        
        new_args = tuple(new_args)
        result = cle.pull(function(*new_args, **new_kwargs))
        if extras:
            for i in range(min(extras)):
                result = result[None, ...]
        return result
    
    return worker_function

# TODO docstring and needs to become more general
@dask_clesperanto_adapter
def single_input_single_output_workflow_applier(input_image, workflow):
    from napari_workflows._undo_redo_functionality import copy_workflow_state
    if len(workflow.roots()) != 1 or len(workflow.leafs()) != 1:
        warnings.warn('Workflow Must Have Only 1 Input and 1 Output!')
        return
    new_workflow = copy_workflow_state(workflow)
    new_workflow.set(workflow.roots()[0],input_image)
    
    return np.array(new_workflow.get(workflow.leafs()[0]))

