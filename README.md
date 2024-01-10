# eBay Checker

This project is a tool designed to check accounts on the eBay platform.

## Description

The program utilizes Python's asynchronous capabilities to verify a set of user accounts on the eBay website. It performs login attempts using provided account credentials and tracks the success of the login.

## Installation

1. Clone the repository: `git clone https://github.com/Craxti/ebay_checker.git`
2. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Run the program: `python ebay_checker.py`
2. Input the number of processes you wish to run.
3. Choose whether to use proxies (Y/n).
4. Wait for the account check process to complete.

## Configuration

The project uses configuration files to store information such as paths to account files and the eBay login URL. These settings can be modified within the respective files in the `parser/config` directory.

## Notes

- `logs.log` - a log file containing debugging information about the program execution.
- `parser` - a directory containing modules for handling accounts, proxies, and eBay verification.
- `requirements.txt` - a file listing the project's dependencies.

## Contributing

Please see the CONTRIBUTING.md file to learn about the process for contributing to this project.

## License

This project is licensed under the terms of the MIT License. See the LICENSE file for details.

---

Author: Craxty
