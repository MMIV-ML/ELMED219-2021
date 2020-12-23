# Setting up your system

#### Are you using Mac?
Then you must install [xcode](https://developer.apple.com/xcode/resources) (for free) before you start. See also [here](https://www.youtube.com/watch?v=m9m6HozVjo8) and [here](https://medium.com/@LondonAppBrewery/how-to-download-and-setup-xcode-10-for-ios-development-b63bed1865c). <br>Thereafter (see also [here](https://stackoverflow.com/questions/9329243/how-to-install-xcode-command-line-tools)):


- Launch the `terminal.app`, found in /Applications/Utilities/
- Type the following command string: `xcode-select --install`


#### On Mac, Windows and Linux we will use the [command line](https://en.wikipedia.org/wiki/Command-line_interface#Command-line_interpreter) (shell)
See e.g. [Basic Unix Commands](https://people.duke.edu/~ccc14/pcfb/unix.html) and [Computing Skills for Biologists](https://computingskillsforbiologists.com) [[here](https://github.com/CSB-book/CSB)] if this is unfamiliar to you. See also the
[Unix Shell](http://swcarpentry.github.io/shell-novice) lessons (thanks to [Anne Fouilloux](https://www.mn.uio.no/geo/english/people/adm/annefou), UiO)

#### ... and luckily also the [Jupyter notebook](https://www.nature.com/articles/d41586-018-07196-1)
- for openness [!](https://www.nature.com/news/interactive-notebooks-sharing-the-code-1.16261) and reproduciblity [!](https://arxiv.org/pdf/1810.08055.pdf)

## GitHub:
The course code is hosted on the code-sharing platform GitHub (where you now are reading this). If you do not have a GitHub account already you should make one now (https://github.com/join). We recommend that you are using the platform for your own projects during the course. Hence:


- Create an account on GitHub (https://github.com) using the `Sign up for GitHub` form on the right side of the page.
- Send your GitHub username to your instructor.
- Once your instructor adds you to the course GitHub organization you will receive an email asking you to accept the invitation. Click on the link to accept.
- Check if this worked
  - Go to https://github.com.
  - Sign in if necessary.
  - In the upper left corner click on the drop down with your name.
  - Confirm that the name of the course GitHub organization is present

## ITK-SNAP:
ITK-SNAP is an open-source image analysis tool used to segment and label structures in 3D medical images. ITK-SNAP is supported on Mac, Windows and Linux and provides semi-automatic segmentation using active contour methods, as well as manual delineation and image navigation. You can read and interact with DICOM and NIFTI images, and plot time-course data. Download the newest release of ITK-SNAP at http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.SNAP3

## Anaconda:
We recommend installing Python via the [Anaconda Distribution](https://www.anaconda.com/download). Be sure to use the "Python 3.8.x" version. We will use the Conda Package Management System within the Anaconda Distribution. From the [documentation](https://conda.io/docs):
> Conda is an open source package management system and environment management system that runs on Windows, macOS and Linux. Conda quickly installs, runs and updates packages and their dependencies. Conda easily creates, saves, loads and switches between environments on your local computer.

After the installation run `python --version` in a terminal window (in "Anaconda Prompt" if you are using Windows). If the output show "Python 3.8.x" (and "Anaconda") you are good to go.


## Install and test the course environment

After you have successfully installed Anaconda, go through the following steps (if you are using Windows, be at the "Anaconda Prompt").

### Install Git:
```bash
conda install git
```
### Download the repository:
```bash
git clone https://github.com/MMIV-ML/ELMED219-2021
cd ELMED219-2021
```
### Configure the Python-environment:
```bash
conda env update
```

### Activate the environment:
```bash
conda activate elmed219-2021
```

### Install a Jupyter kernel:
```bash
python -m ipykernel install --user --name elmed219-2021 --display-name "ELMED219-2021"
```

### Test you installation:
Go through the notebook `0.0-test.ipynb` in the `notebooks`-directory:
```bash
cd notebooks
jupyter notebook  (or, jupyter lab)
```


## Update:
The code and environment will be updated during the course. Run the following commands regularly:
* Update code: `git pull`
* Update environment:
```bash
conda activate elmed210-2021
conda env update
```

# Unix Shell

Learners need to understand what files and directories are and what a working directory is. These concepts are covered in the
[Unix Shell](http://swcarpentry.github.io/shell-novice) lessons (thanks to [Anne Fouilloux](https://www.mn.uio.no/geo/english/people/adm/annefou), UiO)

# Programming with Python

The best way to learn how to program is to do something useful, so [this](http://swcarpentry.github.io/python-novice-inflammation) introduction to Python is built around a common scientific task: **data analysis** (we are studying inflammation in patients who have been given a new treatment for arthritis, and need to analyze the first dozen data sets of their daily inflammation); see also [here](https://github.com/swcarpentry/python-novice-inflammation).


## A note on R (tip for previous R users)

**It is possible to run R-scripts in Jupyter notebooks**  (Jupyter = Julia, Python and R).

If you want to continue working with R (*not part of this course*) you should:

- Be using the latest R version (https://www.r-project.org) and the RStudio Desktop [[download](https://rstudio.com/products/rstudio/download)] for your Windows, MacOS or Linux system.
- **Install the R kernel** by opening an R console and then follow the instructions at https://irkernel.github.io/installation
- Necessary (or new) R libraries should be installed via RStudio and the corresponding R environment.
- See also [here](https://datatofish.com/r-jupyter-notebook) and [here](https://developers.refinitiv.com/article/setup-jupyter-notebook-r).
- The [rpy2](https://github.com/rpy2/rpy2) interface to use R form Python is also possible (but can be a bit more messy).
