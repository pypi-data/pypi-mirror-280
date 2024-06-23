# Starlyng Smart Reboot

This project manages servers by rebooting using BCM due to crashes.

## Prerequisites

Install ipmitool on the server you will run the script. You can usually do this via your package manager:
* Ubuntu: sudo apt-get install ipmitool
* macOS: brew install ipmitool
* If outside local network, set Port Forwarding on the network for BCM IP to 623

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.x.
* You have a basic understanding of Python and virtual environments.

## Setting Up Your Development Environment

To set up your development environment and run the project, follow these steps:

### Clone the Repository

First, clone the repository to your local machine:

```bash
git https://github.com/starlyngapp/smart-reboot.git
cd smart-reboot
```

## Create and Activate Virtual Environment

For macOS and Linux:

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

## Setup Environment for VSCode

* Open the Command Palette (Ctrl+Shift+P)
* Search for the Python: Create Environment command, and select it
* Select Venv
* Select Python interpreter
* Select dependencies to install

## Install Required Packages

Install all dependencies listed in the dev-requirements.txt file:

```bash
pip install -r dev-requirements.txt
```

## Installation

To install only the package (without dev dependencies):

```bash
pip install starlyng_smart_reboot
```

To install development dependencies (useful for contributing to the project):

```bash
pip install starlyng_smart_reboot[dev]
```

Alternatively, you can install the development dependencies using:

```bash
pip install -r dev-requirements.txt
```

## Environment Configuration

To configure smart reboot, you need to set up environment variables. This can be done by creating a `.env` file in the root of the project.

An example `.env` file is provided as `.env.example`. You can copy this file and update the values as needed.

### Steps to Configure Environment Variables

1. **Copy the example environment file:**

```sh
cp .env.example .env
```

2. **Open the `.env` file and update the values:**

```env
# .env
# List of server IPs and ports in the format ip:port, separated by commas
BCM_SERVERS=192.168.1.1:8001,192.168.1.2:8002

# BCM username
BCM_USER=user

# BCM password
BCM_PASSWORD=secret
```

3. **Save the `.env` file.**

The `BCM_SERVERS` variable should be a comma-separated list of server IP addresses and ports.

## Usage

To run the main function:

```bash
smart_reboot
```

## PyPI

[starlyng-smart-reboot](https://pypi.org/project/starlyng-smart-reboot/)

## Command-line Arguments

You can also override configuration using command-line arguments:

```bash
smart_reboot --bcm_servers "192.168.1.1:22,192.168.1.2:22" --bcm_username "bcm_username" --bcm_password "secret"
```

Or locally:

```bash
python main.py --bcm_servers "192.168.1.1:22,192.168.1.2:22" --bcm_username "bcm_username" --bcm_password "secret"
```

### Building and Uploading Your Package

1. **Build the package**:

```bash
python setup.py sdist bdist_wheel
```

2. **Upload to PyPI**:

```bash
twine upload dist/*
```

Upload using specific project name referenced in .pypirc

```bash
twine upload dist/* --repository starlyng-smart-reboot
```

## Running Tests

To run tests, execute the following command in your terminal:

```bash
pytest
```

This command will run all tests and report the results. You can also run specific tests by providing the path and filename of the test file.

## Contributing to the Project

Contributions to this project are welcome. Here's how you can contribute:

1. Fork the project.
2. Create your feature branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -am 'Add some YourFeature').
4. Push to the branch (git push origin feature/YourFeature).
5. Open a pull request.

## Contact

If you have any questions, please contact us at:

- GitHub: [@justinsherwood](https://github.com/justinsherwood)