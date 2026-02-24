# GitHub Repository Setup Guide

This guide walks through the manual steps to configure branch protection, required status checks,
and review rules so that **nothing merges to `main` without human approval and green CI**.

---

## 1. Prerequisites

- Repository admin access to `dsactivi-2/Call-System-complete-`
- GitHub CLI (`gh`) installed (optional but faster): https://cli.github.com

---

## 2. Enable Branch Protection on `main`

### Option A – GitHub UI

1. Go to **Settings** → **Branches** → **Add branch protection rule**
2. Branch name pattern: `main`
3. Enable the following options:

   | Option | Value |
   |--------|-------|
   | **Require a pull request before merging** | ✅ Enabled |
   | └─ Required number of approvals | `1` |
   | └─ Dismiss stale PR approvals when new commits are pushed | ✅ Enabled |
   | └─ Require review from code owners | ✅ Enabled (`CODEOWNERS` must be present) |
   | **Require status checks to pass before merging** | ✅ Enabled |
   | └─ Require branches to be up to date before merging | ✅ Enabled |
   | └─ Status checks (add each): | See section 3 |
   | **Require conversation resolution before merging** | ✅ Recommended |
   | **Do not allow bypassing the above settings** | ✅ Enabled (prevents admins from bypassing) |
   | **Allow force pushes** | ❌ Disabled |
   | **Allow deletions** | ❌ Disabled |

4. Click **Create** / **Save changes**

### Option B – GitHub CLI

```bash
gh api repos/dsactivi-2/Call-System-complete-/branches/main/protection \
  --method PUT \
  --header "Accept: application/vnd.github+json" \
  --field required_status_checks='{"strict":true,"contexts":["Python (ruff + pytest) (3.11)","Python (ruff + pytest) (3.12)","Analyze (python)","Analyze (javascript-typescript)"]}' \
  --field enforce_admins=true \
  --field required_pull_request_reviews='{"required_approving_review_count":1,"dismiss_stale_reviews":true,"require_code_owner_reviews":true}' \
  --field restrictions=null \
  --field allow_force_pushes=false \
  --field allow_deletions=false
```

---

## 3. Required Status Checks

After running the CI at least once, add these as required checks:

| Check name | Workflow |
|-----------|---------|
| `Python (ruff + pytest) (3.11)` | `.github/workflows/ci.yml` |
| `Python (ruff + pytest) (3.12)` | `.github/workflows/ci.yml` |
| `Analyze (python)` | `.github/workflows/codeql.yml` |
| `Analyze (javascript-typescript)` | `.github/workflows/codeql.yml` |

> **Note**: The exact check names appear in the GitHub UI only after the workflows have run at
> least once. Copy them from the **Checks** tab of a previous PR.

---

## 4. Protect the `develop` Branch (Optional)

Repeat the same steps for `develop` with a lower bar (e.g. 0 required approvals, but CI still required):

```bash
gh api repos/dsactivi-2/Call-System-complete-/branches/develop/protection \
  --method PUT \
  --header "Accept: application/vnd.github+json" \
  --field required_status_checks='{"strict":false,"contexts":["Python (ruff + pytest) (3.12)"]}' \
  --field enforce_admins=false \
  --field required_pull_request_reviews='{"required_approving_review_count":0}' \
  --field restrictions=null
```

---

## 5. Auto-Merge (Optional)

Enable auto-merge so PRs are merged automatically once all checks pass and an approval is given:

```bash
# Enable auto-merge feature for the repo
gh api repos/dsactivi-2/Call-System-complete- \
  --method PATCH \
  --field allow_auto_merge=true \
  --field delete_branch_on_merge=true
```

Then on individual PRs, contributors can enable auto-merge:

```bash
gh pr merge <PR_NUMBER> --auto --squash
```

---

## 6. Merge Queue (Optional – GitHub Team/Enterprise)

If your plan supports it, enable the **Merge Queue** in:
**Settings** → **Branches** → branch rule → **Require merge queue**

This serialises merges and re-runs CI on the queued combination before landing to `main`.

---

## 7. Verify the Setup

1. Create a test branch: `git checkout -b test/branch-protection`
2. Push an empty commit: `git commit --allow-empty -m "test" && git push`
3. Open a PR → verify you cannot merge without approval and green checks
4. Verify that a direct push to `main` is rejected

---

## 8. CODEOWNERS Verification

Ensure `CODEOWNERS` is committed to the repository root (or `.github/CODEOWNERS`).
GitHub will automatically request reviews from owners listed there when a PR modifies their files.

Check active code owners:
```bash
gh api repos/dsactivi-2/Call-System-complete-/contents/CODEOWNERS --jq '.content' | base64 -d
```
