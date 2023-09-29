<p align="center">
  <img src="docs/assets/pydeus.png" width="175px" height="175px">
</p>
<h1 align="center">
  PyDeus (clone repo for tests)
    origin https://github.com/AltDeus/pydeus.git

</h1>
<p align="center">
    <h3 align="center">The progressive, easy-to-use, asynchronouse, customizable API wrapper</h3>
</p>

<br/>

## Installation
From PyPI
```
pip install pydeus
```

From github
```
pip install -U https://github.com/AltDeus/pydeus.git
```

## Documentation
[**PyDeus official documentation**](https://pydeus.staypony.space/docs)

## Example usage
```py
from pydeus import ModeusClient, Credentials

credentials = Credentials(email='your email', password='your password')
client = ModeusClient(credentials)

client.timetable.get_current_day()

...
```
