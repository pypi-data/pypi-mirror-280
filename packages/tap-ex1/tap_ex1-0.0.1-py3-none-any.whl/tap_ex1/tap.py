"""Ex1 tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_ex1.streams import ProductsStream


STREAM_TYPES = [ProductsStream] #List of custom stream types here
import logging #Import the logging module for log purposes

class TapEx1(Tap):
    """Ex1 tap class."""

    name = "tap-ex1"

    # TODO: Update this section with the actual config values you expect:
    '''config_jsonschema = th.PropertiesList(
        th.Property(
            "auth_token",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "project_ids",
            th.ArrayType(th.StringType),
            required=True,
            description="Project IDs to replicate",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://api.mysample.com",
            description="The url for the API service",
        ),
    ).to_dict()'''

    def discover_streams(self) -> list[ProductsStream]:

        logging.info("Discovering streams............") #Log the message

        return [stream_class(tap=self) for stream_class in STREAM_TYPES]



if __name__ == "__main__":
    TapEx1.cli()
