# Nirpy Research
Snippets and data from the blog of [Nirpy Research](https://nirpyresearch.com/).

## Data
This folder contains the original datasets used in some of the posts. 

### milk.csv
This dataset is used in the following posts:
* [Classification of NIR spectra by Principal Components Analysis](https://nirpyresearch.com/classification-nir-spectra-principal-component-analysis-python/)

### milk-powder.csv 
Used in the following posts:
* [Classification of NIR Spectra by Linear Discriminant Analysis in Python](https://nirpyresearch.com/classification-nir-spectra-linear-discriminant-analysis-python/)
* [PLS Discriminant Analysis for binary classification in Python](https://nirpyresearch.com/pls-discriminant-analysis-binary-classification-python/)

### peach_spectra+brixvalues.csv
This dataset is used in the following posts:
* [Principal Component Regression in Python](https://nirpyresearch.com/principal-component-regression-python/)
* [Partial Least Square Regression in Python](https://nirpyresearch.com/partial-least-squares-regression-python/)
* [A Variable Selection Method for PLS in Python](https://nirpyresearch.com/variable-selection-method-pls-python/)
* [Two Scatter Correction Techniques for NIR Spectroscopy in Python](https://nirpyresearch.com/two-scatter-correction-techniques-nir-spectroscopy-python/)
* [Exporting NIR Regression Models Built in Python](https://nirpyresearch.com/exporting-nir-regression-models-built-in-python/)
* [Principal Component Regression in Python Revisited](https://nirpyresearch.com/principal-component-regression-python-revisited/)
* [Principal Component Selection with a Greedy Algorithm](https://nirpyresearch.com/principal-component-selection-greedy-algorithm/)
* [Principal Component Selection with Simulated Annealing](https://nirpyresearch.com/principal-component-selection-with-simulated-annealing/)
* [Minimal prediction models for linear regression](https://nirpyresearch.com/minimal-prediction-models-linear-regression/)
* [The Akaike Information Criterion for model selection](https://nirpyresearch.com/akaike-information-criterion-for-model-selection/)
* [Parallel computation of loops for cross-validation analysis](https://nirpyresearch.com/parallel-computation-cross-validation/)

### plums.csv
Used in the following posts:
* [Detecting outliers using the Mahalanobis distance with PCA in Python](https://nirpyresearch.com/detecting-outliers-using-mahalanobis-distance-pca-python/)
* [PCA and kernel PCA explained](https://nirpyresearch.com/pca-kernel-pca-explained/)

### Honey2021.csv
Used in the following posts:
* [Aquagrams with Python and Matplotlib](https://nirpyresearch.com/aquagrams-python-matplotlib/)

### Raman_spectra_mixtures.csv
Used in the following posts:
* [Multivariate curve resolution: an introduction](https://nirpyresearch.com/multivariate-curve-resolution-introduction/)

### ABS_plastic.csv
Used in the following posts:
* [Optimal spectra smoothing with Fourier ring correlation](https://nirpyresearch.com/optimal-spectra-smoothing-fourier-ring-correlation/)

### Incombustible Material NIR.csv
Kindly provided by S. D'Hyon. About 60 samples with varying "incombustible content". Mix is coal and calcium carbonate. The data is raw and unmodified using a ChemWiz-ADK NIR spectrometer. 

## Snippets
Whatever piece of code that can be of general use or will not make it in the last versions of the posts will be (in time) posted here.

* [bootstrap.py](https://github.com/nevernervous78/nirpyresearch/blob/master/snippets/bootstrap.py) - Data splitter implementing the Bootstrap cross-validation method. This is not currently available in scikit-learn. This class is consistent with scikit-learn usage in a limited case. For more info on how to use this class, read the tutorial [K-fold and Montecarlo cross-validation vs Bootstrap: a primer](https://nirpyresearch.com/kfold-montecarlo-cross-validation-bootstrap-primer/).
* [Scatter Correction](https://github.com/nevernervous78/nirpyresearch/blob/master/snippets/Scatter_corrections_techniques.ipynb) - Jupyter notebook associated with the post: [Two Scatter Correction Techniques for NIR Spectroscopy in Python](https://nirpyresearch.com/two-scatter-correction-techniques-nir-spectroscopy-python/).
* [Basic PLS Regression](https://github.com/nevernervous78/nirpyresearch/blob/master/snippets/Basic%20PLS%20regression%20in%20Python.ipynb) - Jupyter notebook associated with the [Partial Least Square Regression in Python](https://nirpyresearch.com/partial-least-squares-regression-python/) post.
* [PCA vs Kernel PCA](https://github.com/nevernervous78/nirpyresearch/blob/master/snippets/PCA_and_kernelPCA_explained.ipynb) - Jupyter notebook with the code described in the [PCA and kernel PCA explained](https://nirpyresearch.com/pca-kernel-pca-explained/) post.
* [Simulated annealing](https://github.com/nevernervous78/nirpyresearch/blob/master/snippets/Wavelength%20band%20selection%20with%20simulated%20annealing.ipynb) - Companion Jupyter notebook to the [simulated annealing](https://nirpyresearch.com/principal-component-selection-with-simulated-annealing/) post.
