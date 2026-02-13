# nuitka-minimal
minimal example that compiles with nuitka

# Steps

1. Install required apt package:

```bash
sudo apt install patchelf
```

2. Create a light environment with only the required dependencies:

```bash
python3 -m venv ~/venvs/fpl-lite
pip install -r requirements.txt
```

Build:

```bash
nuitka --standalone --include-package-data=imgui_bundle --include-package-data=pygfx --include-package-data=cmap --include-package=cmap.data --include-package-data=wgpu --include-package=wgpu.resources --include-package-data=wgpu.resources main.py
```
