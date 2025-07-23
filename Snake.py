from memos.configs.mem_os import MOSConfig
import json, textwrap
print(textwrap.indent(json.dumps(MOSConfig.model_json_schema(), indent=2), "  "))
