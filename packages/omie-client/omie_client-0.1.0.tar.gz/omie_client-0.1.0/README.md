## Omie's Python SDK

![Omie's Logo](assets/omie-logo.jpeg)
<p align="center">
An unofficial implementation of Omie's API. 
</p>

For a full reference of the API documentation look at Omie [Developer Portal](https://developer.omie.com.br/)

### Installation:
```shell
$ pip install omie-client
```

### Getting started
```python
>>> from omie_client import OmieClient
>>> omie_client = OmieClient(app_key="your-app-key", app_secret="your-app-secret")
>>> payment = omie_client.accounts_payable.get_by_id(9873625)
Payment(
    codigo_lancamento_omie=9873625,
    codigo_lancamento_integracao='MAJAWg',
    codigo_cliente_fornecedor=9809218639,
    data_vencimento=datetime.date(2024, 5, 14),
    ....
)
```

### Features

Our foundation is built upon established and modern libraries.

- [HTTPX - A next-generation HTTP client for Python.](https://github.com/encode/httpx)
- [Pydantic - Data validation using Python type hints.](https://github.com/pydantic/pydantic)
