# Instagram Non-Followers Checker

This simple Python script compares your Instagram `following.html` and `followers.html` (downloaded via Instagram's official data request) and shows who you follow but who doesn't follow you back.

## Setup

1. Download your data from Instagram:
   - Go to your profile > Settings > Your Activity > Download Your Information.
   - Select HTML format and wait for the email with the .zip file.
   - Extract it and locate:
     - `followers_and_following/followers.html`
     - `followers_and_following/following.html`

2. Place both files inside the `/data` folder.

3. Install requirements:
```bash
pip install -r requirements.txt
