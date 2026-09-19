import os
import sys
import argparse
from core.file_organizer import FileOrganizer
from core.system_monitor import SystemMonitor
from core.web_scraper import WebScraper
from core.pdf_processor import PDFProcessor
from core.notifier import Notifier
from core.image_processor import ImageProcessor
from core.network_scanner import NetworkScanner
from utils.logger import get_logger

logger = get_logger("MainLauncher")

try:
    from rich.console import Console
    from rich.panel import Panel
    console = Console()
except ImportError:
    console = None

def run_cli_menu():
    organizer = FileOrganizer()
    monitor = SystemMonitor()
    scraper = WebScraper()
    pdf_proc = PDFProcessor()
    notifier = Notifier()
    img_proc = ImageProcessor()
    net_scan = NetworkScanner()

    while True:
        if console:
            console.clear()
            console.print(Panel.fit("[bold cyan]⚡ Task Automation Suite with Python[/bold cyan]\nSelect an option to automate tasks:", title="Menu"))
            console.print("[1] 📂 Organize Files in Target Folder")
            console.print("[2] 🧹 Clean Temporary Files")
            console.print("[3] 🛡️ Run System Health Check")
            console.print("[4] 💾 Create Zip Backup")
            console.print("[5] 🌐 Check Monitored Websites Health")
            console.print("[6] 📡 Ping Host / Scan Ports")
            console.print("[7] 🖼️ Compress / Convert Image")
            console.print("[8] 🔔 Send Test Notification")
            console.print("[9] 🚀 Launch Web Dashboard")
            console.print("[0] ❌ Exit")
        else:
            print("\n=== Task Automation Suite ===")
            print("1. Organize Files")
            print("2. Clean Temp Files")
            print("3. System Health Check")
            print("4. Create Backup")
            print("5. Web Health Check")
            print("6. Network Ping / Port Scan")
            print("7. Image Optimization")
            print("8. Send Notification")
            print("9. Launch Web Dashboard")
            print("0. Exit")

        choice = input("\nEnter choice [0-9]: ").strip()

        if choice == "1":
            target = input("Enter target folder path (default './downloads_demo'): ").strip() or "./downloads_demo"
            res = organizer.organize_directory(target)
            print(f"\nResult: {res.get('message')}")
        elif choice == "2":
            target = input("Enter target folder path (default './downloads_demo'): ").strip() or "./downloads_demo"
            res = organizer.clean_temp_files(target)
            print(f"\nResult: {res.get('message')}")
        elif choice == "3":
            res = monitor.run_health_check()
            print(f"\nResult: {res.get('message')}")
            metrics = res.get('metrics', {})
            if metrics:
                print(f"CPU: {metrics['cpu']['usage_percent']}% | RAM: {metrics['memory']['usage_percent']}% | Disk: {metrics['disk']['usage_percent']}%")
        elif choice == "4":
            res = monitor.create_backup()
            print(f"\nResult: {res.get('message')}")
        elif choice == "5":
            res = scraper.check_monitored_sites()
            print(f"\nResult: {res.get('message')}")
            for r in res.get('results', []):
                print(f" - {r.get('name')}: {r.get('message')}")
        elif choice == "6":
            host = input("Enter target host/IP (default '8.8.8.8'): ").strip() or "8.8.8.8"
            res_ping = net_scan.ping_host(host=host)
            print(f"\nPing: {res_ping.get('message')}")
            res_scan = net_scan.scan_common_ports(host=host)
            print(f"Port Scan: Open Ports = {res_scan.get('open_ports')}")
        elif choice == "7":
            img_path = input("Enter image file path: ").strip()
            if img_path:
                res = img_proc.compress_image(img_path)
                print(f"\nResult: {res.get('message')}")
            else:
                print("No image path specified.")
        elif choice == "8":
            msg = input("Enter notification message: ").strip() or "Test Alert from CLI"
            res = notifier.send_notification("CLI Alert", msg)
            print(f"\nResult: Notification dispatched.")
        elif choice == "9":
            print("\nLaunching Web Dashboard...")
            from web.app import run_server
            run_server()
            break
        elif choice == "0":
            print("Exiting Task Automation Suite. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid selection. Try again.")

        input("\nPress Enter to continue...")

def main():
    parser = argparse.ArgumentParser(description="Task Automation Suite with Python")
    parser.add_argument("--web", action="store_true", help="Launch the Web Dashboard UI")
    parser.add_argument("--port", type=int, default=5000, help="Port for the Web Dashboard server (default: 5000)")
    parser.add_argument("--cli", action="store_true", help="Launch interactive CLI menu")
    parser.add_argument("--run", type=str, choices=["organize", "clean", "system", "backup", "webcheck", "ping"], help="Directly run a single automation task")

    args = parser.parse_args()

    if args.web:
        from web.app import run_server
        run_server(port=args.port)
    elif args.run:
        if args.run == "organize":
            res = FileOrganizer().organize_directory()
        elif args.run == "clean":
            res = FileOrganizer().clean_temp_files()
        elif args.run == "system":
            res = SystemMonitor().run_health_check()
        elif args.run == "backup":
            res = SystemMonitor().create_backup()
        elif args.run == "webcheck":
            res = WebScraper().check_monitored_sites()
        elif args.run == "ping":
            res = NetworkScanner().ping_host()
        print(res.get("message", "Task completed."))
    elif args.cli:
        run_cli_menu()
    else:
        run_cli_menu()

if __name__ == "__main__":
    main()
