"""This module contains the NotionTimeMachine class."""
import re


# Note that in addition to the property limits below, payloads have a maximum size of 1000 block elements and 500KB overall.


class NotionRichText:
    """Class for storing a Notion rich text object."""

    def __init__(self, text):
        """Initialize the class.
        Parameters:
            text (str): The text of the rich text object."""
        if text is not None:
            if len(text) > 2000:
                self.text = text[:2000]
                print(
                    f"Text for {type(self).__name__} has been truncated to 2000 characters."
                )
            else:
                self.text = text
            return self.text
        else:
            return None


class NotionPageReference:
    """Class for storing a Notion page reference."""

    def __init__(self, reference):
        """Initialize the class.
        Parameters:
            reference (str): The Notion reference of the page."""
        if not self is not None:
            if not self._is_valid_guid(reference):
                raise ValueError(
                    "Invalid page reference format. Must be in GUID format."
                )
        self.reference = reference
        return self.reference

    def _is_valid_guid(self, value):
        """Check if the value is in GUID format.
        Returns:
            bool: True if value is in GUID format, False otherwise."""
        pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
        return bool(re.match(pattern, value))


class NotionDate:
    """Class for storing a Notion date."""

    def __init__(self, year: int, month: int, day: int) -> str:
        """Initialize the class.
        Parameters:
            year (int): The year of the date.
            month (int): The month of the date.
            day (int): The day of the date.

        Returns:
            date (str): The date in ISO 8601 format."""
        self.year = year
        self.month = month
        self.day = day
        self.date = f"{self.year}-{self.month}-{self.day}"
        return self.date


class TimeMachinePerson(NotionPageReference):
    """Class for storing a Time Machine person."""

    def __init__(self, page_id: str = None, gedcom_ref: str = None):
        """Class for storing a Time Machine person.
        Each person is a Notion page with several custom properties.

        Parameters
        ----------

            page_id (str): The ID of the person's Notion page. Must be in GUID format.

            gedcom_ref (str): The reference of the individual in the GEDCOM file.
        """
        self.page_id = NotionPageReference.__init__(self, page_id)
        self.gedcom_ref = gedcom_ref

    class BriefBiography(NotionRichText):
        """The brief biography of the person."""

        def __init__(self, text: str):
            """Initialize the class.
            Parameters:
                text (str): The text of the brief biography.
                id (fixed): The Notion ID of the property."""
            self.text = NotionRichText.__init__(self, text)
            self.id = "%3E%5Dx%3A"

    class NotableFigure:
        """Whether the person is a notable figure."""

        def __init__(self, notable_figure: bool = False):
            """Initialize the class.
            Parameters:
                notable_figure (bool): Whether the person is a notable figure.
                id (fixed): The Notion ID of the property."""
            self.notable_figure = notable_figure
            self.id = "IQKR"

    class Notes(NotionRichText):
        """Notes about the person."""

        def __init__(self, notes: str = None):
            """Initialize the class.
            Parameters:
                notes (str): Notes about the person.
                id (fixed): The Notion ID of the property."""
            self.notes = NotionRichText.__init__(self, notes)
            self.id = "JFzR"

    class DatesApprox:
        """Whether the dates are approximate."""

        def __init__(self, dates_approx: bool):
            """Initialize the class.
            Parameters:
                dates_approx (bool): Whether the dates are approximate.
                id (fixed): The Notion ID of the property."""
            self.dates_approx = dates_approx
            self.id = "NNeY"

    class Branch(NotionPageReference):
        """The branch of the person."""

        def __init__(self, branch: str):
            """Initialize the class.
            Parameters:
                branch (str): The branch of the person. Must be a Notion page reference.
                id (fixed): The Notion ID of the property."""
            self.branch = NotionPageReference.__init__(self, branch)
            self.id = "OEb%7C"

    class Spouse(NotionPageReference):
        """The spouse of the person."""

        def __init__(self, spouse: str):
            """Initialize the class.
            Parameters:
                spouse (str): The spouse of the person. Must be a Notion page reference.
                id (fixed): The Notion ID of the property."""
            self.spouse = NotionPageReference.__init__(self, spouse)
            self.id = "P%5Bp%3E"

    class Images:
        """Image of the person."""

        def __init__(self, images: str):
            """Initialize the class.
            Parameters:
                images (str): URL of the image of the person.
                id (fixed): The Notion ID of the property."""
            self.images = images
            self.id = "Pj%5CT"

    class Parents(NotionPageReference):
        """The parents of the person."""

        def __init__(self, parents: list):
            """Initialize the class.
            Parameters:
                parents (list): The parents of the person. Represented as a list of Notion page IDs.
                id (fixed): The Notion ID of the property."""
            validated_parents = []
            for parent in parents:
                validated_parents.append(NotionPageReference.__init__(self, parent))

            self.parents = validated_parents
            self.id = "UVq%5D"

    class Siblings(NotionPageReference):
        """The siblings of the person."""

        def __init__(self, siblings: list):
            """Initialize the class.
            Parameters:
                siblings (list): A list of Notion page IDs as the siblings of the person.
                id (fixed): The Notion ID of the property."""
            validated_siblings = []
            for sibling in siblings:
                validated_siblings.append(NotionPageReference.__init__(self, sibling))
            self.siblings = validated_siblings
            self.id = "_iE%3F"

    class Library(NotionPageReference):
        """The library of the person."""

        def __init__(self, library: list):
            """Initialize the class.
            Parameters:
                library (list): A list of Notion page IDs as the library of the person.
                id (fixed): The Notion ID of the property."""
            validated_library = []
            for book in library:
                validated_library.append(NotionPageReference.__init__(self, book))
            self.library = validated_library
            self.id = "%5B%5DpC"

    class Children(NotionPageReference):
        """The children of the person."""

        def __init__(self, children: list):
            """Initialize the class.
            Parameters:
                children (list): A list of Notion page IDs as the children of the person.
                id (fixed): The Notion ID of the property."""
            validated_children = []
            for child in children:
                validated_children.append(NotionPageReference.__init__(self, child))
            self.children = validated_children
            self.id = "%5Dpsl"

    class PlaceOfDeathBurial(NotionRichText):
        """The place of death or burial of the person."""

        def __init__(self, place_of_death_burial: str):
            """Initialize the class.
            Parameters:
                place_of_death_burial (str): The place of death or burial of the person.
                id (fixed): The Notion ID of the property."""
            self.place_of_death_burial = NotionRichText.__init__(
                self, place_of_death_burial
            )
            self.id = "%60Cn%7D"

    class Tags:
        """Tags assigned to the person."""

        def __init__(self, tags: list):
            """Initialize the class.
            Parameters:
                tags (list): List of tags on the person, represented as a list of strings. Stored as the 'name' property in Notion.
                id (fixed): The Notion ID of the property."""
            self.tags = tags
            self.id = "%60y_o"

    class AssociatedWith(NotionPageReference):
        """Associated people of the person."""

        def __init__(self, associated_with: list):
            """Initialize the class.
            Parameters:
                associated_with (list): List of Notion page IDs of the associated people of the person.
                id (fixed): The Notion ID of the property."""
            validated_associated_with = []
            for associated in associated_with:
                validated_associated_with.append(
                    NotionPageReference.__init__(self, associated)
                )
            self.associated_with = validated_associated_with
            self.id = "aoDr"

    class DisplayName(NotionRichText):
        """The display name of the person."""

        def __init__(self, display_name: str):
            """Initialize the class.
            Parameters:
                display_name (str): The display name of the person.
                id (fixed): The Notion ID of the property."""
            self.display_name = NotionRichText.__init__(self, display_name)
            self.id = "gvML"

    class NickName(NotionRichText):
        """The nickname of the person."""

        def __init__(self, nickname: str):
            """Initialize the class.
            Parameters:
                nickname (str): The nickname of the person.
                id (fixed): The Notion ID of the property."""
            self.nickname = NotionRichText.__init__(self, nickname)
            self.id = "i%5D%7B%3F"

    class PlaceOfBirth(NotionRichText):
        """The place of birth of the person."""

        def __init__(self, place_of_birth: str):
            """Initialize the class.
            Parameters:
                place_of_birth (str): The place of birth of the person.
                id (fixed): The Notion ID of the property."""
            self.place_of_birth = NotionRichText.__init__(self, place_of_birth)
            self.id = "prt%3E"

    class Gender:
        """The gender of the person."""

        def __init__(self, gender: str):
            # Check if the gender string is either 'M' or 'F'
            if gender == "M" or "F":
                self.gender = gender
            else:
                print("Invalid gender string. Must be either 'M' or 'F'.")

    class BirthDeath(NotionDate):
        """The birth and/or death date of the person."""

        def __init__(self, birth: tuple[3] = None, death: tuple[3] = None):
            """Initialize the class.
            Parameters:
                birth (tuple): The birth date of the person. Must be a tuple of (year, month, day).
                death (tuple): The death date of the person. Must be a tuple of (year, month, day).
                id (fixed): The Notion ID of the property."""
            if birth is not None:
                self.birth = NotionDate.__init__(self, birth[0], birth[1], birth[2])
            if death is not None:
                self.death = NotionDate.__init__(self, death[0], death[1], death[2])
            self.id = "rCAI"

    class Marrraige(NotionDate):
        """The marriage date of the person."""

        def __init__(self, marriage: tuple[3]):
            """Initialize the class.
            Parameters:
                marriage (tuple): The marriage date of the person. Must be a tuple of (year, month, day).
                id (fixed): The Notion ID of the property."""
            self.marriage = NotionDate.__init__(
                self, marriage[0], marriage[1], marriage[2]
            )
            self.id = "%7BRvC"

    class Title(NotionRichText):
        """The title of the person."""

        def __init__(self, title: str):
            """Initialize the class.
            Parameters:
                title (str): The title of the person.
                id (fixed): The Notion ID of the property."""
            self.title = NotionRichText.__init__(self, title)
            self.id = "%7DBDt"

    class AltNames(NotionRichText):
        """The alternate names of the person."""

        def __init__(self, alt_names: str):
            """Initialize the class.
            Parameters:
                alt_names (str): The alternate names of the person.
                id (fixed): The Notion ID of the property."""
            self.alt_names = NotionRichText.__init__(self, alt_names)
            self.id = "~%5E%3E%3C"

    class FullBirthName(NotionRichText):
        """The full birth name of the person."""

        def __init__(self, full_birth_name: str):
            """Initialize the class.
            Parameters:
                full_birth_name (str): The full birth name of the person.
                id (fixed): The Notion ID of the property."""
            self.full_birth_name = NotionRichText.__init__(self, full_birth_name)
            self.id = "title"
