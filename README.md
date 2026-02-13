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

I will admit I found claude useful for playing wack-a-mole with the nuitka build system (one of the few things I think LLMs useful for 😆). If we continue to use this I should see if there's a proper or automated way to get the package data stuff.
