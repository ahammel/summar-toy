from collections import namedtuple
import pprint

Node = namedtuple("Node", ["event", "summaries"])
Summary = namedtuple("Summary", ["name", "value"])

class SummarTree(object):
    def __init__(self):
        self._tree = []

    def __repr__(self):
        return "<SummarTree: {}>".format(pprint.pformat(self._tree))

    def pprint(self):
        pprint.pprint([dict(n._asdict()) for n in self._tree])

    def add_event(self, event):
        if not event in [node.event for node in self._tree]:
            node = Node(event, {})
            self._tree.append(node)

    def summarize(self, node, summary):
        for n in self._tree:
            if n == node:
                node.summaries[summary.name] = summary.value

    def since_last_summary(self, summary_name):
        head_node = self._tree[-1]
        last_summary = None
        events = []
        for node in self._tree[::-1]:
            if summary_name in node.summaries:
                last_summary = node.summaries[summary_name]
            else:
                events.append(node.event)
        return (head_node, last_summary, events)
