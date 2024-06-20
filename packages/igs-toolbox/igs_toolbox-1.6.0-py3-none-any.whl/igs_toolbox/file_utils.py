import json
from pathlib import Path
from typing import Any, Dict


def read_json_file(file: Path) -> Dict[str, Any]:
    for encoding in ("utf-8", "iso-8859-1"):
        try:
            with file.open(encoding=encoding) as fp:
                return json.load(fp)  # type: ignore[no-any-return]
        except UnicodeDecodeError:
            pass
    raise RuntimeError(f"Failed to decode file {file}")
