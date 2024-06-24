from typing import List, Tuple
from shapely import geometry
import numpy as np
import cv2

from camera import Camera



def densify_geometry(line_geometry: List[Tuple[float, float]], step: float) -> List[Tuple[float, float]]:
    # taken from https://gis.stackexchange.com/a/373279
    # step: add a vertice every step in whatever unit your coordinate reference system use.

    line_geometry = geometry.LineString(line_geometry)
    length_m=line_geometry.length # get the length

    xy=[] # to store new tuples of coordinates

    for distance_along_old_line in np.arange(0,length_m,step): 

        point = line_geometry.interpolate(distance_along_old_line) # interpolate a point every step along the old line
        xp,yp = point.x, point.y # extract the coordinates

        xy.append((xp,yp)) # and store them in xy list

    return xy

def to_visible_image_polygons(
        polyline: List[Tuple[float, float]],
        camera: Camera,
        asset_width: float,
        simplify_tol=0.
) -> Tuple[List[List[Tuple[int, int]]], List[List[Tuple[int, int]]], List[Tuple[int, int]]]:
    polylines = get_visible_polylines(polyline, camera)
    w, h = camera.image_width - 1 , camera.image_height - 1
    image_borders = geometry.Polygon([(0,0), (0,h), (w, h), (w, 0)])
    visible_polylines , visible_polygons = [], []
    for pline in polylines:
        if len(pline) == 1:
            polygon: geometry.Polygon = geometry.Point(pline).buffer(
                asset_width, cap_style="round")
        elif len(pline) > 1:
            polygon: geometry.Polygon = geometry.LineString(pline).buffer(
                asset_width, cap_style="flat")
        else:
            continue
        if isinstance(polygon, geometry.MultiPolygon):
            polygon = list(polygon.geoms)[0]
        polygon = polygon.intersection(image_borders)
        if simplify_tol > 0.:
            polygon = polygon.simplify(simplify_tol)
        polygon = list(polygon.exterior.coords)
        if not polygon:
            continue
        visible_polylines.append(pline)
        visible_polygons.append(polygon)
    return visible_polygons, visible_polylines, list(image_borders.exterior.coords)



def get_visible_polylines(
        polyline_wc: List[Tuple[int, int]], camera: Camera) -> List[List[Tuple[int, int]]]:
    """Convert polyline from world coordinates into image coordinates,
    then check if such coordinate is in the image.
    This process may break a polyline into multiple segment of polylines,
    and only coordinates that are in the image are returned."""
    if not len(polyline_wc):
        return []
    w, h = camera.image_width - 1 , camera.image_height - 1
    image_border_lines = [
        [(0, 0), (0, h)],
        [(0, h), (w, h)],
        [(w, h), (w, 0)],
        [(w, 0), (0, 0)]]
    polyline_wc = np.array(polyline_wc, dtype=np.float64)
    polyline_ics = camera.world_coords_to_image_coords(
        asset_lats=polyline_wc[:, 1], asset_longs=polyline_wc[:, 0], return_outside=True)
    total_ics = len(polyline_ics)
    def is_inside(p):
        x, y = p
        return not (x < 0 or y < 0 or x >= camera.image_width or y >= camera.image_height)
    if total_ics == 1:
        return [[polyline_ics[0]]] if is_inside(polyline_ics[0]) else []
    polyline_vis_rle = rle(list(map(is_inside, polyline_ics)))
    visible_polylines = []
    for n, s, vis in zip(*polyline_vis_rle):
        if not vis:
            continue
        pline = []
        # add start point that extends to the edge of the image
        if s > 0:
            for bline in image_border_lines:
                isct_p = intersect(polyline_ics[s-1], polyline_ics[s], *bline)
                if isct_p is None:
                    continue
                pline.append((round(isct_p[0]), round(isct_p[1])))
        # add the points
        pline.extend(polyline_ics[s:s+n])
        # add end point that extends to the edge of the image
        if s+n < total_ics:
            for bline in image_border_lines:
                isct_p = intersect(pline[-1], polyline_ics[s+n], *bline)
                if isct_p is None:
                    continue
                pline.append((round(isct_p[0]), round(isct_p[1])))
        visible_polylines.append(pline)
    return visible_polylines

def rle(inarray):
    """ run length encoding. Partial credit to R rle function. 
        Multi datatype arrays catered for including non Numpy
        returns: tuple (runlengths, startpositions, values).
        Taken from: <https://stackoverflow.com/a/32681075>"""
    ia = np.asarray(inarray)                # force numpy
    n = len(ia)
    if n == 0: 
        return (None, None, None)
    else:
        y = ia[1:] != ia[:-1]               # pairwise unequal (string safe)
        i = np.append(np.where(y), n - 1)   # must include last element posi
        z = np.diff(np.append(-1, i))       # run lengths
        p = np.cumsum(np.append(0, z))[:-1] # positions
        return(z, p, ia[i])
    

def intersect(p1, p2, p3, p4):
    """Intersection between line(p1, p2) and line(p3, p4).
    Taken from <https://gist.github.com/kylemcdonald/6132fc1c29fd3767691442ba4bc84018>."""
    x1,y1 = p1
    x2,y2 = p2
    x3,y3 = p3
    x4,y4 = p4
    denom = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)
    if denom == 0: # parallel
        return None
    ua = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / denom
    if ua < 0 or ua > 1: # out of range
        return None
    ub = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / denom
    if ub < 0 or ub > 1: # out of range
        return None
    x = x1 + ua * (x2-x1)
    y = y1 + ua * (y2-y1)
    return (x,y)

def calculate_intersection(polygons_mask, boxes_mask):
    combined_mask = cv2.bitwise_and(polygons_mask, boxes_mask)
    cv2.imwrite("samples/refine_camera/dummy_polygons.jpg", polygons_mask)
    cv2.imwrite("samples/refine_camera/dummy_boxes.jpg", boxes_mask)
    cv2.imwrite("samples/refine_camera/dummy.jpg", combined_mask)
    intersected_pixels = np.sum(combined_mask == 255)
    total_intersected_pixels = np.sum(boxes_mask == 255)
    intersection_percentage = intersected_pixels / total_intersected_pixels * 100
    return intersection_percentage

