import os
import json
import re

# Configuration
DATA_DIR = r"C:\Users\Admin\Downloads\ai enterprise"
UNSTRUCTURED_DIR = os.path.join(DATA_DIR, "unstructured")
OUTPUT_DIR = os.path.join(DATA_DIR, "output")

def extract_triples_from_text(filename, text):
    triples = []
    
    # Meeting Notes Patterns
    if "meeting_notes" in filename:
        attendees_match = re.search(r"Attendees:\s*(.*)", text)
        if attendees_match:
            attendees = [a.strip() for a in attendees_match.group(1).split(",")]
            meeting_name = "Enterprise AI Strategy Review"
            for attendee in attendees:
                triples.append({"subject": attendee, "relation": "ATTENDED", "object": meeting_name})
        
        discussion_match = re.search(r"Discussion:\s*(.*?)(?=Action Items:|$)", text, re.DOTALL)
        if discussion_match:
            topics = re.findall(r"- (.*)", discussion_match.group(1))
            for topic in topics:
                if "InsightAI" in topic and "healthcare diagnostics" in topic:
                    triples.append({"subject": "InsightAI", "relation": "EXPANDING_INTO", "object": "Healthcare Diagnostics"})
                if "Apollo Hospitals" in topic:
                    triples.append({"subject": "Apollo Hospitals", "relation": "DEMANDS", "object": "InsightAI"})
                if "Fortis Healthcare" in topic:
                    triples.append({"subject": "Fortis Healthcare", "relation": "DEMANDS", "object": "InsightAI"})

    # Email Communications Patterns
    elif "email_communications" in filename:
        sender_match = re.search(r"From:\s*(.*)", text)
        receiver_match = re.search(r"To:\s*(.*)", text)
        if sender_match and receiver_match:
            triples.append({"subject": sender_match.group(1).strip(), "relation": "SENT_EMAIL_TO", "object": receiver_match.group(1).strip()})
        
        revenue_match = re.search(r"InsightAI platform revenue crossed USD ([\d.]+) million", text)
        if revenue_match:
             triples.append({"subject": "InsightAI", "relation": "GENERATED_REVENUE", "object": f"USD {revenue_match.group(1)} Million"})
        
        clients_match = re.search(r"BFSI clients including (.*)\.", text)
        if clients_match:
            clients = [c.strip() for c in clients_match.group(1).split("and")]
            for client in clients:
                triples.append({"subject": client, "relation": "USES", "object": "InsightAI"})

    # Company Policy Patterns
    elif "company_policy" in filename:
        if "ISO 27001" in text:
            triples.append({"subject": "Employees", "relation": "COMPLIES_WITH", "object": "ISO 27001"})
        if "role-based access control" in text:
            triples.append({"subject": "Enterprise Data", "relation": "GOVERNED_BY", "object": "RBAC"})
        if "Information Security Office" in text:
            triples.append({"subject": "Data Breach", "relation": "REPORTED_TO", "object": "Information Security Office"})

    # Industry Reports Patterns
    elif "industry_reports" in filename:
        if "Indian AI analytics market" in text:
            triples.append({"subject": "Indian AI Analytics Market", "relation": "GROWING_AT", "object": "25% CAGR"})
        players = ["TCS", "Infosys", "Wipro"]
        for player in players:
            if player in text:
                triples.append({"subject": player, "relation": "INVESTS_IN", "object": "Knowledge Graph Platforms"})

    # Support Cases Patterns
    elif "support_cases" in filename:
        client_match = re.search(r"Client:\s*(.*)", text)
        issue_match = re.search(r"Issue:\s*(.*)", text)
        resolution_match = re.search(r"Resolution:\s*(.*)", text)
        if client_match and issue_match:
            triples.append({"subject": client_match.group(1).strip(), "relation": "REPORTED_ISSUE", "object": issue_match.group(1).strip()})
        if issue_match and resolution_match:
            triples.append({"subject": issue_match.group(1).strip(), "relation": "RESOLVED_BY", "object": resolution_match.group(1).strip()})

    return triples

def main():
    all_triples = []
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(UNSTRUCTURED_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(UNSTRUCTURED_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                triples = extract_triples_from_text(filename, content)
                for t in triples:
                    t["source"] = filename
                all_triples.extend(triples)

    output_file = os.path.join(OUTPUT_DIR, "knowledge_graph_triples.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_triples, f, indent=2)

    # Also generate CSV for Neo4j import
    csv_file = os.path.join(OUTPUT_DIR, "knowledge_graph_triples.csv")
    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write("subject,relation,object,source\n")
        for t in all_triples:
            f.write(f'"{t["subject"]}","{t["relation"]}","{t["object"]}","{t["source"]}"\n')

    print(f"Extracted {len(all_triples)} triples.")
    print(f"Saved to {output_file} and {csv_file}")

if __name__ == "__main__":
    main()
