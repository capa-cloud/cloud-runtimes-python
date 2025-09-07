"""
Telemetry runtime implementation.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from ..types.enhanced import (
    CreateSpanRequest,
    CreateSpanResponse,
    GetMetricsRequest,
    GetMetricsResponse,
    IncrementCounterRequest,
    RecordHistogramRequest,
    RecordMetricRequest,
    SetGaugeRequest,
    TraceContext,
)


class TelemetryRuntimes(ABC):
    """Telemetry Runtimes standard API."""

    @abstractmethod
    async def with_trace_id(
        self,
        trace_id: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        """Add existing trace ID to the outgoing context.
        
        Args:
            trace_id: The trace ID to add
            metadata: Optional metadata for the request
            
        Returns:
            Updated context with trace ID
            
        Raises:
            CloudRuntimesError: If adding trace ID fails
        """
        pass

    @abstractmethod
    async def with_auth_token(
        self,
        token: str,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Set auth API token on the instantiated client.
        
        Args:
            token: The authentication token
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If setting auth token fails
        """
        pass

    @abstractmethod
    async def build_tracer(
        self,
        tracer_name: str,
        version: Optional[str] = None,
        schema_url: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Any:
        """Build a tracer with the given name and optional version/schema.
        
        Args:
            tracer_name: The name of the tracer
            version: Optional version of the tracer
            schema_url: Optional schema URL
            metadata: Optional metadata for the request
            
        Returns:
            Tracer instance
            
        Raises:
            CloudRuntimesError: If building tracer fails
        """
        pass

    @abstractmethod
    async def get_context_propagators(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Any:
        """Get context propagators.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            Context propagators instance
            
        Raises:
            CloudRuntimesError: If getting propagators fails
        """
        pass

    @abstractmethod
    async def build_meter(
        self,
        meter_name: str,
        version: Optional[str] = None,
        schema_url: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> Any:
        """Build a meter with the given name and optional version/schema.
        
        Args:
            meter_name: The name of the meter
            version: Optional version of the meter
            schema_url: Optional schema URL
            metadata: Optional metadata for the request
            
        Returns:
            Meter instance
            
        Raises:
            CloudRuntimesError: If building meter fails
        """
        pass

    @abstractmethod
    async def record_metric(
        self,
        name: str,
        value: float,
        metric_type: str,
        unit: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Record a metric value.
        
        Args:
            name: The metric name
            value: The metric value
            metric_type: The type of metric (counter, gauge, histogram)
            unit: Optional unit of measurement
            tags: Optional metric tags
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If recording metric fails
        """
        pass

    @abstractmethod
    async def record_metric_with_request(
        self,
        request: RecordMetricRequest,
    ) -> None:
        """Record a metric using a structured request object.
        
        Args:
            request: RecordMetricRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If recording metric fails
        """
        pass

    @abstractmethod
    async def increment_counter(
        self,
        name: str,
        value: float = 1.0,
        tags: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Increment a counter metric.
        
        Args:
            name: The counter name
            value: The increment value (default 1.0)
            tags: Optional counter tags
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If incrementing counter fails
        """
        pass

    @abstractmethod
    async def increment_counter_with_request(
        self,
        request: IncrementCounterRequest,
    ) -> None:
        """Increment a counter using a structured request object.
        
        Args:
            request: IncrementCounterRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If incrementing counter fails
        """
        pass

    @abstractmethod
    async def record_histogram(
        self,
        name: str,
        value: float,
        unit: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Record a histogram value.
        
        Args:
            name: The histogram name
            value: The histogram value
            unit: Optional unit of measurement
            tags: Optional histogram tags
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If recording histogram fails
        """
        pass

    @abstractmethod
    async def record_histogram_with_request(
        self,
        request: RecordHistogramRequest,
    ) -> None:
        """Record a histogram using a structured request object.
        
        Args:
            request: RecordHistogramRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If recording histogram fails
        """
        pass

    @abstractmethod
    async def set_gauge(
        self,
        name: str,
        value: float,
        unit: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> None:
        """Set a gauge metric value.
        
        Args:
            name: The gauge name
            value: The gauge value
            unit: Optional unit of measurement
            tags: Optional gauge tags
            metadata: Optional metadata for the request
            
        Raises:
            CloudRuntimesError: If setting gauge fails
        """
        pass

    @abstractmethod
    async def set_gauge_with_request(
        self,
        request: SetGaugeRequest,
    ) -> None:
        """Set a gauge using a structured request object.
        
        Args:
            request: SetGaugeRequest containing all parameters
            
        Raises:
            CloudRuntimesError: If setting gauge fails
        """
        pass

    @abstractmethod
    async def get_metrics(
        self,
        names: Optional[List[str]] = None,
        prefix: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> GetMetricsResponse:
        """Get current metric values.
        
        Args:
            names: Optional list of metric names to retrieve
            prefix: Optional prefix to filter metrics
            tags: Optional tags to filter metrics
            start_time: Optional start time for time-based metrics
            end_time: Optional end time for time-based metrics
            metadata: Optional metadata for the request
            
        Returns:
            GetMetricsResponse containing metric data
            
        Raises:
            CloudRuntimesError: If getting metrics fails
        """
        pass

    @abstractmethod
    async def get_metrics_with_request(
        self,
        request: GetMetricsRequest,
    ) -> GetMetricsResponse:
        """Get metrics using a structured request object.
        
        Args:
            request: GetMetricsRequest containing all parameters
            
        Returns:
            GetMetricsResponse containing metric data
            
        Raises:
            CloudRuntimesError: If getting metrics fails
        """
        pass

    @abstractmethod
    async def create_span(
        self,
        operation_name: str,
        parent_span_id: Optional[str] = None,
        trace_id: Optional[str] = None,
        start_time: Optional[int] = None,
        tags: Optional[Dict[str, str]] = None,
        metadata: Optional[Dict[str, str]] = None,
    ) -> CreateSpanResponse:
        """Create a new span.
        
        Args:
            operation_name: The name of the operation
            parent_span_id: Optional parent span ID
            trace_id: Optional trace ID
            start_time: Optional start time
            tags: Optional span tags
            metadata: Optional metadata for the request
            
        Returns:
            CreateSpanResponse containing span information
            
        Raises:
            CloudRuntimesError: If creating span fails
        """
        pass

    @abstractmethod
    async def create_span_with_request(
        self,
        request: CreateSpanRequest,
    ) -> CreateSpanResponse:
        """Create a span using a structured request object.
        
        Args:
            request: CreateSpanRequest containing all parameters
            
        Returns:
            CreateSpanResponse containing span information
            
        Raises:
            CloudRuntimesError: If creating span fails
        """
        pass

    @abstractmethod
    async def get_trace_context(
        self,
        metadata: Optional[Dict[str, str]] = None,
    ) -> TraceContext:
        """Get the current trace context.
        
        Args:
            metadata: Optional metadata for the request
            
        Returns:
            TraceContext containing current trace information
            
        Raises:
            CloudRuntimesError: If getting trace context fails
        """
        pass

    @abstractmethod
    async def inject_trace_context(
        self,
        headers: Dict[str, str],
        metadata: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        """Inject trace context into headers.
        
        Args:
            headers: The headers to inject trace context into
            metadata: Optional metadata for the request
            
        Returns:
            Updated headers with trace context
            
        Raises:
            CloudRuntimesError: If injecting trace context fails
        """
        pass

    @abstractmethod
    async def extract_trace_context(
        self,
        headers: Dict[str, str],
        metadata: Optional[Dict[str, str]] = None,
    ) -> TraceContext:
        """Extract trace context from headers.
        
        Args:
            headers: The headers to extract trace context from
            metadata: Optional metadata for the request
            
        Returns:
            TraceContext extracted from headers
            
        Raises:
            CloudRuntimesError: If extracting trace context fails
        """
        pass