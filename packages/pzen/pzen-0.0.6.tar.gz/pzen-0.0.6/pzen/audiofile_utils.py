from pathlib import Path
from typing import Literal, overload

import librosa
import numpy as np
import soundfile
import torch

from .cache_utils import with_memory
from .core_types import StrPath
from .signal_utils import Signal, normalize, normalize_min_max


@with_memory
def load_resampled(
    path: StrPath,
    sr: int,
    offset_sec: float = 0.0,
    duration_sec: float | None = None,
    duration_samples: int | None = None,
) -> Signal:
    """
    Wrapper around librosa.load (because resampling can be somewhat slow, and I prefer
    the more explicit caching approach).
    """
    print(f"Loading audio from '{path}' at sample rate {sr}...")
    signal, sampling_rate_loaded = librosa.load(
        path, sr=sr, offset=offset_sec, duration=duration_sec
    )
    assert sampling_rate_loaded == sr
    if duration_samples is not None:
        signal = signal[:duration_samples]
    return Signal(x=signal, sr=sr)


@overload
def soundfile_write(
    path: StrPath,
    data: np.ndarray | torch.Tensor,
    sr: int,
    *,
    clip: Literal["normalize", "normalize_min_max", "ignore", "warn", "error"] = "warn",
) -> None: ...


@overload
def soundfile_write(
    path: StrPath,
    data: Signal,
    *,
    clip: Literal["normalize", "normalize_min_max", "ignore", "warn", "error"] = "warn",
) -> None: ...


def soundfile_write(
    path: StrPath,
    data: np.ndarray | torch.Tensor | Signal,
    sr: int | None = None,
    *,
    clip: Literal["normalize", "normalize_min_max", "ignore", "warn", "error"] = "warn",
) -> None:
    """
    Wrapper for soundfile.write with improvements:
    - allow normalization (apparently default behavior is to clip, see
      https://stackoverflow.com/q/69388531/1804173)
    - warn if clip
    - nan check
    - torch support
    - support pathlib and str
    - output path creation
    """

    if isinstance(data, torch.Tensor):
        data = data.detach().cpu().numpy()
    elif isinstance(data, Signal):
        sr = data.sr
        data = data.x

    assert sr is not None
    assert isinstance(data, np.ndarray)
    assert np.all(np.isfinite(data)), "Audio data contains NaNs or Infs."

    if clip == "normalize":
        data = normalize(data)

    elif clip == "normalize_min_max":
        data = normalize_min_max(data)

    else:
        num_clipped = int(np.sum(data > +1.0)) + int(np.sum(data < -1.0))
        if num_clipped > 0:
            msg = f"Audio data contains {num_clipped} clipped samples (out of {len(data)})"
            if clip == "error":
                raise ValueError(msg)
            elif clip == "warn":
                print(f"WARNING: {msg}")

    Path(path).parent.mkdir(exist_ok=True, parents=True)
    soundfile.write(str(path), data, sr)
