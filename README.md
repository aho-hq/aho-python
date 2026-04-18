# aho_sdk Python SDK

Official Python SDK for the [Aho](https://aho.com) Verifiable Credentials API.

## Installation

```bash
# Basic installation (sync only)
pip install aho-sdk

# With async support
pip install aho-sdk[async]

# With validation (Pydantic models)
pip install aho-sdk[validation]

# All features
pip install aho-sdk[all]
```

## Quick Start

```python
import os
from aho_sdk import Issuer

# Initialize the Issuer client
issuer = Issuer(api_key=os.environ['AHO_ISSUER_API_KEY'])

# Issue a credential
credential = issuer.credentials.create(
    schema_uuid='your-schema-uuid',
    subject_identifier='user@example.com',
    claims={
        'name': 'Jane Doe',
        'role': 'Engineer'
    }
)

print(credential['uuid'])
```

## Clients

The SDK provides the following clients:

| Client | Purpose | API Key Type |
|--------|---------|--------------|
| `Account` | Manage account settings, domains, and API keys | Account API Key |
| `System` | System health and status endpoints | System API Key |
| `Holder` | Manage holder credentials and presentations | Holder API Key |
| `Verifier` | Create presentation requests and verify credentials | Verifier API Key |
| `Issuer` | Issue and manage verifiable credentials | Issuer API Key |
| `Schemas` | Browse and retrieve credential schemas | Schemas API Key |
| `Unauthenticated` | Public endpoints (no authentication required) | None (public) |

## Usage Examples

### Issuing Credentials

```python
from aho_sdk import Issuer

issuer = Issuer(api_key=os.environ['AHO_ISSUER_API_KEY'])

# List all schemas
schemas = issuer.schemas.list()
for schema in schemas:
    print(schema['name'])

# Create a schema
schema = issuer.schemas.create(
    name='EmployeeBadge',
    claims=[
        {'name': 'employee_id', 'type': 'string', 'required': True},
        {'name': 'department', 'type': 'string', 'required': True},
        {'name': 'hire_date', 'type': 'date', 'required': False}
    ]
)

# Issue a credential
credential = issuer.credentials.create(
    schema_uuid=schema['uuid'],
    subject_identifier='jane.doe@company.com',
    claims={
        'employee_id': 'EMP-12345',
        'department': 'Engineering',
        'hire_date': '2024-01-15'
    }
)

# Revoke a credential
issuer.credentials.revoke(uuid=credential['uuid'], reason='Employee departed')
```

### Verifying Credentials

```python
from aho_sdk import Verifier

verifier = Verifier(api_key=os.environ['AHO_VERIFIER_API_KEY'])

# Create a presentation request
request = verifier.requests.create(
    name='Employment Verification',
    query_format='dcql',
    credentials=[
        {
            'id': 'employee_badge',
            'format': 'vc+sd-jwt',
            'claims': [
                {'path': ['employee_id']},
                {'path': ['department']}
            ]
        }
    ]
)

# Get the QR code for the request (supports 'png', 'svg' formats)
qr = verifier.requests.qr_code(uuid=request['uuid'], output_format='svg')

# List responses to the request
responses = verifier.responses.list(request_uuid=request['uuid'])
```

### Managing Holder Credentials

```python
from aho_sdk import Holder

holder = Holder(api_key=os.environ['AHO_HOLDER_API_KEY'])

# List credentials
credentials = holder.credentials.list(status='active')

# Create a presentation (selective disclosure)
presentation = holder.presentations.create(
    credential_uuid='credential-uuid',
    disclosed_claims=['name', 'department']
)
```

### Account Management

```python
from aho_sdk import Account

account = Account(api_key=os.environ['AHO_API_KEY'])

# Manage domains
domains = account.domains.list()
account.domains.verify(id=domain['id'])

# Manage signing keys
keys = account.signing_keys.list()
account.signing_keys.rotate(id=key['id'])

# Configure webhooks
account.webhooks.create(
    url='https://your-app.com/webhooks/aho',
    events=['credential.issued', 'credential.revoked']
)
```

## Pagination

List methods return `Page` objects with built-in iteration:

```python
# Iterate through all pages automatically
for credential in issuer.credentials.list():
    print(credential['uuid'])

# Or handle pages manually
page = issuer.credentials.list(per_page=50)
while page:
    for credential in page.data:
        print(credential['uuid'])
    page = page.next_page()

# Collect all items
all_credentials = list(issuer.credentials.list())
```

## File Uploads

For endpoints that accept file uploads:

```python
# Upload a file
issuer.media.upload(
    file=open('document.pdf', 'rb'),
    metadata={'description': 'Employee contract'}
)

# The SDK auto-detects MIME types from file extensions
# You can also pass a Path:
from pathlib import Path
issuer.media.upload(file=Path('document.pdf'))
```

## Binary Responses

Some endpoints return binary data (images, PDFs):

```python
# Get QR code as PNG
png_data = verifier.requests.qr_code(uuid='...', output_format='png')
with open('qr.png', 'wb') as f:
    f.write(png_data)

# Get QR code as SVG
svg_data = verifier.requests.qr_code(uuid='...', output_format='svg')
with open('qr.svg', 'w') as f:
    f.write(svg_data.decode('utf-8'))
```

## Error Handling

```python
from aho_sdk import (
    Issuer,
    ValidationError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
    ApiError
)

try:
    issuer.credentials.create(invalid_params)
except ValidationError as e:
    # 422 - Validation failed
    for error in e.field_errors:
        print(f"{error['field']}: {error['hint']}")
except AuthenticationError as e:
    # 401 - Invalid API key
    print("Check your API key")
except NotFoundError as e:
    # 404 - Resource not found
    print(f"Resource not found: {e.message}")
except RateLimitError as e:
    # 429 - Rate limited (SDK auto-retries with exponential backoff)
    print(f"Retry after {e.retry_after} seconds")
except ApiError as e:
    # Other API errors
    print(f"Error {e.status_code}: {e.message}")
    print(f"Request ID: {e.request_id}")
```

### Error Classes

| Error Class | HTTP Status | Description |
|-------------|-------------|-------------|
| `AuthenticationError` | 401 | Invalid or missing API key |
| `ForbiddenError` | 403 | Insufficient permissions |
| `NotFoundError` | 404 | Resource not found |
| `ConflictError` | 409 | Resource conflict |
| `ValidationError` | 422 | Request validation failed |
| `RateLimitError` | 429 | Rate limit exceeded |
| `ServerError` | 5xx | Server-side error |
| `NetworkError` | - | Connection/timeout error |
| `ApiError` | * | Base class for all API errors |

## Rate Limiting

The SDK automatically handles rate limits with exponential backoff:

- **Idempotent methods** (GET, DELETE, PUT): Auto-retry up to 3 times
- **Non-idempotent methods** (POST, PATCH): Only retry with idempotency key

```python
# Use idempotency keys for safe retries on POST/PATCH
issuer.credentials.create(
    schema_uuid='...',
    claims={...},
    idempotency_key='unique-request-id'
)
```

## Configuration

```python
import logging

# Custom configuration
issuer = Issuer(
    api_key=os.environ['AHO_ISSUER_API_KEY'],
    base_url='https://api.aho.com',  # Custom base URL
    timeout=60,                       # Request timeout in seconds
    logger=logging.getLogger('aho')   # Enable debug logging
)
```

## Async Support

The SDK provides async versions of all clients. Install with async support:

```bash
pip install aho-sdk[async]
```

Then use the async clients:

```python
import asyncio
from aho_sdk import AsyncIssuer

async def main():
    # Use async context manager for automatic cleanup
    async with AsyncIssuer(api_key=os.environ['AHO_ISSUER_API_KEY']) as issuer:
        # All methods are async
        credentials = await issuer.credentials.list()

        # Async iteration through pages
        async for credential in credentials:
            print(credential['uuid'])

        # Or await individual operations
        credential = await issuer.credentials.get(uuid='...')

asyncio.run(main())
```

Async clients available:
- `AsyncAccount` - Async version of `Account`
- `AsyncSystem` - Async version of `System`
- `AsyncHolder` - Async version of `Holder`
- `AsyncVerifier` - Async version of `Verifier`
- `AsyncIssuer` - Async version of `Issuer`
- `AsyncSchemas` - Async version of `Schemas`
- `AsyncUnauthenticated` - Async version of `Unauthenticated`

## Requirements

- Python 3.9+
- httpx (for async support, optional)

## License

MIT
