from dotmap import DotMap
import functools

from pattern.etc import singleton
from pathlib import Path
import yaml
from loguru import logger
import os


@singleton
class IConfig:
    
    DEFAULT_UMAP = dict(
         n_neighbors=15,
         n_components=5,
         min_dist=0.0,
         metric="cosine"
    )
    
    DEFAULT_PCA = dict(
        
    )
    
    DEFAULT_HDBSCAN = dict(
        
    )
    
    DEFAULT_KMEANS = dict(
        
    )
    
    # You can create as many default templates manually as you want ...
    
    def __init__(self):
        try:
            with open(str(Path(os.getcwd()) / "config.yaml")) as fp:
                config = DotMap(yaml.safe_load(fp))
        except:
            config = DotMap()
            logger.info(f"Config file is not loaded, be aware that no options are propagates from `config.yaml`")
        finally:
            for k, v in config.items():
                if k.startswith("_"):
                    continue
                setattr(self, k, v)


Config = IConfig()


__all__ = ["Config"]
