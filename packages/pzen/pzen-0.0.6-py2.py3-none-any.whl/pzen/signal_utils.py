from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np
from typing_extensions import assert_never

# -----------------------------------------------------------------------------
# Low-level API
# -----------------------------------------------------------------------------


def normalize(x: np.ndarray) -> np.ndarray:
    """
    Normalize signal to stay within [-1, +1], but leave the zero point unmodified.
    """
    abs_max = np.abs(x).max()
    if abs_max != 0:
        return x / abs_max
    else:
        return x


def normalize_min_max(x: np.ndarray, min: float = -1.0, max: float = 1.0) -> np.ndarray:
    """
    This function normalizes the min/max to [-1, +1].

    Note that this can be a bit confusing, because it may look like the output has a constant
    DC-offset.
    """
    orig_max = x.max()
    orig_min = x.min()

    if orig_max > orig_min:
        return min + (x - orig_min) / (orig_max - orig_min) * (max - min)
    else:
        return x


def pad_to_multiple_of(x: np.ndarray, block_size: int) -> np.ndarray:
    """
    Right-pad signal so that its length is a multiple of `block_size`.
    """
    assert block_size > 0
    n_pad = (block_size - len(x) % block_size) % block_size
    x = np.pad(x, (0, n_pad))
    return x


# -----------------------------------------------------------------------------
# High-level API
# -----------------------------------------------------------------------------


@dataclass
class Samples:
    value: int


@dataclass
class Seconds:
    value: float


"""
Note on naming: Alternative names considered 'Duration' or 'Length'. While most usages
actually are semantically more a "duration" or "length" there can also be usages that
are semantically an "offset", which would make duration/length awkward. `t: Time` is
short and works reasonable well for both.
"""
Time = Samples | Seconds


def in_samples(t: Time | None, sr: int) -> int:
    if t is None:
        return 0
    elif isinstance(t, Samples):
        return t.value
    elif isinstance(t, Seconds):
        return round(t.value * sr)
    else:
        assert_never(t)


LinLog = Literal["lin", "log"]
LinExp = Literal["lin", "exp"]

Quantity = Literal["root-power", "power"]


@dataclass
class Signal:
    """
    High-level wrapper of signals.

    Note on naming: Alternative names considered 'Audio' or 'Wave'. However, this class
    is more general than audio/wave signals, because it could also be used for other
    kind of signals like amplitude envelops, frequency sequences, phases, etc.
    """

    x: np.ndarray
    sr: int

    def __post_init__(self) -> None:
        # Invariants
        assert self.x.ndim == 1, f"Signals must have a dimension of 1, but is {self.x.ndim}"
        assert self.sr > 0

    # Construction helpers

    @staticmethod
    def empty(sr: int) -> Signal:
        return Signal(x=np.array([]), sr=sr)

    @staticmethod
    def zeros(t: Time, sr: int) -> Signal:
        n = in_samples(t, sr)
        return Signal(x=np.zeros(n), sr=sr)

    @staticmethod
    def ones(t: Time, sr: int) -> Signal:
        n = in_samples(t, sr)
        return Signal(x=np.ones(n), sr=sr)

    @staticmethod
    def full(t: Time, value: float, sr: int) -> Signal:
        n = in_samples(t, sr)
        return Signal(x=np.full(n, value), sr=sr)

    # Basic operators

    def __len__(self) -> int:
        return len(self.x)

    def __add__(self, other: Signal) -> Signal:
        assert (
            self.sr == other.sr
        ), f"Can only add signals of same sample rate, but {self.sr} != {other.sr}"
        assert len(self) == len(other), (
            f"Trying to add signals with different lengths ({len(self)} != {len(other)}). "
            "Use `mix_at` if implicit length extension is desired."
        )
        return Signal(x=self.x + other.x, sr=self.sr)

    def __mul__(self, other: Signal) -> Signal:
        assert (
            self.sr == other.sr
        ), f"Can only multiply signals of same sample rate, but {self.sr} != {other.sr}"
        assert len(self) == len(
            other
        ), f"Trying to multiply signals with different lengths ({len(self)} != {len(other)})."
        return Signal(x=self.x * other.x, sr=self.sr)

    # Misc

    @property
    def unpack(self) -> tuple[np.ndarray, int]:
        return self.x, self.sr

    def in_samples(self, t: Time | None) -> int:
        return in_samples(t, self.sr)

    def len(self) -> int:
        """Convenience alternative to __len__ for more fluent API."""
        return len(self)

    def len_in_sec(self) -> float:
        return len(self) / self.sr

    # Basic element-wise (shape preserving) operations

    def scale(self, factor: float) -> Signal:
        return Signal(factor * self.x, self.sr)

    def abs(self) -> Signal:
        return Signal(np.abs(self.x), self.sr)

    def square(self) -> Signal:
        return Signal(self.x * self.x, self.sr)

    def normalize(self) -> Signal:
        return Signal(normalize(self.x), self.sr)

    def normalize_min_max(self, min: float = -1.0, max: float = 1.0) -> Signal:
        return Signal(normalize_min_max(self.x, min, max), self.sr)

    def into_exp_envelope(self, min_db: float = -80.0, quantity: Quantity = "root-power") -> Signal:
        """
        Converts a given (linear) envelope, assumed to be in [0.0, 1.0] to an equivalent _exponentially_
        scaled envelope to counter the _logarithmic_ perception of loudness.

        Due to the nature of the conversion, a minimum level has to be specified, which is easiest
        to do in terms of decibel. Downside: The conversion from decibel to a plain factor requires
        to clarify to quantity semantics, i.e., "root-power quantity" or "power quantity". Since
        envelopes typically operate on amplitude level, which are root-power quantities, we default
        to "root-power".
        """
        decibels = self.normalize_min_max(min_db, 0.0).x
        if quantity == "root-power":
            factors = 10 ** (decibels / 20)
        elif quantity == "power":
            factors = 10 ** (decibels / 10)
        else:
            assert_never(quantity)
        return Signal(x=factors, sr=self.sr)

    # Length affecting operations

    def pad(self, *, pad_l: Time | None = None, pad_r: Time | None = None) -> Signal:
        n_pad_l = self.in_samples(pad_l)
        n_pad_r = self.in_samples(pad_r)
        x = np.pad(self.x, (n_pad_l, n_pad_r))
        return Signal(x, self.sr)

    def pad_to_multiple_of(self, block_size: Time) -> Signal:
        x = pad_to_multiple_of(self.x, block_size=self.in_samples(block_size))
        return Signal(x, self.sr)

    def concat(self, other: Signal) -> Signal:
        assert (
            self.sr == other.sr
        ), f"Can only concatenate signals of same sample rate, but {self.sr} != {other.sr}"
        return Signal(x=np.concatenate([self.x, other.x]), sr=self.sr)

    # Advanced operations

    def mix_at(self, offset: Time, other: Signal, allow_extend: bool = True) -> Signal:
        assert (
            self.sr == other.sr
        ), f"Can only mix signals of same sample rate, but {self.sr} != {other.sr}"

        offset_index = self.in_samples(offset)
        if offset_index < 0:
            raise ValueError(f"Negative offset indices ({offset_index}) are not supported")
        required_len = offset_index + other.len()

        if required_len > self.len():
            if not allow_extend:
                raise ValueError(
                    f"Mixing signal would require a length of {required_len}, "
                    f"but signal only has length {self.len()}"
                )
            x = np.pad(self.x, (0, required_len - self.len()))
        else:
            x = self.x.copy()

        x[offset_index : offset_index + other.len()] += other.x
        return Signal(x=x, sr=self.sr)

    # Envelope modulations

    def envelope_ramped(self, kind: LinExp, t_l: Time, t_r: Time | None = None) -> Signal:
        gen = SignalGenerator(self.sr)
        envelope = gen.envelope_ramped(Samples(self.len()), t_l, t_r)
        if kind == "exp":
            envelope = envelope.into_exp_envelope()
        return envelope * self


# -----------------------------------------------------------------------------
# Generator API
# -----------------------------------------------------------------------------


DEFAULT_TIME = Seconds(1.0)


class SignalGenerator:
    def __init__(self, sr: int):
        self.sr = sr

    def _in_samples(self, t: Time) -> int:
        return in_samples(t, self.sr)

    def _make_signal(self, x: np.ndarray) -> Signal:
        return Signal(x=x, sr=self.sr)

    # Forwarded construction helpers

    def empty(self) -> Signal:
        return Signal.empty(sr=self.sr)

    def zeros(self, t: Time) -> Signal:
        return Signal.zeros(t, sr=self.sr)

    def ones(self, t: Time) -> Signal:
        return Signal.ones(t, sr=self.sr)

    def full(self, t: Time, value: float) -> Signal:
        return Signal.full(t, value, sr=self.sr)

    # General purpose generators

    def ramp(self, t: Time, start: float = 0.0, end: float = 1.0) -> Signal:
        n = self._in_samples(t)
        return self._make_signal(np.linspace(start, end, n))

    # Possible extension would be to have `multi_ramp` that takes a vararg of
    # tuples of (delta: Time, value: float), allowing to chain linear ramps

    # Envelope generators

    def envelope_ramped(self, t: Time, t_l: Time, t_r: Time | None = None) -> Signal:
        """
        Returns an envelope that ramps up from 0 -> 1 and back from 1 -> 0.
        """
        if t_r is None:
            t_r = t_l
        n = self._in_samples(t)
        n_l = self._in_samples(t_l)
        n_r = self._in_samples(t_r)
        ramp_l = np.linspace(0.0, 1.0, n_l + 1)[1:-1]
        ramp_r = np.linspace(1.0, 0.0, n_r + 1)[1:-1]

        n_l = len(ramp_l)
        n_r = len(ramp_r)

        if n_l + n_r <= n:
            x = np.ones(n)
            x[: len(ramp_l)] = ramp_l
            x[n - len(ramp_r) :] = ramp_r
            return self._make_signal(x)
        else:
            if n_l < n:
                x1 = np.pad(ramp_l, (0, n - n_l), constant_values=1.0)
            else:
                x1 = ramp_l[:n]
            if n_r < n:
                x2 = np.pad(ramp_r, (n - n_r, 0), constant_values=1.0)
            else:
                x2 = ramp_r[-n:]
            return self._make_signal(np.minimum(x1, x2))

    # Frequency generators

    def vibrato(
        self,
        t: Time,
        f: float,
        f_vibrato: float = 6.0,
        semitones: float = 0.3,
        t_l: Time = Seconds(0.1),
        t_r: Time | None = None,
    ) -> Signal:
        if t_r is None:
            t_r = t_l

        modulation_strength = Signal.ones(t, sr=self.sr).envelope_ramped("lin", t_l, t_r).x
        modulation = modulation_strength * self.sine(freq=f_vibrato, t=t).scale(semitones).x

        factors = 2 ** (modulation / 12.0)
        freqs = f * factors

        return self._make_signal(freqs)

    def sweep(
        self,
        t: Time,
        f1: float,
        f2: float,
    ) -> Signal:
        n = self._in_samples(t)
        ratio = f2 / f1
        freqs = f1 * np.exp(np.linspace(0.0, np.log(ratio), n))
        return self._make_signal(freqs)

    # Audio-like generators

    def silence(self, t: Time = DEFAULT_TIME) -> Signal:
        # Technically redundant to `zeros` but alias can express intent better.
        return Signal.zeros(t, self.sr)

    def sine(
        self, freq: float = 440.0, t: Time = DEFAULT_TIME, phase_offset: float = 0.0
    ) -> Signal:
        """
        Generate perfect sine from a frequency.
        """
        n = self._in_samples(t)
        ts = np.arange(n) / self.sr
        x = np.sin(phase_offset + 2.0 * np.pi * freq * ts)
        return self._make_signal(x)

    def sine_from_freqs(self, freqs: Signal, phase_offset: float = 0.0) -> Signal:
        assert self.sr == freqs.sr
        phases = np.cumsum(freqs.x) / self.sr
        x = np.sin(phase_offset + 2.0 * np.pi * phases)
        return self._make_signal(x)
