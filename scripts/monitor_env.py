import os
import sys
import yaml
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib

# جمع معلومات البيئة
env_data = {
    "python_version": sys.version.split()[0],
    "tensorflow_version": tf.__version__,
    "numpy_version": np.__version__,
    "pandas_version": pd.__version__,
    "matplotlib_version": matplotlib.__version__,
    "gpu_available": tf.config.list_physical_devices('GPU') != [],
    "environment_path": sys.prefix
}

# حفظ المعلومات في ملف YAML
yaml_path = "environment_status.yaml"

with open(yaml_path, "w") as file:
    yaml.dump(env_data, file, default_flow_style=False)

print(f"✅ تم حفظ معلومات البيئة داخل {yaml_path}")
