#!/usr/bin/env python3
"""
Aliar - Multimedia Processing Application
Main entry point for the application.
"""

import sys
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from aliar.core.app import AliarApp
from aliar.utils.logger import setup_logging


def main():
    """Main entry point for the Aliar application."""
    print("Hello World!")
    
    # Setup logging
    setup_logging(level="INFO")
    
    # Create and run the application
    app = AliarApp()
    app.run()


if __name__ == "__main__":
    main()
