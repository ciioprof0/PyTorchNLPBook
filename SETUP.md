# Setup Instructions

The recommended setup is described below. Modifications to this setup will be called out as appropriate.

## Clone the Repository

Clone the [repository](https://github.com/ciioprof0/PyTorchNLPBook) from GitHub using one of the options below:

- Option A. The web URL:

```{bash}
git clone https://github.com/ciioprof0/PyTorchNLPBook.git
```

- Option B. The SSH URL:

```{bash}
git clone git@github.com:ciioprof0/PyTorchNLPBook.git
```

- Option C. The GitHub CLI:

```{bash}
gh repo clone ciioprof0/PyTorchNLPBook
```

## Create the local environment

Install the Conda Environment

It is highly recommended that a conda environment is used to house your PyTorch installation. This has the benefit of insulating against version differences. See [Installing conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) for instructions on how to install conda pn your system. The [Miniconda](https://docs.anaconda.com/miniconda/) installer is sufficient for this purpose.

Alternatives to using conda for installation can be found on [pytorch.org](https://pytorch.org).

### Create the conda environment

When you have conda installed, you can create an environment with the following command from the project root directory:

Step 1. Create the environment from the `environment.yml` file:

```{bash}
conda env create -f setup/conda/environment.yml --no-default-packages
```

Step 2. Activate the environment:

```{bash}
source activate nlpbook
```

Step 3. Download the data:

_Note_. The script below has not yet been updated to download the missing data files. Please see the `data/README.md` for manual installation instructions.

```{bash}
bash src/get-all-data.sh
```