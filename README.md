# Pipeline for training MLAgents environments using Kaggle Notebooks

<img src='result_spyder.gif' width='500'>

## Why this combination?

The main advantage of the [Kaggle](https://www.kaggle.com/) core is the ability to work in the background for quite a long time for free (compared to [Colab](https://colab.research.google.com/)). This allows you not to use your own computer for rather lengthy calculations.

[Unity MLAgents](https://unity.com/ru/products/machine-learning-agents) makes it easy to create your own reinforcement learning environments and has connections to Python and Gym to standardize the environment.

[Stable Baselines](https://stable-baselines3.readthedocs.io/en/master/) provides state-of-the-art, robust reinforcement learning methods, as well as easy tracking of experiments in [Tensorboard](https://www.tensorflow.org/tensorboard?hl=ru).

## What you should pay attention to
MLAgents, Gym and Stable Baselines may conflict with each other due to different versions of the packages themselves, as well as additionally installed dependencies (such as **numpy**).
This is made worse by the fact that we cannot control the version of python in environments such as Kaggle Notebook or Colab. Therefore, when installing, you should ignore the python version, and install the additional shimmy package for stable baselines:

```
!pip install --ignore-requires-python mlagents==1.0.0
!pip install stable-baselines3
!pip install shimmy>=0.2.1
```

In addition, you need to remember that you do not have a display to display the Unity environment, so the visualization option must be disabled:

```
unity_env = UnityEnvironment(env_path, no_graphics=True)
```
## Converting to a Unity model

To convert the resulting SAC model into **.onnx** format for use in Unity, you can run the script [onnx_convert.py](onnx_convert.py) after first changing the ```CONTINUOUS_ACTIONS_SIZE``` to your own and placing **saс_model.zip** in the same folder.

## Enviroment and results

My own environment was used, created in Unity using Ariticulation Body (allows you to achieve realism in joints and actuators for robotics).
The environment is a spider with 8 degrees of freedom. A reward is given for each step in proportion to the speed in the desired direction with a shift (negative reward for standing still). More details about the environment will be written in another repository.
The Soft Aсtor-Critic algorithm from Stable Baselines 3 taught a spider to walk in **100,000** steps.

<img src='result.jpg' width='500'>

## Tensorboard Visualization

To visualize the results, you can use Google Colab by loading the resulting tensorboard archive into the content folder and calling the console commands:

```
!unzip ./sac_spyder_tensorboard.zip
%load_ext tensorboard
%tensorboard --logdir /content/kaggle/working/sac_spyder_tensorboard
```
