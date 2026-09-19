import os
import json
from flask import Flask, render_template, jsonify, request

from core.file_organizer import FileOrganizer
from core.system_monitor import SystemMonitor
from core.web_scraper import WebScraper
from core.pdf_processor import PDFProcessor
from core.notifier import Notifier
from core.scheduler import TaskScheduler
from core.image_processor import ImageProcessor
from core.network_scanner import NetworkScanner
from utils.logger import get_recent_logs, get_logger

logger = get_logger("WebApp")

app = Flask(__name__, template_folder="templates", static_folder="static")

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json")
file_organizer = FileOrganizer(CONFIG_PATH)
system_monitor = SystemMonitor(CONFIG_PATH)
web_scraper = WebScraper(CONFIG_PATH)
pdf_processor = PDFProcessor()
notifier = Notifier(CONFIG_PATH)
task_scheduler = TaskScheduler(CONFIG_PATH)
image_processor = ImageProcessor()
network_scanner = NetworkScanner()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/metrics", methods=["GET"])
def get_metrics():
    res = system_monitor.get_system_metrics()
    return jsonify(res)

@app.route("/api/logs", methods=["GET"])
def get_logs():
    logs = get_recent_logs(max_lines=80)
    return jsonify({"success": True, "logs": logs})

@app.route("/api/run-task", methods=["POST"])
def run_task():
    data = request.json or {}
    task_name = data.get("task")

    logger.info(f"Dashboard triggered task: '{task_name}'")

    if task_name == "organize_files":
        target = data.get("target_dir")
        result = file_organizer.organize_directory(target)
    elif task_name == "clean_temp":
        target = data.get("target_dir")
        result = file_organizer.clean_temp_files(target)
    elif task_name == "system_check":
        result = system_monitor.run_health_check()
    elif task_name == "create_backup":
        result = system_monitor.create_backup()
    elif task_name == "web_check":
        result = web_scraper.check_monitored_sites()
    elif task_name == "scrape_url":
        url = data.get("url", "https://www.python.org")
        result = web_scraper.fetch_page_summary(url)
    elif task_name == "notify":
        title = data.get("title", "Dashboard Alert")
        msg = data.get("message", "Test notification from Web Dashboard.")
        result = notifier.send_notification(title, msg)
    elif task_name == "ping_host":
        host = data.get("host", "8.8.8.8")
        result = network_scanner.ping_host(host=host)
    elif task_name == "port_scan":
        host = data.get("host", "127.0.0.1")
        result = network_scanner.scan_common_ports(host=host)
    elif task_name == "network_ifaces":
        result = network_scanner.get_network_interfaces()
    elif task_name == "compress_image":
        img_path = data.get("image_path", "")
        result = image_processor.compress_image(img_path)
    else:
        result = {"success": False, "message": f"Unknown task: {task_name}"}

    return jsonify(result)

@app.route("/api/scheduler/status", methods=["GET"])
def scheduler_status():
    return jsonify(task_scheduler.get_status())

@app.route("/api/scheduler/toggle", methods=["POST"])
def scheduler_toggle():
    if task_scheduler.running:
        res = task_scheduler.stop()
    else:
        res = task_scheduler.start()
    return jsonify(res)

def run_server(port=5000, debug=False):
    logger.info(f"Starting Web Dashboard server on http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=debug)

if __name__ == "__main__":
    run_server()
