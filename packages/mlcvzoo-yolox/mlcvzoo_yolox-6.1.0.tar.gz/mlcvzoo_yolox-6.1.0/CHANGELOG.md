# MLCVZoo mlcvzoo_yolox module Versions:

6.1.0 (2024-06-07):
------------------
Implement and use API changes introduced by mlcvzoo-base version 6.0.0

6.0.1 (2023-05-03):
------------------
Python 3.10 compatibility

6.0.0 (2023-02-14):
------------------
Implement API changes introduces by mlcvzoo-base version 5.0.0
- Remove detector-config and use the feature of the single ModelConfiguration
- Remove duplicate attributes

5.3.0 (2023-02-08):
------------------
- Include YOLOX multi-gpu training capabilities
- Update poetry lock file
-
5.2.0 (2023-01-25):
------------------
- Upgrade TensorRT version from 8.2.3.0 to 8.4.2.4
  - Increment version in mlcvzoo_yolox/pyproject.toml
- Add tests for the conversion of different yolox versions (s, m, l, x) to TensorRT models
  - The higher TensorRT version yields no reduction in memory costs,
    a lack of VRAM on the GPU still results in an error
  - Update torch2trt to latest stable commit
- Fix post-processing bug for yolox predictions
  - Add the third-party module boxes.py where the bug resides
  - Always choose the first detection (highest NMS score) if there are several available

5.1.1 (2022-11-10):
------------------
Remove dependency on backports.strenum

5.1.0 (2022-09-09):
------------------
- Ensure ConfigBuilder version 7 compatibility
- Remove call to yolox Trainer.after_epoch(...)
  - It generated duplicated checkpoints
  - This removes the possibility to run an evaluation during training
  - For evaluating model checkpoints after training the mlcvzoo-modeltrainer
    (mlcvzoo-util module) is recommended

5.0.0 (2022-08-08):
------------------
- Adapt to mlcvzoo-base 4.0.0

4.0.2 (2022-07-11):
------------------
Prepare package for PyPi

4.0.1 (2022-06-29):
------------------
Fix num_classes bug:
- Ensure that the model in yolox gets initialized with the correct number of classes

4.0.0 (2022-06-13):
------------------
Refactor and update:
- Update to yolox version 0.3.0
- Refactor initialization of yolox experiments in the MLCVZoo
  - Define the default parameters for the yolox versions (nano, s, m, l ...) in a lookup dictionary
  - Don't use an extra .py experiment file, but add a config entry that allows to
    define parameters that should be overwritten for the experiments
  - Remove unneeded configuration attributes
- Fix num_classes method
  - Add missing decorator
  - Don't use deprecated attribute

3.0.0 (2022-05-16):
------------------
Use new features from AnnotationClassMapper that have been added with mlcvzoo_base v3.0.0

2.0.0 (2022-04-05)
------------------
- initial release of the package
