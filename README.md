# Image Processing
## Description
This project is a learning project that convert de-colorize image and re-colorize image using AI mode.

## How it works
The application convert the images in `original` directory into grayscale images and store in `grayscale` directory.
After that, it colorizes the grayscale images in `grayscale` directory and store in `recolor` directory.

## Specification
This project run on Python v3.9.10.

## Setup
1. Download the model from this [link](https://drive.google.com/drive/folders/1FaDajjtAsntF_Sw5gqF0WyakviA5l8-a) 
and place it in `/model` directory
2. Install the dependencies
```shell
$ pipenv install
```

## Run the project
1. Activate pipenv shell
```shell
pipenv shell
```
2. Run main function
```shell
python main.py
```

