from kurbopy import BezPath, Point
import math


def tangent(seg, t):
    return seg.deriv().eval(t)


def wonkiness(path: BezPath):
    def nxt(lst, n):
        return lst[(n + 1) % len(lst)]

    segs = path.segments()
    segscore = 0
    for i, seg in enumerate(segs):
        in_curvature = seg.curvature(0.9)
        out_curvature = nxt(segs, i).curvature(0.1)
        curvaturediff = abs(1000 * (in_curvature + out_curvature))
        # print("In curve: %e Out curve: %e" % (in_curvature, out_curvature))
        in_tangent = tangent(seg, 0.9)
        out_tangent = tangent(nxt(segs, i), 0.1)
        anglediff = abs(
            abs(in_tangent.to_vec2().atan2()) - abs(out_tangent.to_vec2().atan2())
        ) % (math.pi / 4)
        # print(
        #     "Seg %i Angle diff: %.9e Curve diff: %.9e" % (i, anglediff, curvaturediff)
        # )
        total_len = seg.arclen(0.1) + nxt(segs, i).arclen(0.1)
        segscore += 100 * (anglediff + curvaturediff) / (1 + total_len)
    print("Total score", segscore)
    return segscore / len(segs)


b = BezPath()
b.move_to(Point(0, 0))
b.line_to(Point(100, 0))
b.line_to(Point(100, 100))
b.line_to(Point(90, 100))
b.line_to(Point(90, 90))
b.line_to(Point(75, 150))
b.close_path()
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
b.plot(ax)
plt.show()
print(list(f for f in b.segments()))
print(wonkiness(b))
