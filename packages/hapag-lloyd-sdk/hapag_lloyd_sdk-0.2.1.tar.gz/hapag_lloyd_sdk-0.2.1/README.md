# Hapag Lloyd Python SDK

This SDK contains all publicly available APIs for Hapag Lloyd.

## Installation

```bash
pip install hapag-lloyd-sdk
```

## Usage

Quick start with environment variables:

```python
from hapag_lloyd_sdk import HapagLloydClient

client = HapagLloydClient()
```

If you have not set the environment variables, you can pass them as arguments:

```python
from hapag_lloyd_sdk import HapagLloydClient
client = HapagLloydClient(client_id='xxx', client_secret='xxx')
```
