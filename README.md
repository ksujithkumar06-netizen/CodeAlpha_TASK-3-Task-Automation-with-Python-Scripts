# ⚡ Task Automation Suite with Python Scripts

A production-ready, modular, cross-platform local task automation framework built with **Python 3.14**, **Flask**, **Schedule**, **psutil**, **PyPDF**, and **Rich**. 

Featuring an extensible core engine, an interactive CLI interface, and a modern glassmorphism Web Control Dashboard for real-time telemetry monitoring, automated task execution, and job scheduling.

---

## 🌟 Key Features

### 📂 File Organizer & Hygiene (`core/file_organizer.py`)
- **Automated Categorization:** Scans target directories and sorts files by extension into `Documents`, `Images`, `Videos`, `Audio`, `Archives`, and `Code` folders.
- **Temp File Purge:** Identifies and cleans temporary files (`.tmp`, `.bak`, `.log`).
- **Batch Renamer:** Sequentially renames files with custom zero-padded prefixes (e.g., `file_001.png`).

### 📄 PDF Document Processing (`core/pdf_processor.py`)
- **PDF Merger:** Combines multiple PDF documents into a single output file.
- **Text & Metadata Extraction:** Reads total page counts, document metadata, and extracts page text.

### 🌐 Web Scraper & Health Monitor (`core/web_scraper.py`)
- **HTTP Health Audit:** Monitors target URLs for HTTP status codes and measures latency in milliseconds.
- **Page Metadata Scraper:** Extracts HTML titles, word counts, character counts, and text snippets.

### 🛡️ System Diagnostics & Backups (`core/system_monitor.py`)
- **Real-Time Telemetry:** Captures CPU %, RAM %, and Disk % utilization via `psutil`.
- **Threshold Warnings:** Flags warnings when CPU > 85%, Memory > 85%, or Disk > 90%.
- **Automated Zip Backups:** Creates compressed, timestamped `.zip` archives (`backup_YYYYMMDD_HHMMSS.zip`) of specified files/folders.

### 📡 Network Diagnostics (`core/network_scanner.py`)
- **Ping Latency Audit:** Measures round-trip ping latency to remote hosts.
- **TCP Port Scanner:** Scans common application & database ports (`22`, `80`, `443`, `3306`, `5000`, `8080`, etc.).
- **Adapter Info:** Queries active network interfaces and IP addresses.

### 🖼️ Image Processor (`core/image_processor.py`)
- **Image Compression:** Reduces file size for JPEG, PNG, and WebP images.
- **Format Converter:** Converts between WEBP, PNG, and JPEG formats.
- **Thumbnail Generator:** Generates resized thumbnails (`200x200`).

### 🔔 Multi-Channel Notifier (`core/notifier.py`)
- **Multi-Dispatch:** Sends notifications to stdout console logs, HTTP Webhooks (Slack/Discord format), and native Windows OS desktop toast popups.

### ⏰ Background Task Scheduler (`core/scheduler.py`)
- **Threaded Daemon Worker:** Periodically executes tasks based on intervals defined in `config.json`. Non-blocking start, stop, and status control.

---

## 🚀 Quick Start Guide

### 1. Installation

Clone or navigate to the project repository and install the dependencies:

```bash
cd "c:/Users/HP/OneDrive/Desktop/Task Automation with Python Scripts"
pip install -r requirements.txt
```

### 2. Launch the Web Dashboard

Start the Flask web server:

```bash
python main.py --web
```

Open your web browser and navigate to:
👉 **[http://localhost:5000](http://localhost:5000)** or **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

### 3. Launch the Interactive CLI Menu

```bash
python main.py --cli
```

---

### 4. Execute One-Shot Commands

Run specific tasks directly from the command line:

```bash
python main.py --run organize
python main.py --run clean
python main.py --run system
python main.py --run backup
python main.py --run webcheck
python main.py --run ping
```

---

## 🏗️ Architecture & Data Flow

```mermaid
graph TB
    subgraph Interfaces
        CLI["CLI Menu (main.py --cli)"]
        WebUI["Web Dashboard (http://127.0.0.1:5000)"]
    end

    subgraph Web App (Flask app.py)
        API_Metrics["GET /api/metrics"]
        API_Logs["GET /api/logs"]
        API_Tasks["POST /api/run-task"]
        API_Sched["POST /api/scheduler/toggle"]
    end

    subgraph Core Engines (core/)
        FileOrg["FileOrganizer"]
        PDFProc["PDFProcessor"]
        WebScrape["WebScraper"]
        SysMon["SystemMonitor"]
        NetScan["NetworkScanner"]
        ImgProc["ImageProcessor"]
        Notifier["Notifier"]
        Sched["TaskScheduler"]
    end

    CLI --> Core Engines
    WebUI --> Web App
    Web App --> Core Engines
```

---

## 📂 Project Structure

```text
Task Automation with Python Scripts/
│
├── core/                       # Core Automation Engines
│   ├── __init__.py
│   ├── file_organizer.py       # File sorting, temp cleaning, batch renaming
│   ├── pdf_processor.py        # PDF merging and text extraction
│   ├── web_scraper.py          # Site health check & page scraping
│   ├── system_monitor.py       # System telemetry & zip backups
│   ├── network_scanner.py      # Ping, port scanner, network adapters
│   ├── image_processor.py      # Compression, format conversion, thumbnails
│   ├── notifier.py             # Webhook, console, & desktop notifications
│   └── scheduler.py            # Background job scheduler
│
├── web/                        # Flask Web Control Dashboard
│   ├── app.py                  # Flask server & REST API endpoints
│   ├── templates/
│   │   └── index.html          # Glassmorphism HTML dashboard template
│   └── static/
│       ├── css/style.css       # Custom dark-mode styling & animations
│       └── js/app.js           # Client-side AJAX polling & UI logic
│
├── utils/                      # Helper Utilities
│   └── logger.py               # Centralized logging module
│
├── tests/                      # Unit Test Suite
│   └── test_automation.py      # Automated tests for all core modules
│
├── config.json                 # System configuration & extension mappings
├── main.py                     # Unified CLI & Web launcher
├── requirements.txt            # Python package dependencies
└── README.md                   # Project documentation
```

---

## ⚙️ Configuration (`config.json`)

Customize sorting extensions, monitoring URLs, thresholds, and scheduling frequencies in `config.json`:

```json
{
  "app_name": "Task Automation Suite",
  "file_organizer": {
    "target_dir": "./downloads_demo",
    "temp_patterns": [".tmp", ".bak", ".log"]
  },
  "system_monitor": {
    "cpu_threshold_percent": 85.0,
    "memory_threshold_percent": 85.0,
    "disk_threshold_percent": 90.0
  },
  "scheduler": {
    "auto_organize_interval_minutes": 60,
    "system_check_interval_minutes": 30,
    "web_scrape_interval_minutes": 15
  }
}
```

---

## 🧪 Running Unit Tests

Execute the automated test suite with Python's built-in test runner:

```bash
python -m unittest discover tests
```

Output:
```text
Ran 7 tests in 2.679s

OK (100% Success)
```

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
