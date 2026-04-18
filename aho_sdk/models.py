"""Pydantic models for runtime validation of Aho API responses.

Auto-generated from OpenAPI spec - DO NOT EDIT
"""
from __future__ import annotations

from typing import Annotated, Any, Literal, Optional, Union
from pydantic import BaseModel, ConfigDict, Discriminator, Tag

class VerificationResult(BaseModel):
    """Verification response with standard envelope. Contains:
- success: Whether the API call succeeded
- data: Object with verified (bool), status (string), message, verified_at, credential details"""
    model_config = ConfigDict(extra='ignore')

    success: bool
    data: dict[str, Any]

class PresentationVerifyResult(BaseModel):
    """Response from verifying a holder's selective disclosure presentation.
Contains verification status, disclosed claims, and credential/presentation metadata."""
    model_config = ConfigDict(extra='ignore')

    success: bool
    data: dict[str, Any]

class TyposquattingWarning(BaseModel):
    """Present if the domain resembles a well-known domain"""
    model_config = ConfigDict(extra='ignore')

    similar_to: str
    similar_to_rank: str

class IssuerRef(BaseModel):
    """Issuer reference with optional domain verification status"""
    model_config = ConfigDict(extra='ignore')

    name: Optional[str] = None
    did: Optional[str] = None
    domain: Optional[str | None] = None
    domain_fully_verified: Optional[bool] = None

class SchemaRef(BaseModel):
    """Credential schema reference"""
    model_config = ConfigDict(extra='ignore')

    uuid: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    slug: Optional[str] = None

class SubjectRef(BaseModel):
    """Credential subject identification"""
    model_config = ConfigDict(extra='ignore')

    identifier_type: Optional[str | None] = None
    did: Optional[str | None] = None

class SigningKeyRef(BaseModel):
    """Reference to the signing key used for a credential"""
    model_config = ConfigDict(extra='ignore')

    id: Optional[str] = None
    key_id: Optional[str] = None
    algorithm: Optional[Literal["es256", "es384", "ed25519"]] = None

class TrustSignal(BaseModel):
    """A trust verification signal with status indicator"""
    model_config = ConfigDict(extra='ignore')

    icon: Optional[str] = None
    text: Optional[str] = None
    status: Optional[Literal["success", "danger", "neutral"]] = None

class PaginationMeta(BaseModel):
    """Pagination metadata for list responses"""
    model_config = ConfigDict(extra='ignore')

    current_page: int
    per_page: int
    total_count: int
    total_pages: int

class FieldError(BaseModel):
    """Structured field-level validation error"""
    model_config = ConfigDict(extra='ignore')

    field: str
    issue: Literal["type_mismatch", "missing_required", "invalid_enum", "pattern_mismatch", "length_violation", "range_violation", "format_invalid", "array_size_violation", "duplicate_items", "unexpected_property", "validation_failed"]
    expected: Optional[str | None] = None
    got: Optional[str | None] = None
    hint: Optional[str | None] = None

class RateLimitError(BaseModel):
    """Rate limit exceeded error response (HTTP 429)"""
    model_config = ConfigDict(extra='ignore')

    success: bool
    error: dict[str, Any]
    retry_after: int

class Credential(BaseModel):
    """A verifiable credential issued to a holder"""
    model_config = ConfigDict(extra='ignore')

    uuid: Optional[str] = None
    status: Optional[Literal["active", "suspended", "revoked", "expired", "archived"]] = None
    subject_identifier: Optional[str] = None
    subject_identifier_type: Optional[Literal["email", "did"]] = None
    issued_at: Optional[str] = None
    expires_at: Optional[str | None] = None
    created_at: Optional[str] = None
    schema: Optional[dict[str, Any] | None] = None
    issuer: Optional[dict[str, Any]] = None
    verification_url: Optional[str] = None
    credential_jwt: Optional[str | None] = None
    claims: Optional[dict[str, Any] | None] = None
    subject_id: Optional[str | None] = None
    vc_json: Optional[dict[str, Any] | None] = None
    issuer_signing_key: Optional[dict[str, Any] | None] = None
    verification_logs_count: Optional[int] = None
    updated_at: Optional[str] = None

class Presentation(BaseModel):
    """A verifiable presentation with selective disclosure of claims"""
    model_config = ConfigDict(extra='ignore')

    uuid: str
    credential_uuid: str
    disclosed_claims: list[str]
    disclosed_values: Optional[dict[str, Any] | None] = None
    audience: Optional[str | None] = None
    purpose: Optional[str | None] = None
    status: Literal["active", "expired", "revoked"]
    expires_at: Optional[str | None] = None
    verification_count: int
    created_at: str
    presentation_token: Optional[str] = None
    share_data: Optional[dict[str, Any] | None] = None

class IssuerCredentialSchema(BaseModel):
    """An issuer's credential schema with full details"""
    model_config = ConfigDict(extra='ignore')

    uuid: str
    slug: str
    name: str
    credential_type: str
    schema_type: Literal["custom", "education_credential", "employment_credential", "open_badge", "certificate"]
    status: Literal["draft", "active", "archived"]
    supported_formats: list[Literal["jwt_vc", "sd_jwt_vc", "mdoc", "data_integrity"]]
    template_key: Optional[str | None] = None
    credential_count: int
    json_ld_context: Optional[list[str]] = None
    subject_schema: Optional[dict[str, Any]] = None
    sd_jwt_vc_config: Optional[dict[str, Any]] = None
    mdoc_config: Optional[dict[str, Any]] = None
    render_templates: Optional[list[dict[str, Any]]] = None
    created_at: str
    updated_at: str

class CredentialSchema(BaseModel):
    """A template defining the structure of a credential"""
    model_config = ConfigDict(extra='ignore')

    slug: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    credential_type: Optional[str] = None
    category: Optional[str] = None
    visibility: Optional[Literal["public", "private"]] = None
    claims: Optional[list[dict[str, Any]]] = None
    tags: Optional[list[str]] = None
    url: Optional[str] = None
    context_url: Optional[str] = None
    external_url: Optional[str | None] = None
    source: Optional[str | None] = None
    subject_schema: Optional[dict[str, Any] | None] = None
    json_ld_context: Optional[list[str] | None] = None
    svg_template_key: Optional[str | None] = None

class RenderTemplate(BaseModel):
    """A visual rendering template for credentials (SVG or PDF)"""
    model_config = ConfigDict(extra='ignore')

    id: str
    name: str
    description: Optional[str | None] = None
    render_suite: Literal["svg_mustache", "pdf_mustache"]
    template_type: Literal["custom", "system"]
    media_type: Literal["image/svg+xml", "application/pdf"]
    digest_multibase: str
    render_properties: Optional[list[str] | None] = None
    exposed_fields: Optional[list[str]] = None
    content: Optional[str | None] = None
    created_at: str
    updated_at: str

class RenderTemplateValidationResult(BaseModel):
    """Result of template validation without saving"""
    model_config = ConfigDict(extra='ignore')

    success: Optional[bool] = None
    valid: Optional[bool] = None
    digest_multibase: Optional[str | None] = None
    extracted_variables: Optional[list[str]] = None
    errors: Optional[list[str]] = None
    warnings: Optional[list[str]] = None

class CredentialOfferResult(BaseModel):
    """Result of creating a credential offer"""
    model_config = ConfigDict(extra='ignore')

    offer_id: str
    offer_uri: str
    deep_link: str
    tx_code: Optional[str | None] = None
    expires_at: str

class WebhookPayload(BaseModel):
    """Payload sent to verifier webhook endpoints when a holder responds to a presentation request.
The webhook includes an X-Webhook-Signature header for verification (HMAC-SHA256 of timestamp.payload using API key).
Verifiers should validate this signature before processing the payload."""
    model_config = ConfigDict(extra='ignore')

    event: Literal["presentation_response.approved", "presentation_response.declined"]
    timestamp: str
    request: dict[str, Any]
    response: dict[str, Any]
    verifier: dict[str, Any]
    holder: Optional[dict[str, Any] | None] = None
    disclosed_claims: Optional[dict[str, Any] | None] = None
    credential: Optional[dict[str, Any] | None] = None

class BatchOperationResult(BaseModel):
    """Result of a batch operation (revoke_batch, suspend_batch, reinstate_batch).
Contains per-UUID results for debugging and summary counts."""
    model_config = ConfigDict(extra='ignore')

    items: list[dict[str, Any]]
    summary: dict[str, Any]

class CredentialOffer(BaseModel):
    """A credential offer that holders can claim via wallet apps (OID4VCI)"""
    model_config = ConfigDict(extra='ignore')

    uuid: str
    status: Literal["pending", "accepted", "expired", "revoked"]
    subject_identifier: Optional[str | None] = None
    subject_claims: dict[str, Any]
    expires_at: Optional[str | None] = None
    created_at: str
    schema: dict[str, Any]
    offer_uri: Optional[str | None] = None
    deep_link: Optional[str | None] = None

class PresentationRequest(BaseModel):
    """An OpenID4VP presentation request created by a verifier"""
    model_config = ConfigDict(extra='ignore')

    uuid: str
    name: str
    purpose: Optional[str | None] = None
    status: Literal["draft", "active", "expired", "closed"]
    query_format: Literal["presentation_exchange", "dcql"]
    expires_at: Optional[str | None] = None
    max_responses: Optional[int | None] = None
    callback_url: Optional[str | None] = None
    redirect_url: Optional[str | None] = None
    created_at: str
    updated_at: str
    verifier: dict[str, Any]
    urls: Optional[dict[str, Any] | None] = None
    stats: Optional[dict[str, Any] | None] = None
    dcql_query: Optional[dict[str, Any] | None] = None
    presentation_definition: Optional[dict[str, Any] | None] = None

class PresentationResponse(BaseModel):
    """A holder's response to a presentation request"""
    model_config = ConfigDict(extra='ignore')

    uuid: str
    status: Literal["pending", "approved", "declined"]
    responded_at: Optional[str | None] = None
    created_at: str
    holder: Optional[dict[str, Any] | None] = None
    disclosed_claims: Optional[dict[str, Any] | None] = None
    claim_mapping: Optional[dict[str, Any] | None] = None
    credential: Optional[dict[str, Any] | None] = None
    credentials: Optional[list[dict[str, Any]] | None] = None

class DataSource(BaseModel):
    """A data source for automated credential issuance"""
    model_config = ConfigDict(extra='ignore')

    slug: str
    name: str
    source_type: Literal["postgresql", "csv"]
    status: Literal["draft", "active", "paused", "error"]
    mapping_count: int
    connection_info: Optional[dict[str, Any] | None] = None
    source_file: Optional[dict[str, Any] | None] = None
    created_at: str
    updated_at: str

class DataSourceMapping(BaseModel):
    """A mapping between a data source and credential schema"""
    model_config = ConfigDict(extra='ignore')

    slug: str
    name: Optional[str | None] = None
    display_name: str
    data_source: dict[str, Any]
    credential_schema: dict[str, Any]
    field_mapping: Optional[dict[str, Any] | None] = None
    query_config: Optional[dict[str, Any] | None] = None
    automation_count: int
    created_at: str
    updated_at: str

class DataSourceTestResult(BaseModel):
    """Result of testing a data source connection"""
    model_config = ConfigDict(extra='ignore')

    message: str
    status: Literal["connected", "error"]
    error: Optional[str | None] = None

class CredentialAutomation(BaseModel):
    """An automated credential issuance policy"""
    model_config = ConfigDict(extra='ignore')

    id: str
    name: str
    trigger_mode: Literal["manual", "scheduled", "webhook"]
    status: Literal["draft", "active", "paused", "error"]
    schedule: Optional[str | None] = None
    data_source_mapping: dict[str, Any]
    account_domain: dict[str, Any]
    can_run: bool
    running: bool
    last_run: Optional[dict[str, Any] | None] = None
    webhook: Optional[dict[str, Any] | None] = None
    created_at: str
    updated_at: str

class AutomationTriggerResult(BaseModel):
    """Result of triggering an automation"""
    model_config = ConfigDict(extra='ignore')

    message: str
    run_id: str
    status: Literal["pending"]

class AutomationWebhook(BaseModel):
    """Webhook configuration for an automation"""
    model_config = ConfigDict(extra='ignore')

    automation_id: str
    automation_name: str
    trigger_url: str
    token: str
    generated_at: Optional[str | None] = None
    trigger_mode: Literal["manual", "scheduled", "webhook"]
    enabled: bool

class AccountDomain(BaseModel):
    """A custom domain for the account's verifiable credentials"""
    model_config = ConfigDict(extra='ignore')

    domain: str
    did: str
    primary: bool
    fully_verified: bool
    txt_status: Literal["pending", "verified", "failed"]
    txt_verified_at: Optional[str | None] = None
    cname_verified: bool
    cname_verified_at: Optional[str | None] = None
    created_at: str
    updated_at: str

class AccountDomainVerification(BaseModel):
    """Domain verification instructions"""
    model_config = ConfigDict(extra='ignore')

    txt: Optional[dict[str, Any]] = None
    cname: Optional[dict[str, Any]] = None

class DomainVerificationResult(BaseModel):
    """Result of domain verification check"""
    model_config = ConfigDict(extra='ignore')

    domain: Optional[str] = None
    fully_verified: Optional[bool] = None
    txt_verification: Optional[dict[str, Any]] = None
    cname_verification: Optional[dict[str, Any]] = None

class SigningKey(BaseModel):
    """A cryptographic signing key for verifiable credentials"""
    model_config = ConfigDict(extra='ignore')

    key_id: str
    algorithm: Literal["es256", "es384", "ed25519"]
    status: Literal["pending", "active", "revoked", "expired"]
    usable: bool
    legacy: bool
    expires_at: Optional[str | None] = None
    created_at: str
    updated_at: str

class CertificateResponse(BaseModel):
    """X.509 certificate for a signing key"""
    model_config = ConfigDict(extra='ignore')

    domain: Optional[str] = None
    key_id: Optional[str] = None
    certificate_type: Optional[Literal["self_signed", "acme", "uploaded"]] = None
    subject: Optional[str] = None
    issuer: Optional[str] = None
    expires_at: Optional[str] = None
    san_dns_names: Optional[list[str]] = None
    certificate_chain_pem: Optional[list[str]] = None

class ApiKey(BaseModel):
    """An API key for programmatic access.

Each account has one secret key and one publishable key:
- **Secret keys**: For server-to-server API calls. Masked in responses.
- **Publishable keys**: For browser-based requests. Always shown in full."""
    model_config = ConfigDict(extra='ignore')

    id: str
    type: Literal["secret_key", "publishable_key"]
    name: str
    status: Literal["pending", "active", "revoked", "expired"]
    usable: bool
    allowed_sources: list[str]
    key: Optional[str | None] = None
    masked_key: Optional[str | None] = None
    last_used_at: Optional[str | None] = None
    expires_at: Optional[str | None] = None
    created_at: str
    updated_at: str

class Webhook(BaseModel):
    """A webhook endpoint for receiving event notifications"""
    model_config = ConfigDict(extra='ignore')

    id: str
    url: str
    configured: bool
    created_at: Optional[str | None] = None
    updated_at: Optional[str | None] = None

class WebhookTestResult(BaseModel):
    """Result of testing a webhook endpoint"""
    model_config = ConfigDict(extra='ignore')

    message: Optional[str] = None
    status_code: Optional[int | None] = None
    error: Optional[str | None] = None

class UpdateApiKeyParams(BaseModel):
    """Parameters for updating an API key"""
    model_config = ConfigDict(extra='ignore')

    api_key: Optional[dict[str, Any]] = None

class CreateDomainParams(BaseModel):
    """Parameters for registering a domain"""
    model_config = ConfigDict(extra='ignore')

    domain: str

class CreateSigningKeyParams(BaseModel):
    """Parameters for generating a signing key"""
    model_config = ConfigDict(extra='ignore')

    algorithm: Optional[Literal["es256", "es384", "ed25519"]] = None
    activate: Optional[bool] = None

class RotateSigningKeyParams(BaseModel):
    """Parameters for rotating a signing key"""
    model_config = ConfigDict(extra='ignore')

    algorithm: Optional[Literal["es256", "es384", "ed25519"]] = None

class CreateWebhookParams(BaseModel):
    """Parameters for configuring a webhook"""
    model_config = ConfigDict(extra='ignore')

    url: str

class UpdateWebhookParams(BaseModel):
    """Parameters for updating a webhook"""
    model_config = ConfigDict(extra='ignore')

    url: Optional[str] = None

class CreatePresentationParams(BaseModel):
    """Parameters for creating a selective disclosure presentation"""
    model_config = ConfigDict(extra='ignore')

    credential_uuid: str
    disclosed_claims: list[str]
    audience: Optional[str] = None
    purpose: Optional[str] = None
    expires_in: Optional[int] = None

class VerifyPresentationParams(BaseModel):
    """Parameters for verifying a presentation"""
    model_config = ConfigDict(extra='ignore')

    token: str

class CreatePresentationRequestParams(BaseModel):
    """Parameters for creating a presentation request"""
    model_config = ConfigDict(extra='ignore')

    name: str
    purpose: Optional[str] = None
    query_format: Optional[Literal["presentation_exchange", "dcql"]] = None
    dcql_query: Optional[dict[str, Any]] = None
    presentation_definition: Optional[dict[str, Any]] = None
    expires_in: Optional[int] = None
    max_responses: Optional[int] = None
    callback_url: Optional[str] = None
    redirect_url: Optional[str] = None

class UpdatePresentationRequestParams(BaseModel):
    """Parameters for updating a presentation request"""
    model_config = ConfigDict(extra='ignore')

    name: Optional[str] = None
    purpose: Optional[str] = None
    callback_url: Optional[str] = None
    redirect_url: Optional[str] = None

class CreateAutomationParams(BaseModel):
    """Parameters for creating a credential automation"""
    model_config = ConfigDict(extra='ignore')

    name: str
    data_source_mapping: str
    account_domain: str
    trigger_mode: Literal["manual", "scheduled", "webhook"]
    schedule: Optional[str] = None

class UpdateAutomationParams(BaseModel):
    """Parameters for updating an automation"""
    model_config = ConfigDict(extra='ignore')

    name: Optional[str] = None
    trigger_mode: Optional[Literal["manual", "scheduled", "webhook"]] = None
    schedule: Optional[str] = None
    status: Optional[Literal["draft", "active", "paused"]] = None

class CreateCredentialParams(BaseModel):
    """Parameters for issuing a credential"""
    model_config = ConfigDict(extra='ignore')

    schema_id: str
    subject_identifier: str
    subject_identifier_type: Optional[Literal["email", "did"]] = None
    claims: dict[str, Any]
    expires_in: Optional[int] = None
    signing_key_id: Optional[str] = None

class RevokeCredentialParams(BaseModel):
    """Parameters for revoking a credential"""
    model_config = ConfigDict(extra='ignore')

    reason: str

class RevokeBatchParams(BaseModel):
    """Parameters for batch revoking credentials"""
    model_config = ConfigDict(extra='ignore')

    uuids: list[str]
    reason: str

class SuspendBatchParams(BaseModel):
    """Parameters for batch suspending credentials"""
    model_config = ConfigDict(extra='ignore')

    uuids: list[str]

class ReinstateBatchParams(BaseModel):
    """Parameters for batch reinstating credentials"""
    model_config = ConfigDict(extra='ignore')

    uuids: list[str]

class CreateDataSourceMappingParams(BaseModel):
    """Parameters for creating a data source mapping"""
    model_config = ConfigDict(extra='ignore')

    data_source_id: str
    credential_schema_id: str
    name: Optional[str] = None
    field_mapping: dict[str, Any]
    query_config: Optional[dict[str, Any]] = None

class UpdateDataSourceMappingParams(BaseModel):
    """Parameters for updating a data source mapping"""
    model_config = ConfigDict(extra='ignore')

    name: Optional[str] = None
    field_mapping: Optional[dict[str, Any]] = None
    query_config: Optional[dict[str, Any]] = None

class PostgresqlConnectionSettings(BaseModel):
    """PostgreSQL connection settings"""
    model_config = ConfigDict(extra='ignore')

    host: str
    port: Optional[int] = None
    database: str
    username: Optional[str] = None
    password: Optional[str] = None
    sslmode: Optional[Literal["prefer", "require", "disable"]] = None

class CreateOfferParams(BaseModel):
    """Parameters for creating a credential offer"""
    model_config = ConfigDict(extra='ignore')

    schema_id: str
    subject_identifier: Optional[str] = None
    subject_claims: dict[str, Any]
    expires_in: Optional[int] = None
    require_tx_code: Optional[bool] = None

class CreateSchemaParams(BaseModel):
    """Parameters for creating a credential schema"""
    model_config = ConfigDict(extra='ignore')

    name: str
    credential_type: str
    schema_type: Literal["custom", "education_credential", "employment_credential", "open_badge", "certificate"]
    subject_schema: dict[str, Any]
    supported_formats: Optional[list[Literal["jwt_vc", "sd_jwt_vc", "mdoc", "data_integrity"]]] = None

class UpdateSchemaParams(BaseModel):
    """Parameters for updating a draft schema"""
    model_config = ConfigDict(extra='ignore')

    name: Optional[str] = None
    subject_schema: Optional[dict[str, Any]] = None
    supported_formats: Optional[list[Literal["jwt_vc", "sd_jwt_vc", "mdoc", "data_integrity"]]] = None

class VerifyCredentialParams(BaseModel):
    """Parameters for verifying a credential"""
    model_config = ConfigDict(extra='ignore')

    uuid: Optional[str] = None
    jwt: Optional[str] = None
    skip_status_check: Optional[bool] = None
    skip_expiration_check: Optional[bool] = None
    skip_signature_check: Optional[bool] = None

class CreateRenderTemplateParams(BaseModel):
    """Parameters for creating a render template"""
    model_config = ConfigDict(extra='ignore')

    name: str
    description: Optional[str] = None
    render_suite: Literal["svg_mustache", "pdf_mustache"]
    content: str

class UpdateRenderTemplateParams(BaseModel):
    """Parameters for updating a render template"""
    model_config = ConfigDict(extra='ignore')

    name: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None

class ValidateRenderTemplateParams(BaseModel):
    """Parameters for validating a render template"""
    model_config = ConfigDict(extra='ignore')

    render_suite: Literal["svg_mustache", "pdf_mustache"]
    content: str

class DcApiSession(BaseModel):
    """A DC API session for thin client credential verification"""
    model_config = ConfigDict(extra='ignore')

    session_id: Optional[str] = None
    status: Optional[Literal["pending", "processing", "completed", "failed"]] = None
    verified: Optional[bool] = None
    trusted: Optional[bool] = None
    claims: Optional[dict[str, Any] | None] = None
    issuer: Optional[dict[str, Any] | None] = None
    document_type: Optional[str | None] = None
    expires_at: Optional[str] = None
    created_at: Optional[str] = None
    completed_at: Optional[str | None] = None
    render_url: Optional[str | None] = None

class DcApiSessionCreateResponse(BaseModel):
    """Response from creating a DC API session"""
    model_config = ConfigDict(extra='ignore')

    success: bool
    data: dict[str, Any]

class DcApiSessionVerifyResponse(BaseModel):
    """Response from verifying a DC API session"""
    model_config = ConfigDict(extra='ignore')

    success: bool
    data: dict[str, Any]

class CreateDcSessionParams(BaseModel):
    """Parameters for creating a DC API session"""
    model_config = ConfigDict(extra='ignore')

    claims: Optional[list[str]] = None
    return_claims: Optional[Union[bool, Literal["all"], list[str]]] = None
    document_types: Optional[list[str]] = None
    client_name: Optional[str] = None

class VerifyDcSessionParams(BaseModel):
    """Parameters for verifying a DC API session"""
    model_config = ConfigDict(extra='ignore')

    response: str
    origin: Optional[str] = None

class RenderParams(BaseModel):
    """Parameters for rendering claims as a visual credential"""
    model_config = ConfigDict(extra='ignore')

    template: Optional[str] = None
    render_method: Optional[dict[str, Any]] = None
    claims: dict[str, Any]
    format: Optional[Literal["svg", "pdf", "html"]] = None

class RenderResponse(BaseModel):
    """Rendered credential response"""
    model_config = ConfigDict(extra='ignore')

    success: bool
    data: dict[str, Any]

class TrustMeta(BaseModel):
    """Trust verification metadata for an organization"""
    model_config = ConfigDict(extra='ignore')

    level: Literal["unverified", "email_verified", "domain_fully_verified"]
    email_verified: bool
    domain_fully_verified: bool
    domain_verified_at: Optional[str | None] = None
    domain_rank: Optional[int | None] = None
    domain_rank_display: Literal["Top 100 website", "Top 1K website", "Top 10K website", "Top 100K website", "Known website", "Unknown website"]
    typosquatting_warning: Optional[TyposquattingWarning | None] = None

class CredentialIssuance(BaseModel):
    """A credential issuance record from the issuer's perspective"""
    model_config = ConfigDict(extra='ignore')

    uuid: Optional[str] = None
    status: Optional[Literal["pending", "issued", "suspended", "revoked", "active", "expired", "archived"]] = None
    subject_identifier: Optional[str] = None
    subject_identifier_type: Optional[Literal["email", "did"]] = None
    issued_at: Optional[str] = None
    expires_at: Optional[str | None] = None
    schema: Optional[dict[str, Any] | None] = None
    issuer: Optional[dict[str, Any]] = None
    verification_url: Optional[str] = None
    credential_jwt: Optional[str | None] = None
    created_at: Optional[str] = None
    subject_id: Optional[str | None] = None
    claims: Optional[dict[str, Any] | None] = None
    vc_json: Optional[dict[str, Any] | None] = None
    issuer_signing_key: Optional[Any] = None
    verification_logs_count: Optional[int] = None
    updated_at: Optional[str] = None

class SigningKeyDetails(BaseModel):
    model_config = ConfigDict(extra='ignore')

    key_id: str
    algorithm: Literal["es256", "es384", "ed25519"]
    status: Literal["pending", "active", "revoked", "expired"]
    usable: bool
    legacy: bool
    expires_at: Optional[str | None] = None
    created_at: str
    updated_at: str
    public_key_jwk: Optional[dict[str, Any]] = None
    certificates: Optional[list[dict[str, Any]]] = None
    did_verification_method: Optional[str] = None
    did_key: Optional[str] = None

class KeyRotationResult(BaseModel):
    """Result of key rotation"""
    model_config = ConfigDict(extra='ignore')

    message: Optional[str] = None
    old_key: Optional[SigningKey] = None
    new_key: Optional[SigningKey] = None

class ApiKeyRegenerationResponse(BaseModel):
    model_config = ConfigDict(extra='ignore')

    message: Optional[str] = None
    api_key: Optional[ApiKey] = None
    warning: Optional[str | None] = None

class ApiKeyUpdateResponse(BaseModel):
    model_config = ConfigDict(extra='ignore')

    message: Optional[str] = None
    api_key: Optional[ApiKey] = None

class CreateDataSourceParams(BaseModel):
    """Parameters for creating a data source"""
    model_config = ConfigDict(extra='ignore')

    name: str
    source_type: Literal["postgresql", "csv"]
    connection_settings: Optional[PostgresqlConnectionSettings] = None

class UpdateDataSourceParams(BaseModel):
    """Parameters for updating a data source"""
    model_config = ConfigDict(extra='ignore')

    name: Optional[str] = None
    connection_settings: Optional[PostgresqlConnectionSettings] = None

class IssuerRefWithTrust(BaseModel):
    """Issuer reference including trust verification indicators"""
    model_config = ConfigDict(extra='ignore')

    did: str
    name: str
    trust: Optional[TrustMeta] = None

# Common models used across the API

class PageMeta(BaseModel):
    """Pagination metadata."""
    model_config = ConfigDict(extra='ignore')

    current_page: int
    per_page: int
    total_count: int
    total_pages: int

class FieldError(BaseModel):
    """Field-level validation error."""
    model_config = ConfigDict(extra='ignore')

    field: str
    issue: str
    hint: str

class ErrorDetail(BaseModel):
    """API error detail."""
    model_config = ConfigDict(extra='ignore')

    message: str
    code: Optional[str] = None
    details: Optional[Union[list[FieldError], dict[str, list[str]], str]] = None

class ErrorResponse(BaseModel):
    """API error response."""
    model_config = ConfigDict(extra='ignore')

    error: ErrorDetail
