# Pipeline for training MLAgents environments using Kaggle Notebooks
A custom environment was created for the project in Unity using MLAgents. Next, the environment was trained using reinforcement learning algorithms in Kaggle Notebook using Stable Baselines3. At the moment, I have not found other examples on the Internet where it would be possible to combine these frameworks and runtimes.

<img src='result_spyder.gif' width='500'>

## Why this combination?

Unity MLAgents makes it easy to create your own reinforcement learning environments and has connections to Python and Gym to standardize the environment.

The main advantage of the Kaggle core is the ability to work in the background for quite a long time for free (compared to Colab). This allows you not to use your own computer for rather lengthy calculations.

Stable Baselines provides state-of-the-art, robust reinforcement learning methods, as well as easy tracking of experiments in Tensorboard.

## What you should pay attention to
MLAgents, Gym and Stable Baselines may conflict with each other due to different versions of the packages themselves, as well as additionally installed dependencies (such as numpy).
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

To convert the resulting SAC model into .onnx format for use in Unity, you can run the script after first changing the CONTINUOUS_ACTIONS_SIZE to your own.

## Enviroment and results

My own environment was used, created in Unity using Ariticulation Body (allows you to achieve realism in joints and actuators for robotics).
The environment is a spider with 8 degrees of freedom. A reward is given for each step in proportion to the speed in the desired direction with a shift (negative reward for standing still). More details about the environment will be written in another repository.
The Soft Aсtor-Critic algorithm from Stable Baselines 3 taught a spider to walk in 100,000 steps.

<img src='result.jpg' width='500'>

## Tensorboard Visualization

To visualize the results, you can use Google Colab by loading the resulting tensorboard archive into the content folder and calling the console commands:

```
!unzip ./sac_spyder_tensorboard.zip
%load_ext tensorboard
%tensorboard --logdir /content/kaggle/working/sac_spyder_tensorboard
```
