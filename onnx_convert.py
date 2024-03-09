from typing import Tuple, Any

import torch as th
from torch.nn import Parameter

from stable_baselines3 import SAC

CONTINUOUS_ACTIONS_SIZE = 12


class OnnxablePolicy(th.nn.Module):
    def __init__(self, actor: th.nn.Module):
        super().__init__()
        self.actor = actor
        self.version_number = Parameter(th.Tensor([3]), requires_grad=False)
        self.memory_size = Parameter(th.Tensor([0]), requires_grad=False)
        self.continuous_action_output_shape = Parameter(th.Tensor([CONTINUOUS_ACTIONS_SIZE]), requires_grad=False)

    def forward(self, observation: th.Tensor) -> tuple[Any, Parameter, Parameter, Parameter]:
        # NOTE: You may have to postprocess (unnormalize) actions
        # to the correct bounds (see commented code below)
        return self.actor(observation, deterministic=True), self.continuous_action_output_shape, self.version_number, self.memory_size

model = SAC.load("sac_model.zip", device="cpu")
onnxable_model = OnnxablePolicy(model.policy.actor)

observation_size = model.observation_space.shape
dummy_input = th.randn(1, *observation_size)
th.onnx.export(
    onnxable_model,
    dummy_input,
    "my_sac_actor.onnx",
    opset_version=17,
    input_names=["obs_0"],
    output_names=["continuous_actions", "continuous_action_output_shape", "version_number", "memory_size"],
)

##### Load and test with onnx

import onnxruntime as ort
import numpy as np

onnx_path = "my_sac_actor.onnx"

observation = np.zeros((1, *observation_size)).astype(np.float32)
ort_sess = ort.InferenceSession(onnx_path)
scaled_action = ort_sess.run(None, {"obs_0": observation})[0]

print(scaled_action)

# Post-process: rescale to correct space
# Rescale the action from [-1, 1] to [low, high]
# low, high = model.action_space.low, model.action_space.high
# post_processed_action = low + (0.5 * (scaled_action + 1.0) * (high - low))

# Check that the predictions are the same
with th.no_grad():
    print(model.actor(th.as_tensor(observation), deterministic=True))