"""
Encryption SaaS runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional

from ..types.saas import (
    DecryptRequest,
    DecryptResponse,
    EncryptRequest,
    EncryptResponse,
    GenerateKeyRequest,
    GenerateKeyResponse,
    HashRequest,
    HashResponse,
    VerifyHashRequest,
    VerifyHashResponse,
)


class EncryptionRuntimes(ABC):
    """Encryption SaaS Runtimes standard API."""

    @abstractmethod
    async def encrypt(
        self,
        data: bytes,
        algorithm: str = "AES-256-GCM",
        key: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> EncryptResponse:
        """Encrypt data.
        
        Args:
            data: The data to encrypt
            algorithm: Encryption algorithm to use
            key: Optional encryption key (if not provided, a new key will be generated)
            metadata: Optional metadata for the request
            
        Returns:
            EncryptResponse containing encrypted data
            
        Raises:
            CloudRuntimesError: If encryption fails
        """
        pass

    @abstractmethod
    async def encrypt_with_request(
        self,
        request: EncryptRequest,
    ) -> EncryptResponse:
        """Encrypt data using a structured request object.
        
        Args:
            request: EncryptRequest containing all parameters
            
        Returns:
            EncryptResponse containing encrypted data
            
        Raises:
            CloudRuntimesError: If encryption fails
        """
        pass

    @abstractmethod
    async def decrypt(
        self,
        encrypted_data: bytes,
        key: str,
        algorithm: str = "AES-256-GCM",
        metadata: Optional[Dict[str, str]] = None,
    ) -> DecryptResponse:
        """Decrypt data.
        
        Args:
            encrypted_data: The encrypted data to decrypt
            key: The decryption key
            algorithm: Decryption algorithm to use
            metadata: Optional metadata for the request
            
        Returns:
            DecryptResponse containing decrypted data
            
        Raises:
            CloudRuntimesError: If decryption fails
        """
        pass

    @abstractmethod
    async def decrypt_with_request(
        self,
        request: DecryptRequest,
    ) -> DecryptResponse:
        """Decrypt data using a structured request object.
        
        Args:
            request: DecryptRequest containing all parameters
            
        Returns:
            DecryptResponse containing decrypted data
            
        Raises:
            CloudRuntimesError: If decryption fails
        """
        pass

    @abstractmethod
    async def generate_key(
        self,
        algorithm: str = "AES-256",
        key_size: Optional[int] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> GenerateKeyResponse:
        """Generate encryption key.
        
        Args:
            algorithm: Key generation algorithm
            key_size: Optional key size in bits
            metadata: Optional metadata for the request
            
        Returns:
            GenerateKeyResponse containing generated key
            
        Raises:
            CloudRuntimesError: If key generation fails
        """
        pass

    @abstractmethod
    async def generate_key_with_request(
        self,
        request: GenerateKeyRequest,
    ) -> GenerateKeyResponse:
        """Generate key using a structured request object.
        
        Args:
            request: GenerateKeyRequest containing all parameters
            
        Returns:
            GenerateKeyResponse containing generated key
            
        Raises:
            CloudRuntimesError: If key generation fails
        """
        pass

    @abstractmethod
    async def hash_data(
        self,
        data: bytes,
        algorithm: str = "SHA-256",
        salt: Optional[bytes] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> HashResponse:
        """Hash data.
        
        Args:
            data: The data to hash
            algorithm: Hashing algorithm to use
            salt: Optional salt for hashing
            metadata: Optional metadata for the request
            
        Returns:
            HashResponse containing hash result
            
        Raises:
            CloudRuntimesError: If hashing fails
        """
        pass

    @abstractmethod
    async def hash_data_with_request(
        self,
        request: HashRequest,
    ) -> HashResponse:
        """Hash data using a structured request object.
        
        Args:
            request: HashRequest containing all parameters
            
        Returns:
            HashResponse containing hash result
            
        Raises:
            CloudRuntimesError: If hashing fails
        """
        pass

    @abstractmethod
    async def verify_hash(
        self,
        data: bytes,
        hash_value: str,
        algorithm: str = "SHA-256",
        salt: Optional[bytes] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> VerifyHashResponse:
        """Verify hash.
        
        Args:
            data: The original data
            hash_value: The hash to verify against
            algorithm: Hashing algorithm used
            salt: Optional salt used in hashing
            metadata: Optional metadata for the request
            
        Returns:
            VerifyHashResponse containing verification result
            
        Raises:
            CloudRuntimesError: If hash verification fails
        """
        pass

    @abstractmethod
    async def verify_hash_with_request(
        self,
        request: VerifyHashRequest,
    ) -> VerifyHashResponse:
        """Verify hash using a structured request object.
        
        Args:
            request: VerifyHashRequest containing all parameters
            
        Returns:
            VerifyHashResponse containing verification result
            
        Raises:
            CloudRuntimesError: If hash verification fails
        """
        pass

    @abstractmethod
    async def generate_random_bytes(
        self,
        length: int,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bytes:
        """Generate cryptographically secure random bytes.
        
        Args:
            length: Number of random bytes to generate
            metadata: Optional metadata for the request
            
        Returns:
            Random bytes
            
        Raises:
            CloudRuntimesError: If random generation fails
        """
        pass

    @abstractmethod
    async def generate_uuid(
        self,
        version: int = 4,
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Generate UUID.
        
        Args:
            version: UUID version (1, 4, or 5)
            metadata: Optional metadata for the request
            
        Returns:
            Generated UUID string
            
        Raises:
            CloudRuntimesError: If UUID generation fails
        """
        pass

    @abstractmethod
    async def sign_data(
        self,
        data: bytes,
        private_key: str,
        algorithm: str = "RSA-SHA256",
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Sign data with private key.
        
        Args:
            data: The data to sign
            private_key: The private key for signing
            algorithm: Signing algorithm to use
            metadata: Optional metadata for the request
            
        Returns:
            Base64 encoded signature
            
        Raises:
            CloudRuntimesError: If signing fails
        """
        pass

    @abstractmethod
    async def verify_signature(
        self,
        data: bytes,
        signature: str,
        public_key: str,
        algorithm: str = "RSA-SHA256",
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Verify signature with public key.
        
        Args:
            data: The original data
            signature: Base64 encoded signature to verify
            public_key: The public key for verification
            algorithm: Signing algorithm used
            metadata: Optional metadata for the request
            
        Returns:
            True if signature is valid
            
        Raises:
            CloudRuntimesError: If signature verification fails
        """
        pass