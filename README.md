# 🚀 Daily Automated Contribution & Tech Digest

An automated GitHub Actions bot that runs every day, fetches daily tech insights, and commits them.

## 📌 Features
- **Meaningful Content**: Fetches top stories and insights into `digests/YYYY-MM-DD.md` rather than empty or dummy commits.
- **Fail-safe Heartbeat**: If an API is ever unreachable, logs a fallback heartbeat to `activity.log`.
- **Works in Private Repos**: Can be completely hidden so nobody sees your commit contents while your GitHub contribution graph still stays green.

---

## 🛠️ Quick Setup (5 Minutes)

### 1. Initialize Git & Push to GitHub
In this folder:
```bash
git init
git add .
git commit -m "feat: initial commit for daily digest bot"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/<REPO_NAME>.git
git push -u origin main
```

### 2. Configure Action Permissions
1. Open your repository on GitHub.
2. Go to **Settings** -> **Actions** -> **General**.
3. Under **Workflow permissions**, select **"Read and write permissions"**.
4. Click **Save**.

### 3. Ensure the Green Square Attribution
For GitHub to turn your squares green:
1. Open `.github/workflows/daily-commit.yml`.
2. Ensure `git config user.email` uses the email associated with your GitHub account (or set a GitHub repository secret named `USER_EMAIL` under **Settings** -> **Secrets and variables** -> **Actions**).

---

## 🔒 How to Hide It (Private Mode)
If you don't want anyone to see this repository or your commits:
1. Create this repo as **Private**.
2. Go to your public GitHub profile (`https://github.com/<your-username>`).
3. Click the **Contribution settings** dropdown (top-right of your green contribution chart).
4. Check **"Private contributions"**.

Now, your contribution squares will turn green every day, but public visitors will only see:
> *"1 contribution in private repositories"*
No one can view the code, commit messages, or repository.
