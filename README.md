# Ubuntu Image Fetcher 🐧

> _"I am because we are"_ - A Python image downloader embodying Ubuntu philosophy

**Power Learn Project - Python Week 6 Assignment**  
_Libraries and File Handling Assignment_

A Python application that respectfully connects to the global web community to fetch and organize images while emphasizing community, respect, sharing, and practicality.

## ✨ Features

- **Single & Batch Downloads**: Download individual images or process multiple URLs
- **Smart Organization**: Auto-creates `Fetched_Images` directory with organized storage
- **Duplicate Prevention**: MD5 hash-based detection prevents redundant downloads
- **Security Focused**: Validates file types, implements size limits, and safe filename generation
- **Graceful Error Handling**: Never crashes, provides helpful feedback for all scenarios
- **Ubuntu Philosophy**: Every feature designed around community, respect, sharing, and practicality

## 🚀 Quick Start

### Prerequisites

- Python 3.6+
- Internet connection

### Installation

1. **Clone or download the project**

   ```bash
   git clone https://github.com/Mayen007/Ubuntu_Requests
   cd Ubuntu_Requests
   ```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Run the application**
   ```bash
   python index.py
   ```

## 💻 Usage

### Interactive Mode

Run the program and choose your approach:

```bash
python index.py
```

**Option 1 - Single Image:**

- Enter one image URL
- Image downloads to `Fetched_Images/` directory

**Option 2 - Multiple Images:**

- Enter URLs one per line
- Press Enter on empty line to start batch download
- View summary report when complete

### Example Session

```
🐧 Ubuntu Image Fetcher
==================================================
Connecting communities through shared visual resources
Principles: Community • Respect • Sharing • Practicality
==================================================

Choose your approach:
1. Fetch a single image
2. Fetch multiple images

Enter your choice (1 or 2): 1

🔗 Please enter the image URL: https://example.com/image.jpg

🌐 Connecting to: https://example.com/image.jpg
✅ Successfully saved: image.jpg (245.3KB)

📁 Saved to: Fetched_Images\image.jpg

🌍 Ubuntu spirit: Through sharing, we build community!
```

## 🏗️ Architecture

### Core Class: `UbuntuImageFetcher`

```python
class UbuntuImageFetcher:
    def __init__(self, directory="Fetched_Images")
    def fetch_image(self, url)              # Download single image
    def fetch_multiple_images(self, urls)    # Batch download
    def display_summary(self, results)       # Show operation summary
```

### Key Methods

- **`fetch_image(url)`**: Downloads single image with full error handling
- **`fetch_multiple_images(urls)`**: Processes multiple URLs with progress tracking
- **`_is_safe_content_type()`**: Validates image file types for security
- **`_check_duplicate()`**: Prevents duplicate downloads using MD5 hashing
- **`_generate_filename()`**: Creates appropriate filenames from URLs

## 🛡️ Security Features

| Feature                | Description                                                            |
| ---------------------- | ---------------------------------------------------------------------- |
| **Content Validation** | Only downloads verified image formats (JPEG, PNG, GIF, WebP, BMP, SVG) |
| **Size Limits**        | 50MB maximum file size to prevent abuse                                |
| **Safe Filenames**     | Secure, filesystem-friendly filename generation                        |
| **Timeout Protection** | Network timeouts prevent hanging connections                           |
| **Header Validation**  | Checks HTTP headers before downloading                                 |

## 🌐 Ubuntu Principles Implementation

### 🤝 Community

- Connects respectfully to global web resources
- Uses proper User-Agent identification
- Enables sharing through organized directory structure

### 🙏 Respect

- Graceful error handling - never crashes
- Bandwidth conscious with size limits and delays
- Respects server responses and HTTP status codes
- Polite request patterns (HEAD requests first)

### 📤 Sharing

- Organized directory structure for easy sharing
- Prevents duplicate downloads to save space
- Clear feedback and operation summaries
- Batch processing for efficient operations

### 🔧 Practicality

- Real-world error handling for network issues
- Multiple image format support
- User-friendly interface with clear prompts
- Production-ready security features

## 📁 Project Structure

```
Ubuntu_Requests/
├── index.py              # Main Ubuntu Image Fetcher application
├── requirements.txt      # Python dependencies
├── LICENSE              # License file
├── Fetched_Images/      # Created automatically for downloaded images
└── venv/               # Virtual environment (recommended)
```

## 🔧 Dependencies

```
certifi==2025.8.3
charset-normalizer==3.4.3
idna==3.10
requests==2.32.5
urllib3==2.5.0
```

## ❌ Error Handling

The application gracefully handles:

- **Network Issues**: Connection timeouts, DNS failures
- **HTTP Errors**: 404 Not Found, 403 Forbidden, 500 Server Error
- **Invalid Content**: Non-image URLs, corrupted files
- **File System**: Permission issues, disk space problems
- **Security**: Malicious URLs, oversized files

## 🎯 Requirements Met

✅ **Core Requirements:**

- [x] Prompts user for image URL
- [x] Creates "Fetched_Images" directory using `os.makedirs(exist_ok=True)`
- [x] Downloads images using `requests` library
- [x] Handles HTTP errors appropriately
- [x] Extracts filenames from URLs or generates appropriate ones
- [x] Saves images in binary mode

✅ **Challenge Questions:**

- [x] Multiple URL support with batch processing
- [x] Security precautions for unknown sources
- [x] Duplicate prevention using MD5 hashing
- [x] HTTP header validation (Content-Type, Content-Length)

## 🚀 Advanced Usage

### Programmatic Usage

```python
from index import UbuntuImageFetcher

# Initialize fetcher
fetcher = UbuntuImageFetcher("MyImages")

# Download single image
success, message, filepath = fetcher.fetch_image("https://example.com/image.jpg")
print(message)

# Batch download
urls = ["https://site1.com/img1.jpg", "https://site2.com/img2.png"]
results = fetcher.fetch_multiple_images(urls)
fetcher.display_summary(results)
```

## 📊 Performance

- **Memory Efficient**: Streams large files instead of loading into memory
- **Bandwidth Conscious**: Respects server resources with delays and limits
- **Fast Duplicate Detection**: Hash-based comparison for quick duplicate prevention
- **Concurrent Safe**: Thread-safe design for future enhancement

## 🤝 Contributing

This project embodies the Ubuntu philosophy of community collaboration. Contributions that enhance any of the four principles (Community, Respect, Sharing, Practicality) are welcome!

## 📄 License

Open source in the spirit of Ubuntu - shared knowledge benefits everyone.

---

_Ubuntu Image Fetcher - Connecting communities through shared visual resources_  
_"Through code, we build bridges between communities"_
