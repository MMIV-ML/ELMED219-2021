# Lab 3: BRATS and multimodal MRI

This lab will introduce multiparametric / multspectral MRI, the concepts of noise and contrast-to-noise ratio (CNR). It will also introduce **supervised learning** (tissue clasification) of the head based on four-channel MRI recordings and manual delination of six different tissue types (or labels: AIR, GM, WM, CSF, MUS. FAT), using K-nearest neighorhood (KNN) clasification in 4D feature space. It will further introduce a multimodal dataset from the BRATS (Brain Tumor Segmentation) challenge and introduce **unsupervised learning** (K-means clustering) of these data using tool from `scikit-learn`.


## Slides

[ELMED219-Lab-BRATS-and-multimodal-MRI](https://docs.google.com/presentation/d/e/2PACX-1vTAsaZCQpvCk6zSlrYqzBVyNLIw-AV6vqM09_HB4ItVKDCeo8ckhsggU4plwgWeeQR5jMvt-LmeiJZq/pub?start=false&loop=false&delayms=3000)  (in prep.)

## Jupyter notebooks

- [`ELMED219-Lab3-mri-multispectral-KNN-segm.ipynb`](https://nbviewer.jupyter.org/github/MMIV-ML/ELMED219-2021/blob/main/Lab3-BRATS/ELMED219-Lab3-mri-multispectral-KNN-segm.ipynb) 
- [`ELMED219-Lab3-glioma-segm-hd-glio-tcga-06-1802.ipynb`](https://nbviewer.jupyter.org/github/MMIV-ML/ELMED219-2021/blob/main/Lab3-BRATS/ELMED219-Lab3-glioma-segm-hd-glio-tcga-06-1802.ipynb)
- [`ELMED219-Lab3-glioma-unsupervised-segm-K-means.ipynb`](https://nbviewer.jupyter.org/github/MMIV-ML/ELMED219-2021/blob/main/Lab3-BRATS/ELMED219-Lab3-glioma-unsupervised-segm-K-means.ipynb)

## Your turn! 

The notebooks have several excerices and suggestions for experiments with the models and their (hyper)parameters.
