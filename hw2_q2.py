from collections import namedtuple
from enum import Enum

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """

from itertools import islice

def process_pair(a, b):
    # Cure משפר Sick ל-Healthy ו-Dying ל-Sick, לא משפיע על Cure
    if a.category == Condition.CURE and b.category != Condition.CURE:
        new_b_category = (
            Condition.HEALTHY if b.category == Condition.SICK else
            Condition.SICK if b.category == Condition.DYING else
            b.category
        )
        return [a, Agent(b.name, new_b_category)]
    if b.category == Condition.CURE and a.category != Condition.CURE:
        new_a_category = (
            Condition.HEALTHY if a.category == Condition.SICK else
            Condition.SICK if a.category == Condition.DYING else
            a.category
        )
        return [Agent(a.name, new_a_category), b]
    if a.category == Condition.CURE and b.category == Condition.CURE:
        return [a, b]
    # SICK & SICK: שניהם מחמירים ל-DYING
    if a.category == Condition.SICK and b.category == Condition.SICK:
        return [Agent(a.name, Condition.DYING), Agent(b.name, Condition.DYING)]
    # SICK & DYING: Sick נהיה Dying, Dying נהיה Dead
    if a.category == Condition.SICK and b.category == Condition.DYING:
        return [Agent(a.name, Condition.DYING), Agent(b.name, Condition.DEAD)]
    if a.category == Condition.DYING and b.category == Condition.SICK:
        return [Agent(a.name, Condition.DEAD), Agent(b.name, Condition.DYING)]
    # DYING & DYING: שניהם נהיים Dead
    if a.category == Condition.DYING and b.category == Condition.DYING:
        return [Agent(a.name, Condition.DEAD), Agent(b.name, Condition.DEAD)]
    # כל מקרה אחר - אין שינוי
    return [a, b]

def meetup(agent_listing: tuple) -> list:
    # סוכנים שצריכים להיפגש (לא HEALTHY ולא DEAD)
    to_meet = [agent for agent in agent_listing if agent.category not in (Condition.HEALTHY, Condition.DEAD)]
    updated = {}
    it = iter(to_meet)
    while True:
        pair = list(islice(it, 2))
        if not pair:
            break
        if len(pair) == 1:
            updated[pair[0].name] = pair[0]
        else:
            for agent in process_pair(pair[0], pair[1]):
                updated[agent.name] = agent
    # מחזירים את כל הסוכנים המקוריים, עם עדכון אם היה
    return [updated.get(agent.name, agent) for agent in agent_listing]

