import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "searchbar_component",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("searchbar_component", path=build_dir)

def searchbar(key=None):
    """Create a new instance of "searchbar".
    Parameters
    ----------
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.
    Returns
    -------
    str
        The selected or typed value in the searchbar.
    """
    component_value = _component_func(key=key, default="")
    return component_value

__all__ = ["searchbar"]
