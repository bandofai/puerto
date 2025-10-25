"""
Book API Client - Unified interface for Goodreads, LibraryThing, and Open Library APIs

Provides cached, rate-limited access to book metadata services.
"""

import os
import time
import json
import hashlib
import requests
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from functools import wraps


class RateLimiter:
    """Rate limiting for API calls"""

    def __init__(self, calls_per_minute: int = 30):
        self.min_interval = 60.0 / calls_per_minute
        self.last_called = 0.0

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - self.last_called
            left_to_wait = self.min_interval - elapsed

            if left_to_wait > 0:
                time.sleep(left_to_wait)

            result = func(*args, **kwargs)
            self.last_called = time.time()

            return result

        return wrapper


class APICache:
    """Simple file-based cache for API responses"""

    def __init__(self, cache_dir: Path, ttl_days: int = 30):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.ttl = timedelta(days=ttl_days)

    def _get_cache_key(self, endpoint: str, params: Dict) -> str:
        key_str = f"{endpoint}:{json.dumps(params, sort_keys=True)}"
        return hashlib.md5(key_str.encode()).hexdigest()

    def get(self, endpoint: str, params: Dict) -> Optional[Dict]:
        cache_key = self._get_cache_key(endpoint, params)
        cache_file = self.cache_dir / f"{cache_key}.json"

        if not cache_file.exists():
            return None

        # Check TTL
        mtime = datetime.fromtimestamp(cache_file.stat().st_mtime)
        if datetime.now() - mtime > self.ttl:
            cache_file.unlink()
            return None

        with open(cache_file, 'r') as f:
            return json.load(f)

    def set(self, endpoint: str, params: Dict, data: Dict):
        cache_key = self._get_cache_key(endpoint, params)
        cache_file = self.cache_dir / f"{cache_key}.json"

        with open(cache_file, 'w') as f:
            json.dump(data, f, indent=2)


class BookAPIClient:
    """Unified client for book metadata APIs"""

    def __init__(self, cache_dir: Optional[Path] = None):
        # Get library path
        project_dir = Path.cwd() / '.reading-tracker'
        user_dir = Path.home() / '.reading-tracker'

        if project_dir.exists():
            base_dir = project_dir
        elif user_dir.exists():
            base_dir = user_dir
        else:
            base_dir = user_dir
            base_dir.mkdir(parents=True, exist_ok=True)

        # Initialize cache
        cache_dir = cache_dir or (base_dir / '.cache')
        self.cache = APICache(cache_dir)

        # Load config for API keys
        config_file = base_dir / 'config.json'
        if config_file.exists():
            with open(config_file, 'r') as f:
                config = json.load(f)
                self.goodreads_key = config.get('apis', {}).get('goodreads_key')
                self.librarything_key = config.get('apis', {}).get('librarything_key')
                rate_limit = config.get('apis', {}).get('rate_limit_per_minute', 30)
        else:
            self.goodreads_key = os.getenv('GOODREADS_API_KEY')
            self.librarything_key = os.getenv('LIBRARYTHING_API_KEY')
            rate_limit = 30

        # Rate limiter
        self.rate_limiter = RateLimiter(calls_per_minute=rate_limit)

    @property
    def rate_limited_get(self):
        """Rate-limited HTTP GET"""
        return self.rate_limiter(requests.get)

    def fetch_book_by_isbn(self, isbn: str, prefer_api: str = 'openlibrary') -> Optional[Dict]:
        """
        Fetch book metadata by ISBN

        Args:
            isbn: ISBN-10 or ISBN-13
            prefer_api: 'openlibrary', 'goodreads', 'librarything'

        Returns:
            Normalized book data or None
        """

        # Check cache first
        cached = self.cache.get('isbn_lookup', {'isbn': isbn})
        if cached:
            return cached

        # Try preferred API first
        result = None

        if prefer_api == 'openlibrary':
            result = self._fetch_openlibrary(isbn)
        elif prefer_api == 'goodreads' and self.goodreads_key:
            result = self._fetch_goodreads(isbn)
        elif prefer_api == 'librarything' and self.librarything_key:
            result = self._fetch_librarything(isbn)

        # Fallback to Open Library (no key required)
        if not result:
            result = self._fetch_openlibrary(isbn)

        # Cache result
        if result:
            self.cache.set('isbn_lookup', {'isbn': isbn}, result)

        return result

    def _fetch_openlibrary(self, isbn: str) -> Optional[Dict]:
        """Fetch from Open Library API"""

        try:
            url = f"https://openlibrary.org/api/books"
            params = {
                'bibkeys': f'ISBN:{isbn}',
                'format': 'json',
                'jscmd': 'data'
            }

            response = self.rate_limited_get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            key = f'ISBN:{isbn}'

            if key not in data:
                return None

            book_data = data[key]

            # Normalize to our schema
            normalized = {
                'title': book_data.get('title'),
                'subtitle': book_data.get('subtitle'),
                'authors': [a['name'] for a in book_data.get('authors', [])],
                'publishers': [p['name'] for p in book_data.get('publishers', [])],
                'publisher': book_data.get('publishers', [{}])[0].get('name') if book_data.get('publishers') else None,
                'published_year': self._extract_year(book_data.get('publish_date')),
                'pages': book_data.get('number_of_pages'),
                'cover_url': book_data.get('cover', {}).get('large'),
                'description': self._extract_description(book_data.get('description')),
                'genres': [s['name'] for s in book_data.get('subjects', [])[:5]],
                'isbn': isbn,
                'source': 'openlibrary'
            }

            return normalized

        except Exception as e:
            print(f"Open Library API error: {e}")
            return None

    def _fetch_goodreads(self, isbn: str) -> Optional[Dict]:
        """Fetch from Goodreads API (requires API key)"""

        if not self.goodreads_key:
            return None

        try:
            # Note: Goodreads API is deprecated, this is a placeholder
            # In practice, you'd need to use web scraping or alternate methods
            print("⚠️  Goodreads API is deprecated. Consider web scraping or alternative sources.")
            return None

        except Exception as e:
            print(f"Goodreads API error: {e}")
            return None

    def _fetch_librarything(self, isbn: str) -> Optional[Dict]:
        """Fetch from LibraryThing API (requires API key)"""

        if not self.librarything_key:
            return None

        try:
            url = "https://www.librarything.com/services/rest/1.1/"
            params = {
                'method': 'librarything.ck.getwork',
                'isbn': isbn,
                'apikey': self.librarything_key
            }

            response = self.rate_limited_get(url, params=params, timeout=10)
            response.raise_for_status()

            # Parse XML response (LibraryThing returns XML)
            # This is a simplified example
            print("⚠️  LibraryThing integration needs XML parsing implementation")
            return None

        except Exception as e:
            print(f"LibraryThing API error: {e}")
            return None

    def search_books(self, query: str, limit: int = 10) -> list:
        """
        Search for books by title/author

        Args:
            query: Search query
            limit: Max results

        Returns:
            List of book results
        """

        # Check cache
        cached = self.cache.get('search', {'query': query, 'limit': limit})
        if cached:
            return cached

        # Use Open Library search
        try:
            url = "https://openlibrary.org/search.json"
            params = {
                'q': query,
                'limit': limit
            }

            response = self.rate_limited_get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()
            results = []

            for doc in data.get('docs', []):
                result = {
                    'title': doc.get('title'),
                    'authors': doc.get('author_name', []),
                    'published_year': doc.get('first_publish_year'),
                    'isbn': doc.get('isbn', [None])[0] if doc.get('isbn') else None,
                    'pages': doc.get('number_of_pages_median'),
                    'cover_id': doc.get('cover_i'),
                    'source': 'openlibrary'
                }

                results.append(result)

            # Cache results
            self.cache.set('search', {'query': query, 'limit': limit}, results)

            return results

        except Exception as e:
            print(f"Search error: {e}")
            return []

    def get_cover_url(self, cover_id: int, size: str = 'L') -> str:
        """
        Get Open Library cover URL

        Args:
            cover_id: Open Library cover ID
            size: S, M, or L

        Returns:
            Cover image URL
        """
        return f"https://covers.openlibrary.org/b/id/{cover_id}-{size}.jpg"

    @staticmethod
    def _extract_year(date_str: Optional[str]) -> Optional[int]:
        """Extract year from various date formats"""
        if not date_str:
            return None

        import re
        match = re.search(r'\d{4}', str(date_str))
        return int(match.group()) if match else None

    @staticmethod
    def _extract_description(description) -> Optional[str]:
        """Extract description from various formats"""
        if isinstance(description, dict):
            return description.get('value')
        elif isinstance(description, str):
            return description
        else:
            return None


# Example usage
if __name__ == '__main__':
    client = BookAPIClient()

    # Fetch by ISBN
    book = client.fetch_book_by_isbn('978-0135957059')
    if book:
        print(f"Found: {book['title']} by {', '.join(book['authors'])}")

    # Search
    results = client.search_books('Pragmatic Programmer')
    print(f"\nSearch results: {len(results)} books found")
    for result in results[:3]:
        print(f"  • {result['title']}")
