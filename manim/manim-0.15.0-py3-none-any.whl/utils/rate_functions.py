"""A selection of rate functions, i.e., *speed curves* for animations.
Please find a standard list at https://easings.net/. Here is a picture
for the non-standard ones

.. manim:: RateFuncExample
    :save_last_frame:

    class RateFuncExample(Scene):
        def construct(self):
            x = VGroup()
            for k, v in rate_functions.__dict__.items():
                if "function" in str(v):
                    if (
                        not k.startswith("__")
                        and not k.startswith("sqrt")
                        and not k.startswith("bezier")
                    ):
                        try:
                            rate_func = v
                            plot = (
                                ParametricFunction(
                                    lambda x: [x, rate_func(x), 0],
                                    t_range=[0, 1, .01],
                                    use_smoothing=False,
                                    color=YELLOW,
                                )
                                .stretch_to_fit_width(1.5)
                                .stretch_to_fit_height(1)
                            )
                            plot_bg = SurroundingRectangle(plot).set_color(WHITE)
                            plot_title = (
                                Text(rate_func.__name__, weight=BOLD)
                                .scale(0.5)
                                .next_to(plot_bg, UP, buff=0.1)
                            )
                            x.add(VGroup(plot_bg, plot, plot_title))
                        except: # because functions `not_quite_there`, `function squish_rate_func` are not working.
                            pass
            x.arrange_in_grid(cols=8)
            x.height = config.frame_height
            x.width = config.frame_width
            x.move_to(ORIGIN).scale(0.95)
            self.add(x)


There are primarily 3 kinds of standard easing functions:

#. Ease In - The animation has a smooth start.
#. Ease Out - The animation has a smooth end.
#. Ease In Out - The animation has a smooth start as well as smooth end.

.. note:: The standard functions are not exported, so to use them you do something like this:
    rate_func=rate_functions.ease_in_sine
    On the other hand, the non-standard functions, which are used more commonly, are exported and can be used directly.

.. manim:: RateFunctions1Example

    class RateFunctions1Example(Scene):
        def construct(self):
            line1 = Line(3*LEFT, 3*RIGHT).shift(UP).set_color(RED)
            line2 = Line(3*LEFT, 3*RIGHT).set_color(GREEN)
            line3 = Line(3*LEFT, 3*RIGHT).shift(DOWN).set_color(BLUE)

            dot1 = Dot().move_to(line1.get_left())
            dot2 = Dot().move_to(line2.get_left())
            dot3 = Dot().move_to(line3.get_left())

            label1 = Tex("Ease In").next_to(line1, RIGHT)
            label2 = Tex("Ease out").next_to(line2, RIGHT)
            label3 = Tex("Ease In Out").next_to(line3, RIGHT)

            self.play(
                FadeIn(VGroup(line1, line2, line3)),
                FadeIn(VGroup(dot1, dot2, dot3)),
                Write(VGroup(label1, label2, label3)),
            )
            self.play(
                MoveAlongPath(dot1, line1, rate_func=rate_functions.ease_in_sine),
                MoveAlongPath(dot2, line2, rate_func=rate_functions.ease_out_sine),
                MoveAlongPath(dot3, line3, rate_func=rate_functions.ease_in_out_sine),
                run_time=7
            )
            self.wait()
"""


from __future__ import annotations

__all__ = [
    "linear",
    "smooth",
    "rush_into",
    "rush_from",
    "slow_into",
    "double_smooth",
    "there_and_back",
    "there_and_back_with_pause",
    "running_start",
    "not_quite_there",
    "wiggle",
    "squish_rate_func",
    "lingering",
    "exponential_decay",
]

import typing
from functools import wraps
from math import sqrt

import numpy as np

from ..utils.bezier import bezier
from ..utils.simple_functions import sigmoid


# This is a decorator that makes sure any function it's used on will
# return 0 if t<0 and 1 if t>1.
def unit_interval(function):
    @wraps(function)
    def wrapper(t, *args, **kwargs):
        if 0 <= t <= 1:
            return function(t, *args, **kwargs)
        elif t < 0:
            return 0
        else:
            return 1

    return wrapper


# This is a decorator that makes sure any function it's used on will
# return 0 if t<0 or t>1.
def zero(function):
    @wraps(function)
    def wrapper(t, *args, **kwargs):
        if 0 <= t <= 1:
            return function(t, *args, **kwargs)
        else:
            return 0

    return wrapper


@unit_interval
def linear(t: float) -> float:
    return t


@unit_interval
def smooth(t: float, inflection: float = 10.0) -> float:
    error = sigmoid(-inflection / 2)
    return min(
        max((sigmoid(inflection * (t - 0.5)) - error) / (1 - 2 * error), 0),
        1,
    )


@unit_interval
def rush_into(t: float, inflection: float = 10.0) -> float:
    return 2 * smooth(t / 2.0, inflection)


@unit_interval
def rush_from(t: float, inflection: float = 10.0) -> float:
    return 2 * smooth(t / 2.0 + 0.5, inflection) - 1


@unit_interval
def slow_into(t: float) -> float:
    return np.sqrt(1 - (1 - t) * (1 - t))


@unit_interval
def double_smooth(t: float) -> float:
    if t < 0.5:
        return 0.5 * smooth(2 * t)
    else:
        return 0.5 * (1 + smooth(2 * t - 1))


@zero
def there_and_back(t: float, inflection: float = 10.0) -> float:
    new_t = 2 * t if t < 0.5 else 2 * (1 - t)
    return smooth(new_t, inflection)


@zero
def there_and_back_with_pause(t: float, pause_ratio: float = 1.0 / 3) -> float:
    a = 1.0 / pause_ratio
    if t < 0.5 - pause_ratio / 2:
        return smooth(a * t)
    elif t < 0.5 + pause_ratio / 2:
        return 1
    else:
        return smooth(a - a * t)


@unit_interval
def running_start(
    t: float,
    pull_factor: float = -0.5,
) -> typing.Iterable:  # what is func return type?
    return bezier([0, 0, pull_factor, pull_factor, 1, 1, 1])(t)


def not_quite_there(
    func: typing.Callable[[float], float] = smooth,
    proportion: float = 0.7,
) -> typing.Callable[[float], float]:
    def result(t):
        return proportion * func(t)

    return result


@zero
def wiggle(t: float, wiggles: float = 2) -> float:
    return there_and_back(t) * np.sin(wiggles * np.pi * t)


def squish_rate_func(
    func: typing.Callable[[float], float],
    a: float = 0.4,
    b: float = 0.6,
) -> typing.Callable[[float], float]:
    def result(t):
        if a == b:
            return a

        if t < a:
            return func(0)
        elif t > b:
            return func(1)
        else:
            return func((t - a) / (b - a))

    return result


# Stylistically, should this take parameters (with default values)?
# Ultimately, the functionality is entirely subsumed by squish_rate_func,
# but it may be useful to have a nice name for with nice default params for
# "lingering", different from squish_rate_func's default params


@unit_interval
def lingering(t: float) -> float:
    return squish_rate_func(lambda t: t, 0, 0.8)(t)


@unit_interval
def exponential_decay(t: float, half_life: float = 0.1) -> float:
    # The half-life should be rather small to minimize
    # the cut-off error at the end
    return 1 - np.exp(-t / half_life)


@unit_interval
def ease_in_sine(t: float) -> float:
    return 1 - np.cos((t * np.pi) / 2)


@unit_interval
def ease_out_sine(t: float) -> float:
    return np.sin((t * np.pi) / 2)


@unit_interval
def ease_in_out_sine(t: float) -> float:
    return -(np.cos(np.pi * t) - 1) / 2


@unit_interval
def ease_in_quad(t: float) -> float:
    return t * t


@unit_interval
def ease_out_quad(t: float) -> float:
    return 1 - (1 - t) * (1 - t)


@unit_interval
def ease_in_out_quad(t: float) -> float:
    return 2 * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 2) / 2


@unit_interval
def ease_in_cubic(t: float) -> float:
    return t * t * t


@unit_interval
def ease_out_cubic(t: float) -> float:
    return 1 - pow(1 - t, 3)


@unit_interval
def ease_in_out_cubic(t: float) -> float:
    return 4 * t * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 3) / 2


@unit_interval
def ease_in_quart(t: float) -> float:
    return t * t * t * t


@unit_interval
def ease_out_quart(t: float) -> float:
    return 1 - pow(1 - t, 4)


@unit_interval
def ease_in_out_quart(t: float) -> float:
    return 8 * t * t * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 4) / 2


@unit_interval
def ease_in_quint(t: float) -> float:
    return t * t * t * t * t


@unit_interval
def ease_out_quint(t: float) -> float:
    return 1 - pow(1 - t, 5)


@unit_interval
def ease_in_out_quint(t: float) -> float:
    return 16 * t * t * t * t * t if t < 0.5 else 1 - pow(-2 * t + 2, 5) / 2


@unit_interval
def ease_in_expo(t: float) -> float:
    return 0 if t == 0 else pow(2, 10 * t - 10)


@unit_interval
def ease_out_expo(t: float) -> float:
    return 1 if t == 1 else 1 - pow(2, -10 * t)


@unit_interval
def ease_in_out_expo(t: float) -> float:
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t < 0.5:
        return pow(2, 20 * t - 10) / 2
    else:
        return (2 - pow(2, -20 * t + 10)) / 2


@unit_interval
def ease_in_circ(t: float) -> float:
    return 1 - sqrt(1 - pow(t, 2))


@unit_interval
def ease_out_circ(t: float) -> float:
    return sqrt(1 - pow(t - 1, 2))


@unit_interval
def ease_in_out_circ(t: float) -> float:
    return (
        (1 - sqrt(1 - pow(2 * t, 2))) / 2
        if t < 0.5
        else (sqrt(1 - pow(-2 * t + 2, 2)) + 1) / 2
    )


@unit_interval
def ease_in_back(t: float) -> float:
    c1 = 1.70158
    c3 = c1 + 1
    return c3 * t * t * t - c1 * t * t


@unit_interval
def ease_out_back(t: float) -> float:
    c1 = 1.70158
    c3 = c1 + 1
    return 1 + c3 * pow(t - 1, 3) + c1 * pow(t - 1, 2)


@unit_interval
def ease_in_out_back(t: float) -> float:
    c1 = 1.70158
    c2 = c1 * 1.525
    return (
        (pow(2 * t, 2) * ((c2 + 1) * 2 * t - c2)) / 2
        if t < 0.5
        else (pow(2 * t - 2, 2) * ((c2 + 1) * (t * 2 - 2) + c2) + 2) / 2
    )


@unit_interval
def ease_in_elastic(t: float) -> float:
    c4 = (2 * np.pi) / 3
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        return -pow(2, 10 * t - 10) * np.sin((t * 10 - 10.75) * c4)


@unit_interval
def ease_out_elastic(t: float) -> float:
    c4 = (2 * np.pi) / 3
    if t == 0:
        return 0
    elif t == 1:
        return 1
    else:
        return pow(2, -10 * t) * np.sin((t * 10 - 0.75) * c4) + 1


@unit_interval
def ease_in_out_elastic(t: float) -> float:
    c5 = (2 * np.pi) / 4.5
    if t == 0:
        return 0
    elif t == 1:
        return 1
    elif t < 0.5:
        return -(pow(2, 20 * t - 10) * np.sin((20 * t - 11.125) * c5)) / 2
    else:
        return (pow(2, -20 * t + 10) * np.sin((20 * t - 11.125) * c5)) / 2 + 1


@unit_interval
def ease_in_bounce(t: float) -> float:
    return 1 - ease_out_bounce(1 - t)


@unit_interval
def ease_out_bounce(t: float) -> float:
    n1 = 7.5625
    d1 = 2.75

    if t < 1 / d1:
        return n1 * t * t
    elif t < 2 / d1:
        return n1 * (t - 1.5 / d1) * (t - 1.5 / d1) + 0.75
    elif t < 2.5 / d1:
        return n1 * (t - 2.25 / d1) * (t - 2.25 / d1) + 0.9375
    else:
        return n1 * (t - 2.625 / d1) * (t - 2.625 / d1) + 0.984375


@unit_interval
def ease_in_out_bounce(t: float) -> float:
    if t < 0.5:
        return (1 - ease_out_bounce(1 - 2 * t)) / 2
    else:
        return (1 + ease_out_bounce(2 * t - 1)) / 2
