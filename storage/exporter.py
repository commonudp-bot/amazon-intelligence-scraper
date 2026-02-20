"""Export scraped data to various formats."""

import json
import csv
import logging
from typing import List, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class DataExporter:
    """Exports scraped data to JSON and CSV formats."""

    @staticmethod
    def export_json(
        data: List[Dict[str, Any]],
        filepath: str,
        indent: int = 2,
    ) -> None:
        """
        Export data to JSON file.
        
        Args:
            data: List of dictionaries to export
            filepath: Output file path
            indent: JSON indentation
        """
        try:
            # Create directories if needed
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=indent, ensure_ascii=False)
            
            logger.info(f"Exported {len(data)} records to {filepath}")
        except IOError as e:
            logger.error(f"Failed to export JSON: {e}")
            raise

    @staticmethod
    def export_csv(
        data: List[Dict[str, Any]],
        filepath: str,
    ) -> None:
        """
        Export data to CSV file.
        
        Args:
            data: List of dictionaries to export
            filepath: Output file path
        """
        if not data:
            logger.warning("No data to export")
            return
        
        try:
            # Create directories if needed
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            
            fieldnames = data[0].keys()
            
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            
            logger.info(f"Exported {len(data)} records to {filepath}")
        except IOError as e:
            logger.error(f"Failed to export CSV: {e}")
            raise
