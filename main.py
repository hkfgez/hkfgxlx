from models import AnalyzeRequest, AnalyzeResponse
from engine.scanner import scan_opportunities
from engine.mapper import map_assets_and_eligibility
from engine.resolver import detect_conflicts, summarize_asset_restrictions
from engine.priority import rank_actions
from engine.checklist import build_checklist


def recognize_goal(goal: str) -> str:
    return f"The user wants a unified action view based on this goal: {goal}"


def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    scanned = scan_opportunities(request.opportunities)
    mapped = map_assets_and_eligibility(request.assets, scanned)
    conflicts = detect_conflicts(request.assets, mapped)
    restrictions = summarize_asset_restrictions(request.assets)
    ranked = rank_actions(request.user_goal, mapped)

    best_action = ranked[0] if ranked else None
    second_best_action = ranked[1] if len(ranked) > 1 else None

    not_recommended = [x for x in ranked if x.score < 20 or not x.feasible]

    checklist = build_checklist(best_action, second_best_action, restrictions)

    return AnalyzeResponse(
        user_goal_recognition=recognize_goal(request.user_goal),
        best_action=best_action,
        second_best_action=second_best_action,
        not_recommended_actions=not_recommended,
        conflicts=conflicts,
        asset_restrictions=restrictions,
        action_checklist=checklist,
    )
