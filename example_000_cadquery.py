print("cadquery example")
import cadquery as cq
print("cadquery loaded")

# Parameters
length = 120      # mm
width = 100       # mm
corner_r = 10     # mm
thickness = 5     # plate thickness
hole_d = 50       # diameter of central cutout

plate = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(thickness)
    .edges("|Z")
    .fillet(corner_r)
    .faces(">Z")
    .workplane()
    .hole(hole_d)
)

print("Geometry defined")

cq.exporters.export(plate, "results/plate.step")

print("Step file exported")

cq.exporters.export(plate, "results/plate.stl")

print("STL file exported")
