# Setup Instructions

The recommended setup is described below. Modifications to this setup will be called out as appropriate.

## Conda Environment

It is highly recommended that a conda environment is used to house your PyTorch installation. This has the benefit of insulating against version differences. Alternatives to using conda for installation can be found on [pytorch.org](https://pytorch.org).

### Create the environment

```{bash}
# Create the environment
conda create --name nlpbook
source activate nlpbook
```

### Install PyTorch

Note, this installs the GPU versions as of January, 2019. If this command changes in the future, this README will be updated accordingly. If it is not, please file an issue.

```{bash}
conda install pytorch torchvision -c pytorch
```

If you need the CPU versions, want to use `pip install` of conda, or a host of other configuration variations, please consult the website. They have done a great job of making it easy to retrieve the correct install command.

### Download the Repository

You can download the repository from GitHub [delip/PyTorchNLPBook](https://github.com/joosthub/PyTorchNLPBook) using git or downloading the repository as a zip file. You can also use the following commands to clone the repository:

```{bash}
git clone git@github.com:joosthub/PyTorchNLPBook.git
```

Or

```{bash}
git clone https://github.com/joosthub/PyTorchNLPBook.git
```

### Install the remaining packages with the requirements file

Inside the repository is a requirements file which can be used to install the remaining packages.

```{bash}
cd PyTorchNLPBook
pip install -r requirements.txt
```

### Installing the jupyter kernel

```{bash}
python -m ipykernel install --user --name nlpbook
```

### Download the data

```{bash}
cd data
./get-all-data.sh
```

Note: GloVe is not bundled in our data downloader. See `data/README.md` for more information.

### Run the notebook server

```{bash}
# run from the top level. if running commands in order, will need to `cd ..`
jupyter notebook
```
