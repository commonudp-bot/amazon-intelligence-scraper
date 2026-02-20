"""CAPTCHA detection for blocked requests."""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class CaptchaDetector:
    """Detects CAPTCHA challenges in responses."""

    # Common CAPTCHA indicators
    CAPTCHA_INDICATORS = [
        "robot check",
        "unusual traffic",
        "captcha",
        "challenge",
    ]

    def is_captcha_present(self, html: str) -> bool:
        """
        Check if CAPTCHA is present in HTML response.
        
        Args:
            html: HTML content
            
        Returns:
            True if CAPTCHA detected, False otherwise
        """
        html_lower = html.lower()
        
        for indicator in self.CAPTCHA_INDICATORS:
            if indicator in html_lower:
                logger.warning(f"CAPTCHA detected: {indicator}")
                return True
                
        return False

    def get_captcha_type(self, html: str) -> Optional[str]:
        """
        Identify the type of CAPTCHA if present.
        
        Args:
            html: HTML content
            
        Returns:
            CAPTCHA type or None if not detected
        """
        if not self.is_captcha_present(html):
            return None
            
        if "recaptcha" in html.lower():
            return "recaptcha"
        elif "hcaptcha" in html.lower():
            return "hcaptcha"
        else:
            return "unknown"
