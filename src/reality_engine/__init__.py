"""Reality Engine package."""

from reality_engine.core.temporal import (
    bitemporal_key,
    format_iso8601,
    get_observations_in_interval,
    get_observations_since,
    get_relationships_in_interval,
    get_relationships_since,
    materialize_world_state_at,
    parse_iso8601,
    reconstruct_claims_at,
    reconstruct_events_at,
    reconstruct_observations_at,
)

# Public API
from reality_engine.database import Database

__all__ = [
    "Database",
    "bitemporal_key",
    "format_iso8601",
    "get_observations_in_interval",
    "get_observations_since",
    "get_relationships_in_interval",
    "get_relationships_since",
    "materialize_world_state_at",
    "parse_iso8601",
    "reconstruct_claims_at",
    "reconstruct_events_at",
    "reconstruct_observations_at",
]
