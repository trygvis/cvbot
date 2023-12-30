# coding: utf-8

"""
    CVPartner

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from scienta.cvpartner_api.models.project_role import ProjectRole
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProjectExperience(BaseModel):
    """
    ProjectExperience
    """ # noqa: E501
    order: Optional[StrictInt] = None
    starred: Optional[StrictBool] = None
    disabled: Optional[StrictBool] = None
    version: Optional[StrictInt] = None
    external_unique_id: Optional[StrictStr] = None
    owner_updated_at: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    area_amt: Optional[StrictStr] = None
    area_unit: Optional[StrictStr] = None
    customer: Optional[Dict[str, Any]] = None
    customer_anonymized: Optional[Dict[str, Any]] = None
    customer_description: Optional[Dict[str, Any]] = None
    description: Optional[Dict[str, Any]] = None
    long_description: Optional[Dict[str, Any]] = None
    industry: Optional[Dict[str, Any]] = None
    year_from: Optional[StrictStr] = None
    month_from: Optional[StrictStr] = None
    year_to: Optional[StrictStr] = None
    month_to: Optional[StrictStr] = None
    roles: Optional[List[ProjectRole]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["order", "starred", "disabled", "version", "external_unique_id", "owner_updated_at", "created_at", "updated_at", "area_amt", "area_unit", "customer", "customer_anonymized", "customer_description", "description", "long_description", "industry", "year_from", "month_from", "year_to", "month_to", "roles"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProjectExperience from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "additional_properties",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProjectExperience from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "order": obj.get("order"),
            "starred": obj.get("starred"),
            "disabled": obj.get("disabled"),
            "version": obj.get("version"),
            "external_unique_id": obj.get("external_unique_id"),
            "owner_updated_at": obj.get("owner_updated_at"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "area_amt": obj.get("area_amt"),
            "area_unit": obj.get("area_unit"),
            "customer": obj.get("customer"),
            "customer_anonymized": obj.get("customer_anonymized"),
            "customer_description": obj.get("customer_description"),
            "description": obj.get("description"),
            "long_description": obj.get("long_description"),
            "industry": obj.get("industry"),
            "year_from": obj.get("year_from"),
            "month_from": obj.get("month_from"),
            "year_to": obj.get("year_to"),
            "month_to": obj.get("month_to"),
            "roles": [ProjectRole.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

