"""
Multi-retry test for SHCO comprehensive system testing.

This test is designed to exercise the full retry workflow:
1. Issue creation and linking
2. PR creation with issue link
3. First fix attempt (incomplete)
4. CI failure detection
5. Retry with PR update (not new PR)
6. PR comment on retry
7. Second/third fix attempts
8. CI success
9. Success notification
10. Full workflow completion

Expected behavior:
- Only ONE PR should be created
- PR should have multiple commits (one per attempt)
- PR should have retry comments ("🔄 Retry Attempt X/Y")
- PR should include "Fixes #X" at top
- GitHub should auto-link PR and issue
- CI should pass on final attempt
- Success notification should be sent
"""


def test_complex_import_chain():
    """
    Test complex import chain requiring multiple retry attempts.
    
    Test 43: THE GAUNTLET - Comprehensive system test
    
    This test creates a chain of missing imports that will likely require
    2-3 attempts to fix completely:
    
    Attempt 1: LLM adds User import
    Attempt 2: LLM adds UserProfile import  
    Attempt 3: LLM adds ProfileValidator import
    
    This validates:
    - Retry logic updates existing PR (not creates new PR)
    - PR comments are added for each retry
    - Force push works correctly
    - CI re-runs on updated PR
    - State management across retries
    - Full workflow completion
    """
    # Missing imports - will cause NameError
    user = User("Alice", 30)
    profile = UserProfile(user)
    validator = ProfileValidator(profile)
    
    # Assertions
    assert validator.is_valid()
    assert profile.get_bio() == "Profile for Alice"
    assert user.get_name() == "Alice"

