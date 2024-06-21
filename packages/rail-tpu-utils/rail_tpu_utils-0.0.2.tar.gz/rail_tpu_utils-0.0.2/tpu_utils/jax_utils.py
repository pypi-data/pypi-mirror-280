import os
import logging
def initialize_compilation_cache(
    cache_dir=os.path.expanduser("~/.jax_compilation_cache"),
):
    """Initializes the Jax persistent compilation cache."""
    from jax.experimental.compilation_cache import compilation_cache
    compilation_cache.initialize_cache(cache_dir)
    for logger in [logging.getLogger(name) for name in logging.root.manager.loggerDict]:
        logger.addFilter(
            lambda record: "Not writing persistent cache entry for"
            not in record.getMessage()
        )