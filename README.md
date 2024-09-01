# EAT

### Edge-aware Attention Transformer for Image Super-Resolution (paper link is coming)

## Environment
- [PyTorch == 2.0.1](https://pytorch.org/) 
- [BasicSR == 1.3.4.9](https://github.com/XPixelGroup/BasicSR/blob/master/INSTALL.md) 
### Installation
```
pip install -r requirements.txt
python setup.py develop
```

## How To Train
- Refer to `./options/train` for the configuration file of the model to train.
- Dataset can be downloaded at the [Baidu Disk](https://pan.baidu.com/s/1KBrj464wTdgQ6AHNxdQ2mg?pwd=pu8p).
- The training command is like
```
python eat/train.py -opt options/train/train_HAT_SRx3_from_scratch.yml
```
- Note that the default batch size per gpu is 4, which will cost about 20G memory for each GPU.  

The training logs and weights will be saved in the `./experiments` folder.


## How To Test
- Refer to `./options/test` for the configuration file of the model to be tested, and prepare the testing data and pretrained model.  
- Then run the following codes (taking `HAT_SRx3.pth` as an example):
```
python eat/test.py -opt options/test/HAT_SRx3.yml
```
The testing results will be saved in the `./results` folder.  

## Thanks
A part of our work has been facilitated by the [HAT](https://github.com/XPixelGroup/HAT)  framework, and we are grateful for its outstanding contribution.


