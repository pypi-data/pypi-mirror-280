namespace py proto
namespace cpp proto

struct SSTableMetadata {
    1: optional string table_type,
    2: optional i32 total_count,
    3: optional string tokenizer_name,
    4: optional string tokenizer_version,
}
