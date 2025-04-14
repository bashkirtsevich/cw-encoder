import typing

SignalGen = typing.Generator[float, None, None]

Tone = typing.NamedTuple("Tone", [("freq", int), ("time", float)])

ToneGen = typing.Generator[Tone, None, None]
