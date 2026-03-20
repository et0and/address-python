# Health

Types:

```python
from address.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/address/resources/health.py">check</a>() -> <a href="./src/address/types/health_check_response.py">HealthCheckResponse</a></code>

# Challenge

Types:

```python
from address.types import ChallengeRetrieveResponse
```

Methods:

- <code title="get /challenge">client.challenge.<a href="./src/address/resources/challenge.py">retrieve</a>() -> <a href="./src/address/types/challenge_retrieve_response.py">ChallengeRetrieveResponse</a></code>

# RequestKey

Types:

```python
from address.types import RequestKeyCreateResponse
```

Methods:

- <code title="post /request-key">client.request_key.<a href="./src/address/resources/request_key.py">create</a>(\*\*<a href="src/address/types/request_key_create_params.py">params</a>) -> <a href="./src/address/types/request_key_create_response.py">RequestKeyCreateResponse</a></code>

# Addresses

Types:

```python
from address.types import AddressRetrieveResponse, AddressListResponse
```

Methods:

- <code title="get /v1/addresses/{id}">client.addresses.<a href="./src/address/resources/addresses.py">retrieve</a>(id) -> <a href="./src/address/types/address_retrieve_response.py">AddressRetrieveResponse</a></code>
- <code title="get /v1/addresses">client.addresses.<a href="./src/address/resources/addresses.py">list</a>(\*\*<a href="src/address/types/address_list_params.py">params</a>) -> <a href="./src/address/types/address_list_response.py">AddressListResponse</a></code>

# Search

Types:

```python
from address.types import SearchQueryResponse
```

Methods:

- <code title="get /v1/search">client.search.<a href="./src/address/resources/search.py">query</a>(\*\*<a href="src/address/types/search_query_params.py">params</a>) -> <a href="./src/address/types/search_query_response.py">SearchQueryResponse</a></code>

# Reverse

Types:

```python
from address.types import ReverseGeocodeResponse
```

Methods:

- <code title="get /v1/reverse">client.reverse.<a href="./src/address/resources/reverse.py">geocode</a>(\*\*<a href="src/address/types/reverse_geocode_params.py">params</a>) -> <a href="./src/address/types/reverse_geocode_response.py">ReverseGeocodeResponse</a></code>

# Meta

Types:

```python
from address.types import MetaRetrieveResponse
```

Methods:

- <code title="get /v1/meta">client.meta.<a href="./src/address/resources/meta.py">retrieve</a>() -> <a href="./src/address/types/meta_retrieve_response.py">MetaRetrieveResponse</a></code>
