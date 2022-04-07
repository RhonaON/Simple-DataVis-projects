# DataVis

## Dev

### Setup

```shell
sudo apt install python3-pandas python3-matplotlib python3-tk
```

### Run

```shell
python3 task1.py
```

---

Previous virtual env way we tried, failed due to `tk` error:

https://stackoverflow.com/questions/15884075/tkinter-in-a-virtualenv

## Dev

### Setup

With `python` and `pip` installed:

```shell
pip install --user pipenv
```

```shell
sudo apt install python3-tk
```

### Install new dep

```shell
pipenv install <dep>
```

### Activate virtual env

```shell
pipenv shell
```

### Run code

```shell
pipenv run python3 task1.py
```
