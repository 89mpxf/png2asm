# png2asm
Bootable VGA graphics backplane written in x86 Assembly to display images.
## Limitations
* Only PNG images can be used.
* Images are limited to 32000 bytes in size.
* Images are limited to 320x200 maximum resolution.
* Images can only be displayed in VGA 320x200 256color.
## Dependencies
* Python (tested on 3.10 but should be compatible with lower versions)
* NASM
* PIL pip package
## Build Instructions
1. Run png2bin.py and specify the image you want to convert.

```python png2bin.py (absolute/relative path to image)```

2. Run the make.sh script.

