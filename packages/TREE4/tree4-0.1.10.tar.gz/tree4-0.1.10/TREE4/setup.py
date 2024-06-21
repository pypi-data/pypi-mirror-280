from setuptools import setup, find_packages

VERSION = '0.1.10' 
DESCRIPTION = 'Standard and Non-Standard Tree Based Methods'
LONG_DESCRIPTION = 'The library contains standard CART based methologies for growing trees, includind twoing, as well as non standard techniques two-stage techniques like fast and latent-budget tree. There is also cross validation methods for pruning the tree, and k-folds implementation. As well as a graphical interface to view the tree and information about the nodes, including visual pruning by viewing thhe decrease in deviance created by a split relative to other splits in the grown tree, and an output table containing useful information. For more information and examples please see: https://github.com/danielchfynn/TREE4'

# Setting up
setup(
        name="TREE4", 
        version=VERSION,
        author="Daniel Fynn",
        author_email="<df390@uowmail.edu.au>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        
        keywords=['python', 'tree', 'CART'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)