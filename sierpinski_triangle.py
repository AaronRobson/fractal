#!/usr/bin/python

import operator

'''http://en.wikipedia.org/wiki/Sierpinski_triangle

Sierpinski Triangle, each level reduces the total area by one quarter.
Each level has 3/4 of the area of the last.
'''

creditDict = {
    'author': 'Aaron Robson',
    'title': 'Sierpinski Triangle generator'
}
credits = '{title} by {author}'.format(**creditDict)

def IsIterable(object):
    """Is the Pythonic way; http://bytes.com/groups/python/514838-how-test-if-object-sequence-iterable returns true for lists and tuples etc. but not for strings."""
    return hasattr(object, '__iter__')

class SierpinskiTriangle():
    def __init__(self, origin=None, sideLength=None, *dimensions):
        """Accepts 3 pairs of dimensions as the vertices of a triangle or 4 as the vertices of a rectangle or square which it should be contained in. No input defaults to sides of 1, bottom left being the origin.
        """

        if not sideLength == None:
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
        """Gives a Triangle using pythagoras theorem based on the origin, bottom left vertex and the length of all the sides. Results in order; bottom left, bottom right, top middle.
        Defaults to a 1x1 unit square."""
        if origin == None:
            origin = (0, 0)

        if sideLength == None:
            sideLength = 1

        origin = tuple(map(float, origin))
        sideLength = float(sideLength)

        return origin, (origin[0] + sideLength, origin[1]), ((origin[0] + sideLength)/2, origin[1] + (((sideLength**2 - (sideLength/2)**2))**.5))

    def MeanAverage(self, *values):
        #if IsIterable(values[0]):
        #    values = values[0]

        return float(sum(values)) / len(values)

    def HalfPoint(self, firstCoordinates, secondCoordinates):
        averages = []
        for i in range(min(len(firstCoordinates), len(secondCoordinates))):
            averages.append(self.MeanAverage(firstCoordinates[i], secondCoordinates[i]))
        return tuple(averages)

    def Step(self):
        self.steps += 1
        tempTriangles = []
        """ #3 loops nasty
        for triangle in self.triangles:
            for coordinate in triangle:
                mainTriangle = list(triangle)
                mainTriangle.remove(coordinate)
                newCoordinates = [coordinate]
                for otherCoordinate in mainTriangle:
                    newCoordinates.append(self.HalfPoint(coordinate, otherCoordinate))
                tempTriangles.append(tuple(newCoordinates))
        """

        for triangle in self.triangles:
            middlePoints = (
                self.HalfPoint(triangle[0], triangle[1]),
                self.HalfPoint(triangle[1], triangle[2]),
                self.HalfPoint(triangle[2], triangle[0]),
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

if __name__ == "__main__":
    print(credits)
    st = SierpinskiTriangle()
    print(st.MakeEquilateralTriangle())
    print(st.MeanAverage(10, 20))
    print(st.HalfPoint((0,0), (1,1)))
    print(len(st.triangles), st.triangles)
    st.Step()
    print(len(st.triangles))
    for i in st.triangles:
        print(i)

    #keep the window open
    input('\nPress Enter to Exit:')
