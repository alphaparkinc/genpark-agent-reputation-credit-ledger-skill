import json, sys
from client import AgentReputationCreditLedgerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "agent-reputation-credit-ledger", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "record_agent_interaction", "description": "Records cryptographic execution receipts, updates reputation scores, and enforces slashable penalties."}]}}
    elif method == "tools/call":
        client = AgentReputationCreditLedgerClient()
        res = client.record_agent_interaction()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AgentReputationCreditLedgerClient()
        print(json.dumps(client.record_agent_interaction(), indent=2))
