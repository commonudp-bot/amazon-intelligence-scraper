
'''

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





'''

"""Export scraped data to multiple formats (JSON, CSV, Excel)."""

import json
import csv
import logging
from typing import List, Dict, Any
from pathlib import Path

logger = logging.getLogger(__name__)


class DataExporter:
    """Exports scraped data to JSON, CSV, and Excel formats."""

    # ------------------------------------------------------------------
    # JSON EXPORT
    # ------------------------------------------------------------------
    @staticmethod
    def export_json(
        data: List[Dict[str, Any]],
        filepath: str,
        indent: int = 2,
    ) -> None:
        """Export data to a JSON file."""
        if not data:
            logger.warning("No data to export to JSON")
            return

        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=indent, ensure_ascii=False)

            logger.info("Exported %s records to JSON: %s", len(data), filepath)

        except IOError as e:
            logger.error("Failed to export JSON: %s", e)
            raise

    # ------------------------------------------------------------------
    # CSV EXPORT
    # ------------------------------------------------------------------
    @staticmethod
    def export_csv(
        data: List[Dict[str, Any]],
        filepath: str,
    ) -> None:
        """Export data to a CSV file."""
        if not data:
            logger.warning("No data to export to CSV")
            return

        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)

            fieldnames = list(data[0].keys())

            with open(filepath, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

            logger.info("Exported %s records to CSV: %s", len(data), filepath)

        except IOError as e:
            logger.error("Failed to export CSV: %s", e)
            raise

    # ------------------------------------------------------------------
    # EXCEL EXPORT
    # ------------------------------------------------------------------
    @staticmethod
    def export_excel(
        data: List[Dict[str, Any]],
        filepath: str,
    ) -> None:
        """
        Export data to an Excel file (.xlsx recommended).

        Args:
            data: List of dictionaries to export
            filepath: Output file path (.xlsx or .xls)
        """
        if not data:
            logger.warning("No data to export to Excel")
            return

        try:
            import pandas as pd

            Path(filepath).parent.mkdir(parents=True, exist_ok=True)

            # Validate extension
            ext = Path(filepath).suffix.lower()
            if ext not in {".xlsx", ".xls"}:
                raise ValueError("Excel file must have .xlsx or .xls extension")

            df = pd.DataFrame(data)

            # Choose engine automatically
            if ext == ".xls":
                engine = "xlwt"
            else:
                engine = "openpyxl"

            df.to_excel(filepath, index=False, engine=engine)

            logger.info("Exported %s records to Excel: %s", len(data), filepath)

        except ImportError:
            logger.error(
                "Excel export requires pandas and openpyxl (and xlwt for .xls). "
                "Install with: pip install pandas openpyxl xlwt"
            )
            raise
        except Exception as e:
            logger.error("Failed to export Excel: %s", e)
            raise