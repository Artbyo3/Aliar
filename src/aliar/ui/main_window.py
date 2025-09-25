"""
Main application window and UI components using CustomTkinter.
"""

import logging
import customtkinter as ctk
from typing import Optional

logger = logging.getLogger(__name__)


class MainWindow:
    """Main application window using CustomTkinter."""
    
    def __init__(self):
        self.logger = logger
        self.is_initialized = False
        self.root: Optional[ctk.CTk] = None
        
    def initialize(self) -> bool:
        """Initialize the main window."""
        try:
            # Set appearance mode and color theme
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
            
            # Create main window
            self.root = ctk.CTk()
            self.root.title("Aliar")
            self.root.geometry("400x200")
            
            # Create Hello World label
            self.hello_label = ctk.CTkLabel(
                self.root,
                text="Hello World!",
                font=ctk.CTkFont(size=24, weight="bold")
            )
            self.hello_label.pack(expand=True)
            
            self.logger.info("Main window initialized successfully")
            self.is_initialized = True
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to initialize main window: {e}")
            return False
    
    def show(self) -> None:
        """Show the main window."""
        if self.root and self.is_initialized:
            self.root.mainloop()
        else:
            self.logger.error("Cannot show window - not initialized")
    
    def hide(self) -> None:
        """Hide the main window."""
        if self.root:
            self.root.withdraw()
            self.logger.info("Main window hidden")
