# Image Downloader

Image Downloader is a Python Script for downloading images based on `input_images.txt` file's urls.

## Environment setup
First we need to download `virtualenv` with below command

```bash
pip install virtualenv
```
Then we have to create a virtual environment for this project
```bash
virtualenv -p python3 your_env_name
```
Activating the environment by
```bash
source your_env_name/bin/activate
```
Now we have to install our dependencies. first go to project root then run this command
```bash
pip install -r requirements.txt
```
To Deactivate environment
```bash
deactivate
```


## Usage

```bash
python image_downloader.py
```

## For running test
For running test, go to project root then run this command
```bash
pytest
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)



