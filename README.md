# GPT V1

(Note: this is the first version of the model. Second version can be found [here](https://github.com/MulyaP/GPT-V2)

This is a generative transformer model that I build in order to understand how transformers work. I have used openwebtext dataset to train my model and a decoder-only transformer architecture.
It do not perform great as my laptop is not capable enough to handle expensive computations. However, you can feel free to play with hyperparameters as you like. As per my observation, 
increasing the value of n_layers, n_head, n_embd, block_size and batch_size might significantly improve the model performance. The values I have used are the upper limit for my device but you can change them as per your desire. Although be cautious while doing that as making the model more complex than your system's capability might lead to system crash and memory errors.
Below I have explained the setup process if you wish to run this model on your device.

## Installation

Foremost step is to clone this repository in your device.

Then, if you wish to run this model locally, it is advisable to install cuda toolkit if your GPU is cuda enabled. You can check if your GPU is cuda-enabled or not from [here](https://developer.nvidia.com/cuda-gpus).

Next, creating a virtual environment and working in it is also favourable. To create a virtual enviroment with name 'gpt', first navigate to the project folder in command prompt and then, run this command:

```
python -m venv gpt
```

To activate this environment, run:

```
gpt\Scripts\activate
```

Now that we are in virtual environment, go ahead and run this command to begin the installation of necessary libraries.

```
pip3 install -r requirements.txt
```

After completing this installation, run: 

```
pip3 install torch --index-url https://download.pytorch.org/whl/cu121
```

## Dataset setup

To access the dataset, first clone this huggingface repository in your project folder: [Skylion007/openwebtext](https://huggingface.co/datasets/Skylion007/openwebtext).
If you face any trouble while cloning, refer [this](https://huggingface.co/blog/password-git-deprecation). The process might take some time.

Next up, double check that the cloned repository is named 'openwebtext', if not, then change its name to 'openwebtext'. Now, navigate to your project folder and run the Data-extract file.
Before running this command, ensure that your disk has around 60-70 gb of free space.

```
python Data-extract.py
```

This script might take few hours to run. It will divide your data into two files namely, train and val in the ratio of 90:10 and also create another
file which contains all the characters that occurred in the dataset.

After this is done, you need to do one more thing if you are using a virtual environment. You need to create a new ipykernel for your virtual environment. To do that, simply run this command in your terminal after navigating to your project folder ( where your venv is activated). Let's suppose my venv name is cuda and display name is also cuda:

``` python
python -m ipykernel install --user --name=cuda --display-name "cuda"
```

Now, once this kernel is installed, you can open GPT-V1 in jupyter notebook and then instead of using Python 3 kernel, use the kernel named cuda.

THen, you can go ahead and run all the cells in the GPT-V1 ipynb file.


