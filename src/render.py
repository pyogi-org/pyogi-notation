import math
from typing import List

from parse import Note
from svg import SVG, Point

svg = SVG(margin=50)


NUM_NOTES = 7

WHOLE_NOTE_WIDTH = 50
STAFF_SPACE_HEIGHT = 10
EDGE_NOTE_PADDING = 20
HALF_STAFF_SPACE = STAFF_SPACE_HEIGHT / 2
STAFF_HEIGHT = NUM_NOTES * HALF_STAFF_SPACE


def draw_note(note: Note, point: Point, color: str) -> None:
    accidental = note.accidental
    if accidental == "natural":
        svg.circle(point, HALF_STAFF_SPACE, color)
    elif accidental == "sharp":
        svg.polygon(
            [
                Point(point.x - HALF_STAFF_SPACE, point.y - HALF_STAFF_SPACE),
                Point(point.x - HALF_STAFF_SPACE, point.y + HALF_STAFF_SPACE),
                Point(point.x + HALF_STAFF_SPACE, point.y),
            ],
            color,
        )


def line_width_at_index(index: int) -> int:
    index %= NUM_NOTES
    if index == 0:
        return 2
    if index in [2, 5]:
        return 1
    return 0


def draw_notes(origin: Point, notes: List[Note]) -> None:
    origin.y += 2 * STAFF_HEIGHT  # Start from the middle
    for note in notes:
        position = Point(
            origin.x + (note.time * WHOLE_NOTE_WIDTH),
            origin.y - (note.note * HALF_STAFF_SPACE),
        )
        color = {
            0: "black",
            1: "red",
            2: "blue",
        }.get(note.part, "black")
        draw_note(note, position, color)


def draw_staff(origin: Point, width: float) -> None:
    for i in range(8):
        line_width = line_width_at_index(i)
        if line_width > 0:
            line_y = origin.y + STAFF_HEIGHT - (i * HALF_STAFF_SPACE)
            svg.line(
                Point(origin.x, line_y),
                Point(origin.x + width, line_y),
                line_width,
            )


def draw_staves(origin: Point, count: int, width: float) -> None:
    for i in range(count):
        draw_staff(Point(origin.x, origin.y + (i * STAFF_HEIGHT)), width)


def render(score: List[Note]) -> str:
    min_note = min(note.note for note in score)
    max_note = max(note.note for note in score)
    # TODO: More accurate so it knows e.g. if all notes are within same octave or not
    num_staves = math.ceil((max_note - min_note) / NUM_NOTES) + 1
    width = max(note.time for note in score) * WHOLE_NOTE_WIDTH
    draw_staves(Point(0, 0), num_staves, width + (2 * EDGE_NOTE_PADDING))
    draw_notes(Point(EDGE_NOTE_PADDING, (num_staves - 1) * STAFF_HEIGHT), score)
    return str(svg)
