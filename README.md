Aqui está o conteúdo do seu `README.md` traduzido para o inglês:

---

# Mini Port Scanner

This is a simple port scanner developed in Python. It allows you to scan a range of ports on a domain or IP address and check if the ports are open or closed.

## Requirements

To use this project, you only need Python 3 installed on your machine.

## Installation

Clone the repository using Git:

```bash
git clone https://github.com/bobzinx/mini-port-scan.git
```

Navigate to the project folder:

```bash
cd mini-port-scan
```

## How to Use

Run the `scanner.py` script with the required parameters:

```bash
python3 scanner.py <domain or IP> <starting port> <ending port> --timeout <timeout>
```

### Parameters:

- **domain or IP**: The IP address or domain you want to scan.
- **starting port**: The starting port of the range you want to scan.
- **ending port**: The ending port of the range you want to scan.
- **timeout** (`--timeout`): The timeout (in seconds) for each connection attempt. The default is 1 second.

### Example:

To scan ports 1 through 900 on IP `198.168.1.1` with a timeout of 2 seconds, run:

```bash
python3 scanner.py 198.168.1.1 1 900 --timeout 2
```

## License

This project is licensed under the [MIT License](LICENSE).

---
