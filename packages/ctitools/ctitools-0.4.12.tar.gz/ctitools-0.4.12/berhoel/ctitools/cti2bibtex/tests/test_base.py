"""Basic tests for generating BibTex entries from c't and iX articles."""

# First party library imports.
from berhoel.ctitools.cti2bibtex import BiBTeXEntry
from berhoel.ctitools.ctientry import CTIEntry

__date__ = "2024/06/23 16:37:30 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2022 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"


def test_with_shorttitle() -> None:
    """Test correct generation of BiBTeX file entry."""
    probe = BiBTeXEntry(
        CTIEntry(
            shorttitle="shorttitle",
            title="title",
            author=["author"],
            pages="pages",
            issue="issue",
            info="info",
            journaltitle="journaltitle",
            date="date",
            references="references",
            keywords="keywords",
        ),
    )
    result = str(probe)
    reference = """@article{pages:journaltitle_issue,
  title = {title},
  shorttitle = {shorttitle},
  author = {author},
  date = {date},
  journaltitle = {journaltitle},
  pages = {pages},
  issue = {issue},
  keywords = {keywords},
}
"""
    if result != reference:
        msg = f"{result=} != {reference}"
        raise AssertionError(msg)


def test_without_shorttitle() -> None:
    """Test correct generation of BiBTeX file entry."""
    probe = BiBTeXEntry(
        CTIEntry(
            shorttitle=None,
            title="title",
            author=["author"],
            pages="pages",
            issue="issue",
            info="info",
            journaltitle="journaltitle",
            date="date",
            references="references",
            keywords="keywords",
        ),
    )
    result = str(probe)
    reference = """@article{pages:journaltitle_issue,
  title = {title},
  author = {author},
  date = {date},
  journaltitle = {journaltitle},
  pages = {pages},
  issue = {issue},
  keywords = {keywords},
}
"""
    if result != reference:
        msg = f"{result=} != {reference=}"
        raise AssertionError(msg)
