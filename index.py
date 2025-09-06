import requests
import os
import hashlib
import mimetypes
from urllib.parse import urlparse
from pathlib import Path
import time


class UbuntuImageFetcher:
    """
    Ubuntu Image Fetcher - Connecting communities through shared visual resources

    Principles:
    - Community: Connect to the global web community
    - Respect: Handle errors gracefully and respect server resources
    - Sharing: Organize images for later appreciation and sharing
    """

    def __init__(self, directory="Fetched_Images"):
        self.directory = directory
        self.session = requests.Session()
        # Set a respectful User-Agent
        self.session.headers.update({
            'User-Agent': 'Ubuntu-Image-Fetcher/1.0 (Educational-Purpose)'
        })
        self.downloaded_hashes = set()
        self._load_existing_hashes()

    def _load_existing_hashes(self):
        """Load hashes of existing images to prevent duplicates (Ubuntu: Sharing wisely)"""
        if os.path.exists(self.directory):
            for filename in os.listdir(self.directory):
                filepath = os.path.join(self.directory, filename)
                if os.path.isfile(filepath):
                    try:
                        with open(filepath, 'rb') as f:
                            file_hash = hashlib.md5(f.read()).hexdigest()
                            self.downloaded_hashes.add(file_hash)
                    except Exception:
                        continue  # Skip problematic files gracefully

    def _is_safe_content_type(self, content_type):
        """Check if the content type is a safe image format (Ubuntu: Respect & Security)"""
        safe_types = [
            'image/jpeg', 'image/jpg', 'image/png', 'image/gif',
            'image/webp', 'image/bmp', 'image/svg+xml'
        ]
        return any(safe_type in content_type.lower() for safe_type in safe_types)

    def _get_file_extension(self, url, content_type):
        """Determine appropriate file extension (Ubuntu: Practicality)"""
        # First try to get extension from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if '.' in filename:
            return os.path.splitext(filename)[1]

        # Fall back to content type
        extension = mimetypes.guess_extension(content_type.split(';')[0])
        return extension or '.jpg'

    def _generate_filename(self, url, content_type, original_filename=None):
        """Generate appropriate filename (Ubuntu: Organization)"""
        if original_filename and '.' in original_filename:
            return original_filename

        # Generate based on URL or timestamp
        parsed_url = urlparse(url)
        base_name = os.path.basename(parsed_url.path)

        if not base_name or '.' not in base_name:
            base_name = f"image_{int(time.time())}"
        else:
            base_name = os.path.splitext(base_name)[0]

        extension = self._get_file_extension(url, content_type)
        return f"{base_name}{extension}"

    def _check_duplicate(self, content):
        """Check if image is duplicate using hash (Ubuntu: Sharing efficiently)"""
        content_hash = hashlib.md5(content).hexdigest()
        if content_hash in self.downloaded_hashes:
            return True
        self.downloaded_hashes.add(content_hash)
        return False

    def fetch_image(self, url):
        """
        Fetch a single image with Ubuntu principles
        Returns: (success: bool, message: str, filepath: str or None)
        """
        try:
            print(f"🌐 Connecting to: {url}")

            # First, make a HEAD request to check headers (Ubuntu: Respect)
            try:
                head_response = self.session.head(
                    url, timeout=10, allow_redirects=True)
                content_type = head_response.headers.get('content-type', '')
                content_length = head_response.headers.get('content-length')

                # Check if it's actually an image
                if not self._is_safe_content_type(content_type):
                    return False, f"❌ Not a safe image type: {content_type}", None

                # Check file size (be respectful of bandwidth)
                # 50MB limit
                if content_length and int(content_length) > 50 * 1024 * 1024:
                    return False, "❌ File too large (>50MB). Being respectful of resources.", None

            except requests.exceptions.RequestException:
                # If HEAD fails, continue with GET but be cautious
                content_type = 'image/jpeg'  # Assume default

            # Now fetch the actual image
            response = self.session.get(url, timeout=30, stream=True)
            response.raise_for_status()

            # Update content type from actual response if needed
            actual_content_type = response.headers.get(
                'content-type', content_type)
            if not self._is_safe_content_type(actual_content_type):
                return False, f"❌ Response is not a safe image: {actual_content_type}", None

            # Read content with size limit
            content = b''
            downloaded_size = 0
            max_size = 50 * 1024 * 1024  # 50MB limit

            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    downloaded_size += len(chunk)
                    if downloaded_size > max_size:
                        return False, "❌ File too large. Respecting bandwidth limits.", None
                    content += chunk

            # Check for duplicates (Ubuntu: Sharing wisely)
            if self._check_duplicate(content):
                return False, "⚠️  Image already exists (duplicate detected). Avoiding redundancy.", None

            # Create directory (Ubuntu: Organization)
            os.makedirs(self.directory, exist_ok=True)

            # Generate filename
            filename = self._generate_filename(url, actual_content_type)
            filepath = os.path.join(self.directory, filename)

            # Handle filename conflicts
            counter = 1
            original_filepath = filepath
            while os.path.exists(filepath):
                name, ext = os.path.splitext(original_filepath)
                filepath = f"{name}_{counter}{ext}"
                counter += 1

            # Save the image (Ubuntu: Preservation)
            with open(filepath, 'wb') as f:
                f.write(content)

            file_size = len(content) / 1024  # Size in KB
            return True, f"✅ Successfully saved: {os.path.basename(filepath)} ({file_size:.1f}KB)", filepath

        except requests.exceptions.Timeout:
            return False, "⏱️  Connection timeout. Server may be busy - respecting their resources.", None
        except requests.exceptions.ConnectionError:
            return False, "🔌 Connection failed. Network or server unavailable.", None
        except requests.exceptions.HTTPError as e:
            return False, f"🚫 HTTP Error {e.response.status_code}: Server declined request.", None
        except requests.exceptions.RequestException as e:
            return False, f"🌐 Network error: {str(e)}", None
        except Exception as e:
            return False, f"❌ Unexpected error: {str(e)}", None

    def fetch_multiple_images(self, urls):
        """
        Fetch multiple images (Challenge Question 1)
        Ubuntu: Building community through batch operations
        """
        results = []
        print(f"\n🔄 Processing {len(urls)} images with Ubuntu spirit...\n")

        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}] ", end="")
            success, message, filepath = self.fetch_image(url.strip())
            results.append((url, success, message, filepath))
            print(message)

            # Be respectful - small delay between requests
            if i < len(urls):
                time.sleep(0.5)

        return results

    def display_summary(self, results):
        """Display a summary of operations (Ubuntu: Sharing results)"""
        successful = sum(1 for _, success, _, _ in results if success)
        total = len(results)

        print(f"\n{'='*60}")
        print(f"📊 Ubuntu Image Fetcher Summary")
        print(f"{'='*60}")
        print(f"✅ Successful downloads: {successful}")
        print(f"❌ Failed attempts: {total - successful}")
        print(f"📁 Images stored in: {os.path.abspath(self.directory)}")
        print(f"🤝 Community connections made: {total}")

        if successful > 0:
            print(f"\n🎉 In the spirit of Ubuntu: 'I am because we are'")
            print(f"   Your collection grows through community sharing!")


def main():
    """Main function embodying Ubuntu principles"""
    print("🐧 Ubuntu Image Fetcher")
    print("=" * 50)
    print("Connecting communities through shared visual resources")
    print("Principles: Community • Respect • Sharing • Practicality")
    print("=" * 50)

    fetcher = UbuntuImageFetcher()

    # Get user choice
    print("\nChoose your approach:")
    print("1. Fetch a single image")
    print("2. Fetch multiple images")

    choice = input("\nEnter your choice (1 or 2): ").strip()

    if choice == "1":
        # Single image mode
        url = input("\n🔗 Please enter the image URL: ").strip()
        if url:
            success, message, filepath = fetcher.fetch_image(url)
            print(f"\n{message}")

            if success:
                print(f"📁 Saved to: {filepath}")
                print("\n🌍 Ubuntu spirit: Through sharing, we build community!")

    elif choice == "2":
        # Multiple images mode (Challenge Question 1)
        print("\n📝 Enter image URLs (one per line, empty line to finish):")
        urls = []
        while True:
            url = input().strip()
            if not url:
                break
            urls.append(url)

        if urls:
            results = fetcher.fetch_multiple_images(urls)
            fetcher.display_summary(results)

    else:
        print("❌ Invalid choice. Ubuntu teaches us to choose wisely.")
        return

    print(f"\n🙏 Thank you for using Ubuntu Image Fetcher!")
    print("   Remember: 'Ubuntu' - I am because we are")


if __name__ == "__main__":
    main()
