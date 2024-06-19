from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.completed_job_flow_status_modules_item_type import CompletedJobFlowStatusModulesItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.completed_job_flow_status_modules_item_approvers_item import (
        CompletedJobFlowStatusModulesItemApproversItem,
    )
    from ..models.completed_job_flow_status_modules_item_branch_chosen import (
        CompletedJobFlowStatusModulesItemBranchChosen,
    )
    from ..models.completed_job_flow_status_modules_item_branchall import CompletedJobFlowStatusModulesItemBranchall
    from ..models.completed_job_flow_status_modules_item_iterator import CompletedJobFlowStatusModulesItemIterator


T = TypeVar("T", bound="CompletedJobFlowStatusModulesItem")


@_attrs_define
class CompletedJobFlowStatusModulesItem:
    """
    Attributes:
        type (CompletedJobFlowStatusModulesItemType):
        id (Union[Unset, str]):
        job (Union[Unset, str]):
        count (Union[Unset, int]):
        iterator (Union[Unset, CompletedJobFlowStatusModulesItemIterator]):
        flow_jobs (Union[Unset, List[str]]):
        branch_chosen (Union[Unset, CompletedJobFlowStatusModulesItemBranchChosen]):
        branchall (Union[Unset, CompletedJobFlowStatusModulesItemBranchall]):
        approvers (Union[Unset, List['CompletedJobFlowStatusModulesItemApproversItem']]):
        failed_retries (Union[Unset, List[str]]):
    """

    type: CompletedJobFlowStatusModulesItemType
    id: Union[Unset, str] = UNSET
    job: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    iterator: Union[Unset, "CompletedJobFlowStatusModulesItemIterator"] = UNSET
    flow_jobs: Union[Unset, List[str]] = UNSET
    branch_chosen: Union[Unset, "CompletedJobFlowStatusModulesItemBranchChosen"] = UNSET
    branchall: Union[Unset, "CompletedJobFlowStatusModulesItemBranchall"] = UNSET
    approvers: Union[Unset, List["CompletedJobFlowStatusModulesItemApproversItem"]] = UNSET
    failed_retries: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id
        job = self.job
        count = self.count
        iterator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.iterator, Unset):
            iterator = self.iterator.to_dict()

        flow_jobs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.flow_jobs, Unset):
            flow_jobs = self.flow_jobs

        branch_chosen: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branch_chosen, Unset):
            branch_chosen = self.branch_chosen.to_dict()

        branchall: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branchall, Unset):
            branchall = self.branchall.to_dict()

        approvers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.approvers, Unset):
            approvers = []
            for approvers_item_data in self.approvers:
                approvers_item = approvers_item_data.to_dict()

                approvers.append(approvers_item)

        failed_retries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.failed_retries, Unset):
            failed_retries = self.failed_retries

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if job is not UNSET:
            field_dict["job"] = job
        if count is not UNSET:
            field_dict["count"] = count
        if iterator is not UNSET:
            field_dict["iterator"] = iterator
        if flow_jobs is not UNSET:
            field_dict["flow_jobs"] = flow_jobs
        if branch_chosen is not UNSET:
            field_dict["branch_chosen"] = branch_chosen
        if branchall is not UNSET:
            field_dict["branchall"] = branchall
        if approvers is not UNSET:
            field_dict["approvers"] = approvers
        if failed_retries is not UNSET:
            field_dict["failed_retries"] = failed_retries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.completed_job_flow_status_modules_item_approvers_item import (
            CompletedJobFlowStatusModulesItemApproversItem,
        )
        from ..models.completed_job_flow_status_modules_item_branch_chosen import (
            CompletedJobFlowStatusModulesItemBranchChosen,
        )
        from ..models.completed_job_flow_status_modules_item_branchall import CompletedJobFlowStatusModulesItemBranchall
        from ..models.completed_job_flow_status_modules_item_iterator import CompletedJobFlowStatusModulesItemIterator

        d = src_dict.copy()
        type = CompletedJobFlowStatusModulesItemType(d.pop("type"))

        id = d.pop("id", UNSET)

        job = d.pop("job", UNSET)

        count = d.pop("count", UNSET)

        _iterator = d.pop("iterator", UNSET)
        iterator: Union[Unset, CompletedJobFlowStatusModulesItemIterator]
        if isinstance(_iterator, Unset):
            iterator = UNSET
        else:
            iterator = CompletedJobFlowStatusModulesItemIterator.from_dict(_iterator)

        flow_jobs = cast(List[str], d.pop("flow_jobs", UNSET))

        _branch_chosen = d.pop("branch_chosen", UNSET)
        branch_chosen: Union[Unset, CompletedJobFlowStatusModulesItemBranchChosen]
        if isinstance(_branch_chosen, Unset):
            branch_chosen = UNSET
        else:
            branch_chosen = CompletedJobFlowStatusModulesItemBranchChosen.from_dict(_branch_chosen)

        _branchall = d.pop("branchall", UNSET)
        branchall: Union[Unset, CompletedJobFlowStatusModulesItemBranchall]
        if isinstance(_branchall, Unset):
            branchall = UNSET
        else:
            branchall = CompletedJobFlowStatusModulesItemBranchall.from_dict(_branchall)

        approvers = []
        _approvers = d.pop("approvers", UNSET)
        for approvers_item_data in _approvers or []:
            approvers_item = CompletedJobFlowStatusModulesItemApproversItem.from_dict(approvers_item_data)

            approvers.append(approvers_item)

        failed_retries = cast(List[str], d.pop("failed_retries", UNSET))

        completed_job_flow_status_modules_item = cls(
            type=type,
            id=id,
            job=job,
            count=count,
            iterator=iterator,
            flow_jobs=flow_jobs,
            branch_chosen=branch_chosen,
            branchall=branchall,
            approvers=approvers,
            failed_retries=failed_retries,
        )

        completed_job_flow_status_modules_item.additional_properties = d
        return completed_job_flow_status_modules_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
