import click
import numpy as np
from scipy.io.wavfile import write

from cw import text_to_morse, cw_synth


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("wav_path", type=click.Path(exists=False, dir_okay=False))
@click.argument("text", type=click.STRING)
@click.option("-s", "--sample_rate", type=click.INT, default=11025,
              help="Output sample rate")
@click.option("-f", "--frequency", type=click.INT, default=1000,
              help="Tone frequency")
@click.option("-d", "--dot_time", type=click.FLOAT, default=0.06,
              help="Dot duration in seconds")
def encode(wav_path: str, text: str, sample_rate: int, frequency: int, dot_time: float) -> None:
    message = " ".join(c for c in text.upper())
    tones = text_to_morse(message, freq=frequency, dot_time=dot_time)

    amplitude = np.iinfo(np.int16).max
    signal = np.fromiter(cw_synth(sample_rate, tones), dtype=np.float32) * amplitude

    write(wav_path, sample_rate, signal.astype(np.int16))


if __name__ == '__main__':
    main()
