from arango import ArangoClient
import json

# -------------------------------
# ArangoDB Connection
# -------------------------------
client = ArangoClient(hosts="http://localhost:8529")

db = client.db(
    "resume_graph",
    username="root",
    password="rootpassword"
)

print("✅ Connected to ArangoDB")

