import numpy as np
from scipy.io.wavfile import write

from cw.utils import text_to_morse, cw_synth


def main(wav_path: str, text: str, sample_rate=11025):
    amplitude = np.iinfo(np.int16).max
    tones = text_to_morse(text.upper())
    signal = np.fromiter(cw_synth(sample_rate, tones), dtype=np.float32) * amplitude

    write(wav_path, sample_rate, signal.astype(np.int16))


if __name__ == '__main__':
    main(
        wav_path="examples/morse.wav",
        text=" ".join(c for c in "VVV N  DE R9FEU THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG 0123456789,.?")
    )
