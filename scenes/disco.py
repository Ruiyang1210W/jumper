"""A dark dance floor -- for videos where the light is part of the performance.

Built for a robot that brings its own lights (spotlights on a disco-ball shell): every
other scene floods the floor with a sun and a strong headlight, and coloured pools of
light from the robot vanish in it. Here the world is nearly dark on purpose: a dim
headlight so the body still has a shape, one weak cool directional light so nothing
renders pure black, and a glossy grey-violet checker -- dark only because the light is -- that shows colour where a
spotlight lands and reflects the robot above it.
"""

from __future__ import annotations

from .registry import GROUND, Headlight, Scene


def scene() -> Scene:
    from mjlab.utils import spec_config as sc

    return Scene(
        headlight=Headlight(ambient=(0.02, 0.02, 0.03), diffuse=(0.10, 0.10, 0.12)),
        textures=(
            sc.TextureCfg(
                name="disco_floor", type="2d", builtin="checker",
                rgb1=(0.46, 0.44, 0.52), rgb2=(0.30, 0.29, 0.35),
                width=512, height=512,
            ),
            sc.TextureCfg(
                name="disco_sky", type="skybox", builtin="gradient",
                rgb1=(0.06, 0.04, 0.10), rgb2=(0.01, 0.01, 0.02),
                width=256, height=256,
            ),
        ),
        materials=(
            sc.MaterialCfg(
                name="disco_floor", texture="disco_floor", texuniform=True,
                texrepeat=(16.0, 16.0), reflectance=0.25, geom_names_expr=GROUND,
            ),
        ),
        lights=(
            sc.LightCfg(name="moon", type="directional", pos=(-2.0, -2.0, 3.0),
                        dir=(0.5, 0.5, -1.0), diffuse=(0.10, 0.10, 0.14),
                        castshadow=False),
        ),
    )
