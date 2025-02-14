// DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/cpp/mod.rs
// Based on "crates/re_types/definitions/rerun/archetypes/image.fbs".

#include "image.hpp"

#include "../indicator_component.hpp"

namespace rerun {
    namespace archetypes {
        const char Image::INDICATOR_COMPONENT_NAME[] = "rerun.components.ImageIndicator";

        std::vector<AnonymousComponentBatch> Image::as_component_batches() const {
            std::vector<AnonymousComponentBatch> comp_batches;
            comp_batches.reserve(2);

            comp_batches.emplace_back(data);
            if (draw_order.has_value()) {
                comp_batches.emplace_back(draw_order.value());
            }
            comp_batches.emplace_back(
                ComponentBatch<components::IndicatorComponent<Image::INDICATOR_COMPONENT_NAME>>(
                    nullptr,
                    num_instances()
                )
            );

            return comp_batches;
        }
    } // namespace archetypes
} // namespace rerun
