from PIL import Image
import io

def visualize_graph(graph, save=True, filename="graph.png"):
    """
    Visualizes the given graph by generating a PNG image of its Mermaid representation.
    
    Args:
        graph: The graph object to visualize.
        
    Returns:
        None
    """
    # Generate the Mermaid PNG image from the graph
    image_bytes = graph.get_graph().draw_mermaid_png()
    image = Image.open(io.BytesIO(image_bytes))
    if save:
        image.save(filename)