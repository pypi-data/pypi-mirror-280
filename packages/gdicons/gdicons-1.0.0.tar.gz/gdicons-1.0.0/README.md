# `gdicons`
A Python library to render Geometry Dash icons.

## Usage

Import the library like so:

```python
from gdicons import *
```

By default, it will set its resources path to the one included in a default Steam installation. To override this, call this function:

```python
set_resources_path(<path to Resources folder>)
```

To render an icon, call this function:

```python
rendered_icon = render_icon(<parameter dictionary>)
```

This returns a PIL Image object, which can then be saved to a file.

## Parameter Dictionary

| Parameter name | Parameter description |
| -------------- | --------------------- |
| `"gamemode"`   | The gamemode to render. Can be one of `"cube"`, `"ship"`, `"ball"`, `"ufo"`, `"wave"`, `"robot"`, `"spider"`, `"swing"`, or `"jetpack"`.
| `"id"`         | The ID of the gamemode to render. |
| `"primary"`    | The primary color of the rendered icon. Can be a hexadecimal string (`"#0b172b"`) or color string (`"red"`). |
| `"secondary"`  | The secondary color of the rendered icon. |
| `"glow"`       | The glow color of the rendered icon. Can also be `False` to disable glow. |
| `"quality"`    | The texture quality of the rendered icon. A higher quality leads to a higher size. Can be one of `"low"`/`"normal"`, `"hd"`, or `"uhd"`.

## Usage Example

```python
from gdicons import *

viprin_cube = render_icon({
    "gamemode":  "cube",
    "id":        133,
    "primary":   "#ffff00",
    "secondary": "#b900ff",
    "glow":      "#b900ff",
    "quality":   "uhd"
})
nexus_spider = render_icon({
    "gamemode":  "spider",
    "id":        13,
    "primary":   "#f00",
    "secondary": "#fff",
    "glow":      "#fff",
    "quality":   "uhd"
})

viprin_cube.save("viprin.png")
nexus_spider.save("nexus.png")
```

### Output

![A rendered image of Viprin's cube](examples/viprin.png)
![A rendered image of Nexus' spider](examples/nexus.png)
