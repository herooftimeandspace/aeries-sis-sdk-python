# Architecture

The SDK has three layers:

1. Contract acquisition and normalization under `contracts/` and `tools/sync_contracts.py`.
2. Generated endpoint wrappers under `src/aeries_sis_sdk/generated/`.
3. Hand-written runtime behavior under `src/aeries_sis_sdk/` for transport, errors, retries, auth, and validation.

This split keeps upstream-document parsing separate from the public SDK runtime.

