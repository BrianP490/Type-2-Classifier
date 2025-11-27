# Diabetes Classifier 

## 📌 Problem Statement

Diabetes is a major health problem around the world. America single-handedly has over 53 million people affected by both Type-1 and Type-2 Diabetes. Identifying that someone has diabetes is the first step to prevent any health complications and maintain a healthy lifestyle. 

## 🔎 Scope

The scope of this project is to create a classifying agent that is improves the accuracy of diagnosing a patient with diabetes. This project also serves as a reminder to work alongside doctors and health specialists in order to prevent the development of diabetes.

## 📖 Project Purpose

The purpose of this project is to find a dataset that is capable of analysis and to use that dataset to train a classification agent that correctly categorizes a patient into either having or not having diabetes. The agent model and trained weights can also be used to create an easy to use application. 

## 💻 Installation Instructions:

1. Make sure you have [Conda](https://conda.org/) installed which is the virtual environment and package manager system used.

2. Clone the repository

    ```bash
    git clone https://github.com/CongaJAMM/Type-2-Classifier.git
    ```

    ```bash
    # Example
    C:\Users\brianperez\Desktop\DEV>git clone https://github.com/BrianP490/fake-repository.git
    ```

3. Create the conda environment for the dependencies 
    - More information about the virtual environments creation & activation located in the ['./Setup/README.md'](./setup/README.md)

## 🏋️ Training Script Guide

<details>

Complete configuration file documentation found in: [`./configs/README.md`](./configs/README.md)

However, these are the most important command-line arguments that affect the behavior of the training script:

- --epochs

    - Type: int

    - Default: `1`

    - Description: Number of training epochs to run.

- --learning_rate

    - Type: float

    - Default: `0.0003`

    - Description: Learning rate used by the optimizer.

- --max_grad_norm

    - Type: float

    - Default: `3.0`

    - Description: The Maximum L2 Norm of the gradients for Gradient Clipping.

- --dataloader_batch_size

    - Type: int

    - Default: `64`

    - Description: Batch size used by the dataloaders for training, validation, and testing.

- --dataloader_pin_memory

    - Type: action='store_true' (boolean flag)

    - Default: `false (if flag is not present)`

    - Description: Toggle pinned memory in dataloaders (disabled by default). Include this flag to enable it.

- --dataloader_num_workers

    - Type: int

    - Default: `0`

    - Description: Number of subprocesses to use for data loading.

- --log_iterations

    - Type: int

    - Default: `32`

    - Description: Frequency (in iterations) to log training progress.

- --eval_iterations

    - Type: int

    - Default: `32`

    - Description: Frequency (in iterations) to evaluate the model.

- --use_cuda

    - Type: action='store_true' (boolean flag)

    - Default: `false (if flag is not present)`

    - Description: Toggle CUDA for training if available. Include this flag to enable CUDA.

- --device

    - Type: str

    - Default: `"cpu"`

    - Description: Device to use for training (e.g., "cpu", "cuda:0"). This parameter overrides the --use_cuda flag if specified.

- --save_model

    - Type: action='store_true' (boolean flag)

    - Default: `false (if flag is not present)`

    - Description: Toggle saving the trained model after training. Include this flag to enable model saving.

- --model_output_path

    - Type: str

    - Default: `"./models/trained-model.pt"`

    - Description: File path to save the trained model. Parent directories will be created if they do not exist.

### 📝 Example Commands:

- ```python train.py```
    - Uses the default settings to run the script.
    
- ```python train.py --epochs=32  --log_iterations=4 --eval_iterations=8 --save_model```
    - Explanation: Run for 32 epochs and log the average batch iteration Mean Absolute Error Loss every 4 iterations. Evaluate the Policy under training every 8 epochs. Lastly, save the trained model. Uses the default save path. Uses default for everything else.
    
    
- ```python train.py --epochs=32  --use_cuda --save_model --model_output_path=models/first-trained-model.pt```
    - Explanation: Let the system detect if your system has GPU capabilities and has cuda available for training. During the training setup, the system dynamically sets the device variable for model training. Save the trained model using the specified location. Uses default for everything else.

</details>

## 🗠 Dataset Information

 - All dataset information located in [HuggingFace Dataset](hf://datasets/MaxPrestige/Synthetic-Diabetes-Dataset/Data/Synthetic-Diabetes-Dataset.csv)

## 📂 Folder Directory

 * Created using [githubtree](https://github.com/rescenic/githubtree)

```bash
# EXAMPLE PROJECT STRUCTURE
README.md
```