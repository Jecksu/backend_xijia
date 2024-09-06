
# backend test

## setup

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

## TO DO
+ denoising
+ edge filter
+ edge detection
+ resample
+ rescale
+ threshold
+ intensity normalize
+ gaussian blur

[poetry]:https://python-poetry.org/
