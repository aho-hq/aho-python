"""Python type definitions for the Aho API.

Auto-generated from OpenAPI spec - DO NOT EDIT
"""
from __future__ import annotations

from typing import Any, TypedDict, Literal, TypeGuard
from typing_extensions import NotRequired

class VerificationResult(TypedDict, total=False):
    """Verification response with standard envelope. Contains:
- success: Whether the API call succeeded
- data: Object with verified (bool), status (string), message, verified_at, credential details"""
    # Required: Whether the API call succeeded
    success: bool
    # Required: Verification result data
    data: dict[str, Any]

class PresentationVerifyResult(TypedDict, total=False):
    """Response from verifying a holder's selective disclosure presentation.
Contains verification status, disclosed claims, and credential/presentation metadata."""
    # Required: Whether the API call succeeded
    success: bool
    # Required: Verification result data
    data: dict[str, Any]

class TyposquattingWarning(TypedDict, total=False):
    """Present if the domain resembles a well-known domain"""
    # Required: The well-known domain this resembles
    similar_to: str
    # Required: Ranking tier of the similar domain
    similar_to_rank: str

class IssuerRef(TypedDict, total=False):
    """Issuer reference with optional domain verification status"""
    # Organization name
    name: NotRequired[str]
    # Decentralized Identifier
    did: NotRequired[str]
    # Issuer's verified domain
    domain: NotRequired[str | None]
    # Whether the issuer's domain is fully verified
    domain_fully_verified: NotRequired[bool]

class SchemaRef(TypedDict, total=False):
    """Credential schema reference"""
    # Schema UUID
    uuid: NotRequired[str]
    # Schema display name
    name: NotRequired[str]
    # Credential type identifier
    type: NotRequired[str]
    # URL-friendly schema identifier
    slug: NotRequired[str]

class SubjectRef(TypedDict, total=False):
    """Credential subject identification"""
    # Type of identifier (email, did)
    identifier_type: NotRequired[str | None]
    # Subject's Decentralized Identifier
    did: NotRequired[str | None]

class SigningKeyRef(TypedDict, total=False):
    """Reference to the signing key used for a credential"""
    # Signing key identifier
    id: NotRequired[str]
    # Key ID used in JWT header (kid)
    key_id: NotRequired[str]
    # Signing algorithm
    algorithm: NotRequired[Literal["es256", "es384", "ed25519"]]

class TrustSignal(TypedDict, total=False):
    """A trust verification signal with status indicator"""
    # Visual indicator character
    icon: NotRequired[str]
    # Signal description
    text: NotRequired[str]
    # Signal status level
    status: NotRequired[Literal["success", "danger", "neutral"]]

class PaginationMeta(TypedDict, total=False):
    """Pagination metadata for list responses"""
    # Required: Current page number
    current_page: int
    # Required: Items per page
    per_page: int
    # Required: Total number of items
    total_count: int
    # Required: Total number of pages
    total_pages: int

class FieldError(TypedDict, total=False):
    """Structured field-level validation error"""
    # Required: JSON path to the invalid field
    field: str
    # Required: Machine-readable error type
    issue: Literal["type_mismatch", "missing_required", "invalid_enum", "pattern_mismatch", "length_violation", "range_violation", "format_invalid", "array_size_violation", "duplicate_items", "unexpected_property", "validation_failed"]
    # Expected value/type
    expected: NotRequired[str | None]
    # Actual value/type received
    got: NotRequired[str | None]
    # Human-readable fix suggestion
    hint: NotRequired[str | None]

class RateLimitError(TypedDict, total=False):
    """Rate limit exceeded error response (HTTP 429)"""
    # Required: Always false
    success: bool
    error: dict[str, Any]
    # Required: Seconds to wait before retrying
    retry_after: int

class Credential(TypedDict, total=False):
    """A verifiable credential issued to a holder"""
    # Unique identifier for the credential
    uuid: NotRequired[str]
    # Current status of the credential:
    status: NotRequired[Literal["active", "suspended", "revoked", "expired", "archived"]]
    # Email or DID identifying the credential subject
    subject_identifier: NotRequired[str]
    # Type of identifier used for the subject:
    subject_identifier_type: NotRequired[Literal["email", "did"]]
    # When the credential was issued
    issued_at: NotRequired[str]
    # When the credential expires (null if no expiration)
    expires_at: NotRequired[str | None]
    # When the credential record was created
    created_at: NotRequired[str]
    # The credential schema this credential is based on
    schema: NotRequired[dict[str, Any] | None]
    # The organization that issued this credential
    issuer: NotRequired[dict[str, Any]]
    # URL where this credential can be verified
    verification_url: NotRequired[str]
    # The signed JWT credential token (null if not yet generated)
    credential_jwt: NotRequired[str | None]
    # The credential claims/attributes (dynamic, schema-dependent)
    claims: NotRequired[dict[str, Any] | None]
    # Internal subject identifier
    subject_id: NotRequired[str | None]
    # Raw VC JSON-LD document (only present for some credential types)
    vc_json: NotRequired[dict[str, Any] | None]
    # Information about the signing key used
    issuer_signing_key: NotRequired[dict[str, Any] | None]
    # Number of verification attempts for this credential
    verification_logs_count: NotRequired[int]
    # When the credential was last updated
    updated_at: NotRequired[str]

class Presentation(TypedDict, total=False):
    """A verifiable presentation with selective disclosure of claims"""
    # Required: Unique identifier for the presentation
    uuid: str
    # Required: UUID of the source credential
    credential_uuid: str
    # Required: List of claim names included in this presentation
    disclosed_claims: list[str]
    # The actual values of disclosed claims (dynamic, schema-dependent)
    disclosed_values: NotRequired[dict[str, Any] | None]
    # Intended recipient of this presentation
    audience: NotRequired[str | None]
    # Why this presentation was created
    purpose: NotRequired[str | None]
    # Required: Current status of the presentation:
    status: Literal["active", "expired", "revoked"]
    # When the presentation expires (null if no expiration)
    expires_at: NotRequired[str | None]
    # Required: Number of times this presentation has been verified
    verification_count: int
    # Required: When the presentation was created
    created_at: str
    # The signed SD-JWT presentation token
    presentation_token: NotRequired[str]
    # Data for sharing this presentation
    share_data: NotRequired[dict[str, Any] | None]

class IssuerCredentialSchema(TypedDict, total=False):
    """An issuer's credential schema with full details"""
    # Required: Unique identifier
    uuid: str
    # Required: URL-friendly identifier
    slug: str
    # Required: Display name
    name: str
    # Required: VC type identifier
    credential_type: str
    # Required: Schema category
    schema_type: Literal["custom", "education_credential", "employment_credential", "open_badge", "certificate"]
    # Required: Schema status
    status: Literal["draft", "active", "archived"]
    supported_formats: list[Literal["jwt_vc", "sd_jwt_vc", "mdoc", "data_integrity"]]
    template_key: NotRequired[str | None]
    # Required: Number of credentials issued
    credential_count: int
    # JSON-LD context URLs
    json_ld_context: NotRequired[list[str]]
    # JSON Schema for claims
    subject_schema: NotRequired[dict[str, Any]]
    sd_jwt_vc_config: NotRequired[dict[str, Any]]
    mdoc_config: NotRequired[dict[str, Any]]
    render_templates: NotRequired[list[dict[str, Any]]]
    created_at: str
    updated_at: str

class CredentialSchema(TypedDict, total=False):
    """A template defining the structure of a credential"""
    # URL-friendly identifier (lowercase, hyphenated)
    slug: NotRequired[str]
    # Human-readable name of the schema
    name: NotRequired[str]
    # Detailed description of what this credential type represents
    description: NotRequired[str]
    # Credential type identifier (e.g., PascalCase or standard like mDL)
    credential_type: NotRequired[str]
    # Category for organizing schemas
    category: NotRequired[str]
    # Schema visibility:
    visibility: NotRequired[Literal["public", "private"]]
    # List of claim fields defined in this schema
    claims: NotRequired[list[dict[str, Any]]]
    # Tags for filtering and discovery
    tags: NotRequired[list[str]]
    # URL to the schema documentation page
    url: NotRequired[str]
    # URL to the JSON-LD context document
    context_url: NotRequired[str]
    # URL to external schema definition (e.g., schema.org)
    external_url: NotRequired[str | None]
    # Source of the schema (e.g., 'schema_org', 'custom')
    source: NotRequired[str | None]
    # JSON Schema defining the credential subject structure
    subject_schema: NotRequired[dict[str, Any] | None]
    # JSON-LD context URLs for this schema
    json_ld_context: NotRequired[list[str] | None]
    # Key identifying the SVG template used for rendering
    svg_template_key: NotRequired[str | None]

class RenderTemplate(TypedDict, total=False):
    """A visual rendering template for credentials (SVG or PDF)"""
    # Required: Unique template identifier
    id: str
    # Required: Human-readable template name
    name: str
    # Description of the template
    description: NotRequired[str | None]
    # Required: Template rendering engine:
    render_suite: Literal["svg_mustache", "pdf_mustache"]
    # Required: Template origin:
    template_type: Literal["custom", "system"]
    # Required: MIME type of the rendered output
    media_type: Literal["image/svg+xml", "application/pdf"]
    # Required: SHA-256 hash of template content (multibase base64url encoded)
    digest_multibase: str
    # JSON Pointers to claims rendered by this template
    render_properties: NotRequired[list[str] | None]
    # Field names extracted from render_properties
    exposed_fields: NotRequired[list[str]]
    # Template content (only included when specifically requested)
    content: NotRequired[str | None]
    # Required: When the template was created
    created_at: str
    # Required: When the template was last updated
    updated_at: str

class RenderTemplateValidationResult(TypedDict, total=False):
    """Result of template validation without saving"""
    # Whether the API call succeeded
    success: NotRequired[bool]
    # Whether the template is valid
    valid: NotRequired[bool]
    # Computed hash (only if valid)
    digest_multibase: NotRequired[str | None]
    # Mustache variables found in the template
    extracted_variables: NotRequired[list[str]]
    # Validation errors (only if invalid)
    errors: NotRequired[list[str]]
    # Non-fatal warnings about the template
    warnings: NotRequired[list[str]]

class CredentialOfferResult(TypedDict, total=False):
    """Result of creating a credential offer"""
    # Required: Unique identifier for the offer (used in URLs)
    offer_id: str
    # Required: URL where the offer can be retrieved (for credential_offer_uri)
    offer_uri: str
    # Required: Deep link for wallet apps (openid-credential-offer://)
    deep_link: str
    # PIN/tx_code the holder must enter to claim (only if require_tx_code was true, OID4VCI 1.0)
    tx_code: NotRequired[str | None]
    # Required: When the offer expires
    expires_at: str

class WebhookPayload(TypedDict, total=False):
    """Payload sent to verifier webhook endpoints when a holder responds to a presentation request.
The webhook includes an X-Webhook-Signature header for verification (HMAC-SHA256 of timestamp.payload using API key).
Verifiers should validate this signature before processing the payload."""
    # Required: Event type indicating the holder's response:
    event: Literal["presentation_response.approved", "presentation_response.declined"]
    # Required: When this webhook event was generated (ISO 8601)
    timestamp: str
    # Required: The original presentation request that was responded to
    request: dict[str, Any]
    # Required: The holder's response to the request
    response: dict[str, Any]
    # Required: The organization that made the presentation request
    verifier: dict[str, Any]
    # Information about the credential holder (only present for approved responses)
    holder: NotRequired[dict[str, Any] | None]
    # The actual claim values disclosed by the holder (only present for approved responses)
    disclosed_claims: NotRequired[dict[str, Any] | None]
    # Information about the source credential (only present for approved responses)
    credential: NotRequired[dict[str, Any] | None]

class BatchOperationResult(TypedDict, total=False):
    """Result of a batch operation (revoke_batch, suspend_batch, reinstate_batch).
Contains per-UUID results for debugging and summary counts."""
    # Required: Per-UUID results in submission order
    items: list[dict[str, Any]]
    # Required: Aggregate counts by result status
    summary: dict[str, Any]

class CredentialOffer(TypedDict, total=False):
    """A credential offer that holders can claim via wallet apps (OID4VCI)"""
    # Required: Unique identifier for the offer
    uuid: str
    # Required: Current status of the offer:
    status: Literal["pending", "accepted", "expired", "revoked"]
    # Email or DID of the intended recipient
    subject_identifier: NotRequired[str | None]
    # Required: Pre-filled claim values for the credential
    subject_claims: dict[str, Any]
    # When the offer expires
    expires_at: NotRequired[str | None]
    # Required: When the offer was created
    created_at: str
    # Required: The credential schema for this offer
    schema: dict[str, Any]
    # URL where the offer can be retrieved (included on show)
    offer_uri: NotRequired[str | None]
    # Deep link for wallet apps (openid-credential-offer://...) (included on show)
    deep_link: NotRequired[str | None]

class PresentationRequest(TypedDict, total=False):
    """An OpenID4VP presentation request created by a verifier"""
    # Required: Unique identifier for the presentation request
    uuid: str
    # Required: Display name for the request
    name: str
    # Purpose shown to holder explaining why claims are needed
    purpose: NotRequired[str | None]
    # Required: Current status of the request:
    status: Literal["draft", "active", "expired", "closed"]
    # Required: Query format used:
    query_format: Literal["presentation_exchange", "dcql"]
    # When the request expires
    expires_at: NotRequired[str | None]
    # Maximum number of responses allowed (null = unlimited)
    max_responses: NotRequired[int | None]
    # Webhook URL for response notifications
    callback_url: NotRequired[str | None]
    # Where to redirect holder after response
    redirect_url: NotRequired[str | None]
    # Required: When the request was created
    created_at: str
    # Required: When the request was last updated
    updated_at: str
    # Required: The verifier organization
    verifier: dict[str, Any]
    # URLs for accessing/sharing the request (included on show)
    urls: NotRequired[dict[str, Any] | None]
    # Response statistics (included on show)
    stats: NotRequired[dict[str, Any] | None]
    # DCQL query definition (only for dcql format)
    dcql_query: NotRequired[dict[str, Any] | None]
    # Presentation Exchange definition (only for presentation_exchange format)
    presentation_definition: NotRequired[dict[str, Any] | None]

class PresentationResponse(TypedDict, total=False):
    """A holder's response to a presentation request"""
    # Required: Unique identifier for the response
    uuid: str
    # Required: Status of the response:
    status: Literal["pending", "approved", "declined"]
    # When the holder responded
    responded_at: NotRequired[str | None]
    # Required: When the response record was created
    created_at: str
    # Information about the holder (if available)
    holder: NotRequired[dict[str, Any] | None]
    # Claims disclosed by the holder (detail view only)
    disclosed_claims: NotRequired[dict[str, Any] | None]
    # Mapping of claim names (detail view only)
    claim_mapping: NotRequired[dict[str, Any] | None]
    # Source credential information (detail view only, if single credential)
    credential: NotRequired[dict[str, Any] | None]
    # Multiple credentials (detail view only, for multi-credential responses)
    credentials: NotRequired[list[dict[str, Any]] | None]

class DataSource(TypedDict, total=False):
    """A data source for automated credential issuance"""
    # Required: URL-friendly identifier
    slug: str
    # Required: Display name for the data source
    name: str
    # Required: Type of data source:
    source_type: Literal["postgresql", "csv"]
    # Required: Current status of the data source:
    status: Literal["draft", "active", "paused", "error"]
    # Required: Number of credential schema mappings using this source
    mapping_count: int
    # Connection metadata (passwords are never exposed)
    connection_info: NotRequired[dict[str, Any] | None]
    # CSV file details (for csv source type)
    source_file: NotRequired[dict[str, Any] | None]
    # Required: When the data source was created
    created_at: str
    # Required: When the data source was last updated
    updated_at: str

class DataSourceMapping(TypedDict, total=False):
    """A mapping between a data source and credential schema"""
    # Required: URL-friendly identifier
    slug: str
    # Optional custom name for the mapping
    name: NotRequired[str | None]
    # Required: Display name (custom name or auto-generated)
    display_name: str
    # Required: The linked data source
    data_source: dict[str, Any]
    # Required: The linked credential schema
    credential_schema: dict[str, Any]
    # Maps data source columns to credential claims (full view only)
    field_mapping: NotRequired[dict[str, Any] | None]
    # Query configuration for data extraction (full view only)
    query_config: NotRequired[dict[str, Any] | None]
    # Required: Number of automations using this mapping
    automation_count: int
    # Required: When the mapping was created
    created_at: str
    # Required: When the mapping was last updated
    updated_at: str

class DataSourceTestResult(TypedDict, total=False):
    """Result of testing a data source connection"""
    # Required: Human-readable result message
    message: str
    # Required: Connection test result:
    status: Literal["connected", "error"]
    # Error message if connection failed
    error: NotRequired[str | None]

class CredentialAutomation(TypedDict, total=False):
    """An automated credential issuance policy"""
    # Required: Unique identifier (hashid)
    id: str
    # Required: Display name for the automation
    name: str
    # Required: How the automation is triggered:
    trigger_mode: Literal["manual", "scheduled", "webhook"]
    # Required: Current status:
    status: Literal["draft", "active", "paused", "error"]
    # Cron expression for scheduled mode
    schedule: NotRequired[str | None]
    # Required: The linked data source mapping
    data_source_mapping: dict[str, Any]
    # Required: The domain under which credentials are issued
    account_domain: dict[str, Any]
    # Required: Whether the automation can be triggered
    can_run: bool
    # Required: Whether the automation is currently running
    running: bool
    # Information about the last run (detail view only)
    last_run: NotRequired[dict[str, Any] | None]
    # Webhook configuration (webhook mode only, detail view)
    webhook: NotRequired[dict[str, Any] | None]
    # Required: When the automation was created
    created_at: str
    # Required: When the automation was last updated
    updated_at: str

class AutomationTriggerResult(TypedDict, total=False):
    """Result of triggering an automation"""
    # Required: Result message
    message: str
    # Required: Hashid of the created run log
    run_id: str
    # Required: Initial status of the run
    status: Literal["pending"]

class AutomationWebhook(TypedDict, total=False):
    """Webhook configuration for an automation"""
    # Required: The automation's unique identifier
    automation_id: str
    # Required: Display name of the automation
    automation_name: str
    # Required: Full URL to POST to trigger the automation
    trigger_url: str
    # Required: The webhook token (included in trigger_url)
    token: str
    # When the token was generated
    generated_at: NotRequired[str | None]
    # Required: Current trigger mode of the automation
    trigger_mode: Literal["manual", "scheduled", "webhook"]
    # Required: Whether webhook triggers are allowed (true when trigger_mode=webhook and status=active)
    enabled: bool

class AccountDomain(TypedDict, total=False):
    """A custom domain for the account's verifiable credentials"""
    # Required: The domain name (also serves as unique identifier)
    domain: str
    # Required: The DID derived from this domain
    did: str
    # Required: Whether this is the primary domain for the account
    primary: bool
    # Required: Whether both TXT and CNAME verification have passed
    fully_verified: bool
    # Required: TXT record verification status
    txt_status: Literal["pending", "verified", "failed"]
    # When TXT verification passed
    txt_verified_at: NotRequired[str | None]
    # Required: Whether CNAME verification has passed
    cname_verified: bool
    # When CNAME verification passed
    cname_verified_at: NotRequired[str | None]
    # Required: When the domain was created
    created_at: str
    # Required: When the domain was last updated
    updated_at: str

class AccountDomainVerification(TypedDict, total=False):
    """Domain verification instructions"""
    txt: NotRequired[dict[str, Any]]
    cname: NotRequired[dict[str, Any]]

class DomainVerificationResult(TypedDict, total=False):
    """Result of domain verification check"""
    # The domain name
    domain: NotRequired[str]
    # Whether both verifications passed
    fully_verified: NotRequired[bool]
    txt_verification: NotRequired[dict[str, Any]]
    cname_verification: NotRequired[dict[str, Any]]

class SigningKey(TypedDict, total=False):
    """A cryptographic signing key for verifiable credentials"""
    # Required: Unique key identifier
    key_id: str
    # Required: Cryptographic algorithm (ES256, ES384, or Ed25519)
    algorithm: Literal["es256", "es384", "ed25519"]
    # Required: Key lifecycle status
    status: Literal["pending", "active", "revoked", "expired"]
    # Required: Whether the key can be used for signing (active and not expired)
    usable: bool
    # Required: Whether the key has been rotated and is in legacy grace period
    legacy: bool
    # When the key expires (null = no expiration)
    expires_at: NotRequired[str | None]
    # Required: When the key was created
    created_at: str
    # Required: When the key was last updated
    updated_at: str

class CertificateResponse(TypedDict, total=False):
    """X.509 certificate for a signing key"""
    # Domain the certificate is for
    domain: NotRequired[str]
    # Signing key identifier
    key_id: NotRequired[str]
    # How the certificate was obtained
    certificate_type: NotRequired[Literal["self_signed", "acme", "uploaded"]]
    # Certificate subject common name
    subject: NotRequired[str]
    # Certificate issuer common name
    issuer: NotRequired[str]
    # When the certificate expires
    expires_at: NotRequired[str]
    # Subject alternative DNS names
    san_dns_names: NotRequired[list[str]]
    # PEM-encoded certificate chain
    certificate_chain_pem: NotRequired[list[str]]

class ApiKey(TypedDict, total=False):
    """An API key for programmatic access.

Each account has one secret key and one publishable key:
- **Secret keys**: For server-to-server API calls. Masked in responses.
- **Publishable keys**: For browser-based requests. Always shown in full."""
    # Required: Unique key identifier (hashid)
    id: str
    # Required: Key type
    type: Literal["secret_key", "publishable_key"]
    # Required: Display name for the key
    name: str
    # Required: Key lifecycle status
    status: Literal["pending", "active", "revoked", "expired"]
    # Required: Whether the key can be used (active and not expired)
    usable: bool
    # Required: Allowed IPs/CIDRs (secret keys) or origins (publishable keys)
    allowed_sources: list[str]
    # Full key value. Always shown for publishable keys; only on regeneration for secret keys.
    key: NotRequired[str | None]
    # Masked key (secret keys only)
    masked_key: NotRequired[str | None]
    # When the key was last used
    last_used_at: NotRequired[str | None]
    # When the key expires
    expires_at: NotRequired[str | None]
    # Required: When the key was created
    created_at: str
    # Required: When the key was last updated
    updated_at: str

class Webhook(TypedDict, total=False):
    """A webhook endpoint for receiving event notifications"""
    # Required: Webhook identifier (currently always 'primary')
    id: str
    # Required: The webhook endpoint URL
    url: str
    # Required: Whether the webhook is configured
    configured: bool
    # When the webhook was created (not currently tracked)
    created_at: NotRequired[str | None]
    # When the webhook was last updated (not currently tracked)
    updated_at: NotRequired[str | None]

class WebhookTestResult(TypedDict, total=False):
    """Result of testing a webhook endpoint"""
    # Result message
    message: NotRequired[str]
    # HTTP status code from the webhook endpoint
    status_code: NotRequired[int | None]
    # Error message if the test failed
    error: NotRequired[str | None]

class UpdateApiKeyParams(TypedDict, total=False):
    """Parameters for updating an API key"""
    api_key: NotRequired[dict[str, Any]]

class CreateDomainParams(TypedDict, total=False):
    """Parameters for registering a domain"""
    # Required: Domain name to register
    domain: str

class CreateSigningKeyParams(TypedDict, total=False):
    """Parameters for generating a signing key"""
    # Cryptographic algorithm (default: es256)
    algorithm: NotRequired[Literal["es256", "es384", "ed25519"]]
    # Activate immediately (default: true)
    activate: NotRequired[bool]

class RotateSigningKeyParams(TypedDict, total=False):
    """Parameters for rotating a signing key"""
    # Algorithm for new key (default: same as old key)
    algorithm: NotRequired[Literal["es256", "es384", "ed25519"]]

class CreateWebhookParams(TypedDict, total=False):
    """Parameters for configuring a webhook"""
    # Required: Webhook endpoint URL
    url: str

class UpdateWebhookParams(TypedDict, total=False):
    """Parameters for updating a webhook"""
    # New webhook endpoint URL
    url: NotRequired[str]

class CreatePresentationParams(TypedDict, total=False):
    """Parameters for creating a selective disclosure presentation"""
    # Required: UUID of the credential to present
    credential_uuid: str
    # Required: Claim names to disclose
    disclosed_claims: list[str]
    # Intended recipient of the presentation
    audience: NotRequired[str]
    # Purpose of the presentation
    purpose: NotRequired[str]
    # Expiration in seconds from now
    expires_in: NotRequired[int]

class VerifyPresentationParams(TypedDict, total=False):
    """Parameters for verifying a presentation"""
    # Required: The SD-JWT presentation token to verify
    token: str

class CreatePresentationRequestParams(TypedDict, total=False):
    """Parameters for creating a presentation request"""
    # Required: Display name for the request
    name: str
    # Purpose shown to holder explaining why claims are needed
    purpose: NotRequired[str]
    # Query format to use (default: dcql)
    query_format: NotRequired[Literal["presentation_exchange", "dcql"]]
    # DCQL query definition (for dcql format)
    dcql_query: NotRequired[dict[str, Any]]
    # Presentation Exchange definition (for presentation_exchange format)
    presentation_definition: NotRequired[dict[str, Any]]
    # Expiration in seconds from now
    expires_in: NotRequired[int]
    # Maximum number of responses allowed
    max_responses: NotRequired[int]
    # Webhook URL for response notifications
    callback_url: NotRequired[str]
    # Where to redirect holder after response
    redirect_url: NotRequired[str]

class UpdatePresentationRequestParams(TypedDict, total=False):
    """Parameters for updating a presentation request"""
    # Display name for the request
    name: NotRequired[str]
    # Purpose shown to holder
    purpose: NotRequired[str]
    # Webhook URL for response notifications
    callback_url: NotRequired[str]
    # Where to redirect holder after response
    redirect_url: NotRequired[str]

class CreateAutomationParams(TypedDict, total=False):
    """Parameters for creating a credential automation"""
    # Required: Display name for the automation
    name: str
    # Required: Data source mapping slug or hashid
    data_source_mapping: str
    # Required: Domain name or hashid (e.g., 'trust.example.com')
    account_domain: str
    # Required: How the automation is triggered
    trigger_mode: Literal["manual", "scheduled", "webhook"]
    # Cron expression for scheduled mode
    schedule: NotRequired[str]

class UpdateAutomationParams(TypedDict, total=False):
    """Parameters for updating an automation"""
    # Display name for the automation
    name: NotRequired[str]
    # How the automation is triggered
    trigger_mode: NotRequired[Literal["manual", "scheduled", "webhook"]]
    # Cron expression for scheduled mode
    schedule: NotRequired[str]
    # Automation status
    status: NotRequired[Literal["draft", "active", "paused"]]

class CreateCredentialParams(TypedDict, total=False):
    """Parameters for issuing a credential"""
    # Required: Schema UUID or slug
    schema_id: str
    # Required: Email or DID identifying the credential subject
    subject_identifier: str
    # Type of subject identifier
    subject_identifier_type: NotRequired[Literal["email", "did"]]
    # Required: Credential claims (schema-dependent)
    claims: dict[str, Any]
    # Expiration in seconds from now
    expires_in: NotRequired[int]
    # Specific signing key to use
    signing_key_id: NotRequired[str]

class RevokeCredentialParams(TypedDict, total=False):
    """Parameters for revoking a credential"""
    # Required: Reason for revocation (required for audit)
    reason: str

class RevokeBatchParams(TypedDict, total=False):
    """Parameters for batch revoking credentials"""
    # Required: UUIDs of credentials to revoke (max 100)
    uuids: list[str]
    # Required: Reason for revocation
    reason: str

class SuspendBatchParams(TypedDict, total=False):
    """Parameters for batch suspending credentials"""
    # Required: UUIDs of credentials to suspend (max 100)
    uuids: list[str]

class ReinstateBatchParams(TypedDict, total=False):
    """Parameters for batch reinstating credentials"""
    # Required: UUIDs of credentials to reinstate (max 100)
    uuids: list[str]

class CreateDataSourceMappingParams(TypedDict, total=False):
    """Parameters for creating a data source mapping"""
    # Required: ID of the data source
    data_source_id: str
    # Required: UUID or slug of the credential schema
    credential_schema_id: str
    # Optional custom name for the mapping
    name: NotRequired[str]
    # Required: Maps data source columns to credential claims
    field_mapping: dict[str, Any]
    # Query configuration for data extraction
    query_config: NotRequired[dict[str, Any]]

class UpdateDataSourceMappingParams(TypedDict, total=False):
    """Parameters for updating a data source mapping"""
    # Custom name for the mapping
    name: NotRequired[str]
    # Maps data source columns to credential claims
    field_mapping: NotRequired[dict[str, Any]]
    # Query configuration for data extraction
    query_config: NotRequired[dict[str, Any]]

class PostgresqlConnectionSettings(TypedDict, total=False):
    """PostgreSQL connection settings"""
    # Required: Database server hostname or IP address
    host: str
    # Database server port (1-65535)
    port: NotRequired[int]
    # Required: Name of the database to connect to
    database: str
    # Database user for authentication (optional for local/trusted connections)
    username: NotRequired[str]
    # Database password (optional for passwordless/trusted connections)
    password: NotRequired[str]
    # SSL connection mode: prefer (try SSL first), require (must use SSL), disable (no SSL)
    sslmode: NotRequired[Literal["prefer", "require", "disable"]]

class CreateOfferParams(TypedDict, total=False):
    """Parameters for creating a credential offer"""
    # Required: Schema UUID or slug
    schema_id: str
    # Email or unique ID of the intended recipient
    subject_identifier: NotRequired[str]
    # Required: Pre-filled claim values
    subject_claims: dict[str, Any]
    # Expiration in seconds from now
    expires_in: NotRequired[int]
    # Require PIN/tx_code to claim (OID4VCI 1.0)
    require_tx_code: NotRequired[bool]

class CreateSchemaParams(TypedDict, total=False):
    """Parameters for creating a credential schema"""
    # Required: Display name for the schema
    name: str
    # Required: PascalCase credential type identifier
    credential_type: str
    # Required: Schema category
    schema_type: Literal["custom", "education_credential", "employment_credential", "open_badge", "certificate"]
    # Required: JSON Schema for credential claims
    subject_schema: dict[str, Any]
    # Supported credential formats
    supported_formats: NotRequired[list[Literal["jwt_vc", "sd_jwt_vc", "mdoc", "data_integrity"]]]

class UpdateSchemaParams(TypedDict, total=False):
    """Parameters for updating a draft schema"""
    # Display name for the schema
    name: NotRequired[str]
    # JSON Schema for credential claims
    subject_schema: NotRequired[dict[str, Any]]
    # Supported credential formats
    supported_formats: NotRequired[list[Literal["jwt_vc", "sd_jwt_vc", "mdoc", "data_integrity"]]]

class VerifyCredentialParams(TypedDict, total=False):
    """Parameters for verifying a credential"""
    # Credential UUID to verify
    uuid: NotRequired[str]
    # Credential JWT to verify (alternative to uuid)
    jwt: NotRequired[str]
    # Skip revocation/suspension check
    skip_status_check: NotRequired[bool]
    # Skip expiration check
    skip_expiration_check: NotRequired[bool]
    # Skip cryptographic signature check
    skip_signature_check: NotRequired[bool]

class CreateRenderTemplateParams(TypedDict, total=False):
    """Parameters for creating a render template"""
    # Required: Human-readable template name
    name: str
    # Description of the template
    description: NotRequired[str]
    # Required: Template rendering engine
    render_suite: Literal["svg_mustache", "pdf_mustache"]
    # Required: Template content (SVG or HTML)
    content: str

class UpdateRenderTemplateParams(TypedDict, total=False):
    """Parameters for updating a render template"""
    # Human-readable template name
    name: NotRequired[str]
    # Description of the template
    description: NotRequired[str]
    # Template content (SVG or HTML)
    content: NotRequired[str]

class ValidateRenderTemplateParams(TypedDict, total=False):
    """Parameters for validating a render template"""
    # Required: Template rendering engine
    render_suite: Literal["svg_mustache", "pdf_mustache"]
    # Required: Template content to validate
    content: str

class DcApiSession(TypedDict, total=False):
    """A DC API session for thin client credential verification"""
    # Unique identifier for the session
    session_id: NotRequired[str]
    # Current status of the session:
    status: NotRequired[Literal["pending", "processing", "completed", "failed"]]
    # Whether verification succeeded (only present when completed)
    verified: NotRequired[bool]
    # Whether the credential comes from a trusted issuer
    trusted: NotRequired[bool]
    # Verified claims from the credential (only when completed)
    claims: NotRequired[dict[str, Any] | None]
    # Issuer information (only when completed)
    issuer: NotRequired[dict[str, Any] | None]
    # Document type identifier (e.g., org.iso.18013.5.1.mDL for Mobile Driver's License)
    document_type: NotRequired[str | None]
    # When the session expires
    expires_at: NotRequired[str]
    # When the session was created
    created_at: NotRequired[str]
    # When verification completed (only when completed)
    completed_at: NotRequired[str | None]
    # Signed URL to render the credential visually (only when completed with claims)
    render_url: NotRequired[str | None]

class DcApiSessionCreateResponse(TypedDict, total=False):
    """Response from creating a DC API session"""
    success: bool
    data: dict[str, Any]

class DcApiSessionVerifyResponse(TypedDict, total=False):
    """Response from verifying a DC API session"""
    success: bool
    data: dict[str, Any]

class CreateDcSessionParams(TypedDict, total=False):
    """Parameters for creating a DC API session"""
    # Claims to request from the credential
    claims: NotRequired[list[str]]
    # Which claims to return in the result. true=all requested (default), false=none, 'all'=all, array=specific claims
    return_claims: NotRequired[bool | Literal["all"] | list[str]]
    # Document types to accept (e.g., org.iso.18013.5.1.mDL)
    document_types: NotRequired[list[str]]
    # Display name shown in the wallet (optional, defaults to account name)
    client_name: NotRequired[str]

class VerifyDcSessionParams(TypedDict, total=False):
    """Parameters for verifying a DC API session"""
    # Required: The encrypted response from navigator.credentials.get()
    response: str
    # The origin where the credential was requested (for session transcript)
    origin: NotRequired[str]

class RenderParams(TypedDict, total=False):
    """Parameters for rendering claims as a visual credential"""
    # Built-in template key (e.g., mdl_default). Either template or render_method required.
    template: NotRequired[str]
    # W3C renderMethod object. Either template or render_method required.
    render_method: NotRequired[dict[str, Any]]
    # Required: Claims to render
    claims: dict[str, Any]
    # Output format (default: svg). Ignored when using render_method.
    format: NotRequired[Literal["svg", "pdf", "html"]]

class RenderResponse(TypedDict, total=False):
    """Rendered credential response"""
    success: bool
    data: dict[str, Any]

class TrustMeta(TypedDict, total=False):
    """Trust verification metadata for an organization"""
    # Required: Overall trust level based on completed verifications:
    level: Literal["unverified", "email_verified", "domain_fully_verified"]
    # Required: Whether the organization email matches their claimed domain
    email_verified: bool
    # Required: Whether domain ownership was verified (via DNS TXT record or /.well-known/aho-verification.json file and CNAME entry)
    domain_fully_verified: bool
    # When domain verification was completed (null if not yet verified)
    domain_verified_at: NotRequired[str | None]
    # Domain ranking based on analyzed traffic data (1 = most popular)
    domain_rank: NotRequired[int | None]
    # Required: Human-readable domain ranking tier based on analyzed traffic data:
    domain_rank_display: Literal["Top 100 website", "Top 1K website", "Top 10K website", "Top 100K website", "Known website", "Unknown website"]
    typosquatting_warning: NotRequired[TyposquattingWarning | None]

class CredentialIssuance(TypedDict, total=False):
    """A credential issuance record from the issuer's perspective"""
    # Unique identifier for the credential issuance
    uuid: NotRequired[str]
    # Current status of the credential/issuance:
    status: NotRequired[Literal["pending", "issued", "suspended", "revoked", "active", "expired", "archived"]]
    # Email or DID identifying the credential subject
    subject_identifier: NotRequired[str]
    # Type of identifier used for the subject
    subject_identifier_type: NotRequired[Literal["email", "did"]]
    # When the credential was issued
    issued_at: NotRequired[str]
    # When the credential expires
    expires_at: NotRequired[str | None]
    schema: NotRequired[dict[str, Any] | None]
    issuer: NotRequired[dict[str, Any]]
    # URL to verify this credential
    verification_url: NotRequired[str]
    # The signed JWT credential token
    credential_jwt: NotRequired[str | None]
    created_at: NotRequired[str]
    # Internal subject identifier (detail view only)
    subject_id: NotRequired[str | None]
    # Credential claims/attributes (detail view only)
    claims: NotRequired[dict[str, Any] | None]
    # Raw VC JSON-LD document (detail view only)
    vc_json: NotRequired[dict[str, Any] | None]
    # Signing key used (detail view only)
    issuer_signing_key: NotRequired[Any]
    # Number of verification attempts (detail view only)
    verification_logs_count: NotRequired[int]
    # When last updated (detail view only)
    updated_at: NotRequired[str]

class SigningKeyDetails(TypedDict, total=False):
    # Required: Unique key identifier
    key_id: str
    # Required: Cryptographic algorithm (ES256, ES384, or Ed25519)
    algorithm: Literal["es256", "es384", "ed25519"]
    # Required: Key lifecycle status
    status: Literal["pending", "active", "revoked", "expired"]
    # Required: Whether the key can be used for signing (active and not expired)
    usable: bool
    # Required: Whether the key has been rotated and is in legacy grace period
    legacy: bool
    # When the key expires (null = no expiration)
    expires_at: NotRequired[str | None]
    # Required: When the key was created
    created_at: str
    # Required: When the key was last updated
    updated_at: str
    # Public key in JWK format
    public_key_jwk: NotRequired[dict[str, Any]]
    # Active certificates for this key
    certificates: NotRequired[list[dict[str, Any]]]
    # DID verification method ID
    did_verification_method: NotRequired[str]
    # did:key identifier derived from public key
    did_key: NotRequired[str]

class KeyRotationResult(TypedDict, total=False):
    """Result of key rotation"""
    message: NotRequired[str]
    old_key: NotRequired[SigningKey]
    new_key: NotRequired[SigningKey]

class ApiKeyRegenerationResponse(TypedDict, total=False):
    message: NotRequired[str]
    api_key: NotRequired[ApiKey]
    # Security warning (secret keys only)
    warning: NotRequired[str | None]

class ApiKeyUpdateResponse(TypedDict, total=False):
    message: NotRequired[str]
    api_key: NotRequired[ApiKey]

class CreateDataSourceParams(TypedDict, total=False):
    """Parameters for creating a data source"""
    # Required: Display name for the data source
    name: str
    # Required: Type of data source
    source_type: Literal["postgresql", "csv"]
    connection_settings: NotRequired[PostgresqlConnectionSettings]

class UpdateDataSourceParams(TypedDict, total=False):
    """Parameters for updating a data source"""
    # Display name for the data source
    name: NotRequired[str]
    connection_settings: NotRequired[PostgresqlConnectionSettings]

class IssuerRefWithTrust(TypedDict, total=False):
    """Issuer reference including trust verification indicators"""
    did: str
    name: str
    trust: NotRequired[TrustMeta]

# Common types used across the API

class PageMeta(TypedDict):
    """Pagination metadata."""
    current_page: int
    per_page: int
    total_count: int
    total_pages: int

class PaginatedResponse(TypedDict):
    """Paginated response wrapper."""
    data: list[Any]
    meta: PageMeta

class ErrorDetail(TypedDict, total=False):
    """API error detail."""
    message: str
    code: NotRequired[str]
    details: NotRequired[list[FieldError] | dict[str, list[str]] | str]

class ErrorResponse(TypedDict):
    """API error response."""
    error: ErrorDetail

class FieldError(TypedDict):
    """Field-level validation error."""
    field: str
    issue: str
    hint: str

# Status type aliases
CredentialStatus = Literal["draft", "active", "suspended", "revoked", "expired"]
PresentationRequestStatus = Literal["draft", "active", "closed", "expired"]
QueryFormat = Literal["dcql", "presentation_exchange"]
CredentialFormat = Literal["vc+sd-jwt", "jwt_vc_json", "ldp_vc"]
SigningAlgorithm = Literal["ES256", "ES384", "ES512", "EdDSA"]
SigningKeyStatus = Literal["active", "pending", "revoked"]
VerificationStatus = Literal["pending", "verified", "failed"]
