# cd_http

`cd_http` is a Python package designed for HTTP request handling and manipulation. This package provides a set of tools and utilities to simplify HTTP operations in your projects.

## Features

- **Easy HTTP Requests**: Simplify the process of making HTTP requests.
- **Proxy Support**: Seamlessly integrate proxy support for your requests.
- **Customizable Headers**: Easily add and manage custom headers for your HTTP requests.
- **Version Management**: Track and manage the package version efficiently.
- Session support added 0.2.1

## Installation

To install `cd_http`, simply use `pip`:

```bash
pip install cd_http
```

## Usage

### Basic Example

```python
import cd_http as cdh

# Make a simple GET request
response = cdh.http.get('https://api.example.com/data')
print(response.text)
```

### Using Proxies

```python
import cd_http as cdh

proxy = 'http://proxy.example.com:8080'
response = cdh.http.get('https://api.example.com/data', proxy=proxy)
print(response.text)
```

### Custom Headers

```python
import cd_http as cdh

headers = {'Authorization': 'Bearer YOUR_TOKEN'}
response = cdh.http.get('https://api.example.com/data', headers=headers)
print(response.json())
```
## Download files
```python
import cd_http as cdh

url = "some file you want to download.mp4"
cdh.http.download_file("destination filepath", url=url)
```
## Examples

You can find more example scripts in the `examples` directory of the package. These scripts demonstrate various use cases and features of the `cd_http` package.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue on the [GitHub repository](https://github.com/yourusername/cd_http).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

For more information, visit [codedocta.com](https://codedocta.com).