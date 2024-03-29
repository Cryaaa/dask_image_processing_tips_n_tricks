"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    
    name='dask_image_procesing_tips_n_tricks',
    
    version='0.0.1',  
    
    description='A library containing useful functions and examples for timelapse processing with dask',  
    
    long_description=long_description,
    
    long_description_content_type='text/markdown',  
    
    url='https://github.com/Cryaaa/tribolium-clustering',  

    
    author='Ryan Savill',  

    
    author_email='ryan_george.savill@.tu-dresden.de',

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        

        # Pick your license as you wish
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='image, analysis',

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    #package_dir={'': 'src'},  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(),  # Required

    python_requires='>=3.7',

    install_requires=["dask","numpy",  "scikit-image", "zarr", "napari_workflows"],  

    project_urls={ 
        'Bug Reports': 'https://github.com/Cryaaa/dask_timelapse_processing_utilities/issuess',
        'Source': 'https://github.com/Cryaaa/dask_timelapse_processing_utilities',
    },
)