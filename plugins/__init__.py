"""
Plugin module initialization.

This module provides plugin functionality for the lightnovel-ssr application.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

# Import main plugin classes/functions to make them available at package level
# from .plugin_name import PluginClass

# Define what gets imported when using "from plugins import *"
__all__ = [
  # "PluginClass",
]

# Optional: Plugin registry or initialization code
def initialize_plugins():
  """Initialize all available plugins."""
  pass

# Optional: Auto-discovery of plugins
def discover_plugins():
  """Discover and load available plugins."""
  pass
