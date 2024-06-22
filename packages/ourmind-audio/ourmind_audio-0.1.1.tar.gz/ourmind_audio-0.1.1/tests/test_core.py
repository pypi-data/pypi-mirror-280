from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from collections.abc import Generator
from pathlib import Path

import numpy as np
import pytest
from ourmind_audio._core import (
    WEBM_SIGNATURE,
    _convert_16kHz_wav,
    _find_webm_start,
    _is_audio_16kHz_wav,
    _repair_webm_file_at_index,
    audiofile_to_converted_array,
    search_and_repair_webm_file,
)

# Set the path to the example audio files
EXAMPLE_AUDIO_PATH = Path(__file__).parent / "example_audio" / "jfk"

GOOD_WEBM = Path("tests/example_audio/damaged-webm/good.webm")
BAD_WEBM = Path("tests/example_audio/damaged-webm/broken.webm")


def get_example_audio_files():
    """Helper function to retrieve all audio files from the example audio directory."""
    return [file for file in EXAMPLE_AUDIO_PATH.iterdir() if file.is_file()]


@pytest.mark.parametrize("audio_file", get_example_audio_files())
def test_convert_16kHz_wav(audio_file):
    temp_path = Path(tempfile.mktemp(suffix=".wav"))

    _convert_16kHz_wav(audio_file, temp_path)
    assert _is_audio_16kHz_wav(temp_path)

    # if temp_path.exists():
    #    temp_path.unlink()


@pytest.mark.parametrize("audio_file", get_example_audio_files())
def test_audio_format(audio_file):
    """
    Test that the _is_audio_16kHz_wav function correctly identifies audio files that are not in the desired format.
    """

    # Skip if contains the string "conv_16k_mono.wav"

    if "conv_16k_mono.wav" not in str(audio_file):
        assert not _is_audio_16kHz_wav(audio_file)


@pytest.fixture
def temp_files() -> Generator[tuple[Path, Path], None, None]:
    input_file = tempfile.NamedTemporaryFile(delete=False)
    output_file = tempfile.NamedTemporaryFile(delete=False)
    yield Path(input_file.name), Path(output_file.name)
    os.remove(input_file.name)
    os.remove(output_file.name)


def test_audiofile_to_converted_array_good_and_bad_webm_same():
    """
    Test that audiofile_to_converted_array produces the same output for good and repaired WebM files.
    """
    try:
        good_audio_array = audiofile_to_converted_array(GOOD_WEBM)
        bad_audio_array = audiofile_to_converted_array(BAD_WEBM)
        assert np.array_equal(good_audio_array, bad_audio_array)
    except Exception as e:
        pytest.fail(f"Unexpected exception: {e}")


def test_signature_constants() -> None:
    assert WEBM_SIGNATURE == b"\x1a\x45\xdf\xa3"


def test_find_webm_start(temp_files: tuple[Path, Path]) -> None:
    input_file_path, _ = temp_files

    bad_header = b"\x00\x01\x02\x03"

    # Create a temporary file with random bytes and a WebM signature
    with input_file_path.open("wb") as temp_file:
        temp_file.write(bad_header + b"\x1a\x45\xdf\xa3" + b"\x04\x05\x06\x07")

    assert _find_webm_start(input_file_path) == len(bad_header)


def test_repair_webm_file_at_index(temp_files: tuple[Path, Path]) -> None:
    input_file_path, output_file_path = temp_files

    # Create a temporary file with random bytes and a WebM signature

    good_file = b"\x1a\x45\xdf\xa3" + b"\x04\x05\x06\x07"

    with input_file_path.open("wb") as temp_file:
        temp_file.write(b"\x00\x01\x02\x03" + good_file)

    _repair_webm_file_at_index(input_file_path, output_file_path, 4)

    with output_file_path.open("rb") as output_file:
        output_data = output_file.read()
        assert output_data == good_file


def test_repair_webm_file_at_index_signature_not_found(
    temp_files: tuple[Path, Path],
) -> None:
    input_file_path, output_file_path = temp_files

    # Create a temporary file without a WebM signature
    with input_file_path.open("wb") as temp_file:
        temp_file.write(b"\x00\x01\x02\x03\x04\x05\x06\x07")

    with pytest.raises(
        ValueError, match="No WebM signature found at the given index: 4"
    ):
        _repair_webm_file_at_index(input_file_path, output_file_path, 4)


def test_search_and_repair_webm_file(temp_files: tuple[Path, Path]) -> None:
    input_file_path, output_file_path = temp_files

    with input_file_path.open("wb") as temp_file:
        temp_file.write(b"\x00\x01\x02\x03" + b"\x1a\x45\xdf\xa3" + b"\x04\x05\x06\x07")

    search_and_repair_webm_file(input_file_path, output_file_path)

    with output_file_path.open("rb") as output_file:
        output_data = output_file.read()
        assert output_data == b"\x1a\x45\xdf\xa3\x04\x05\x06\x07"


def create_broken_webm_file(
    original_file: Path, broken_file: Path, num_random_bytes: int = 100, seed: int = 57
) -> None:
    if seed is not None:
        np.random.seed(seed)

    random_bytes = np.random.bytes(num_random_bytes)

    with original_file.open("rb") as f:
        original_data = f.read()

    with broken_file.open("wb") as f:
        f.write(random_bytes)
        f.write(original_data)


def is_webm_file_valid(file_path: Path) -> bool:
    result = subprocess.run(["ffprobe", file_path], capture_output=True, text=True)
    if (
        "EBML header parsing failed" in result.stderr
        or "Invalid data found when processing input" in result.stderr
    ):
        return False
    return True


def test_good_and_bad_webm_files() -> None:
    # Paths to good and bad WebM files
    repaired_webm = BAD_WEBM.with_name("repaired.webm")

    assert is_webm_file_valid(GOOD_WEBM)

    assert not is_webm_file_valid(BAD_WEBM)

    search_and_repair_webm_file(BAD_WEBM, repaired_webm)

    assert is_webm_file_valid(repaired_webm)

    with GOOD_WEBM.open("rb") as good, repaired_webm.open("rb") as repaired:
        assert good.read() == repaired.read()

    repaired_webm.unlink()


def test_good_file_remains_unchanged_after_repair() -> None:
    # Paths to good WebM file
    GOOD_WEBM = Path("tests/example_audio/damaged-webm/good.webm")
    original_good_copy = GOOD_WEBM.with_name("original_good_copy.webm")
    repaired_webm = GOOD_WEBM.with_name("repaired_good.webm")

    assert is_webm_file_valid(GOOD_WEBM)

    shutil.copy(GOOD_WEBM, original_good_copy)

    with GOOD_WEBM.open("rb") as original:
        original_data = original.read()

    search_and_repair_webm_file(GOOD_WEBM, repaired_webm)

    assert is_webm_file_valid(repaired_webm)

    # Ensure the repaired file is identical to the original good file
    with repaired_webm.open("rb") as repaired:
        repaired_data = repaired.read()
        assert original_data == repaired_data

    # Ensure the original good file copy is identical to the good file
    with original_good_copy.open("rb") as original_copy:
        original_copy_data = original_copy.read()
        assert original_data == original_copy_data

    # Clean up the repaired file and the original good copy after the test
    repaired_webm.unlink()
    original_good_copy.unlink()


def test_create_broken_webm_files() -> None:
    # Paths to good WebM file
    GOOD_WEBM = Path("tests/example_audio/damaged-webm/good.webm")

    bad_header_sizes = [50, 100, 150, 200, 250]
    seed = 57  # Groethendieck prime

    for i, bad_header_size in enumerate(bad_header_sizes):
        broken_webm = Path(f"tests/example_audio/damaged-webm/broken_{i}.webm")
        repaired_webm = broken_webm.with_name(f"repaired_{i}.webm")

        create_broken_webm_file(
            GOOD_WEBM, broken_webm, num_random_bytes=bad_header_size, seed=seed
        )

        assert not is_webm_file_valid(broken_webm)

        search_and_repair_webm_file(broken_webm, repaired_webm)

        assert is_webm_file_valid(repaired_webm)

        with GOOD_WEBM.open("rb") as good, repaired_webm.open("rb") as repaired:
            assert good.read() == repaired.read()

        broken_webm.unlink()
        repaired_webm.unlink()
