from __future__ import annotations

from dataclasses import dataclass


@dataclass(kw_only=True)
class DraftPick:
    season: str
    round: int
    roster_id: int
    previous_owner_id: int
    owner_id: int

    @staticmethod
    def from_dict(draft_pick_dict: dict) -> DraftPick:
        return DraftPick(season=draft_pick_dict["season"],
                         round=draft_pick_dict["round"],
                         roster_id=draft_pick_dict["roster_id"],
                         previous_owner_id=draft_pick_dict["previous_owner_id"],
                         owner_id=draft_pick_dict["owner_id"])
    
    @classmethod
    def from_dict_list(cls, draft_pick_dict_list: dict) -> list[DraftPick]:
        draft_picks = list()
        for draft_pick_dict in draft_pick_dict_list:
            draft_picks.append(DraftPick.from_dict(draft_pick_dict))
        return draft_picks
