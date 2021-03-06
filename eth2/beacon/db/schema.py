from abc import ABC, abstractmethod

from eth2.beacon.constants import Root


class BaseSchema(ABC):
    #
    # State
    #
    @staticmethod
    @abstractmethod
    def make_head_state_slot_lookup_key() -> bytes:
        ...

    @staticmethod
    @abstractmethod
    def make_head_state_root_lookup_key() -> bytes:
        ...

    #
    # Block
    #
    @staticmethod
    @abstractmethod
    def make_canonical_head_root_lookup_key() -> bytes:
        ...

    @staticmethod
    @abstractmethod
    def make_block_root_to_slot_lookup_key(block_root: Root) -> bytes:
        ...

    @staticmethod
    @abstractmethod
    def make_block_slot_to_root_lookup_key(slot: int) -> bytes:
        ...

    @staticmethod
    @abstractmethod
    def make_block_root_to_score_lookup_key(block_root: Root) -> bytes:
        ...

    @staticmethod
    @abstractmethod
    def make_finalized_head_root_lookup_key() -> bytes:
        ...

    @staticmethod
    @abstractmethod
    def make_justified_head_root_lookup_key() -> bytes:
        ...

    #
    # Attestaion
    #
    @staticmethod
    @abstractmethod
    def make_attestation_root_to_block_lookup_key(attestaton_root: Root,) -> bytes:
        ...

    #
    # Fork choice
    #
    @staticmethod
    @abstractmethod
    def make_lmd_ghost_context_lookup_key(fork: str) -> bytes:
        ...


class SchemaV1(BaseSchema):
    #
    # State
    #
    @staticmethod
    def make_head_state_slot_lookup_key() -> bytes:
        return b"v1:beacon:head-state-slot"

    @staticmethod
    def make_head_state_root_lookup_key() -> bytes:
        return b"v1:beacon:head-state-root"

    @staticmethod
    def make_canonical_epoch_info_lookup_key() -> bytes:
        return b"v1:beacon:canonical-epoch-info"

    #
    # Block
    #
    @staticmethod
    def make_canonical_head_root_lookup_key() -> bytes:
        return b"v1:beacon:canonical-head-root"

    @staticmethod
    def make_finalized_head_root_lookup_key() -> bytes:
        return b"v1:beacon:finalized-head-root"

    @staticmethod
    def make_justified_head_root_lookup_key() -> bytes:
        return b"v1:beacon:justified-head-root"

    @staticmethod
    def make_justified_head_epoch_lookup_key() -> bytes:
        return b"v1:beacon:justified-head-epoch"

    @staticmethod
    def make_block_slot_to_root_lookup_key(slot: int) -> bytes:
        slot_to_root_key = b"v1:beacon:block-slot-to-root:%d" % slot
        return slot_to_root_key

    @staticmethod
    def make_block_root_to_score_lookup_key(block_root: Root) -> bytes:
        return b"v1:beacon:block-root-to-score:%s" % block_root

    @staticmethod
    def make_block_root_to_slot_lookup_key(block_root: Root) -> bytes:
        return b"v1:beacon:block-root-to-slot:%s" % block_root

    #
    # Attestaion
    #
    @staticmethod
    def make_attestation_root_to_block_lookup_key(attestaton_root: Root,) -> bytes:
        return b"v1:beacon:attestation-root-to-block:%s" % attestaton_root

    #
    # Fork choice
    #
    @staticmethod
    def make_lmd_ghost_context_lookup_key(fork: str) -> bytes:
        return b"v1:beacon:fork-choice-lmd-ghost-context:%s" % fork.encode()
