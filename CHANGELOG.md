# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2026-05-05

### Changed

- **Breaking:** Batch credential operations moved from separate resources to `credentials` resource
  - `client.revoke_batch.create()` → `client.credentials.revoke_batch()`
  - `client.suspend_batch.create()` → `client.credentials.suspend_batch()`
  - `client.reinstate_batch.create()` → `client.credentials.reinstate_batch()`

## [0.1.1] - 2026-05-05

### Changed

- API base URL updated to `https://api.aho.com` (subdomain routing)
- API paths simplified from `/api/v1/*` to `/v1/*`

## [0.1.0] - 2026-04-17

### Added

- Initial release
- Issuer client for credential issuance
- Holder client for wallet management
- Verifier client for presentation verification
- Account client for account management
- Pagination support
- Comprehensive error handling
