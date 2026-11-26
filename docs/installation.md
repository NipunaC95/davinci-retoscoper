# Installation

Resolve 21 free edition supports native Fusion macros and `.drfx` Edit Effects.
This package does not use Python, Workflow Integrations, DCTL, or Lua FFI.

## Build

```bash
python3 package/build_drfx.py
```

The result is written to `dist/Retscope21.drfx/`.

## Windows

Place `Retscope21.drfx` in:

```text
%LOCALAPPDATA%\Blackmagic Design\DaVinci Resolve\Support\Effects\
```

Place `Retscope.setting` in:

```text
%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Macros\
```

## macOS

Place `Retscope21.drfx` in:

```text
~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Effects/
```

Place `Retscope.setting` in:

```text
~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Macros/
```

## Linux

Place `Retscope21.drfx` in:

```text
~/.local/share/BlackmagicDesign/DaVinci Resolve/Effects/
```

Place `Retscope.setting` in:

```text
~/.local/share/BlackmagicDesign/DaVinci Resolve/Fusion/Macros/
```

Restart Resolve and open the Edit Page Effects Library. Search for `Retscope`.
