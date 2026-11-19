from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif"}
EXCLUDED_PARTS = {".git", ".github"}


def natural_key(path):
    return [
        int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", path)
    ]


def main():
    photos = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if any(part in EXCLUDED_PARTS for part in relative.split("/")):
            continue
        photos.append(relative)

    photos.sort(key=natural_key)
    (ROOT / "photos.json").write_text(
        json.dumps(photos, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
