GITHUB_AUTH_SCOPE = ["user:email", "read:user"]
GITHUB_AUTH_CALLBACK_URL = "http://localhost:3000/auth/success/"
GITHUB_AUTH_KEY = "GITHUB_AUTH_KEY"
GITHUB_AUTH_SECRET = "GITHUB_AUTH_SECRET"
GITHUB_AUTH_USE_JWT = False

GITHUB_AUTH_ALLOWED_REDIRECT_URIS = [GITHUB_AUTH_CALLBACK_URL]
