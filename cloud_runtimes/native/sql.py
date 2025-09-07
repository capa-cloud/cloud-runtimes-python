"""
SQL Native Protocol runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ..types.native import (
    SqlBeginTxRequest,
    SqlExecutePreparedRequest,
    SqlExecuteRequest,
    SqlExecuteResponse,
    SqlPrepareRequest,
    SqlPrepareResponse,
    SqlQueryRequest,
    SqlQueryResponse,
    SqlRowResponse,
    SqlTxResponse,
)


class SqlRuntimes(ABC):
    """SQL Native Protocol Runtimes standard API."""

    @abstractmethod
    async def sql_execute(
        self,
        sql: str,
        parameters: Optional[List[Any]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SqlExecuteResponse:
        """Execute SQL statement.
        
        Args:
            sql: The SQL statement to execute
            parameters: Optional parameters for the SQL statement
            metadata: Optional metadata for the request
            
        Returns:
            SqlExecuteResponse containing execution result
            
        Raises:
            CloudRuntimesError: If the SQL execution fails
        """
        pass

    @abstractmethod
    async def sql_execute_with_request(
        self,
        request: SqlExecuteRequest,
    ) -> SqlExecuteResponse:
        """Execute SQL statement using a structured request object.
        
        Args:
            request: SqlExecuteRequest containing all parameters
            
        Returns:
            SqlExecuteResponse containing execution result
            
        Raises:
            CloudRuntimesError: If the SQL execution fails
        """
        pass

    @abstractmethod
    async def sql_query(
        self,
        sql: str,
        parameters: Optional[List[Any]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SqlQueryResponse:
        """Execute SQL query.
        
        Args:
            sql: The SQL query to execute
            parameters: Optional parameters for the SQL query
            metadata: Optional metadata for the request
            
        Returns:
            SqlQueryResponse containing query results
            
        Raises:
            CloudRuntimesError: If the SQL query fails
        """
        pass

    @abstractmethod
    async def sql_query_with_request(
        self,
        request: SqlQueryRequest,
    ) -> SqlQueryResponse:
        """Execute SQL query using a structured request object.
        
        Args:
            request: SqlQueryRequest containing all parameters
            
        Returns:
            SqlQueryResponse containing query results
            
        Raises:
            CloudRuntimesError: If the SQL query fails
        """
        pass

    @abstractmethod
    async def sql_query_row(
        self,
        sql: str,
        parameters: Optional[List[Any]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SqlRowResponse:
        """Execute SQL query and return single row.
        
        Args:
            sql: The SQL query to execute
            parameters: Optional parameters for the SQL query
            metadata: Optional metadata for the request
            
        Returns:
            SqlRowResponse containing single row result
            
        Raises:
            CloudRuntimesError: If the SQL query fails
        """
        pass

    @abstractmethod
    async def sql_query_row_with_request(
        self,
        request: SqlQueryRequest,
    ) -> SqlRowResponse:
        """Execute SQL query for single row using a structured request object.
        
        Args:
            request: SqlQueryRequest containing all parameters
            
        Returns:
            SqlRowResponse containing single row result
            
        Raises:
            CloudRuntimesError: If the SQL query fails
        """
        pass

    @abstractmethod
    async def sql_begin_tx(
        self,
        isolation_level: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SqlTxResponse:
        """Begin a transaction.
        
        Args:
            isolation_level: Optional transaction isolation level
            metadata: Optional metadata for the request
            
        Returns:
            SqlTxResponse containing transaction information
            
        Raises:
            CloudRuntimesError: If beginning transaction fails
        """
        pass

    @abstractmethod
    async def sql_begin_tx_with_request(
        self,
        request: SqlBeginTxRequest,
    ) -> SqlTxResponse:
        """Begin a transaction using a structured request object.
        
        Args:
            request: SqlBeginTxRequest containing all parameters
            
        Returns:
            SqlTxResponse containing transaction information
            
        Raises:
            CloudRuntimesError: If beginning transaction fails
        """
        pass

    @abstractmethod
    async def sql_commit_tx(
        self,
        tx_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Commit a transaction.
        
        Args:
            tx_id: The transaction ID to commit
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If committing transaction fails
        """
        pass

    @abstractmethod
    async def sql_rollback_tx(
        self,
        tx_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Roll back a transaction.
        
        Args:
            tx_id: The transaction ID to roll back
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If rolling back transaction fails
        """
        pass

    @abstractmethod
    async def sql_prepare(
        self,
        sql: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SqlPrepareResponse:
        """Prepare a SQL statement.
        
        Args:
            sql: The SQL statement to prepare
            metadata: Optional metadata for the request
            
        Returns:
            SqlPrepareResponse containing prepared statement information
            
        Raises:
            CloudRuntimesError: If preparing statement fails
        """
        pass

    @abstractmethod
    async def sql_prepare_with_request(
        self,
        request: SqlPrepareRequest,
    ) -> SqlPrepareResponse:
        """Prepare a SQL statement using a structured request object.
        
        Args:
            request: SqlPrepareRequest containing all parameters
            
        Returns:
            SqlPrepareResponse containing prepared statement information
            
        Raises:
            CloudRuntimesError: If preparing statement fails
        """
        pass

    @abstractmethod
    async def sql_execute_prepared(
        self,
        stmt_id: str,
        parameters: Optional[List[Any]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> SqlExecuteResponse:
        """Execute a prepared statement.
        
        Args:
            stmt_id: The prepared statement ID
            parameters: Optional parameters for the prepared statement
            metadata: Optional metadata for the request
            
        Returns:
            SqlExecuteResponse containing execution result
            
        Raises:
            CloudRuntimesError: If executing prepared statement fails
        """
        pass

    @abstractmethod
    async def sql_execute_prepared_with_request(
        self,
        request: SqlExecutePreparedRequest,
    ) -> SqlExecuteResponse:
        """Execute a prepared statement using a structured request object.
        
        Args:
            request: SqlExecutePreparedRequest containing all parameters
            
        Returns:
            SqlExecuteResponse containing execution result
            
        Raises:
            CloudRuntimesError: If executing prepared statement fails
        """
        pass

    @abstractmethod
    async def sql_close_prepared(
        self,
        stmt_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Close a prepared statement.
        
        Args:
            stmt_id: The prepared statement ID to close
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If closing prepared statement fails
        """
        pass

    @abstractmethod
    async def sql_get_connection_info(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Get database connection information.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            Dictionary containing connection information
            
        Raises:
            CloudRuntimesError: If getting connection info fails
        """
        pass

    @abstractmethod
    async def sql_ping(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> bool:
        """Ping the database connection.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            True if connection is alive
            
        Raises:
            CloudRuntimesError: If ping fails
        """
        pass

    @abstractmethod
    async def sql_get_schema(
        self,
        table_name: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Get database or table schema information.
        
        Args:
            table_name: Optional table name to get schema for
            metadata: Optional metadata for the request
            
        Returns:
            Dictionary containing schema information
            
        Raises:
            CloudRuntimesError: If getting schema fails
        """
        pass