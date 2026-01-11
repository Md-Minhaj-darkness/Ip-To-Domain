This is a simple and powerful **Python-based Reverse DNS lookup tool**. With this tool, you can find the corresponding domain name or subdomain from a specific IP address or a file containing many IP addresses.

## Features
* **Single IP Lookup:** Find the domain of a specific IP.
* **Bulk Lookup:** Process multiple IPs from a file at once.
* **Async Support:** It uses `asyncio` to get fast results.
* **Error Handling:** It shows a clear error message if the correct IP is not found or if there is any other problem.

---

## Installation

First, you need to have Python installed on your computer. Then follow the commands below:

1. **Clone the repository:**
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

2. **Install the required libraries:**
This script requires `dnspython` to run. To install it, type:
```bash
pip install dnspython
```

---

## Usage

You can use this script in two ways:

### 1. To check a specific IP:
```bash
python script_name.py -i 8.8.8.8