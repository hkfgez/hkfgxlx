from typing import List, Optional
from models import RankedAction


def build_checklist(
    best_action: Optional[RankedAction],
    second_best_action: Optional[RankedAction],
    restrictions: List[str],
) -> List[str]:
    checklist: List[str] = []

    if best_action:
        checklist.append(f"Prioritize: {best_action.name}")
        checklist.append("Check asset availability and confirm minimum required amount.")
        checklist.append("Review whether switching paths affects current yield or eligibility.")
        checklist.append("Complete the action in the recommended order, not by random module hopping.")

    if second_best_action:
        checklist.append(f"Fallback option: {second_best_action.name}")

    if restrictions:
        checklist.append("Do not move restricted assets until path conflict is resolved.")
        for r in restrictions[:3]:
            checklist.append(f"Restriction: {r}")

    checklist.append("Re-evaluate after action completion if the ecosystem priority changes.")
    return checklist
