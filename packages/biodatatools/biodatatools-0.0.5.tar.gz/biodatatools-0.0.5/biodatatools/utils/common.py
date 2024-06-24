import sys
import simplevc
simplevc.register(sys.modules[__name__])

import json
import gzip

@vc
def _json_load_20240601(i):
	if i.endswith("gz"):
		with gzip.open(i, "rt") as f:
			return json.load(f)
	else:
		with open(i, "rt") as f:
			return json.load(f)
@vc
def _json_dump_20240601(o, obj):
	if o.endswith("gz"):
		with gzip.open(o, 'wt') as f:
			json.dump(obj, f)
	else:
		with open(o, 'wt') as f:
			json.dump(obj, f)

@vc
def _OUTPUT_json_dump_20240601(o, obj):
	return [o]
