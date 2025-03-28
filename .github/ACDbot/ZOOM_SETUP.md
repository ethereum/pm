# Setting Up Your Zoom General App

This guide will help you convert your Zoom app from Server-to-Server OAuth to a General (User Managed) App. This change allows your app to make API calls on behalf of users who have granted permission, while still enabling automatic creation of Zoom meetings.

## Step 1: Create a General App in Zoom Marketplace

1. Go to the [Zoom App Marketplace](https://marketplace.zoom.us/) and sign in
2. Click on "Develop" in the top-right corner and select "Build App"
3. Choose "OAuth" as the app type
4. Fill in the required details for your app:
   - App Name: Your app name
   - App Type: General App
   - Choose what account should own the app (your account)
   - Choose "User-managed app" (Not Account-level app)
   - Leave "Would you like to publish this app?" as "No"

## Step 2: Configure OAuth Settings

1. In your app's configuration, navigate to the "OAuth" section
2. Add the following redirect URL: `http://localhost:8000/callback`
   (You can use any port, but make sure it matches what you use in the token script)
3. Under Scopes, add the following permissions:
   - `meeting:write`
   - `meeting:read:admin`
   - `recording:read:admin`
4. Save your changes

## Step 3: Obtain Client Credentials

1. Note your Client ID and Client Secret from the app settings
2. You'll need these for the next step to get your refresh token

## Step 4: Get Your Initial Refresh Token

Run the provided script to get your initial refresh token:

```bash
python .github/ACDbot/scripts/get_zoom_token.py \
  --client-id YOUR_CLIENT_ID \
  --client-secret YOUR_CLIENT_SECRET \
  --redirect-uri http://localhost:8000/callback
```

This script will:
1. Open a browser window where you'll need to authorize your app
2. Exchange the authorization code for an access token and refresh token
3. Display the tokens and offer to save them to a .env file

## Step 5: Update GitHub Secrets

If you're using GitHub Actions, add the following secrets to your repository:
1. `ZOOM_CLIENT_ID`: Your Zoom app Client ID
2. `ZOOM_CLIENT_SECRET`: Your Zoom app Client Secret
3. `ZOOM_REFRESH_TOKEN`: The refresh token obtained in step 4

## Important Notes

1. **Refresh Token Rotation**: Zoom may occasionally issue a new refresh token when you use the current one. The script will display a message when this happens, and you should update your stored refresh token.

2. **Token Security**: Keep your tokens secure! The refresh token provides access to your Zoom account through the API.

3. **User Flow**: This change maintains the same user flow for creating meetings - instead of using server-to-server credentials, it will use your user credentials via OAuth.

4. **Permission Scopes**: If you need additional API access, you may need to add more scopes to your app and re-authorize to get a new token with those permissions.

## Troubleshooting

If you encounter issues:

1. Ensure your app has the correct scopes configured
2. Verify that your redirect URI exactly matches what's in your app settings
3. Check that your client ID and secret are correct
4. If your refresh token stops working, use the script to generate a new one