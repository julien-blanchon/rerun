// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/datatypes/mesh_properties.fbs".

#pragma once

#include "../result.hpp"

#include <cstdint>
#include <memory>
#include <optional>
#include <utility>
#include <vector>

namespace arrow {
    class DataType;
    class MemoryPool;
    class StructBuilder;
} // namespace arrow

namespace rerun {
    namespace datatypes {
        struct MeshProperties {
            /// If specified, is a flattened array of indices that describe the mesh's triangles,
            /// i.e. its length must be divisible by 3.
            std::optional<std::vector<uint32_t>> vertex_indices;

          public:
            MeshProperties() = default;

            MeshProperties(std::optional<std::vector<uint32_t>> _vertex_indices)
                : vertex_indices(std::move(_vertex_indices)) {}

            MeshProperties& operator=(std::optional<std::vector<uint32_t>> _vertex_indices) {
                vertex_indices = std::move(_vertex_indices);
                return *this;
            }

            /// Returns the arrow data type this type corresponds to.
            static const std::shared_ptr<arrow::DataType>& arrow_datatype();

            /// Creates a new array builder with an array of this type.
            static Result<std::shared_ptr<arrow::StructBuilder>> new_arrow_array_builder(
                arrow::MemoryPool* memory_pool
            );

            /// Fills an arrow array builder with an array of this type.
            static Error fill_arrow_array_builder(
                arrow::StructBuilder* builder, const MeshProperties* elements, size_t num_elements
            );
        };
    } // namespace datatypes
} // namespace rerun
