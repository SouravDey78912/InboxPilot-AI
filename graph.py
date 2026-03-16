from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.email_analyzer import analyze_email
from agents.planner_agent import planner
from tools.calendar_tool import create_calendar_event
from tools.notifier_tool import notify_user
from tools.reminder_tool import create_reminder
from logger import get_logger


logger = get_logger(__name__)


class AgentState(TypedDict):
    email: str
    analysis: str
    action: str


def analyzer_node(state):
    email = state["email"]

    analysis = analyze_email(email)

    return {"analysis": analysis}


def planner_node(state):
    action = planner(state)
    logger.info(f"Planner decided: {action}")
    return {"action": action}


def calendar_node(state):

    logger.info("Running calendar action")

    create_calendar_event(state["analysis"])

    return {}


def reminder_node(state):
    create_reminder(state["analysis"])

    return {}


def notify_node(state):
    notify_user("Important email detected")

    return {}


def router(state):

    action = state["action"]

    logger.info(f"Router received: {action}")

    if action == "calendar_event":
        return "calendar"

    elif action == "reminder":
        return "reminder"

    elif action == "notify":
        return "notify"

    return "end"


def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("analyze", analyzer_node)
    workflow.add_node("plan", planner_node)
    workflow.add_node("calendar", calendar_node)
    workflow.add_node("reminder", reminder_node)
    workflow.add_node("notify", notify_node)

    workflow.set_entry_point("analyze")

    workflow.add_edge("analyze", "plan")

    workflow.add_conditional_edges(
        "plan",
        router,
        {
            "calendar": "calendar",
            "reminder": "reminder",
            "notify": "notify",
            "end": END,
        },
    )

    workflow.add_edge("calendar", END)
    workflow.add_edge("reminder", END)
    workflow.add_edge("notify", END)

    return workflow.compile()
