# SHCO Test Repository

This repository is designed to test the SHCO (Self-Healing Code Orchestrator) agent's ability to automatically fix CI failures.

## Purpose

This repository contains intentional test failures across three categories:
- **Import Errors**: Missing imports, wrong import paths
- **Assertion Errors**: Incorrect expected values in tests
- **Type Errors**: Type mismatches, wrong function signatures

## Test Scenarios

### Phase 1: Import Errors (5 scenarios)
1. Missing import for User class
2. Missing import for Database class
3. Missing import for Config class
4. Wrong import path for utils
5. Missing import for datetime

### Phase 2: Assertion Errors (5 scenarios)
1. Wrong expected count in test_count_users
2. Wrong expected string in test_get_username
3. Wrong expected list length in test_get_items
4. Wrong expected boolean in test_is_active
5. Wrong expected dict keys in test_get_config

### Phase 3: Type Errors (5 scenarios)
1. Passing string instead of int to function
2. Passing int instead of list to function
3. Wrong return type annotation
4. Missing required parameter
5. Extra unexpected parameter

## CI Workflow

The repository uses GitHub Actions to run tests on every push. The workflow:
1. Sets up Python 3.11
2. Installs dependencies
3. Runs pytest
4. Reports failures to SHCO webhook

## SHCO Integration

When a test fails:
1. GitHub sends webhook to SHCO
2. SHCO analyzes the failure
3. SHCO generates a fix
4. SHCO creates a PR with the fix
5. CI runs on the PR
6. If CI passes, the fix is successful!

## Expected Learning Curve

As SHCO processes more failures, it should:
- Decrease attempts needed per fix (3 → 2 → 1)
- Increase first-try success rate (20% → 60%)
- Build knowledge base of common patterns
- Reduce cost per fix

## Monitoring

Track SHCO's learning progress:
```bash
python scripts/show_learning_metrics.py
```

## Setup

1. Configure webhook in repository settings
2. Trigger failures by uncommenting test scenarios
3. Watch SHCO fix them automatically!

