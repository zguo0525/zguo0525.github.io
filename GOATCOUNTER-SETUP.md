# GoatCounter Setup for View Counts

## Step 1: Enable Public Counter API

To display view counts on your GitHub Pages site, you need to enable the public counter API in GoatCounter:

1. Go to your GoatCounter dashboard: https://zguo0525.goatcounter.com
2. Click **Settings** (top menu)
3. Scroll down to **"Allow adding visitor counts on your website"**
4. **Enable** this option
5. Save settings

This allows the public API to return view counts for your pages.

## Step 2: Verify It Works

After enabling the setting:

1. Visit one of your articles on GitHub Pages
2. The view count should appear automatically
3. Refresh the page - the count should update

## How It Works

- GoatCounter tracks all page views automatically
- The JavaScript fetches view counts from: `https://zguo0525.goatcounter.com/counter/PATH.json`
- View counts are displayed on article pages
- No manual updates needed - fully automatic!

## Troubleshooting

**If you see "0 views" or "..." forever:**

1. Make sure you enabled "Allow adding visitor counts" in GoatCounter settings
2. Check browser console for errors (F12 → Console)
3. Verify GoatCounter is receiving data (check your dashboard)
4. Wait a few minutes after enabling the setting for it to take effect

**If the API returns 404:**

- Make sure the article path matches exactly (e.g., `/articles/the-openclaw-playbook.html`)
- The path must match what GoatCounter sees in your dashboard

## Alternative: Manual Sync

If the API doesn't work, you can manually sync view counts:

1. Check view counts in your GoatCounter dashboard
2. Update `data/article-views.json` with the counts
3. Push to GitHub

But with the API enabled, this should work automatically!
