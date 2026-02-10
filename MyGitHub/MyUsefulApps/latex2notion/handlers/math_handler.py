"""
Math Handler

Converts LaTeX math expressions to Notion format.
Notion uses KaTeX for rendering math.
"""

from latex2notion.parser import ASTNode, NodeType


class MathHandler:
    """Handles conversion of math expressions."""
    
    def convert(self, node: ASTNode) -> str:
        """
        Convert a math node to Notion format.
        
        Args:
            node: ASTNode with NodeType.MATH_INLINE or NodeType.MATH_DISPLAY
            
        Returns:
            Notion-compatible math string
        """
        if node.node_type == NodeType.MATH_INLINE:
            # Notion inline equation format - use \( \) delimiters
            # This is the standard LaTeX inline math syntax that Notion recognizes
            return f"\\({node.content}\\)"
        elif node.node_type == NodeType.MATH_DISPLAY:
            # Notion display math - use \[ \] for block equations
            return f"\\[\n{node.content}\n\\]"
        else:
            return ""
    
    def is_math_node(self, node: ASTNode) -> bool:
        """Check if node is a math node."""
        return node.node_type in [NodeType.MATH_INLINE, NodeType.MATH_DISPLAY]
