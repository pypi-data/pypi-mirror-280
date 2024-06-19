# blette

A toolbox for edge detection tasks (binary and multi-label edges).

## Installation

```Bash
# install pytorch
# e.g. for CUDA 11.7
pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117

# openmm dependencies
pip install -U openmim
mim install -U mmengine
mim install -U 'mmcv==2.0.0rc4'  # until mmseg updates...
pip install mmsegmentation

# third-party dependencies
pip install -r requirements.txt

# global package
pip install -e .
```

## Usage

- [SBD](./.readme/sbd.md)
- [Cityscapes](./.readme/cityscapes.md)
- [BSDS500](./.readme/bsds500.md)


## Dev

TODO:
- [ ] Reproduce results
- [ ] Test codes for functions not present in other mm-libraries
- [ ] Improve docstrings
- [ ] Improve documentations
