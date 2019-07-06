# Klazor Client Package

A package that enables client-server communication between your app and klazor server

## Installation
```
pip install git+https://github.com/wilcoln/klazor-client.git
```
## Usage

```python
import klazor_client as kc

kc.config(
    API_URL='http://127.0.0.1:8000/api', # should be 'http://klazor.com/api'
)

# fetch item by its id
course = kc.fetch_course(1)
sheet = kc.fetch_sheet(2)

# fetch all items 
courses = kc.fetch_courses()
sheets = kc.fetch_sheets()
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
