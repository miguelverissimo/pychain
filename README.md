# Seting the project up

### Install system Dependencies:
For ease of use, install dependencies using `homebrew` or your package manager of choice:
```
pyenv
direnv
```

### Setup python and pip:
```
pyenv install 3.7.4
pyenv global 3.7.4
pip install --upgrade pip
pip3 install virtualenv
```

### Clone the project:
```
git clone git@github.com:miguelverissimo/pychain
```


### Change into the project directory:
```
cd pychain
```
This should produce a message saying the environment is locked. Allow the environment with `direnv`

```
direnv allow
```
On the first run you should see a virtual environment being created


### Install project dependencies:
```
pip3 install -r requirements.txt
```

# Development

### Running the tests:
```
python3 -m pytest backend/tests
```

### Adding more project dependencies:
```
pip3 install <name>
pip3 freeze > requirements.txt
```

# Misc
## IF you ever need to (de)activate the virtual environment manually
### Activate:
```
source .direnv/bin/activate
```

### Deactivate:
```
deactivate
```
