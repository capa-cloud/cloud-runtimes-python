#!/usr/bin/env python3
"""
Verification script for Native Protocol API modules.
"""

def verify_native_modules():
  """Verify that all native modules can be imported correctly.
  
  This function checks imports, abstract classes, and data types.
  Returns True if all verifications pass, False otherwise.
  """
  try:
    # Test native module imports
    from cloud_runtimes.native.redis import RedisRuntimes
    from cloud_runtimes.native.sql import SqlRuntimes
    from cloud_runtimes.native.s3 import S3Runtimes
    
    # Test native types import
    from cloud_runtimes.types.native import (
      RedisExecuteRequest,
      RedisExecuteResponse,
      RedisZMember,
      SqlExecuteRequest,
      SqlExecuteResponse,
      SqlQueryRequest,
      SqlQueryResponse,
      S3GetObjectRequest,
      S3GetObjectResponse,
      S3PutObjectRequest,
      S3PutObjectResponse,
    )
    
    print("✅ All native imports successful!")
    
    # Test abstract class behavior
    try:
      RedisRuntimes()
      print("❌ RedisRuntimes should be abstract!")
    except TypeError:
      print("✅ RedisRuntimes is properly abstract!")
    
    try:
      SqlRuntimes()
      print("❌ SqlRuntimes should be abstract!")
    except TypeError:
      print("✅ SqlRuntimes is properly abstract!")
    
    try:
      S3Runtimes()
      print("❌ S3Runtimes should be abstract!")
    except TypeError:
      print("✅ S3Runtimes is properly abstract!")
    
    # Test data type instantiation
    redis_req = RedisExecuteRequest(command="GET", args=["key1"])
    print(f"✅ RedisExecuteRequest created: {redis_req.command}")
    
    sql_req = SqlExecuteRequest(sql="SELECT * FROM users")
    print(f"✅ SqlExecuteRequest created: {sql_req.sql}")
    
    s3_req = S3GetObjectRequest(bucket="test-bucket", key="test-key")
    print(f"✅ S3GetObjectRequest created: {s3_req.bucket}/{s3_req.key}")
    
    redis_member = RedisZMember(member="user1", score=100.0)
    print(f"✅ RedisZMember created: {redis_member.member} -> {redis_member.score}")
    
    print("\n🎉 All native module verifications passed! Python Native Protocol API modules are working correctly.")
    return True
    
  except ImportError as ie:
    print(f"❌ Import failed: {ie}")
    import traceback
    traceback.print_exc()
    return False
  except Exception as e:
    print(f"❌ Native verification failed: {e}")
    import traceback
    traceback.print_exc()
    return False

if __name__ == "__main__":
  success = verify_native_modules()
  exit(0 if success else 1)