
# backend test

## setup and requirement
Make sure your have python above 3.12 installed in your device. In MacOS,you can easily install in your command line:
```
brew install python@3.12
```

This project use [poetry] to manage python packages.
First of all，you should make sure poetry has been successfull installed on your device. For macos,you can install poetry with homebrew as command below:

```
brew install poetry
```

Then you can install all dependencies in project directory with a simple command:

```
poetry install
```

## how to run

Assuming that your computer has python3.10 or above installed, use the following command to run the program.

```
poetry run python3 main.py
```

## How to Use

This NII processor allows you to apply various filters to NII files. Here's how to use it:

1. Basic usage:
   Specify the filters one after the other in the order you wish to process the image
   ```
   python main.py --input <input_file.nii> --output <output_file.nii> --filter <filter1> <filter2> ...
   ```

    Available filters:
   - blur
   - resample
   - threshold
   - rescale
   - denoise
   - edge_detection

2. Filter-specific parameters:

   - Blur:
     ```
     --sigma <value>
     ```

   - Resample:
     ```
     --spacing <x> <y> <z>
     --size <x> <y> <z>
     --method <method>
     --origin <x> <y> <z>
     --direction <xx> <xy> <xz> <yx> <yy> <yz> <zx> <zy> <zz>
     ```

   - Threshold:
     ```
     --type <type>
     --lower <value>
     --upper <value>
     ```

   - Rescale:
     ```
     --min <value>
     --max <value>
     ```

   - Denoise:
     ```
     --min_noise <value>
     --max_noise <value>
     ```

   - Edge Detection:
     ```
     --detect_min <value>
     --detect_max <value>
     ```

3. Example:
   ```
   python main.py --input input.nii --output output.nii --filter blur resample --sigma 1.5 --spacing 1 1 1
   ```

This example applies a blur filter with sigma 1.5, followed by resampling with spacing 1x1x1.






[poetry]:https://python-poetry.org/
