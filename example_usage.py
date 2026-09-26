import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgentReputationCreditLedgerClient

def main():
    client = AgentReputationCreditLedgerClient()
    res = client.record_agent_interaction()
    print("=== Agent Reputation Credit Ledger Output ===")
    print(f"Worker: {res['worker_agent_id']} | Task: {res['task_id']}")
    print(f"Receipt Hash: {res['cryptographic_receipt_hash']}")
    print(f"Reputation: {res['prior_reputation_score']} -> {res['updated_reputation_score']} ({res['trust_verdict']})")
    print(f"Bond: ${res['staked_bond_usd']:,.2f} (Slashed: ${res['slashed_penalty_usd']})")
    print(f"Status: {res['agent_status']}")

if __name__ == '__main__':
    main()
