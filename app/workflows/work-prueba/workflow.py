from langgraph import Node, Edge
from tools import SentimentAnalysisTool, FeedbackTool
from state import SentimentState

class SentimentAnalysisWorkflow:
    def __init__(self):
        self.state = SentimentState()

        # Define nodes
        self.sentiment_analysis_node = Node("SentimentAnalysisNode", SentimentAnalysisTool())
        self.feedback_node = Node("FeedbackNode", FeedbackTool())

        # Define edges
        self.edge1 = Edge("Edge1", self.sentiment_analysis_node, self.feedback_node)
        self.edge2 = Edge("Edge2", self.feedback_node, self.sentiment_analysis_node)

        # Connect nodes
        self.sentiment_analysis_node.add_edge(self.edge1)
        self.feedback_node.add_edge(self.edge2)

    def run(self, text):
        self.state.text = text
        while not self.state.is_stable:
            self.sentiment_analysis_node.run(self.state)
            self.feedback_node.run(self.state)