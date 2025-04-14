# HAM CW Encoder

Convert text into morse code CW wav-file.

## Installation

### Pip

`pip install -r requirements-cli.txt`

## Usage

Common usage:

```
Usage: cw.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  encode
```

Encode:

```
Usage: cw.py encode [OPTIONS] WAV_PATH TEXT

Options:
  -s, --sample_rate INTEGER  Output sample rate
  -f, --frequency INTEGER    Tone frequency
  -d, --dot_time FLOAT       Dot duration in seconds
  --help                     Show this message and exit.
```