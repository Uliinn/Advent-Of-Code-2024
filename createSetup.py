from pathlib import *


for i in range(1,26):

  folder = Path(f"{i}")

  folder.mkdir()

  (folder / "1.py").touch()
  (folder / "2.py").touch()
  (folder / "input.txt").touch()


