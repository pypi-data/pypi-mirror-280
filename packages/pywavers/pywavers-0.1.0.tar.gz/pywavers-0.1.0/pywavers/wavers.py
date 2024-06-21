from typing import Any, Tuple
import numpy as np
import pywavers.pywavers as pw


def read(fp: str, dtype: np.dtype = np.int16) -> Tuple[np.ndarray, int]:
    """Read a WAV file and return the data as a numpy array.
    Parameters
    ----------
    fp : str
        Path to the WAV file.
    dtype : str, optional
        Data type of the returned array. Default is 'int16'.
    Returns
    -------
    data : numpy.ndarray, int
        Data from the WAV file and the sample rate.
    """
    try:
        match dtype:
            case np.int16:
                return pw.read_i16(fp)
            case np.int32:
                return pw.read_i32(fp)
            case np.float32:
                return pw.read_f32(fp)
            case np.float64:
                return pw.read_f64(fp)
            case _:
                raise ValueError(f"Unsupport dtype: {dtype}")
    except Exception as e:
        raise e


def write(fp: str, data: np.ndarray, sample_rate: int, dtype: np.dtype = np.int16):
    """Write a numpy array to a WAV file.
    Parameters
    ----------
    fp : str
        Path to the WAV file.
    data : numpy.ndarray
        Data to be written to the WAV file.
    dtype : str, optional
        Data type of the input array. Default is 'int16'.
    """
    try:
        match dtype:
            case np.int16:
                pw.write_i16(fp, data, sample_rate)
            case np.int32:
                pw.write_i32(fp, data, sample_rate)
            case np.float32:
                pw.write_f32(fp, data, sample_rate)
            case np.float64:
                pw.write_f64(fp, data, sample_rate)
            case _:
                raise ValueError(f"Unsupport dtype: {dtype}")
    except Exception as e:
        raise e


def spec(fp: str) -> Tuple[Any]:
    """Get information about a WAV file.
    Parameters
    ----------
    fp : str
        Path to the WAV file.
    Returns
    -------
    info : dict
        Tuple containing sample rate, number of channels, duration, and encoding of the wav file.
    """
    try:
        wav_spec = pw.wav_spec(fp)
        return (
            wav_spec.sample_rate,
            wav_spec.n_channels,
            wav_spec.duration,
            wav_spec.encoding,
        )

    except Exception as e:
        raise e


ONE_CHANNEL_I16 = "pywavers/test_resources/one_channel_i16.wav"


def test_read_i16_i16():
    """
    Tests reading PCM16 encoded files as PCM16. Correctness is measured against soundfile
    """
    import soundfile as sf

    expected_data, sr = sf.read(ONE_CHANNEL_I16, dtype=np.int16)
    actual_data, sr = read(ONE_CHANNEL_I16)
    assert actual_data.shape == expected_data.shape, "Shape mismatch, {} != {}".format(
        actual_data.shape, expected_data.shape
    )

    for exp, act in zip(expected_data, actual_data):
        assert exp == act, "Data mismatch, {} != {}".format(exp, act)


def test_read_i16_i32():
    """
    Tests reading PCM16 encoded files as int 32. Correctness is measured against soundfile
    """
    import soundfile as sf

    expected_data, sr = sf.read(ONE_CHANNEL_I16, dtype=np.int32, always_2d=True)

    actual_data, sr = read(ONE_CHANNEL_I16, dtype=np.int32)
    assert actual_data.shape == expected_data.shape, "Shape mismatch, {} != {}".format(
        actual_data.shape, expected_data.shape
    )
    assert actual_data.shape == expected_data.shape, "Shape mismatch, {} != {}".format(
        actual_data.shape, expected_data.shape
    )

    for exp, act in zip(expected_data, actual_data):
        assert exp == act, "Data mismatch, {} != {}".format(exp, act)


def test_read_i16_f32():
    """
    Tests reading PCM16 as Float 32. Correctness is measured against soundfile
    """
    import soundfile as sf
    from pytest import approx

    expected_data, sr = sf.read(ONE_CHANNEL_I16, dtype=np.float32, always_2d=True)

    actual_data, sr = read(ONE_CHANNEL_I16, dtype=np.float32)

    assert actual_data.shape == expected_data.shape, "Shape mismatch, {} != {}".format(
        actual_data.shape, expected_data.shape
    )

    for exp, act in zip(expected_data, actual_data):
        assert exp == approx(act, 1e-4), "Data mismatch, {} != {}".format(exp, act)


def test_read_i16_f64():
    """
    Tests reading PCM16 as Float 64. Correctness is measured against soundfile
    """
    import soundfile as sf
    from pytest import approx

    expected_data, sr = sf.read(ONE_CHANNEL_I16, dtype=np.float64)

    actual_data, sr = read(ONE_CHANNEL_I16, dtype=np.float64)

    for exp, act in zip(expected_data, actual_data):
        assert exp == approx(act, 1e-4), "Data mismatch, {} != {}".format(exp, act)


def test_write_i16():
    """
    Tests writing PCM16 encoded files as PCM16. Correctness is measured against soundfile
    """
    import soundfile as sf
    import tempfile
    import os

    expected_data, sr = sf.read(ONE_CHANNEL_I16, dtype=np.int16, always_2d=True)

    with tempfile.NamedTemporaryFile(suffix=".wav") as fp:
        write(fp.name, expected_data, sr, dtype=np.int16)

        actual_data, actual_sr = sf.read(fp.name, dtype=np.int16)
        assert sr == actual_sr, "Sample rate mismatch, {} != {}".format(sr, actual_sr)
        for exp, act in zip(expected_data, actual_data):
            assert exp == act, "Data mismatch, {} != {}".format(exp, act)


def test_write_i32():
    """
    Tests writing PCM16 encoded files as int 32. Correctness is measured against soundfile
    """
    import soundfile as sf
    import tempfile
    import os

    expected_data, sr = sf.read(ONE_CHANNEL_I16, dtype=np.int32, always_2d=True)

    with tempfile.NamedTemporaryFile(suffix=".wav") as fp:
        write(fp.name, expected_data, sr, dtype=np.int32)

        actual_data, actual_sr = sf.read(fp.name, dtype=np.int32)
        assert sr == actual_sr, "Sample rate mismatch, {} != {}".format(sr, actual_sr)
        for exp, act in zip(expected_data, actual_data):
            assert exp == act, "Data mismatch, {} != {}".format(exp, act)


def test_write_f32():
    """
    Tests writing PCM16 encoded files as float 32. Correctness is measured against soundfile
    """
    import soundfile as sf
    import tempfile
    import os

    expected_data, sr = sf.read(ONE_CHANNEL_I16, dtype=np.float32, always_2d=True)

    with tempfile.NamedTemporaryFile(suffix=".wav") as fp:
        write(fp.name, expected_data, sr, dtype=np.float32)

        actual_data, actual_sr = sf.read(fp.name, dtype=np.float32)
        assert sr == actual_sr, "Sample rate mismatch, {} != {}".format(sr, actual_sr)
        for exp, act in zip(expected_data, actual_data):
            assert exp == act, "Data mismatch, {} != {}".format(exp, act)


def test_write_f64():
    """
    Tests writing PCM16 encoded files as float 64. Correctness is measured against soundfile
    """
    import soundfile as sf
    import tempfile
    import os

    expected_data, sr = sf.read(ONE_CHANNEL_I16, dtype=np.float64, always_2d=True)

    with tempfile.NamedTemporaryFile(suffix=".wav") as fp:
        write(fp.name, expected_data, sr, dtype=np.float64)

        actual_data, actual_sr = sf.read(fp.name, dtype=np.float64)
        assert sr == actual_sr, "Sample rate mismatch, {} != {}".format(sr, actual_sr)
        for exp, act in zip(expected_data, actual_data):
            assert exp == act, "Data mismatch, {} != {}".format(exp, act)


def test_info():
    """
    Tests the wav_spec function
    """
    expected_sr = 16000
    expected_channels = 1
    expected_duration = 10
    expected_encoding = pw.WavType.Pcm16
    sample_rate, n_channels, duration, encoding = spec(ONE_CHANNEL_I16)

    assert sample_rate == expected_sr, "Sample rate mismatch, {} != {}".format(
        sample_rate, expected_sr
    )

    assert n_channels == expected_channels, "Channel count mismatch, {} != {}".format(
        n_channels, expected_channels
    )

    assert duration == expected_duration, "Duration mismatch, {} != {}".format(
        duration, expected_duration
    )

    assert encoding == expected_encoding, "Encoding mismatch, {} != {}".format(
        encoding, expected_encoding
    )
