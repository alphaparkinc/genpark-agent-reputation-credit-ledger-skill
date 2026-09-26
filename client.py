import json
import hashlib
from typing import Dict, Any, List, Optional

class AgentReputationCreditLedgerClient:
    """
    Production-grade agent reputation and credit accounting ledger.
    Tracks verifiable execution proofs, maintains historical trust ratings (0.00 - 1.00),
    and enforces slashable bond deductions for rogue or hallucinating worker agents.
    """
    def __init__(self, slash_penalty_pct: float = 0.25):
        self.slash_penalty = slash_penalty_pct

    def record_agent_interaction(
        self,
        worker_agent_id: str = "agent_solidity_auditor_v4",
        task_id: str = "task_dex_router_audit_881",
        execution_successful: bool = True,
        hallucination_flag: bool = False,
        response_time_ms: int = 1420,
        current_staked_bond_usd: float = 5000.0,
        historical_score: float = 0.92
    ) -> Dict[str, Any]:
        receipt_raw = f"{worker_agent_id}:{task_id}:{execution_successful}:{response_time_ms}"
        receipt_hash = hashlib.sha256(receipt_raw.encode("utf-8")).hexdigest()[:24]

        # Penalty calculation
        slashed_amount_usd = 0.0
        if hallucination_flag or not execution_successful:
            slashed_amount_usd = round(current_staked_bond_usd * self.slash_penalty, 2)
            updated_bond = round(current_staked_bond_usd - slashed_amount_usd, 2)
            new_reputation = max(0.0, round(historical_score - 0.20, 3))
            trust_verdict = "SLASHED_REPUTATION_PENALTY_APPLIED"
        else:
            updated_bond = current_staked_bond_usd
            new_reputation = min(1.0, round(historical_score + 0.015, 3))
            trust_verdict = "REPUTATION_UPGRADED_SUCCESS_PROOF"

        return {
            "ledger_id": "rep_rec_5502",
            "worker_agent_id": worker_agent_id,
            "task_id": task_id,
            "cryptographic_receipt_hash": receipt_hash,
            "prior_reputation_score": historical_score,
            "updated_reputation_score": new_reputation,
            "staked_bond_usd": updated_bond,
            "slashed_penalty_usd": slashed_amount_usd,
            "trust_verdict": trust_verdict,
            "agent_status": "CERTIFIED_SWARM_WORKER" if new_reputation >= 0.70 else "PROBATIONARY_QUARANTINE"
        }
