# Retscope 21

Free-Edition-compatible native Fusion macro for aspect-ratio framing, pan/scan,
letterbox/pillar-box overlays, and hard-crop alpha output in DaVinci Resolve 21.

## Features

- Cinema, broadcast, square, vertical, and custom aspect ratios
- Pan X/Y, zoom, and auto-fill framing
- Hard crop or opaque/semi-transparent matte overlay
- Matte RGB color and overlay opacity
- Pixel-aspect-ratio-aware geometry
- Feathered masks and optional border/rule-of-thirds controls
- No Python API, Workflow Integration, DCTL, or Lua FFI dependency

## Package

```text
dist/Retscope21.drfx/
dist/Retscope21.drfx/Effects/Retscope/Retscope.setting
dist/Retscope21.drfx/Effects/Retscope/manifest.xml
dist/Retscope21.drfx/Effects/Retscope/preview.svg
dist/Retscope21.drfx/Fusion/Macros/Retscope.setting
```

Build the package:

```bash
python3 package/build_drfx.py
```

Validate geometry and package metadata:

```bash
python3 -m unittest discover -s tests -v
```

## Installation

### Windows

Copy `Retscope21.drfx` to:

```text
%LOCALAPPDATA%\Blackmagic Design\DaVinci Resolve\Support\Effects\
```

For direct Fusion access, copy `fusion/Retscope.setting` to:

```text
%APPDATA%\Blackmagic Design\DaVinci Resolve\Support\Fusion\Macros\
```

### macOS

Copy `Retscope21.drfx` to:

```text
~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Effects/
```

For direct Fusion access, copy `fusion/Retscope.setting` to:

```text
~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Macros/
```

### Linux

Copy `Retscope21.drfx` to the active Resolve support directory, normally:

```text
~/.local/share/BlackmagicDesign/DaVinci Resolve/Effects/
```

For direct Fusion access, copy `fusion/Retscope.setting` to:

```text
~/.local/share/BlackmagicDesign/DaVinci Resolve/Fusion/Macros/
```

Restart Resolve after installation.

## Inspector Controls

| Parameter | Internal ID | Type | Default | Range |
|---|---|---|---:|---|
| Target Aspect Ratio | `AspectPreset` | ComboBox | 16:9 | Custom through 4:5 |
| Custom Aspect Ratio | `CustomAspect` | Slider | 1.78 | 0.50-4.00 |
| Pan X | `PanX` | Slider | 0.0 | -1.0-1.0 |
| Pan Y | `PanY` | Slider | 0.0 | -1.0-1.0 |
| Zoom | `Zoom` | Slider | 1.0 | 1.0-4.0 |
| Auto-Fill / Fit to Scope | `AutoFill` | Checkbox | true | Boolean |
| Matte Mode | `MatteMode` | ComboBox | Overlay | Hard Crop/Overlay |
| Overlay Opacity | `OverlayOpacity` | Slider | 100% | 0%-100% |
| Matte Color | `MatteColor` | ColorWheel | #000000 | RGB |
| Border Guide | `BorderGuide` | Checkbox | false | Boolean |
| Border Width | `BorderWidth` | Slider | 2 px | 1-5 px |
| Rule of Thirds | `RuleOfThirds` | Checkbox | false | Boolean |
| Guide Opacity | `GuideOpacity` | Slider | 75% | 0%-100% |
| Corner Radius | `CornerRadius` | Slider | 0 px | 0-200 px |
| Feather | `FeatherPixels` | Slider | 0 px | 0-50 px |
| Guides in Render | `GuidesInRender` | Checkbox | false | Boolean |
| Matte in Render | `MatteInRender` | Checkbox | true | Boolean |
| Preserve Alpha | `PreserveAlpha` | Checkbox | false | Boolean |

## Geometry

`DAR = (Width * PixelAspect) / Height`

For a display aspect `T`:

```text
Source DAR >= T:
  normalized width  = 1
  normalized height = DAR / T

Source DAR < T:
  normalized width  = T / DAR
  normalized height = 1
```

Overlay mode retains the full source and applies matte outside the target frame.
Hard-crop mode masks the merge to zero alpha outside the target frame.

## Compatibility

- DaVinci Resolve 21.0 through 21.2+ Free and Studio
- Edit Page Effects Library and Fusion Page macro usage
- Windows, macOS, and Linux
- No Studio-only scripting or DCTL APIs
