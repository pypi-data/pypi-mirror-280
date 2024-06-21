# TPU Utils


## TL;DR: Please stop cross-region traffic

At the very beginning of your launcher, please add this:

```python
from tpu_utils import prevent_cross_region
...

def main(_):
    prevent_cross_region(FLAGS.save_dir, FLAGS.data_dir, ...) # Anything that may be cross region

```

## Installation:

```
pip install rail_tpu_utils 
```

```
pip install git+https://github.com/dibyaghosh/tpu_utils.git
```


## Also has:

- `tpu_utils.initialize_compilation_cache`: Initializes JAX's compilation cache
