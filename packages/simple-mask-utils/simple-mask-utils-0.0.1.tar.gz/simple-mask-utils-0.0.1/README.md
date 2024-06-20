# simple-mask-utils
Utility functions around image segmentation masks and turning them into polygons.


## Installation

You can install the library via `pip` (or `pip3`):

```bash
pip install simple-mask-utils
```

Or directly from the repo:

```bash
pip install https://github.com/waikato-datamining/simple-mask-utils.git
```

## Usage

```python
from smu import mask_to_polygon, polygon_to_lists

mask = ...  # binary mask (0/1) or float mask (0-1)
polys = mask_to_polygon(mask)  # determine polygons
for poly in polys:
    px, py = polygon_to_lists(poly, swap_x_y=True, as_type="int")  # get coordinates
```

See also [this example](example).
