from langgraph import LangGraph, Node, Edge
from tools import DocumentProcessor, DocumentSummarizer

# Define the nodes
node1 = Node("DocumentProcessor", DocumentProcessor)
node2 = Node("DocumentSummarizer", DocumentSummarizer)

# Define the edges
edge1 = Edge("DocumentProcessor", "DocumentSummarizer")

# Create the LangGraph
lg = LangGraph()

# Add the nodes and edges to the LangGraph
lg.add_node(node1)
lg.add_node(node2)
lg.add_edge(edge1)

# Define the workflow
def workflow(document):
    # Process the document
    processed_doc = lg.run_node("DocumentProcessor", document)
    
    # Summarize the processed document
    summary = lg.run_node("DocumentSummarizer", processed_doc)
    
    return summary