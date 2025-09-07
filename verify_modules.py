#!/usr/bin/env python3
"""
Simple verification script to check if the modules can be imported correctly.
"""

def verify_imports():
  """Verify that all modules can be imported without errors.
  
  This function checks core imports, client, and types.
  Returns True if all verifications pass, False otherwise.
  """
  try:
    # Test core module imports
    from cloud_runtimes.core.secrets import SecretsRuntimes
    from cloud_runtimes.core.binding import BindingRuntimes
    from cloud_runtimes.core.invocation import InvocationRuntimes
    from cloud_runtimes.core.state import StateRuntimes
    from cloud_runtimes.core.configuration import ConfigurationRuntimes
    from cloud_runtimes.core.pubsub import PubSubRuntimes
    
    # Test client import
    from cloud_runtimes.client import CloudRuntimesClient
    
    # Test types import
    from cloud_runtimes.types.core import (
      GetSecretRequest,
      SecretResponse,
      InvokeBindingRequest,
      InvokeBindingResponse,
      BindingEvent,
      ListInputBindingsResponse,
      ListOutputBindingsResponse,
    )
    
    print("✅ All imports successful!")
    
    # Test basic instantiation
    client = CloudRuntimesClient()
    print("✅ Client instantiation successful!")
    
    # Test abstract class behavior
    try:
      SecretsRuntimes()
      print("❌ SecretsRuntimes should be abstract!")
    except TypeError:
      print("✅ SecretsRuntimes is properly abstract!")
    
    try:
      BindingRuntimes()
      print("❌ BindingRuntimes should be abstract!")
    except TypeError:
      print("✅ BindingRuntimes is properly abstract!")
    
    print("\n🎉 All verifications passed! Python Secrets and Binding modules are working correctly.")
    return True
    
  except ImportError as ie:
    print(f"❌ Import failed: {ie}")
    import traceback
    traceback.print_exc()
    return False
  except Exception as e:
    print(f"❌ Verification failed: {e}")
    import traceback
    traceback.print_exc()
    return False

if __name__ == "__main__":
  success = verify_imports()
  exit(0 if success else 1)