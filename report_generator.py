import os
import json
import webbrowser
from datetime import datetime
def calculate_complexity(tools, loop_counts):
    complexity_data = {}
    for tool in tools:
        complexity_data[tool['name']] = {
            "time_complexity": f"O({loop_counts[0]})", 
            "space_complexity": f"O({loop_counts[1]})"  
        }
    return complexity_data

def calculate_energy_consumption(processes, loop_counts):
    energy_data = {}
    for process in processes:
        duration = process.get("duration", 1)  
        power = process.get("power", 0.5)  
        energy_data[process['name']] = {
            "energy_consumed": round(duration * power, 2),
            "duration": duration,
            "dynamic_energy": round(duration * power * (loop_counts[0] + loop_counts[1]), 2)
        }
    return energy_data

def generate_report(report_data):
    try:
        report_path = "report.html"
        
        phishing_data = report_data.get("phishing", [])
        phishing_table = "<p>No phishing data detected.</p>" if not phishing_data else \
            "<table><tr><th>URL</th><th>Status</th></tr>" + \
            "".join([f"<tr><td>{entry['url']}</td><td>{entry['status']}</td></tr>" for entry in phishing_data]) + \
            "</table>"
        
        network_data = report_data.get("network_analysis", [])
        network_table = "<p>No network data captured.</p>" if not network_data else \
            "<table><tr><th>Source</th><th>Destination</th></tr>" + \
            "".join([f"<tr><td>{entry['src']}</td><td>{entry['dst']}</td></tr>" for entry in network_data]) + \
            "</table>"
        
        evidence_data = report_data.get("evidence", [])
        evidence_table = "<table><tr><th>Type</th><th>Details</th></tr>" + \
            "".join([f"<tr><td>{entry['type']}</td><td>{json.dumps(entry['details'])}</td></tr>" for entry in evidence_data]) + \
            "</table>"

        tool_complexity = calculate_complexity(report_data.get("tools", []), report_data.get("loop_counts", [0, 0]))
        complexity_table = "<table><tr><th>Tool</th><th>Time Complexity</th><th>Space Complexity</th></tr>" + \
            "".join([f"<tr><td>{tool}</td><td>{data['time_complexity']}</td><td>{data['space_complexity']}</td></tr>" for tool, data in tool_complexity.items()]) + \
            "</table>"

        energy_consumption = calculate_energy_consumption(report_data.get("processes", []), report_data.get("loop_counts", [0, 0]))
        energy_table = "<table><tr><th>Process</th><th>Energy Consumed (kWh)</th><th>Duration (hours)</th><th>Dynamic Energy (kWh)</th></tr>" + \
            "".join([f"<tr><td>{process}</td><td>{data['energy_consumed']}</td><td>{data['duration']}</td><td>{data['dynamic_energy']}</td></tr>" for process, data in energy_consumption.items()]) + \
            "</table>"


        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Cyber Forensics Report</title>
            <link rel="stylesheet" href="main.css">
        </head>
        <body>
            <div class="report-container">
                <header>
                    <h1>Cybercrime Detection and Analysis Report</h1>
                    <p><strong>Date:</strong> {report_data['report_date']}</p>
                    <p><strong>Case Number:</strong> {report_data['case_number']}</p>
                    <p><strong>Classification:</strong> {report_data['classification_level']}</p>
                </header>

                <section>
                    <h2>Executive Summary</h2>
                    <p>{report_data.get("executive_summary", "No executive summary available.")}</p>
                </section>

                <section>
                    <h2>Phishing Analysis</h2>
                    {phishing_table}
                </section>

                <section>
                    <h2>Network Analysis</h2>
                    {network_table}
                </section>

                <section>
                    <h2>Evidence Collection</h2>
                    {evidence_table}
                </section>

                <section>
                    <h2>Tools and Complexity</h2>
                    {complexity_table}
                </section>

                <section>
                    <h2>Energy Consumption</h2>
                    {energy_table}
                </section>

                <section>
                    <h2>Conclusions and Recommendations</h2>
                    <p>{report_data.get("conclusions_and_recommendations", "No conclusions available.")}</p>
                </section>

                <footer class="footer">
                    <p>&copy; {datetime.now().year} Cybercrime Investigation Unit. All rights reserved.</p>
                    <p>This report is confidential and intended for authorized personnel only.</p>
                </footer>
            </div>
        </body>
        </html>
        """

        with open(report_path, "w") as f:
            f.write(html_content)
        
        webbrowser.open(report_path)
        print(f"Report generated at {report_path}")

    except Exception as e:
        print(f"Error during report generation: {e}")
