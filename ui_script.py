import os
import json
import requests
import webbrowser
from datetime import datetime
from scapy.all import sniff, IP, TCP
from report_generator import generate_report
from evidence_collector import collect_evidence
from phishing_detection import check_url
from network_sniffer import start_sniffing
import subprocess

def main():
    # ASCII Art and Title
    print("=" * 60)
    print("💻 CYBERCRIME DETECTION AND EVIDENCE COLLECTION SYSTEM 💻".center(60))
    print("=" * 60)
    print("An advanced tool for detecting phishing, analyzing network traffic, and generating reports.".center(60))
    print("Developed for cybersecurity investigations.".center(60))
    print("=" * 60)

    report_data = {
        "report_date": datetime.now().strftime("%Y-%m-%d"),
        "case_number": "CASE12345",
        "classification_level": "Confidential",
        "phishing": [],
        "network_analysis": [],
        "evidence": [],
        "tools": [
            {"name": "Sniffer", "time_complexity": "N", "space_complexity": "N"},
            {"name": "Phishing Detector", "time_complexity": "1", "space_complexity": "1"}
        ],
        "processes": [
            {"name": "Data Collection", "duration": 1, "power": 0.5},
            {"name": "Data Analysis", "duration": 2, "power": 0.7},
            {"name": "Report Generation", "duration": 0.5, "power": 0.3}
        ]
    }

    # Phishing URL Detection
    print("\n" + "=" * 60)
    print("🔍 PHISHING URL DETECTION".center(60))
    print("=" * 60)
    url = input("Enter a URL to check for phishing: ").strip()
    if url:
        print("Checking URL for phishing threats...")
        is_phishing = check_url(url)
        if is_phishing:
            print("🚨 WARNING: Phishing URL detected!")
            phishing_data = {"url": url, "status": "Phishing"}
            report_data["phishing"].append(phishing_data)
            report_data["evidence"].append(collect_evidence(phishing_data))
        else:
            print("✅ URL is safe.")
    else:
        print("❌ Invalid URL. Please try again.")

    # Network Sniffing
    print("\n" + "=" * 60)
    print("🌐 NETWORK SNIFFING AND ANALYSIS".center(60))
    print("=" * 60)
    print("Starting network sniffing...")
    report_data["network_analysis"] = start_sniffing(count=10)
    print("Network sniffing completed.")
    report_data["evidence"].append(collect_evidence({"type": "Network Analysis", "details": report_data["network_analysis"]}))

    # Report Summary and Recommendations
    print("\n" + "=" * 60)
    print("📝 REPORT GENERATION".center(60))
    print("=" * 60)
    report_data["executive_summary"] = "This report summarizes cybercrime detection activities and findings for the given case."
    report_data["conclusions_and_recommendations"] = "Increase cybersecurity measures and monitor network activity regularly."
    print("Generating report...")
    generate_report(report_data)
    print("✅ Report generated successfully. Check your output folder.")

    # Completion Message
    print("\n" + "=" * 60)
    print("🎉 SYSTEM TASK COMPLETED 🎉".center(60))
    print("=" * 60)
    print("Thank you for using the Cybercrime Detection and Evidence Collection System.".center(60))
    print("Stay safe and monitor your network regularly!".center(60))
    print("=" * 60)
    input("Press any key to Continue...")
    
    subprocess.run(["python3", "ui_script.py"])


if __name__ == "__main__":
    main()