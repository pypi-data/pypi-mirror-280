import base64
import dataclasses
from typing import List, Optional, Tuple, Union, Type
from stellar_sdk.xdr import SCEnvMetaEntry, SCMetaEntry, SCSpecEntry

__all__ = ["parse_contract_metadata", "ContractMetaData"]


@dataclasses.dataclass
class ContractMetaData:
    """The contract metadata parsed from the Stellar Contract WASM."""

    env_meta_base64: Optional[bytes] = None
    env_meta: List[SCEnvMetaEntry] = dataclasses.field(default_factory=list)
    meta_base64: Optional[bytes] = None
    meta: List[SCMetaEntry] = dataclasses.field(default_factory=list)
    spec_base64: Optional[bytes] = None
    spec: List[SCSpecEntry] = dataclasses.field(default_factory=list)


def parse_contract_metadata(wasm: Union[bytes, str]) -> ContractMetaData:
    """Parse contract metadata from the Stellar Contract WASM.

    :param wasm: The Stellar Contract WASM as bytes or base64 encoded string.
    :return: The parsed contract metadata.
    """
    if isinstance(wasm, str):
        wasm = base64.b64decode(wasm)

    custom_sections = get_custom_sections(wasm)
    metadata = ContractMetaData()
    for name, content in custom_sections:
        if name == "contractenvmetav0":
            metadata.env_meta_base64 = content
            metadata.env_meta = parse_entries(content, SCEnvMetaEntry)
        if name == "contractspecv0":
            metadata.spec_base64 = content
            metadata.spec = parse_entries(content, SCSpecEntry)
        if name == "contractmetav0":
            metadata.meta_base64 = content
            metadata.meta = parse_entries(content, SCMetaEntry)
    return metadata


def leb128_decode(data, offset):
    result = 0
    shift = 0
    size = 0
    byte = 0x80
    while byte & 0x80:
        byte = data[offset + size]
        result |= (byte & 0x7F) << shift
        shift += 7
        size += 1
    return result, size


def get_custom_sections(wasm_data: bytes) -> List[Tuple[str, bytes]]:
    assert wasm_data[:4] == b"\x00asm", "Invalid WebAssembly magic number"
    offset = 8  # Skip past the magic number and version
    custom_sections = []

    while offset < len(wasm_data):
        section_id, size_leb = leb128_decode(wasm_data, offset)
        offset += size_leb
        section_size, size_leb_size = leb128_decode(wasm_data, offset)
        offset += size_leb_size

        if section_id == 0:  # Custom Section
            name_len, size_name_len = leb128_decode(wasm_data, offset)
            offset += size_name_len
            name = wasm_data[offset : offset + name_len].decode("utf-8")
            offset += name_len
            content = wasm_data[
                offset : offset + section_size - size_name_len - name_len
            ]
            offset += section_size - size_name_len - name_len
            custom_sections.append((name, content))
        else:
            offset += section_size
    return custom_sections


def parse_entries(
    data: bytes, cls: Type[SCEnvMetaEntry | SCMetaEntry | SCSpecEntry]
) -> List[SCEnvMetaEntry | SCMetaEntry | SCSpecEntry]:
    entries = []
    offset = 0
    while offset < len(data):
        entry = cls.from_xdr_bytes(data[offset:])
        offset += len(entry.to_xdr_bytes())
        entries.append(entry)
    return entries
