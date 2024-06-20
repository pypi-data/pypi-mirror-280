import thriftpy2
from thriftpy2.utils import deserialize, serialize

import os

proto_dir = os.path.join(os.path.dirname(__file__), "../..", "proto")
metadata_thrift = thriftpy2.load(os.path.join(proto_dir, "metadata.thrift"),
                                 module_name="metadata_thrift")

class SSTableMetadata:
    def __init__(self, table_type=None, total_count=None, tokenizer_name=None,
                 tokenizer_version=None):
        self.table_type = table_type
        self.total_count = total_count
        self.tokenizer_name = tokenizer_name,
        self.tokenizer_version = tokenizer_version
    
    @staticmethod
    def deserialize(bin):
        return SSTableMetadata.from_thrift(
                deserialize(metadata_thrift.SSTableMetadata(), bin))
    @staticmethod
    def from_thrift(meta_proto):
        return SSTableMetadata(
            table_type=meta_proto.table_type,
            total_count=meta_proto.total_count,
            tokenizer_name=meta_proto.tokenizer_name,
            tokenizer_version=meta_proto.tokenizer_version,
        )
    
    def serialize(self):
        return serialize(self.to_thrift())
    
    def to_thrift(self):
        return metadata_thrift.SSTableMetadata(
            table_type=self.table_type,
            total_count=self.total_count,
            tokenizer_name=self.tokenizer_name,
            tokenizer_version=self.tokenizer_version,
        )
    
    def __repr__(self) -> str:
        return f"SSTableMetadata(table_type={self.table_type}, total_count={self.total_count}, tokenizer_name={self.tokenizer_name}, tokenizer_version={self.tokenizer_version})"
