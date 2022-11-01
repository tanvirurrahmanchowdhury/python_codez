from pathlib import Path
from fireworks import Firework, Workflow
from graphviz import Digraph


# Copied from fws
state_to_color = {
    "RUNNING": "#F4B90B",
    "WAITING": "#1F62A2",
    "FIZZLED": "#DB0051",
    "READY": "#2E92F2",
    "COMPLETED": "#24C75A",
    "RESERVED": "#BB8BC1",
    "ARCHIVED": "#7F8287",
    "DEFUSED": "#B7BCC3",
    "PAUSED": "#FFCFCA",
}


def wf_to_graph(workflow):
    """
    Creates and renders a graph representation of a
    workflow and firework.  Workflows are rendered as the
    control flow of the fireworks, while Fireworks are
    rendered as a sequence of Firetasks.
    Args:
        workflow (Workflow or Firework): workflow or Firework
            to be rendered
    """
    # Create the dag
    dot = Digraph(comment=workflow.name, graph_attr={"rankdir": "LR"})
    dot.node_attr["shape"] = "rectangle"
    if isinstance(workflow, Workflow):
        for fw in workflow.fws:
            dot.node(str(fw.fw_id), label=fw.name, color=state_to_color[fw.state])

        for start, targets in workflow.links.items():
            for target in targets:
                dot.edge(str(start), str(target))
    elif isinstance(workflow, Firework):
        for n, ft in enumerate(workflow.tasks):
            # Clean up names
            name = ft.fw_name.replace("{", "").replace("}", "")
            name = name.split(".")[-1]
            dot.node(str(n), label=name)
            if n >= 1:
                dot.edge(str(n - 1), str(n))
    return dot
