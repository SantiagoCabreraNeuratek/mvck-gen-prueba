from langgraph import LangGraph, Node, Edge
from tools import SentimentAnalysisTool, FeedbackLoopTool
from state import SentimentState

class SentimentAnalysisWorkflow(LangGraph):
    def __init__(self):
        super().__init__()

        # Define nodes
        self.sentiment_analysis_node = Node(SentimentAnalysisTool())
        self.feedback_loop_node = Node(FeedbackLoopTool())

        # Define edges
        self.edges = [
            Edge(self.sentiment_analysis_node, self.feedback_loop_node),
            Edge(self.feedback_loop_node, self.sentiment_analysis_node)
        ]

        # Define state
        self.state = SentimentState()

    def run(self, text):
        self.state.text = text
        while not self.state.is_converged:
            self.sentiment_analysis_node.run(self.state)
            self.feedback_loop_node.run(self.state)
        return self.state.sentiment