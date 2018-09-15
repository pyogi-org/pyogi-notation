# notation

Reading music sheets is hard. All I want to know is roughly where to put my fingers on the piano. Note length, tempo, velocity and other stuff are minor worries in comparison. Those things can be _felt_, without learning.

I wanted to create a simple, consistent music notation, along with parsers and converters. Turns out writing beautiful renderers is hard, and it can get quite messy with the variety of sheets out there. I haven't yet had the motivation to finish the code, so instead for some peace of mind, I'm documenting the envisioned notation here.

## Stave

![](stem.svg)

## Note

### Head

#### Natural

#### Sharp

#### Flat

### Stem

Assuming `d` is the [note value](https://en.wikipedia.org/wiki/Note_value) (where 1 is a whole note), the stem length is `(log2(1 / d) + 1) * c`. If `d` is 1, the stem length is 0.
