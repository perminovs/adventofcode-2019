import pytest

from day_08.solution import to_layers, render_image


@pytest.mark.parametrize('raw, wide, tall, expected', [
    (
        '123456789012',
        3,
        2,
        [
            '123456',
            '789012',
        ],
    )
])
def test_to_layers(raw, wide, tall, expected):
    assert list(to_layers(raw, wide, tall)) == expected


@pytest.mark.parametrize('image, wide, expected', [
    (
        [
            '0222',
            '1122',
            '2212',
            '0000',
        ],
        2,
        '01\n10\n'
    ),
])
def test_render(image, wide, expected):
    assert render_image(image, wide) == expected
