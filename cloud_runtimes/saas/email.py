"""
Email SaaS runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from ..types.saas import (
    SendEmailRequest,
    SendEmailResponse,
    SendEmailTemplateRequest,
    EmailStatusResponse,
)


class EmailRuntimes(ABC):
    """Email SaaS Runtimes standard API."""

    @abstractmethod
    async def send_email(
        self,
        to: List[str],
        subject: str,
        body: str,
        from_email: Optional[str] = None,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        html_body: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SendEmailResponse:
        """Send an email.
        
        Args:
            to: List of recipient email addresses
            subject: Email subject
            body: Email body (plain text)
            from_email: Optional sender email address
            cc: Optional CC recipients
            bcc: Optional BCC recipients
            html_body: Optional HTML body
            metadata: Optional metadata for the request
            
        Returns:
            SendEmailResponse containing send result
            
        Raises:
            CloudRuntimesError: If sending email fails
        """
        pass

    @abstractmethod
    async def send_email_with_request(
        self,
        request: SendEmailRequest,
    ) -> SendEmailResponse:
        """Send an email using a structured request object.
        
        Args:
            request: SendEmailRequest containing all parameters
            
        Returns:
            SendEmailResponse containing send result
            
        Raises:
            CloudRuntimesError: If sending email fails
        """
        pass

    @abstractmethod
    async def send_email_with_template(
        self,
        to: List[str],
        template_id: str,
        template_data: Dict[str, str],
        from_email: Optional[str] = None,
        cc: Optional[List[str]] = None,
        bcc: Optional[List[str]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SendEmailResponse:
        """Send an email using a template.
        
        Args:
            to: List of recipient email addresses
            template_id: Template identifier
            template_data: Data to populate the template
            from_email: Optional sender email address
            cc: Optional CC recipients
            bcc: Optional BCC recipients
            metadata: Optional metadata for the request
            
        Returns:
            SendEmailResponse containing send result
            
        Raises:
            CloudRuntimesError: If sending email fails
        """
        pass

    @abstractmethod
    async def send_email_with_template_request(
        self,
        request: SendEmailTemplateRequest,
    ) -> SendEmailResponse:
        """Send an email with template using a structured request object.
        
        Args:
            request: SendEmailTemplateRequest containing all parameters
            
        Returns:
            SendEmailResponse containing send result
            
        Raises:
            CloudRuntimesError: If sending email fails
        """
        pass

    @abstractmethod
    async def get_email_status(
        self,
        message_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> EmailStatusResponse:
        """Get email sending status.
        
        Args:
            message_id: The message ID returned from send_email
            metadata: Optional metadata for the request
            
        Returns:
            EmailStatusResponse containing status information
            
        Raises:
            CloudRuntimesError: If getting email status fails
        """
        pass

    @abstractmethod
    async def send_bulk_email(
        self,
        emails: List[SendEmailRequest],
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[SendEmailResponse]:
        """Send multiple emails in bulk.
        
        Args:
            emails: List of email requests to send
            metadata: Optional metadata for the request
            
        Returns:
            List of SendEmailResponse for each email
            
        Raises:
            CloudRuntimesError: If sending bulk emails fails
        """
        pass

    @abstractmethod
    async def validate_email_address(
        self,
        email: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Validate an email address.
        
        Args:
            email: The email address to validate
            metadata: Optional metadata for the request
            
        Returns:
            True if email address is valid
            
        Raises:
            CloudRuntimesError: If email validation fails
        """
        pass

    @abstractmethod
    async def get_email_templates(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[Dict[str, str]]:
        """Get available email templates.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            List of available email templates
            
        Raises:
            CloudRuntimesError: If getting templates fails
        """
        pass

    @abstractmethod
    async def create_email_template(
        self,
        template_id: str,
        subject: str,
        body: str,
        html_body: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Create an email template.
        
        Args:
            template_id: Unique template identifier
            subject: Template subject (can contain variables)
            body: Template body (can contain variables)
            html_body: Optional HTML template body
            metadata: Optional metadata for the request
            
        Returns:
            True if template was created successfully
            
        Raises:
            CloudRuntimesError: If creating template fails
        """
        pass

    @abstractmethod
    async def delete_email_template(
        self,
        template_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Delete an email template.
        
        Args:
            template_id: Template identifier to delete
            metadata: Optional metadata for the request
            
        Returns:
            True if template was deleted successfully
            
        Raises:
            CloudRuntimesError: If deleting template fails
        """
        pass