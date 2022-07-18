# Installation

To execute the notebooks you will need to install a few libraries. I recommend installing [devbio-napari](https://github.com/haesleinhuepf/devbio-napari), which will include all the image analysis tools needed in napari. You can do this by creating a new conda environment:

```
conda create --name dask-processing-env python=3.9 devbio-napari -c conda-forge
```

If you have trouble installing it go to the [github page](https://github.com/haesleinhuepf/devbio-napari). Furthermore, you will need to install the functions included in this github repository. Navigate to your local folder of this repository in the command line, activate your environment and install it as follows:

```
conda activate dask-processing-env
pip install -e .
```
If you want to be able to display the dask graphs you have to additionally install graphviz. First install it to your system by downloading it from the [site](https://graphviz.org/download/). After installing it on your system you need to additionally install it in your environment as follows:

```
conda activate dask-processing-env
pip install graphviz
```

# Running the Notebooks

All notebooks and files to run them are located in the `docs` folder. If you follow the order of the notebooks there should not be any problems in running the code yourself. The only changes that need to be made in order to run them is modifying the location of the files that we process. Every time you see a folder location variable or zarr file location you need to add the locations specific to your system.