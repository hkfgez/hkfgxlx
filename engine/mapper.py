from typing import List
from models import Asset, Opportunity, MappedOpportunity


def map_assets_and_eligibility(
    assets: List[Asset], opportunities: List[Opportunity]
) -> List[MappedOpportunity]:
    mapped: List[MappedOpportunity] = []

    for opp in opportunities:
        matched_asset = None
        available_amount = 0.0
        notes = []
        feasible = False

        for asset in assets:
            if asset.symbol == opp.required_asset:
                matched_asset = asset.symbol
                available_amount = asset.amount

                if asset.locked:
                    notes.append(f"{asset.symbol} is locked and may not be movable.")
                    feasible = False
                elif asset.amount >= opp.min_amount:
                    feasible = True
                else:
                    notes.append(
                        f"Insufficient amount: requires {opp.min_amount}, available {asset.amount}."
                    )
                    feasible = False
                break

        if matched_asset is None:
            notes.append(f"No matching asset found for required asset {opp.required_asset}.")

        mapped.append(
            MappedOpportunity(
                id=opp.id,
                name=opp.name,
                type=opp.type,
                feasible=feasible,
                matched_asset=matched_asset,
                available_amount=available_amount,
                reward_score=opp.reward_score,
                risk_score=opp.risk_score,
                time_sensitive=opp.time_sensitive,
                notes=notes,
            )
        )

    return mapped
