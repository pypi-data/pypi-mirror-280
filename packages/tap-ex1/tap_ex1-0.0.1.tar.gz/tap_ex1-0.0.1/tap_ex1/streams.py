"""Stream type classes for tap-ex1."""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_ex1.client import Ex1Stream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = importlib_resources.files(__package__) / "schemas"
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.


class ProductsStream(Ex1Stream):
    """Define custom stream."""

    name = "products"
    path = "/products"
    primary_keys: t.ClassVar[list[str]] = ["id"]  
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property("id",th.NumberType),
        th.Property("title", th.StringType),
        th.Property("description", th.StringType),
        th.Property("category", th.StringType),
        th.Property("price", th.NumberType),
        th.Property("discountPercentage", th.NumberType),
        th.Property("rating", th.NumberType),
        th.Property("stock", th.NumberType),
        th.Property(
            "tags",
            th.ArrayType(
                th.StringType
            )
        ),
        th.Property("brand", th.StringType),
        th.Property("sku", th.StringType),
        th.Property("weight", th.NumberType),
        th.Property(
            "dimensions",
            th.ObjectType(
                th.Property("width", th.NumberType),
                th.Property("height", th.NumberType),
                th.Property("depth", th.NumberType),
            )
        ),     
        th.Property("warrantyInformation", th.StringType),
        th.Property("shippingInformation", th.StringType),
        th.Property("availabilityStatus", th.StringType),
        th.Property(
            "reviews",
            th.ArrayType(
                th.ObjectType(
                    th.Property("rating", th.NumberType),
                    th.Property("comment", th.StringType),
                    th.Property("date", th.DateTimeType),
                    th.Property("reviewerName", th.StringType),
                    th.Property("reviewerEmail", th.EmailType),
                )
            )
        ),
        th.Property("returnPolicy", th.StringType),
        th.Property("minimumOrderQuantity", th.NumberType),
        th.Property(
            "meta",
            th.ObjectType(
                th.Property("createdAt", th.DateTimeType),
                th.Property("updatedAt", th.DateTimeType),
                th.Property("barcode", th.StringType),
                th.Property("qrCode", th.StringType),
            )
        ),  
        th.Property("images", 
            th.ArrayType(
                th.StringType
            )
        ),
        th.Property("thumbnail", th.StringType)
    ).to_dict()


'''class GroupsStream(Ex1Stream):
    """Define custom stream."""

    name = "groups"
    path = "/groups"
    primary_keys: t.ClassVar[list[str]] = ["id"]
    replication_key = "modified"
    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("id", th.StringType),
        th.Property("modified", th.DateTimeType),
    ).to_dict()'''
