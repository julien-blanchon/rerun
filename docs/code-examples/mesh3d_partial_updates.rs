//! Log a simple colored triangle, then update its vertices' positions each frame.

use rerun::{archetypes::Mesh3D, components::Position3D, external::glam, RecordingStreamBuilder};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let (rec, storage) =
        RecordingStreamBuilder::new("rerun_example_mesh3d_partial_updates").memory()?;

    let vertex_positions = [[-1.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]];

    // Log the initial state of our triangle
    rec.set_time_sequence("frame", 0);
    rec.log(
        "triangle",
        &Mesh3D::new(vertex_positions)
            .with_vertex_normals([[0.0, 0.0, 1.0]])
            .with_vertex_colors([0xFF0000FF, 0x00FF00FF, 0x0000FFFF]),
    )?;

    // Only update its vertices' positions each frame
    for i in 1..300 {
        rec.set_time_sequence("frame", i);

        let factor = (i as f32 * 0.04).sin().abs();
        let vertex_positions: [Position3D; 3] = [
            (glam::Vec3::from(vertex_positions[0]) * factor).into(),
            (glam::Vec3::from(vertex_positions[1]) * factor).into(),
            (glam::Vec3::from(vertex_positions[2]) * factor).into(),
        ];
        rec.log_component_batches("triangle", false, 3, [&vertex_positions as _])?;
    }

    rerun::native_viewer::show(storage.take())?;
    Ok(())
}
