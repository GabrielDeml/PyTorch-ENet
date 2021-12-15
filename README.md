# PyTorch-ENet

Project website: [https://gabrieldeml.github.io/CS539-final/](https://gabrieldeml.github.io/CS539-final/)

PyTorch implementation is tested on Cityscapes datasets. Pre-trained version of the models trained on Cityscapes with different activation functions are available [here](https://github.com/GabrielDeml/PyTorch-ENet/tree/master/Saved_Modelsa).

## Installation

### Local pip

1. Python 3 and pip
2. Set up a virtual environment (optional, but recommended)
3. Install dependencies using pip: `pip install -r requirements.txt`

## Usage

Run [`main.py`](https://github.com/davidtvs/PyTorch-ENet/blob/master/main.py), the main script file used for training and/or testing the model. The following options are supported:

```
python main.py [-h] [--mode {train,test,full}] [--resume]
               [--batch-size BATCH_SIZE] [--epochs EPOCHS]
               [--learning-rate LEARNING_RATE] [--lr-decay LR_DECAY]
               [--lr-decay-epochs LR_DECAY_EPOCHS]
               [--weight-decay WEIGHT_DECAY] [--dataset {camvid,cityscapes}]
               [--dataset-dir DATASET_DIR] [--height HEIGHT] [--width WIDTH]
               [--weighing {enet,mfb,none}] [--with-unlabeled]
               [--workers WORKERS] [--print-step] [--imshow-batch]
               [--device DEVICE] [--name NAME] [--save-dir SAVE_DIR]
```

For help on the optional arguments run: `python main.py -h`

### Example Prediction

```bash
python main.py -m predict --save-dir Saved_Models/mish_mish_full_dataset/ --name mish_mish_full_dataset_enet --dataset cityscapes --dataset-dir test_data/ --batch-size 10
```

## Development

### Examples: Training

```
python main.py -m train --save-dir save/folder/ --name model_name --dataset name --dataset-dir path/root_directory/
```

### Examples: Resuming training

```
python main.py -m train --resume True --save-dir save/folder/ --name model_name --dataset name --dataset-dir path/root_directory/
```

### Examples: Testing

```
python main.py -m test --save-dir save/folder/ --name model_name --dataset name --dataset-dir path/root_directory/
```
