# 🚫 PDF De-Watermarker: Because Nobody Likes Unwanted Stamps on Their Documents

[![Built with Python](https://img.shields.io/badge/Built%20with-Python-blue.svg)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What is this sorcery? 🧙‍♂️

Ever had a PDF that looks like it went through a stamp-collecting enthusiast's fever dream? Universities thinks they are clever with their "COPY" text when you print?  Fear not! This magical script removes those pesky watermarks faster than you can say "proprietary document marking system."

## Features ✨

- Removes watermarks like a digital pressure washer
- Handles both annotations and XObject forms (fancy talk for "different types of watermarks")
- Won't explode if something goes wrong (proper error handling included!)
- Command-line interface that won't make you cry

## Prerequisites 📋

Before you embark on this watermark-removing adventure, you'll need:

- Python 3.x (because we're not savages)
- A burning desire to see your PDFs watermark-free
- The following packages (because even wizards need their tools):
  ```
  argparse>=1.4.0
  PyPDF2>=3.0.0
  ```

## Setup 🛠️

1. Clone this magical repository:
   ```bash
   git clone https://github.com/jasonbrianhall/removewatermarkpdf.git
   cd removewatermarkpdf
   ```

3. Install the requirements (because dependencies matter):
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🎮

It's as easy as:
```bash
python dewatermark.py -i "that_watermarked_pdf.pdf" -o "freedom.pdf"
```

Or if you're feeling fancy:
```bash
python dewatermark.py --input "that_watermarked_pdf.pdf" --output "freedom.pdf"
```

## How it Works 🤓

1. Opens your PDF (duh)
2. Hunts down watermarks like a digital bounty hunter
3. Removes them with surgical precision
4. Saves your now-pristine PDF

## Warning ⚠️

This script doesn't make your coffee or solve world peace. It just removes watermarks. Also:
- Always check output files
- Keep backups of your originals
- Don't use this on classified government documents (we're looking at you, spy agencies)

## License 📜

MIT License - Because sharing is caring, and lawyers need something to read.

## Credits 👏

- Coffee ☕
- Stack Overflow 🚀
- That one person who wrote the PyPDF2 documentation

## Support 🆘

If this script saved your day:
- Tell your friends
- Pay it forward
- Name your firstborn "PDF De-Watermarker" (okay, maybe not that last one)

---
Made with ❤️  and probably too much caffeine

_Remember: With great power comes great responsibility. Use this tool wisely, and may your PDFs be forever watermark-free!_ 🎉
