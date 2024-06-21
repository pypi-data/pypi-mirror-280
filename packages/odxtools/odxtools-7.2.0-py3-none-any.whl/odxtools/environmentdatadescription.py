# SPDX-License-Identifier: MIT
from dataclasses import dataclass
from typing import Any, Dict, List, Optional
from xml.etree import ElementTree

from typing_extensions import override

from .complexdop import ComplexDop
from .decodestate import DecodeState
from .encodestate import EncodeState
from .environmentdata import EnvironmentData
from .exceptions import odxraise, odxrequire
from .odxlink import OdxDocFragment, OdxLinkDatabase, OdxLinkId, OdxLinkRef
from .odxtypes import ParameterValue
from .snrefcontext import SnRefContext
from .utils import dataclass_fields_asdict


@dataclass
class EnvironmentDataDescription(ComplexDop):
    """This class represents environment data descriptions

    An environment data description provides a list of all environment
    data objects that are potentially applicable to decode a given
    response. (If a given environment data object is applicable
    depends on the value of the DtcDOP that is associated with it.)

    """

    # in ODX 2.0.0, ENV-DATAS seems to be a mandatory
    # sub-element of ENV-DATA-DESC, in ODX 2.2 it is not
    # present
    env_datas: List[EnvironmentData]
    env_data_refs: List[OdxLinkRef]
    param_snref: Optional[str]
    param_snpathref: Optional[str]

    def __post_init__(self) -> None:
        self.bit_length = None

    @staticmethod
    def from_et(et_element: ElementTree.Element,
                doc_frags: List[OdxDocFragment]) -> "EnvironmentDataDescription":
        """Reads Environment Data Description from Diag Layer."""
        kwargs = dataclass_fields_asdict(ComplexDop.from_et(et_element, doc_frags))

        param_snref = None
        if (param_snref_elem := et_element.find("PARAM-SNREF")) is not None:
            param_snref = odxrequire(param_snref_elem.get("SHORT-NAME"))
        param_snpathref = None
        if (param_snpathref_elem := et_element.find("PARAM-SNPATHREF")) is not None:
            param_snpathref = odxrequire(param_snpathref_elem.get("SHORT-NAME-PATH"))
        env_data_refs = [
            odxrequire(OdxLinkRef.from_et(env_data_ref, doc_frags))
            for env_data_ref in et_element.iterfind("ENV-DATA-REFS/ENV-DATA-REF")
        ]

        # ODX 2.0.0 says ENV-DATA-DESC could contain a list of ENV-DATAS
        env_datas = [
            EnvironmentData.from_et(env_data_elem, doc_frags)
            for env_data_elem in et_element.iterfind("ENV-DATAS/ENV-DATA")
        ]

        return EnvironmentDataDescription(
            param_snref=param_snref,
            param_snpathref=param_snpathref,
            env_data_refs=env_data_refs,
            env_datas=env_datas,
            **kwargs)

    def _build_odxlinks(self) -> Dict[OdxLinkId, Any]:
        odxlinks = {self.odx_id: self}

        for ed in self.env_datas:
            odxlinks.update(ed._build_odxlinks())

        return odxlinks

    def _resolve_odxlinks(self, odxlinks: OdxLinkDatabase) -> None:
        # ODX 2.0 specifies environment data objects here, ODX 2.2
        # uses references
        if self.env_data_refs:
            self.env_datas = [odxlinks.resolve(x) for x in self.env_data_refs]
        else:
            for ed in self.env_datas:
                ed._resolve_odxlinks(odxlinks)

    def _resolve_snrefs(self, context: SnRefContext) -> None:
        # ODX 2.0 specifies environment data objects here, ODX 2.2
        # uses references
        if self.env_data_refs:
            for ed in self.env_datas:
                ed._resolve_snrefs(context)

    @override
    def encode_into_pdu(self, physical_value: Optional[ParameterValue],
                        encode_state: EncodeState) -> None:
        """Convert a physical value into bytes and emplace them into a PDU.

        Since environmental data is supposed to never appear on the
        wire, this method just raises an EncodeError exception.
        """
        odxraise("EnvironmentDataDescription DOPs cannot be encoded or decoded")

    @override
    def decode_from_pdu(self, decode_state: DecodeState) -> ParameterValue:
        """Extract the bytes from a PDU and convert them to a physical value.

        Since environmental data is supposed to never appear on the
        wire, this method just raises an DecodeError exception.
        """
        odxraise("EnvironmentDataDescription DOPs cannot be encoded or decoded")
