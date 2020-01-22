'''
run: file.py srcFolder(Pokedex/) destFolder(PNG/)
'''
import sys
from pathlib import Path
from PIL import Image

# get source and destination paths
src_dir = Path.cwd() / sys.argv[1]
dest_dir = Path.cwd() / sys.argv[2]

# get files in source directory
src_path = Path(src_dir)

# create destination folder
dest_path = Path(dest_dir)
dest_path.mkdir(exist_ok=True)

for f in src_path.iterdir():
  img = Image.open(f)
  file_path = Path(dest_dir / f'{f.stem}.png')
  img.save(file_path)




