# ppt

## Running the checks

A small standard-library test verifies that the `.pptx` deck is a valid PowerPoint package
(valid zip, required parts present, at least one slide).

```sh
python -m pytest
# or, without pytest:
python -m unittest discover -s tests
```
