from typing import List

from day_08.data import RAW_DATA

WIDE = 25
TALL = 6


def to_layers(raw: str, wide: int, tall: int) -> List[str]:
    wides = list(chunks(raw, wide))
    layers = list(chunks(wides, tall))
    return [''.join(layer) for layer in layers]


def chunks(iterable, size):
    float_chunk_count = len(iterable) / size
    chunk_count = int(float_chunk_count)
    if chunk_count != float_chunk_count:
        raise ValueError(f'Wrong chunk size')

    for i in range(0, chunk_count):
        yield iterable[i * size: (i + 1) * size]


def render_pixel(image: List[str], pixel_idx: int) -> str:
    for layer in image:
        if layer[pixel_idx] == '2':
            continue
        return layer[pixel_idx]


def render_image(image: List[str], wide):
    rendered = []
    for i in range(len(image[0])):
        rendered.append(render_pixel(image, i))
        if (i + 1) % wide == 0:
            rendered.append('\n')
    return ''.join(rendered)


def main():
    layers = to_layers(RAW_DATA, WIDE, TALL)
    min_zero_cnt, best_layer_idx = layers[0].count('0'), '0'
    for idx, layer in enumerate(layers[1:], start=1):
        zero_cnt = layer.count('0')
        if zero_cnt < min_zero_cnt:
            min_zero_cnt = zero_cnt
            best_layer_idx = idx

    ones = layers[best_layer_idx].count('1')
    twos = layers[best_layer_idx].count('2')
    print(ones * twos)

    rendered = render_image(layers, WIDE)
    print(rendered.replace('1', '#').replace('0', ' '))


if __name__ == '__main__':
    main()
