# PyThermalGreen
Collaborative project to obtain urban heat island patches through Remote Sensing.

## How to execute?

You can install the library using Python pip.

```
pip install PyThermalGreen
```

The project initially requires raster files processed for NDVI and Earth Surface Temperature to process urban heat island spaces.
```
ndvi_file = 'ndvi.tif'
tst_file = 'tst.tif'
output = 'way/to/save/your/file.tif'
```
To run the code you just need to use the function
```
thermal_green = PyThermalGreen('tst_file_path', 'ndvi_file_path', 'output_file_path')
```
This is an example output of a .tif file using PyThermalGreen:
![texto alternativo](https://github.com/guilherber/PyThermalGreen/raw/main/docs/example.jpg)

## Important Details

Use the same geographic projection for interpretation

## Collab

To collaborate, do not hesitate to send an e-mail to (guissan.gui@gmail.com)
