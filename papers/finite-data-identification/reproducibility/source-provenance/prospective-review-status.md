# Prospective-failure reviewer reconciliation

The load-bearing exact lower certificate is copied verbatim as `../verification/prospective-hostile-certificate.json` from PR #220.

PR #221 subsequently reconciled the execution-status caveat without changing the scientific result:

```text
reconciliation terminal = dc782001d75247ab1c56d9ee52aac430c12333cc
independent_recomputation_executed = YES
independent_recomputation_agrees = YES
fresh_remote_classification = FAIL
frozen Phi4 SHA-256 = 48abd5f52812ef7503cfdde92fe630b99ded9c10c4ef35d2c4edc8d934028125
fresh F1 hostile lower diagnostic = 0.6246936110450201
banked exact F1 lower = 0.6246936110454476
fresh F2 hostile lower diagnostic = 0.6217658417777434
banked exact F2 lower = 0.6217658417777687
```

The fresh values are an independent numerical cross-check; the exact banked PR #220 certificate remains the load-bearing lower authority. No new physics was executed while preparing this publication packet.
