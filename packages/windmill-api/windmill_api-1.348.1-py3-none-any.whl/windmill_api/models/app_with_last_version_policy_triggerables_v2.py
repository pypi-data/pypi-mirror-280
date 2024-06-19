from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_with_last_version_policy_triggerables_v2_additional_property import (
        AppWithLastVersionPolicyTriggerablesV2AdditionalProperty,
    )


T = TypeVar("T", bound="AppWithLastVersionPolicyTriggerablesV2")


@_attrs_define
class AppWithLastVersionPolicyTriggerablesV2:
    """ """

    additional_properties: Dict[str, "AppWithLastVersionPolicyTriggerablesV2AdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.app_with_last_version_policy_triggerables_v2_additional_property import (
            AppWithLastVersionPolicyTriggerablesV2AdditionalProperty,
        )

        d = src_dict.copy()
        app_with_last_version_policy_triggerables_v2 = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AppWithLastVersionPolicyTriggerablesV2AdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        app_with_last_version_policy_triggerables_v2.additional_properties = additional_properties
        return app_with_last_version_policy_triggerables_v2

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "AppWithLastVersionPolicyTriggerablesV2AdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "AppWithLastVersionPolicyTriggerablesV2AdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
