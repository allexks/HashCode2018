toRow"""Define all needed classes and methods related to them."""


class Intersection:
    """Defines an intersection by its position"""

    def __init__(self, row, col):
        self.row = row
        self.col = col


def distanceBetween(Intersection1, Intersection2):
    """Return the distance between two intersections"""
    return abs(Intersection1.row - Intersection2.row)\
        + abs(Intersection1.col - Intersection2.col)


def cmpInters(Intersection1, Intersection2):
    """Return True if both intersections have equal parameters"""
    return Intersection1.row == Intersection2.row and\
        Intersection1.col == Intersection2.col


class Ride:
    """Defines a ride by its input parameters"""

    def __init__(self,
                 startIntersection,
                 endIntersection,
                 earliestStepToStart,
                 latestStepToFinish):
        self.startPos = startIntersection
        self.endPos = endIntersection
        self.earliestStep = earliestStepToStart
        self.latestStep = latestStepToFinish

    def getRideDistance(self):
        return distanceBetween(self.startPos, self.endPos)


class Vehicle:
    def __init__(self):
        """All vehicles should start from (0, 0)"""
        self.currPos = Intersection(0, 0)
        self.assignedRides = list()
        self.isBusy - False
        self.currRide = None
        self.hasReachedRideStartPos = False

    def __str__(self):
        """Return the string formed from the list with all assigned rides;

        Very useful for the output
        """
        return self.assignedRides.join(" ")

    def distanceToRide(self, ride):
        """Return the distance to the start intersection of a ride"""
        return distanceBetween(self.currPos, ride.startPos)

    def hasReachedDestination(self):
        return cmpInters(self.currPos, self.currRide.endPos)

    def checkIfPossibleAndAssignRide(self, newRide, currStep):
        """Check whether the ride can be completed on time and assigns it;

        Returns True if assigned and False if not assigned.
        """
        # the minimum time required to accomplish the ride
        # equals the distance
        # from the current position of the car
        # to the last intersection of the ride
        # through the first intersection of the ride
        minTimeToGo = distanceBetween(self.currPos, newRide.startPos)\
            + newRide.endPos

        if minTimeToGo <= newRide.latestStep - currStep:
            self.currRide = newRide
            self.assignedRides.append(newRide)
            self.isBusy = True
            self.hasReachedRideStartPos = False
            return True
        else:
            print "Unable to complete the ride in time"
            return False

    def _move1StepCloserTo(self, toDestination):
        """Helper function; for use in self.move() only.

        Either move the vehicle one step towards its goal
        or stay in the same place according to the rules
        of the simulation
        """
        currRow = self.currPos.row
        currCol = self.currPos.col
        toRow = toDestination.row
        toCol = toDestination.col

        # First we move it to the correct row
        if currRow < toRow:
            currRow += 1

        elif currRow > toRow:
            currRow -= 1

        # Then to the correct column
        elif currCol < toCol:
            currCol += 1
            if currCol == toCol:
                self.hasReachedRideStartPos = True

        elif currCol > toCol:
            currCol -= 1
            if currCol == toCol:
                self.hasReachedRideStartPos = True

    def move(self, currStep):
        """First move the vehicle towards the beginning inresection of the ride
        then move it towards the end.
        """
        if not self.hasReachedRideStartPos:
            self._move1StepCloserTo(self.currRide.startPos)
        else:
            self._move1StepCloserTo(self.currRide.endPos)
