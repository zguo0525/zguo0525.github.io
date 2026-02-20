// Article view counter using GoatCounter API
// Fetches view counts directly from GoatCounter for accurate tracking

(function() {
  'use strict';

  const GOATCOUNTER_SITE = 'zguo0525'; // Your GoatCounter site code

  // Get the current article path
  function getArticlePath() {
    const path = window.location.pathname;
    // Extract full path like /articles/the-openclaw-playbook.html
    return path;
  }

  // Fetch view count from GoatCounter API
  async function fetchViewCountFromGoatCounter(articlePath) {
    try {
      // GoatCounter counter API format: https://SITE.goatcounter.com/counter/PATH.json
      // Note: You need to enable "Allow adding visitor counts" in GoatCounter settings
      const apiUrl = `https://${GOATCOUNTER_SITE}.goatcounter.com/counter${articlePath}.json`;
      
      const response = await fetch(apiUrl, {
        cache: 'no-cache'
      });

      if (!response.ok) {
        // If API fails, try fallback to JSON file
        return await fetchViewCountFromJSON(articlePath);
      }

      const data = await response.json();
      // GoatCounter returns count in the 'count' field
      return data.count || 0;
    } catch (error) {
      console.error('Error fetching from GoatCounter:', error);
      // Fallback to JSON file if GoatCounter API fails
      return await fetchViewCountFromJSON(articlePath);
    }
  }

  // Fallback: Fetch view count from GitHub JSON file
  async function fetchViewCountFromJSON(articlePath) {
    try {
      const match = articlePath.match(/\/articles\/([^\/]+)\.html/);
      const articleSlug = match ? match[1] : null;
      
      if (!articleSlug) {
        return 0;
      }

      const response = await fetch('https://raw.githubusercontent.com/zguo0525/zguo0525.github.io/main/data/article-views.json', {
        cache: 'no-cache'
      });

      if (!response.ok) {
        return 0;
      }

      const views = await response.json();
      return views[articleSlug] || 0;
    } catch (error) {
      console.error('Error fetching from JSON:', error);
      return 0;
    }
  }

  // Display view count
  function displayViewCount(count) {
    const viewCounter = document.getElementById('article-view-count');
    if (viewCounter) {
      if (count === null) {
        viewCounter.textContent = '...';
      } else {
        viewCounter.textContent = count.toLocaleString();
      }
    }
  }

  // Initialize view tracking
  async function init() {
    const articlePath = getArticlePath();
    
    // Only track article pages
    if (!articlePath.includes('/articles/')) {
      return;
    }

    // Show loading state
    displayViewCount(null);

    // Fetch view count from GoatCounter
    const count = await fetchViewCountFromGoatCounter(articlePath);
    
    // Display the count
    displayViewCount(count || 0);
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
