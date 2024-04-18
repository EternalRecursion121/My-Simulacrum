from transformers import AutoTokenizer
from datasets import load_from_disk
import yaml
from os import listdir
import pandas as pd

directory = listdir("/workspace/axolotl/last_run_prepared/")[0]
with open('config.yml', 'r') as f:
    cfg = yaml.safe_load(f)
model_id = cfg['base_model']
tok = AutoTokenizer.from_pretrained(model_id)
ds = load_from_disk(f'last_run_prepared/{directory}/')

