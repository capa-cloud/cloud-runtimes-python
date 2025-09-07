"""
SaaS API data types for Cloud Runtimes.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from .common import Metadata


# Email types
@dataclass
class EmailAttachment:
    """Email attachment."""
    
    name: str
    content_type: str
    data: bytes


@dataclass
class SendEmailRequest:
    """Request to send email."""
    
    from_: str  # 'from' is a Python keyword, so we use 'from_'
    to: List[str]
    cc: Optional[List[str]] = None
    bcc: Optional[List[str]] = None
    subject: str = ""
    body: str = ""
    body_type: str = "text"  # text, html
    attachments: Optional[List[EmailAttachment]] = None
    metadata: Optional[Metadata] = None


@dataclass
class SendEmailTemplateRequest:
    """Request to send email with template."""
    
    from_: str
    to: List[str]
    cc: Optional[List[str]] = None
    bcc: Optional[List[str]] = None
    template_id: str = ""
    template_data: Optional[Dict[str, Any]] = None
    metadata: Optional[Metadata] = None


@dataclass
class SendEmailResponse:
    """Response from send email."""
    
    message_id: str
    status: str
    metadata: Optional[Metadata] = None


@dataclass
class EmailStatusResponse:
    """Email status response."""
    
    message_id: str
    status: str
    delivered_at: Optional[datetime] = None
    error_message: Optional[str] = None
    metadata: Optional[Metadata] = None


# SMS types
@dataclass
class SendSMSRequest:
    """Request to send SMS."""
    
    from_: str
    to: str
    message: str
    metadata: Optional[Metadata] = None


@dataclass
class SendSMSTemplateRequest:
    """Request to send SMS with template."""
    
    from_: str
    to: str
    template_id: str
    template_data: Optional[Dict[str, Any]] = None
    metadata: Optional[Metadata] = None


@dataclass
class SendSMSResponse:
    """Response from send SMS."""
    
    message_id: str
    status: str
    metadata: Optional[Metadata] = None


@dataclass
class SMSStatusResponse:
    """SMS status response."""
    
    message_id: str
    status: str
    delivered_at: Optional[datetime] = None
    error_message: Optional[str] = None
    metadata: Optional[Metadata] = None


# Encryption types
@dataclass
class EncryptRequest:
    """Request to encrypt data."""
    
    data: bytes
    key_id: Optional[str] = None
    algorithm: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class EncryptResponse:
    """Response from encrypt."""
    
    encrypted_data: bytes
    key_id: Optional[str] = None
    algorithm: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class DecryptRequest:
    """Request to decrypt data."""
    
    encrypted_data: bytes
    key_id: Optional[str] = None
    algorithm: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class DecryptResponse:
    """Response from decrypt."""
    
    data: bytes
    metadata: Optional[Metadata] = None


@dataclass
class GenerateKeyRequest:
    """Request to generate key."""
    
    key_type: str  # symmetric, asymmetric
    algorithm: str  # AES, RSA, etc.
    key_size: Optional[int] = None
    metadata: Optional[Metadata] = None


@dataclass
class GenerateKeyResponse:
    """Response from generate key."""
    
    key_id: str
    public_key: Optional[bytes] = None
    private_key: Optional[bytes] = None
    metadata: Optional[Metadata] = None


@dataclass
class HashRequest:
    """Request to hash data."""
    
    data: bytes
    algorithm: str  # SHA256, SHA512, MD5, etc.
    salt: Optional[bytes] = None
    metadata: Optional[Metadata] = None


@dataclass
class HashResponse:
    """Response from hash."""
    
    hash: bytes
    salt: Optional[bytes] = None
    metadata: Optional[Metadata] = None


@dataclass
class VerifyHashRequest:
    """Request to verify hash."""
    
    data: bytes
    hash: bytes
    algorithm: str
    salt: Optional[bytes] = None
    metadata: Optional[Metadata] = None


@dataclass
class VerifyHashResponse:
    """Response from verify hash."""
    
    valid: bool
    metadata: Optional[Metadata] = None


# IM (Instant Messaging) types
@dataclass
class SendIMMessageRequest:
    """Request to send instant message."""
    
    from_: str
    to: Optional[str] = None  # for direct message
    group_id: Optional[str] = None  # for group message
    message: str = ""
    type: str = "text"  # text, image, file, etc.
    metadata: Optional[Metadata] = None


@dataclass
class SendIMMessageResponse:
    """Response from send instant message."""
    
    message_id: str
    timestamp: datetime
    metadata: Optional[Metadata] = None


@dataclass
class CreateGroupRequest:
    """Request to create group."""
    
    name: str
    description: Optional[str] = None
    members: Optional[List[str]] = None
    metadata: Optional[Metadata] = None


@dataclass
class CreateGroupResponse:
    """Response from create group."""
    
    group_id: str
    metadata: Optional[Metadata] = None


# IVR (Interactive Voice Response) types
@dataclass
class MakeCallRequest:
    """Request to make call."""
    
    from_: str
    to: str
    message: Optional[str] = None
    voice: Optional[str] = None  # voice type
    language: Optional[str] = None  # language code
    metadata: Optional[Metadata] = None


@dataclass
class MakeCallResponse:
    """Response from make call."""
    
    call_id: str
    status: str
    metadata: Optional[Metadata] = None


@dataclass
class CallStatusResponse:
    """Call status response."""
    
    call_id: str
    status: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration: Optional[int] = None  # in seconds
    error_message: Optional[str] = None
    metadata: Optional[Metadata] = None


# Proxy types
@dataclass
class ProxyRequest:
    """Request to proxy HTTP request."""
    
    method: str
    url: str
    headers: Optional[Metadata] = None
    body: Optional[bytes] = None
    timeout: Optional[int] = None  # in seconds
    proxy_id: Optional[str] = None
    metadata: Optional[Metadata] = None


@dataclass
class ProxyResponse:
    """Response from proxy request."""
    
    status_code: int
    headers: Optional[Metadata] = None
    body: Optional[bytes] = None
    duration: Optional[float] = None  # in seconds
    metadata: Optional[Metadata] = None