import gc
from collections.abc import Iterable
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from .core_types import StrPath

_DEFAULT_FIGSIZE = (12, 8)


@contextmanager
def plot(
    figsize: tuple[float, float] = _DEFAULT_FIGSIZE,
    fig_title: str | None = None,
    interactive: bool = False,
    save_as: StrPath | None = None,
    run_gc_collection: bool = False,
) -> Generator[tuple[Figure, Axes], None, None]:
    with _subplots_wrapper(
        nrows=1,
        ncols=1,
        figsize=figsize,
        fig_title=fig_title,
        interactive=interactive,
        save_as=save_as,
        sharex=False,
        sharey=False,
        run_gc_collection=run_gc_collection,
    ) as (fig, axes):
        assert isinstance(axes, Axes)
        yield fig, axes


@contextmanager
def plot_rows(
    nrows: int,
    figsize: tuple[float, float] = _DEFAULT_FIGSIZE,
    fig_title: str | None = None,
    interactive: bool = False,
    save_as: StrPath | None = None,
    sharex: bool = True,
    run_gc_collection: bool = False,
) -> Generator[tuple[Figure, list[Axes]], None, None]:
    with _subplots_wrapper(
        nrows=nrows,
        ncols=1,
        figsize=figsize,
        fig_title=fig_title,
        interactive=interactive,
        save_as=save_as,
        sharex=sharex,
        sharey=False,
        run_gc_collection=run_gc_collection,
    ) as (fig, axes):
        # Note that matplotlib returns a numpy array, which is type erasing and
        # has no practical benefits to me. Therefore, convert to a list.
        axes = list(axes)
        assert all(isinstance(ax, Axes) for ax in axes)
        yield fig, axes


@contextmanager
def plot_cols(
    ncols: int,
    figsize: tuple[float, float] = _DEFAULT_FIGSIZE,
    fig_title: str | None = None,
    interactive: bool = False,
    save_as: StrPath | None = None,
    sharey: bool = True,
    run_gc_collection: bool = False,
) -> Generator[tuple[Figure, list[Axes]], None, None]:
    with _subplots_wrapper(
        nrows=1,
        ncols=ncols,
        figsize=figsize,
        fig_title=fig_title,
        interactive=interactive,
        save_as=save_as,
        sharex=False,
        sharey=sharey,
        run_gc_collection=run_gc_collection,
    ) as (fig, axes):
        # Note that matplotlib returns a numpy array, which is type erasing and
        # has no practical benefits to me. Therefore, convert to a list.
        axes = list(axes)
        assert all(isinstance(ax, Axes) for ax in axes)
        yield fig, axes


@contextmanager
def _subplots_wrapper(
    nrows: int,
    ncols: int,
    figsize: tuple[float, float],
    fig_title: str | None,
    interactive: bool,
    save_as: StrPath | None,
    sharex: bool,
    sharey: bool,
    run_gc_collection: bool,
) -> Generator[tuple[Figure, Any], None, None]:

    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=figsize,
        sharex=sharex,
        sharey=sharey,
    )
    if fig_title is not None:
        fig.suptitle(fig_title)

    if isinstance(axes, Iterable):
        for ax in axes:
            ax.grid()
    else:
        axes.grid()

    try:
        yield fig, axes
    finally:
        fig.tight_layout()

        if interactive:
            plt.show()

        if save_as is not None:
            Path(save_as).parent.mkdir(parents=True, exist_ok=True)
            fig.savefig(str(save_as))

        plt.close(fig)

        # Work-around for plotting in a multi-processing environment (e.g. during
        # using a torch data loader).
        if run_gc_collection:
            gc.collect()
