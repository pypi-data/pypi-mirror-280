"""
Main interface for ivs-realtime service.

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ivs_realtime import (
        Client,
        IvsrealtimeClient,
    )

    session = Session()
    client: IvsrealtimeClient = session.client("ivs-realtime")
    ```
"""

from .client import IvsrealtimeClient

Client = IvsrealtimeClient

__all__ = ("Client", "IvsrealtimeClient")
