"""Proposal generation for claims."""
from __future__ import annotations

from typing import Any


class Proposal:
    def __init__(self, **kw: Any) -> None:
        self.__dict__.update(kw)


class ClaimProposer:
    def propose(self, entity: Any, observations: Any) -> list[Any]:
        return []


class RuleBasedProposer(ClaimProposer):
    def propose(self, entity: Any, observations: Any) -> list[Any]:
        out: list[Any] = []
        obs_list = observations if isinstance(observations, list) else [observations]
        for obs in obs_list:
            if isinstance(obs, dict):
                out.append(
                    Proposal(
                        proposal_id=f"prop-{obs.get('id', '')}",
                        entity_id=str(entity),
                        claims=[{"subject": entity, "predicate": "observed", "value": obs.get("observed_value")}],
                    )
                )
            else:
                out.append(Proposal(entity_id=str(entity), claims=[]))
        return out
