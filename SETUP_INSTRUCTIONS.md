# SHCO Test Repository - Setup Instructions

**Complete guide to setting up the test repository**

---

## 📋 **Prerequisites**

- GitHub account with access to PitchConnect organization
- GitHub CLI (`gh`) installed (optional but recommended)
- SHCO webhook endpoint running: `https://shco-webhook.svaberg.stream/webhook`
- `GITHUB_WEBHOOK_SECRET` from SHCO `.env` file

---

## 🚀 **Step 1: Create Repository**

### **Option A: Using GitHub CLI** (Recommended)

```bash
# Navigate to the template directory
cd agentics/test-repo-template

# Create repository in PitchConnect organization
gh repo create PitchConnect/shco-test-repo \
  --public \
  --description "Test repository for SHCO agent learning and validation" \
  --clone

# Navigate to the cloned repository
cd shco-test-repo

# Copy all template files
cp -r ../test-repo-template/* .
cp -r ../test-repo-template/.github .

# Initial commit
git add .
git commit -m "Initial commit: SHCO test repository setup"
git push origin main
```

### **Option B: Using GitHub Web UI**

1. Go to https://github.com/organizations/PitchConnect/repositories/new
2. Repository name: `shco-test-repo`
3. Description: "Test repository for SHCO agent learning and validation"
4. Visibility: Public
5. Initialize with README: ✅ (check)
6. Click "Create repository"

7. Clone the repository:
   ```bash
   git clone https://github.com/PitchConnect/shco-test-repo.git
   cd shco-test-repo
   ```

8. Copy template files:
   ```bash
   # From agentics directory
   cp -r test-repo-template/* shco-test-repo/
   cp -r test-repo-template/.github shco-test-repo/
   
   cd shco-test-repo
   git add .
   git commit -m "Add test scenarios and CI workflow"
   git push origin main
   ```

---

## 🔗 **Step 2: Configure Webhook**

1. Go to repository settings:
   ```
   https://github.com/PitchConnect/shco-test-repo/settings/hooks
   ```

2. Click "Add webhook"

3. Configure webhook:
   - **Payload URL**: `https://shco-webhook.svaberg.stream/webhook`
   - **Content type**: `application/json`
   - **Secret**: (Get from SHCO `.env` file: `GITHUB_WEBHOOK_SECRET`)
   - **Which events**: Select "Let me select individual events"
     - ✅ Check "Workflow runs"
     - ❌ Uncheck everything else
   - **Active**: ✅ Checked

4. Click "Add webhook"

5. Verify webhook:
   - You should see a green checkmark after the first ping
   - If red X, check the webhook secret matches `.env`

---

## ⚙️ **Step 3: Update SHCO Configuration**

Edit `agentics/.env`:

```bash
# ========== Test Repository Configuration ==========

# Target repository for testing
SHCO_TARGET_REPO=PitchConnect/shco-test-repo

# Webhook filtering (optional - recommended for testing)
WEBHOOK_FILTER_BRANCHES=true
WEBHOOK_ALLOWED_BRANCHES=main

# Webhook age filtering
WEBHOOK_MAX_FAILURE_AGE_HOURS=24

# Dry-run mode (optional - for initial testing)
# DRY_RUN_MODE=true  # Uncomment to analyze without creating PRs
```

Restart SHCO webhook service:
```bash
cd agentics
docker-compose restart webhook
```

---

## ✅ **Step 4: Verify Setup**

### **4.1: Check Repository Structure**

```bash
cd shco-test-repo

# Verify files exist
ls -la
# Should see:
# - README.md
# - requirements.txt
# - src/
# - tests/
# - .github/workflows/test.yml
```

### **4.2: Check CI Workflow**

```bash
# Trigger CI by pushing a commit
git commit --allow-empty -m "Test CI workflow"
git push origin main

# Check workflow status
gh run list
# Should show workflow running/completed
```

### **4.3: Check Webhook Endpoint**

```bash
# Test webhook endpoint is reachable
curl -I https://shco-webhook.svaberg.stream/health

# Should return: 200 OK
```

### **4.4: Check SHCO Logs**

```bash
cd agentics
docker-compose logs -f webhook

# Should see:
# - Webhook service started
# - Health check endpoint ready
# - No errors
```

---

## 🧪 **Step 5: Trigger First Test Failure**

### **5.1: Enable Import Error Test**

Edit `tests/test_import_errors.py`:

```python
# Uncomment lines 11-14
def test_import_error_1_missing_user():
    """Test missing User import."""
    user = User("Alice", 30)  # NameError: name 'User' is not defined
    assert user.get_name() == "Alice"
```

### **5.2: Commit and Push**

```bash
git add tests/test_import_errors.py
git commit -m "Test 1: Trigger import error for User class"
git push origin main
```

### **5.3: Monitor SHCO**

```bash
# Watch SHCO logs
cd agentics
docker-compose logs -f webhook

# Expected flow:
# 1. Webhook received ✅
# 2. Event processed ✅
# 3. Agent execution queued ✅
# 4. Triage: "Missing import for User class" ✅
# 5. Generate fix: "Add 'from src.models import User'" ✅
# 6. PR created ✅
# 7. CI runs on PR ✅
# 8. Discord notification sent ✅
```

### **5.4: Check Discord**

Go to Discord #general channel:
- Should see notification: "🚀 SHCO Started - Execution #1"
- Should see notification: "✅ Fix Successful!" (if fix worked)

### **5.5: Check GitHub**

Go to repository:
- Should see new PR created by SHCO
- PR should have fix: `from src.models import User`
- CI should be running/passed on PR

---

## 📊 **Step 6: Run Full Test Suite**

### **Test Schedule** (15 executions over 2 weeks)

**Week 1: Import Errors** (5 executions)
```bash
# Day 1: Test 1 - Missing User import
# Day 2: Test 2 - Missing Database import
# Day 3: Test 3 - Missing Config import
# Day 4: Test 4 - Wrong import path
# Day 5: Test 5 - Missing datetime import
```

**Week 2: Assertion Errors** (5 executions)
```bash
# Day 8: Test 6 - Wrong expected count
# Day 9: Test 7 - Wrong expected string
# Day 10: Test 8 - Wrong expected list length
# Day 11: Test 9 - Wrong expected boolean
# Day 12: Test 10 - Wrong expected dict keys
```

**Week 3: Type Errors** (5 executions)
```bash
# Day 15: Test 11 - String instead of list
# Day 16: Test 12 - Int instead of list
# Day 17: Test 13 - Wrong return type
# Day 18: Test 14 - Missing parameter
# Day 19: Test 15 - Extra parameter
```

### **Process for Each Test**

1. Uncomment one test in the appropriate file
2. Commit and push
3. Wait for SHCO to process (5-10 minutes)
4. Verify PR created and CI passed
5. Merge PR (or let SHCO auto-merge if configured)
6. Check metrics: `python scripts/show_learning_metrics.py`
7. Move to next test

---

## 📈 **Step 7: Monitor Learning Progress**

### **Daily Metrics Check**

```bash
cd agentics
python scripts/show_learning_metrics.py

# Expected progression:
# Executions 1-5:  Success 60%, Avg Attempts 2.8
# Executions 6-10: Success 75%, Avg Attempts 2.1 ↓
# Executions 11-15: Success 85%, Avg Attempts 1.5 ↓
```

### **Weekly Review**

Check:
- ✅ Success rate increasing
- ✅ Attempts decreasing
- ✅ First-try success increasing
- ✅ Knowledge base growing
- ✅ Cost decreasing

### **Red Flags** 🚨

If you see:
- ❌ Success rate < 50% after 10 executions
- ❌ No improvement in attempts
- ❌ Knowledge base not growing
- ❌ Frequent webhook errors

Then:
1. Check SHCO logs for errors
2. Verify webhook configuration
3. Check Discord notifications
4. Review vector DB storage

---

## 🎯 **Success Criteria**

After 15 executions, you should see:

| Metric | Target | Status |
|--------|--------|--------|
| Total Executions | 15 | ✅ |
| Success Rate | 80%+ | ✅ |
| Avg Attempts | 1.5-2.0 | ✅ |
| First-Try Success | 40-60% | ✅ |
| Knowledge Base | 15 patterns | ✅ |
| Improvement Rate | +20-30% | ✅ |

---

## 🔧 **Troubleshooting**

### **Webhook Not Receiving Events**

```bash
# Check webhook deliveries in GitHub
https://github.com/PitchConnect/shco-test-repo/settings/hooks

# Click on webhook → Recent Deliveries
# Should see successful deliveries (green checkmark)

# If red X:
# - Check webhook secret matches .env
# - Check webhook URL is correct
# - Check SHCO webhook service is running
```

### **SHCO Not Processing Events**

```bash
# Check SHCO logs
docker-compose logs webhook | grep ERROR

# Common issues:
# - Webhook signature verification failed → Check secret
# - Event filtered out → Check filtering configuration
# - Database connection failed → Check PostgreSQL/Qdrant
```

### **PR Not Created**

```bash
# Check SHCO logs for errors
docker-compose logs webhook | grep "generate_fix"

# Common issues:
# - GitHub token expired → Update GITHUB_TOKEN in .env
# - Insufficient permissions → Check token has repo write access
# - Dry-run mode enabled → Check DRY_RUN_MODE in .env
```

### **CI Still Failing After Fix**

```bash
# Check PR diff to see what SHCO changed
# Common issues:
# - Fix was incomplete → SHCO will retry
# - Fix was wrong → SHCO will learn and try different approach
# - Test is flaky → May need manual intervention
```

---

## 📚 **Next Steps**

After successful testing:

1. **Week 4**: Review metrics and learning curve
2. **Week 5**: Enable dry-run mode on real repository
3. **Week 6**: Enable on single production repository
4. **Month 2**: Gradual expansion to more repositories

---

## ✅ **Verification Checklist**

Before starting tests:

- [ ] Repository created in PitchConnect organization
- [ ] All template files copied
- [ ] GitHub Actions workflow configured
- [ ] Webhook configured with correct URL and secret
- [ ] SHCO `.env` updated with test repository
- [ ] SHCO webhook service running
- [ ] Webhook endpoint reachable
- [ ] Discord notifications configured
- [ ] Databases (PostgreSQL, Qdrant) running
- [ ] First test failure triggered successfully
- [ ] SHCO processed event and created PR
- [ ] Metrics dashboard working

---

**Status**: Ready to start testing! 🚀

**First Action**: Create repository and configure webhook, then trigger first test failure!

