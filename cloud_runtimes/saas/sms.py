"""
SMS SaaS runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from ..types.saas import (
    SendSMSRequest,
    SendSMSResponse,
    SendSMSTemplateRequest,
    SMSStatusResponse,
)


class SMSRuntimes(ABC):
    """SMS SaaS Runtimes standard API."""

    @abstractmethod
    async def send_sms(
        self,
        to: str,
        message: str,
        from_number: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SendSMSResponse:
        """Send an SMS message.
        
        Args:
            to: Recipient phone number
            message: SMS message content
            from_number: Optional sender phone number
            metadata: Optional metadata for the request
            
        Returns:
            SendSMSResponse containing send result
            
        Raises:
            CloudRuntimesError: If sending SMS fails
        """
        pass

    @abstractmethod
    async def send_sms_with_request(
        self,
        request: SendSMSRequest,
    ) -> SendSMSResponse:
        """Send an SMS using a structured request object.
        
        Args:
            request: SendSMSRequest containing all parameters
            
        Returns:
            SendSMSResponse containing send result
            
        Raises:
            CloudRuntimesError: If sending SMS fails
        """
        pass

    @abstractmethod
    async def send_sms_with_template(
        self,
        to: str,
        template_id: str,
        template_data: Dict[str, str],
        from_number: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SendSMSResponse:
        """Send an SMS using a template.
        
        Args:
            to: Recipient phone number
            template_id: Template identifier
            template_data: Data to populate the template
            from_number: Optional sender phone number
            metadata: Optional metadata for the request
            
        Returns:
            SendSMSResponse containing send result
            
        Raises:
            CloudRuntimesError: If sending SMS fails
        """
        pass

    @abstractmethod
    async def send_sms_with_template_request(
        self,
        request: SendSMSTemplateRequest,
    ) -> SendSMSResponse:
        """Send an SMS with template using a structured request object.
        
        Args:
            request: SendSMSTemplateRequest containing all parameters
            
        Returns:
            SendSMSResponse containing send result
            
        Raises:
            CloudRuntimesError: If sending SMS fails
        """
        pass

    @abstractmethod
    async def get_sms_status(
        self,
        message_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SMSStatusResponse:
        """Get SMS sending status.
        
        Args:
            message_id: The message ID returned from send_sms
            metadata: Optional metadata for the request
            
        Returns:
            SMSStatusResponse containing status information
            
        Raises:
            CloudRuntimesError: If getting SMS status fails
        """
        pass

    @abstractmethod
    async def send_bulk_sms(
        self,
        messages: List[SendSMSRequest],
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[SendSMSResponse]:
        """Send multiple SMS messages in bulk.
        
        Args:
            messages: List of SMS requests to send
            metadata: Optional metadata for the request
            
        Returns:
            List of SendSMSResponse for each message
            
        Raises:
            CloudRuntimesError: If sending bulk SMS fails
        """
        pass

    @abstractmethod
    async def validate_phone_number(
        self,
        phone_number: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Validate a phone number.
        
        Args:
            phone_number: The phone number to validate
            metadata: Optional metadata for the request
            
        Returns:
            True if phone number is valid
            
        Raises:
            CloudRuntimesError: If phone validation fails
        """
        pass

    @abstractmethod
    async def get_sms_templates(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[Dict[str, str]]:
        """Get available SMS templates.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            List of available SMS templates
            
        Raises:
            CloudRuntimesError: If getting templates fails
        """
        pass

    @abstractmethod
    async def create_sms_template(
        self,
        template_id: str,
        message: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Create an SMS template.
        
        Args:
            template_id: Unique template identifier
            message: Template message (can contain variables)
            metadata: Optional metadata for the request
            
        Returns:
            True if template was created successfully
            
        Raises:
            CloudRuntimesError: If creating template fails
        """
        pass

    @abstractmethod
    async def delete_sms_template(
        self,
        template_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Delete an SMS template.
        
        Args:
            template_id: Template identifier to delete
            metadata: Optional metadata for the request
            
        Returns:
            True if template was deleted successfully
            
        Raises:
            CloudRuntimesError: If deleting template fails
        """
        pass

    @abstractmethod
    async def get_delivery_report(
        self,
        message_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        """Get SMS delivery report.
        
        Args:
            message_id: The message ID to get report for
            metadata: Optional metadata for the request
            
        Returns:
            Dictionary containing delivery report information
            
        Raises:
            CloudRuntimesError: If getting delivery report fails
        """
        pass