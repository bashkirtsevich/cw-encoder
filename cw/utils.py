import math
import typing

from .consts import MORSE_TABLE, MORSE_DOT, MORSE_DASH, MORSE_SPACE
from .types import Tone, SignalGen, ToneGen


def cw_synth(sample_rate: int, tones: typing.Iterable[Tone]) -> SignalGen:
    spms = sample_rate / 1000
    factor = 2 * math.pi / sample_rate

    for freq, sec in tones:
        samples = int(spms * sec * 1000)
        freq_factor = freq * factor

        for sample in range(samples):
            yield math.sin(sample * freq_factor)


def text_to_morse(text: str, freq: int = 1000, dot_time: float = 0.06, freq_silence: int = 0) -> ToneGen:
    dash_time = dot_time * 3
    sep_time = dot_time
    space_time = dot_time

    for liter in text:
        if not (code := MORSE_TABLE.get(liter)):
            continue

        for c in code:
            if c == MORSE_DOT:
                yield Tone(freq, dot_time)

            elif c == MORSE_DASH:
                yield Tone(freq, dash_time)

            elif c == MORSE_SPACE:
                yield Tone(freq_silence, space_time)

            else:
                raise ValueError(f"Unexpected literal '{c}'")

            yield Tone(freq_silence, sep_time)
