"""
Main application class for Aliar.
"""

import logging
from typing import Optional

from aliar.ui.main_window import MainWindow

logger = logging.getLogger(__name__)


class AliarApp:
    """Main application class for Aliar multimedia processing."""
    
    def __init__(self):
        """Initialize the Aliar application."""
        self.logger = logger
        self.is_running = False
        self.main_window: Optional[MainWindow] = None
        
    def initialize(self) -> bool:
        """Initialize the application components."""
        try:
            self.logger.info("Initializing Aliar application...")
            
            # Initialize UI components
            self.main_window = MainWindow()
            if not self.main_window.initialize():
                self.logger.error("Failed to initialize main window")
                return False
            
            # TODO: Initialize audio/video components
            # TODO: Initialize AI/ML models
            
            return True
        except Exception as e:
            self.logger.error(f"Failed to initialize application: {e}")
            return False
    
    def run(self) -> None:
        """Run the main application loop."""
        if not self.initialize():
            self.logger.error("Failed to initialize application")
            return
            
        self.is_running = True
        self.logger.info("Aliar application started successfully!")
        
        try:
            # Show the main window (this will block until window is closed)
            if self.main_window:
                self.main_window.show()
        except KeyboardInterrupt:
            self.logger.info("Application interrupted by user")
        except Exception as e:
            self.logger.error(f"Application error: {e}")
        finally:
            self.shutdown()
    
    def shutdown(self) -> None:
        """Shutdown the application gracefully."""
        self.logger.info("Shutting down Aliar application...")
        self.is_running = False
        
        # Clean up UI
        if self.main_window:
            self.main_window.hide()
        
        # TODO: Clean up resources
        # TODO: Stop audio/video streams
        # TODO: Save application state
