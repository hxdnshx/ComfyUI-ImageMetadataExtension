# https://github.com/ltdrdata/ComfyUI-Inspire-Pack
from ..meta import MetaField
from ..formatters import calc_model_hash, calc_lora_hash, calc_vae_hash, convert_skip_clip, extract_embedding_hashes, extract_embedding_names
import re



SAMPLERS = {
    "KSampler //Inspire": {
    }
}





CAPTURE_FIELD_LIST = {
    "KSampler //Inspire": {
        MetaField.SEED: {"field_name": "seed"},
        MetaField.STEPS: {"field_name": "steps"},
        MetaField.CFG: {"field_name": "cfg"},
        MetaField.SAMPLER_NAME: {"field_name": "sampler_name"},
        MetaField.SCHEDULER: {"field_name": "scheduler"},
    }
}