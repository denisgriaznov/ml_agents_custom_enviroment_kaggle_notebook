## ML Agents custom enviroment with Stable Baselines 3
A custom environment was created for the project in Unity using MLAgents. Next, the environment was trained using reinforcement learning algorithms in Kaggle Notebook using Stable Baselines3. At the moment, I have not found other examples on the Internet where it would be possible to combine these frameworks and runtimes.

## Why this combination?

Unity MLAgents makes it easy to create your own reinforcement learning environments and has connections to Python and Gym to standardize the environment.

The main advantage of the Kaggle core is the ability to work in the background for quite a long time for free (compared to Colab). This allows you not to use your own computer for rather lengthy calculations.

Stable Baselines provides state-of-the-art, robust reinforcement learning methods, as well as easy tracking of experiments in Tensorboard.
