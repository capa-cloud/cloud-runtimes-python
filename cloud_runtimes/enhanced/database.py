"""
Database runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ..types.enhanced import (
    CreateTableRequest,
    CreateTableResponse,
    DeleteTableRequest,
    DeleteTableResponse,
    GetConnectionRequest,
    GetConnectionResponse,
    InsertRequest,
    InsertResponse,
    QueryRequest,
    QueryResponse,
    UpdateRequest,
    UpdateResponse,
)


class DatabaseRuntimes(ABC):
    """Database Runtimes standard API."""

    @abstractmethod
    async def get_connection(
        self,
        database_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> GetConnectionResponse:
        """Get a database connection.
        
        Args:
            database_name: The name of the database
            metadata: Optional metadata for the request
            
        Returns:
            GetConnectionResponse containing connection information
            
        Raises:
            CloudRuntimesError: If getting connection fails
        """
        pass

    @abstractmethod
    async def get_connection_with_request(
        self,
        request: GetConnectionRequest,
    ) -> GetConnectionResponse:
        """Get a connection using a structured request object.
        
        Args:
            request: GetConnectionRequest containing all parameters
            
        Returns:
            GetConnectionResponse containing connection information
            
        Raises:
            CloudRuntimesError: If getting connection fails
        """
        pass

    @abstractmethod
    async def create_table(
        self,
        database_name: str,
        table_name: str,
        schema: Dict[str, Any],
        metadata: Optional[Dict[str, str]] = None,
    ) -> CreateTableResponse:
        """Create a database table.
        
        Args:
            database_name: The name of the database
            table_name: The name of the table to create
            schema: The table schema definition
            metadata: Optional metadata for the request
            
        Returns:
            CreateTableResponse containing creation result
            
        Raises:
            CloudRuntimesError: If table creation fails
        """
        pass

    @abstractmethod
    async def create_table_with_request(
        self,
        request: CreateTableRequest,
    ) -> CreateTableResponse:
        """Create a table using a structured request object.
        
        Args:
            request: CreateTableRequest containing all parameters
            
        Returns:
            CreateTableResponse containing creation result
            
        Raises:
            CloudRuntimesError: If table creation fails
        """
        pass

    @abstractmethod
    async def delete_table(
        self,
        database_name: str,
        table_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> DeleteTableResponse:
        """Delete a database table.
        
        Args:
            database_name: The name of the database
            table_name: The name of the table to delete
            metadata: Optional metadata for the request
            
        Returns:
            DeleteTableResponse containing deletion result
            
        Raises:
            CloudRuntimesError: If table deletion fails
        """
        pass

    @abstractmethod
    async def delete_table_with_request(
        self,
        request: DeleteTableRequest,
    ) -> DeleteTableResponse:
        """Delete a table using a structured request object.
        
        Args:
            request: DeleteTableRequest containing all parameters
            
        Returns:
            DeleteTableResponse containing deletion result
            
        Raises:
            CloudRuntimesError: If table deletion fails
        """
        pass

    @abstractmethod
    async def insert(
        self,
        database_name: str,
        table_name: str,
        data: Dict[str, Any],
        metadata: Optional[Dict[str, str]] = None,
    ) -> InsertResponse:
        """Insert data into a database table.
        
        Args:
            database_name: The name of the database
            table_name: The name of the table
            data: The data to insert
            metadata: Optional metadata for the request
            
        Returns:
            InsertResponse containing insertion result
            
        Raises:
            CloudRuntimesError: If data insertion fails
        """
        pass

    @abstractmethod
    async def insert_with_request(
        self,
        request: InsertRequest,
    ) -> InsertResponse:
        """Insert data using a structured request object.
        
        Args:
            request: InsertRequest containing all parameters
            
        Returns:
            InsertResponse containing insertion result
            
        Raises:
            CloudRuntimesError: If data insertion fails
        """
        pass

    @abstractmethod
    async def insert_with_data(
        self,
        database_name: str,
        table_name: str,
        data: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> InsertResponse:
        """Insert data with automatic serialization.
        
        Args:
            database_name: The name of the database
            table_name: The name of the table
            data: The data object to insert (will be serialized)
            metadata: Optional metadata for the request
            
        Returns:
            InsertResponse containing insertion result
            
        Raises:
            CloudRuntimesError: If data insertion fails
        """
        pass

    @abstractmethod
    async def query(
        self,
        database_name: str,
        table_name: str,
        query_filter: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> QueryResponse:
        """Query data from a database table.
        
        Args:
            database_name: The name of the database
            table_name: The name of the table
            query_filter: Optional filter conditions
            metadata: Optional metadata for the request
            
        Returns:
            QueryResponse containing query results
            
        Raises:
            CloudRuntimesError: If data query fails
        """
        pass

    @abstractmethod
    async def query_with_request(
        self,
        request: QueryRequest,
    ) -> QueryResponse:
        """Query data using a structured request object.
        
        Args:
            request: QueryRequest containing all parameters
            
        Returns:
            QueryResponse containing query results
            
        Raises:
            CloudRuntimesError: If data query fails
        """
        pass

    @abstractmethod
    async def query_with_data(
        self,
        database_name: str,
        table_name: str,
        data: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> QueryResponse:
        """Query data with automatic filter serialization.
        
        Args:
            database_name: The name of the database
            table_name: The name of the table
            data: The filter object (will be serialized)
            metadata: Optional metadata for the request
            
        Returns:
            QueryResponse containing query results
            
        Raises:
            CloudRuntimesError: If data query fails
        """
        pass

    @abstractmethod
    async def update(
        self,
        database_name: str,
        table_name: str,
        data: Dict[str, Any],
        query_filter: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> UpdateResponse:
        """Update data in a database table.
        
        Args:
            database_name: The name of the database
            table_name: The name of the table
            data: The data to update
            query_filter: Optional filter conditions
            metadata: Optional metadata for the request
            
        Returns:
            UpdateResponse containing update result
            
        Raises:
            CloudRuntimesError: If data update fails
        """
        pass

    @abstractmethod
    async def update_with_request(
        self,
        request: UpdateRequest,
    ) -> UpdateResponse:
        """Update data using a structured request object.
        
        Args:
            request: UpdateRequest containing all parameters
            
        Returns:
            UpdateResponse containing update result
            
        Raises:
            CloudRuntimesError: If data update fails
        """
        pass

    @abstractmethod
    async def update_with_data(
        self,
        database_name: str,
        table_name: str,
        data: Any,
        metadata: Optional[Dict[str, str]] = None,
    ) -> UpdateResponse:
        """Update data with automatic serialization.
        
        Args:
            database_name: The name of the database
            table_name: The name of the table
            data: The data object to update (will be serialized)
            metadata: Optional metadata for the request
            
        Returns:
            UpdateResponse containing update result
            
        Raises:
            CloudRuntimesError: If data update fails
        """
        pass

    @abstractmethod
    async def begin_transaction(
        self,
        database_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> str:
        """Begin a database transaction.
        
        Args:
            database_name: The name of the database
            metadata: Optional metadata for the request
            
        Returns:
            Transaction ID
            
        Raises:
            CloudRuntimesError: If beginning transaction fails
        """
        pass

    @abstractmethod
    async def commit_transaction(
        self,
        transaction_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Commit a database transaction.
        
        Args:
            transaction_id: The transaction ID
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If committing transaction fails
        """
        pass

    @abstractmethod
    async def rollback_transaction(
        self,
        transaction_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Rollback a database transaction.
        
        Args:
            transaction_id: The transaction ID
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If rolling back transaction fails
        """
        pass

    @abstractmethod
    async def execute_sql(
        self,
        database_name: str,
        sql: str,
        parameters: Optional[List[Any]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> QueryResponse:
        """Execute raw SQL query.
        
        Args:
            database_name: The name of the database
            sql: The SQL query to execute
            parameters: Optional query parameters
            metadata: Optional metadata for the request
            
        Returns:
            QueryResponse containing query results
            
        Raises:
            CloudRuntimesError: If SQL execution fails
        """
        pass

    @abstractmethod
    async def list_tables(
        self,
        database_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> List[str]:
        """List all tables in a database.
        
        Args:
            database_name: The name of the database
            metadata: Optional metadata for the request
            
        Returns:
            List of table names
            
        Raises:
            CloudRuntimesError: If listing tables fails
        """
        pass

    @abstractmethod
    async def get_table_schema(
        self,
        database_name: str,
        table_name: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Get the schema of a table.
        
        Args:
            database_name: The name of the database
            table_name: The name of the table
            metadata: Optional metadata for the request
            
        Returns:
            Dictionary containing table schema
            
        Raises:
            CloudRuntimesError: If getting table schema fails
        """
        pass