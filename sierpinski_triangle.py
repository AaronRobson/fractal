#!/usr/bin/python

'''http://en.wikipedia.org/wiki/Sierpinski_triangle

Sierpinski Triangle, each level reduces the total area by one quarter.
Each level has 3/4 of the area of the last.
'''

credits = 'Sierpinski Triangle generator'


def IsIterable(object):
    """Is the Pythonic way;
    http://bytes.com/groups/python/514838-how-test-if-object-sequence-iterable
    returns true for lists and tuples etc. but not for strings.
    """
    return hasattr(object, '__iter__')


def MeanAverage(*values):
    return float(sum(values)) / len(values)


def HalfPoint(firstCoordinates, secondCoordinates):
    averages = []
    for i in range(min(len(firstCoordinates), len(secondCoordinates))):
        averages.append(
            MeanAverage(firstCoordinates[i], secondCoordinates[i]))
    return tuple(averages)


def _format_point(point):
    return '({})'.format(', '.join('{:.2f}'.format(value) for value in point))


def _format_triangle(triangle):
    return '({})'.format(', '.join(map(_format_point, triangle)))


def _format_triangles(triangles):
    return '\n'.join(map(_format_triangle, triangles))


class SierpinskiTriangle():
    def __init__(self, origin=None, sideLength=None, *dimensions):
        """Accepts 3 pairs of dimensions as the vertices of a triangle or 4 as
        the vertices of a rectangle or square which it should be contained in.
        No input defaults to sides of 1, bottom left being the origin.
        """

        if sideLength is not None:
            origTri = self.MakeEquilateralTriangle(origin, sideLength)
        else:
            origTri = dimensions
            if not len(dimensions):
                origTri = self.MakeEquilateralTriangle()

        self.orig = [origTri]

        self.Reset()

    def Reset(self):
        self.steps = 0
        self.triangles = self.orig

    def MakeEquilateralTriangle(self, origin=None, sideLength=None):
        """Gives a Triangle using pythagoras theorem based on the origin,
        bottom left vertex and the length of all the sides.
        Results in order; bottom left, bottom right, top middle.
        Defaults to a 1x1 unit square."""
        if origin is None:
            origin = (0, 0)

        if sideLength is None:
            sideLength = 1

        origin = tuple(map(float, origin))
        sideLength = float(sideLength)

        return (
            origin,
            (origin[0] + sideLength, origin[1]),
            (
                (origin[0] + sideLength)/2,
                origin[1] + (((sideLength**2 - (sideLength/2)**2))**.5))
            )

    def Step(self):
        self.steps += 1
        tempTriangles = []

        for triangle in self.triangles:
            middlePoints = (
                HalfPoint(triangle[0], triangle[1]),
                HalfPoint(triangle[1], triangle[2]),
                HalfPoint(triangle[2], triangle[0]),
            )

            temp = (
                (middlePoints[2], triangle[0], middlePoints[0]),
                (middlePoints[0], triangle[1], middlePoints[1]),
                (middlePoints[1], triangle[2], middlePoints[2]),
            )

            tempTriangles.extend(temp)

        self.triangles = tempTriangles

    def NumOfTriangles(self):
        return len(self.triangles)

    def AreaProportion(self):
        return .75**self.steps

    def __str__(self):
        return str(len(self.triangles)) + '\n' + \
            _format_triangles(self.triangles)


if __name__ == "__main__":
    print(credits)
    st = SierpinskiTriangle()
    print(st.MakeEquilateralTriangle())

    print(str(st))

    st.Step()

    print(str(st))
