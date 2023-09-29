# TODO: Add __add__ to the class. Example: name+code = +name,+code
class SortPapametr:
    """Represents a sort parameter."""

    def __init__(self, name: str):
        """Initialize a new sort parameter.

        Args:
            name: str - The name of the sort parameter
        """
        self.name = name

    def __str__(self) -> str:
        """Return a string representation of the parameter.

        Returns:
            str
        """
        return str(self.name)

    @property
    def decrease(self) -> str:
        """Sorting in order of decreasing value.

        Returns:
            Name with '-'
        """
        return '{0}{1}'.format('-', self.name)

    @property
    def increase(self) -> str:
        """Sorting in order of increasing value.

        Returns:
            Name with '+'
        """
        return '{0}{1}'.format('+', self.name)


class SortPerson:
    """Represents list of types of sorting search results by person."""

    full_name = SortPapametr('fullName')


class SortTrainingTeam:
    """Represents list of types of sorting search result by training team."""

    name = SortPapametr('name')
    name_short = SortPapametr('cu_name_short')
    code = SortPapametr('code')
    name_short_code = SortPapametr('cu_name_short,+code')


class SortSpecialties:
    """Represents list of types of sorting search result by specialties."""

    name = SortPapametr('name')
    code = SortPapametr('code')


class SortRoom:
    """Represents list of types of sorting search result by room."""

    name = SortPapametr('name')
    building_name = SortPapametr('building.name')
    bulding_address = SortPapametr('bulding.address')
    total_capacity = SortPapametr('totalCapacity')
    projector_available = SortPapametr(
        'projectorAvailable',
    )  # NOTE: Anyway return false -> true


class SortLearingProfle:
    """Represents list of types of sorting search result by learning profile."""

    name = SortPapametr('name')


class SortModule:
    """Represents list of types of sorting search result by module."""

    name = SortPapametr('name')
