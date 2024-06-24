# CognxCore
Google Gemini api python package

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install CognxCore.

```bash
pip install CognxCore
```

## Usage

```python
import CognxCore

#Google Gemini API Key
api_key = input("Enter your API key: ")
ai = CognxCore(api_key)

#Prompt and response
prompt = input("Enter your prompt: ")
response = ai.generate_content(prompt)
print(response)

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
