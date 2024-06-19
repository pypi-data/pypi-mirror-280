"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)


DEFINITION = """
query Templatev1 {
  template_v1 {
    name
    autoApproved
    condition
    patch {
      path
      identifier
    }
    targetPath
    template
    templateTest {
      name
      variables
      current
      expectedOutput
      expectedTargetPath
      expectedToRender
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class TemplatePatchV1(ConfiguredBaseModel):
    path: str = Field(..., alias="path")
    identifier: Optional[str] = Field(..., alias="identifier")


class TemplateTestV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    variables: Optional[Json] = Field(..., alias="variables")
    current: Optional[str] = Field(..., alias="current")
    expected_output: str = Field(..., alias="expectedOutput")
    expected_target_path: Optional[str] = Field(..., alias="expectedTargetPath")
    expected_to_render: Optional[bool] = Field(..., alias="expectedToRender")


class TemplateV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    auto_approved: Optional[bool] = Field(..., alias="autoApproved")
    condition: Optional[str] = Field(..., alias="condition")
    patch: Optional[TemplatePatchV1] = Field(..., alias="patch")
    target_path: str = Field(..., alias="targetPath")
    template: str = Field(..., alias="template")
    template_test: list[TemplateTestV1] = Field(..., alias="templateTest")


class Templatev1QueryData(ConfiguredBaseModel):
    template_v1: Optional[list[TemplateV1]] = Field(..., alias="template_v1")


def query(query_func: Callable, **kwargs: Any) -> Templatev1QueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        Templatev1QueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return Templatev1QueryData(**raw_data)
