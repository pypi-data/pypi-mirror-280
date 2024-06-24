"""Test article entry processing."""

from pathlib import Path
import zipfile

import _pytest
import pytest
from typing_extensions import Buffer

from berhoel.ctitools import CTI
from berhoel.ctitools.ctientry import CTIEntry

__date__ = "2024/06/24 00:32:44 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2022 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"


@pytest.fixture()
def cti_entry_data_1() -> bytes:
    """Return content for sample CTI file.

    :return: sample data
    """
    return b"""Java nur mit -server-Option

Dr. Volker Zota, Dusan Wasserb\xc7\xcfch
vza
154
10
c07

Praxis,Hotline,Java, Server, Internet, Programmierung, JAR-Archiv
Ein Artikel

Von Torsten T. Will und Ein Autor, Duzan Zivadinovic
ola
 74
 3
c08

kurz vorgestellt,Code Review, Open Source, Entwicklungssystem,Entwicklungs-Tools,Open-Source-Projekt Review Board
"""  # noqa: E501


@pytest.fixture()
def cti_entry_1(tmp_path: Path, cti_entry_data_1: Buffer) -> Path:
    """Return path to sample CTI file.

    :param tmp_path: directory for temporary files
    :param cti_entry_data_1: content for sample file

    :return: path to sample CTI file
    """
    p = tmp_path / "cti_entry_1.cti"
    p.write_bytes(cti_entry_data_1)
    return p


@pytest.fixture()
def cti_entry_zip_1(tmp_path: Path, cti_entry_data_1: str) -> Path:
    """Return path to zipped sample CTI file.

    :param tmp_path: directory for temporary files
    :param cti_entry_data_1: content for sample file

    :return: path to sample CTI file
    """
    p = tmp_path / "cti_entry_1.zip"
    with zipfile.ZipFile(p, "w") as myzip:
        myzip.writestr("cti_entry_1.frm", cti_entry_data_1)
    return p


@pytest.fixture()
def cti_entry_data_2() -> bytes:
    """Return test entry."""
    return b"""Doppelt gemoppelt
\334\344\374\366\337\351
Von Torsten T. Will und Ein Autor, Duzan Zivadinovic
ola
 74
 3
c08

kurz vorgestellt,Code Review, Open Source, Entwicklungssystem,Entwicklungs-Tools,Open-Source-Projekt Review Board
"""  # noqa: E501


@pytest.fixture()
def cti_entry(request: _pytest.fixtures.SubRequest) -> str:
    """Return filename for test file.

    :param request: testfile request

    :return: file name
    """
    return request.getfixturevalue(request.param)


@pytest.fixture()
def cti_entry_2(tmp_path: Path, cti_entry_data_2: Buffer) -> Path:
    """Provide sample data file.

    :param tmp_path: temporary path for storing files
    :param cti_entry_data_2: content for sample file

    :returns: path to sample file
    """
    p = tmp_path / "cti_entry_2.cti"
    p.write_bytes(cti_entry_data_2)
    return p


@pytest.fixture()
def cti_entry_zip_2(tmp_path: Path, cti_entry_data_2: str) -> Path:
    """Provide zipped sample CTI files.

    :param tmp_path: temporary path for storing files
    :param cti_entry_data_2: content for sample file

    :returns: path to zipped data file
    """
    p = tmp_path / "cti_entry_2.zip"
    with zipfile.ZipFile(p, "w") as myzip:
        myzip.writestr("cti_entry_2.cti", cti_entry_data_2)
    return p


@pytest.fixture()
def cti_entry_data_3() -> bytes:
    """Provide sampe cti entries.

    :return: sample data
    """
    return b"""Familienleben
Digitals Alpha-Linie: Vorstellung von f\201nf 64-Bit-Rechnern in London
Behme, Henning
hb
 13
 1
i93

Markt + Trends
Schlu\341folgerungsmuster
Objektorientierte Verkn\201pfung von Wissensbasen und Datenbanken
Higa, Kunihiko/Morrison, Joline+Mike
hb
132
 1
i93

Wissen
"""


@pytest.fixture()
def cti_entry_3(tmp_path: Path, cti_entry_data_3: Buffer) -> Path:
    """Provide cti entries.

    :param tmp_path: temporary path for storing files
    :param cti_entry_data_3: content for sample file

    :return: path to sample file
    """
    p = tmp_path / "cti_entry_3.cti"
    p.write_bytes(cti_entry_data_3)
    return p


@pytest.mark.parametrize("cti_entry", ["cti_entry_1", "cti_entry_zip_1"], indirect=True)
def test_process_author_1(cti_entry: str) -> None:
    """Another test fopr input encoding handling.

    :param cti_etnry: sampel entry

    :raises: AssertionError
    """
    probe = iter(CTI(cti_entry))
    result = next(probe).author
    reference = ("Dr. Volker Zota", "Dušan Wasserbäch")
    if result != reference:
        msg = f"{result=} != {reference=}"
        raise AssertionError(msg)


def test_ctientry_1() -> None:
    """Check comparison operator for class `CTIEntry`."""
    if CTIEntry(
        shorttitle="a",
        title="a",
        author=("a", ),
        pages=1,
        issue="1",
        info={"a": "b"},
        journaltitle="a",
        date="a",
        references="a",
        keywords="a",
    ) != CTIEntry(
        shorttitle="a",
        title="a",
        author=("a",),
        pages=1,
        issue="1",
        info={"a": "b"},
        journaltitle="a",
        date="a",
        references="a",
        keywords="a",
    ):
        msg = "Comparison failed"
        raise AssertionError(msg)


def test_ctientry_2() -> None:
    """Check comparison operator for class `CTIEntry`."""
    if CTIEntry(
        shorttitle="b",
        title="a",
        author=("a",),
        pages=1,
        issue="1",
        info={"a": "b"},
        journaltitle="a",
        date="a",
        references="a",
        keywords="a",
    ) == CTIEntry(
        shorttitle="a",
        title="a",
        author=("a",),
        pages=1,
        issue="1",
        info={"a": "b"},
        journaltitle="a",
        date="a",
        references="a",
        keywords="a",
    ):
        msg = "Comparison failed"
        raise AssertionError(msg)


@pytest.mark.parametrize("cti_entry", ["cti_entry_2", "cti_entry_zip_2"], indirect=True)
def test_process_author_2(cti_entry: str) -> None:
    """Another test for processing autor entries.

    :cti_entry: input data

    :raises: AssertionError
    """
    probe = iter(CTI(cti_entry))
    result = next(probe).author
    reference = (
        "Torsten T. Will",
        "Ein Autor",
        "Dušan Živadinović",
    )
    if result != reference:
        msg = f"{result=} != {reference=}"
        raise AssertionError(msg)


@pytest.mark.parametrize("cti_entry", ["cti_entry_2", "cti_entry_zip_2"], indirect=True)
def test_process_chars_2(cti_entry: str) -> None:
    """Testing handling of character encoding.

    :param cti_entry: test string

    :raises: AssertionError
    """
    probe = iter(CTI(cti_entry))
    title = next(probe).title
    if title != "Üäüößé":
        msg = f'{title=} != "Üäüößé"'
        raise AssertionError(msg)


def test_process_authors_ix_3(cti_entry_3: Path) -> None:
    """Testing autor entries for iX.

    :param cti_entry_3: Path to test file.
    """
    references = (
        CTIEntry(
            shorttitle="Familienleben",
            title="Digitals Alpha-Linie: Vorstellung von fünf 64-Bit-Rechnern in "
            "London",
            author=("Henning Behme",),
            pages=13,
            issue="1993 / 1",
            info={"paper": "i", "year": "93"},
            journaltitle="iX",
            date="1993-01-01",
            references="",
            keywords="Markt + Trends",
        ),
        CTIEntry(
            shorttitle="Schlußfolgerungsmuster",
            title="Objektorientierte Verknüpfung von Wissensbasen und Datenbanken",
            author=("Kunihiko Higa", "Joline+Mike Morrison"),
            pages=132,
            issue="1993 / 1",
            info={"paper": "i", "year": "93"},
            journaltitle="iX",
            date="1993-01-01",
            references="",
            keywords="Wissen",
        ),
    )

    data_read = False
    for probe, ref in zip(iter(CTI(cti_entry_3)), references):
        if probe != ref:
            msg = f"{probe=} != {ref=}"
            AssertionError(msg)
        data_read = True
    if not data_read:
        msg = "No data read"
        raise AssertionError(msg)
