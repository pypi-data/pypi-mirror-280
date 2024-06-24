from typing import Any, List, Union, Dict
from django.db.models import Model


class SetPropertyException(Exception):
    pass


class ManagesProperties:
    def __init__(self):
        self.validation_rules: Dict[str, Any] = {}

    def set_property(self, attr: str, value: Any, with_hooks: bool = True) -> None:
        """Set a property on the component, handling complex nested paths."""
        segments = self._parse_property_path(attr)
        base_attr = segments[0]
    
        if not self._is_public(base_attr):
            raise SetPropertyException(f'Attribute "{base_attr}" is not public.')
    
        try:
            self._set_nested_property(self, segments, value, attr)
            if with_hooks:
                self._invoke_hooks(base_attr, '.'.join(segments[1:]), value)
        except (AttributeError, KeyError, IndexError, TypeError) as e:
            raise SetPropertyException(f'Error setting property "{attr}": {str(e)}')

    def _parse_property_path(self, path: str) -> List[Union[str, int]]:
        """Parse a property path into segments, handling both dot notation and list indices."""
        segments = []
        for segment in path.replace('[', '.[').split('.'):
            if segment.startswith('[') and segment.endswith(']'):
                segments.append(int(segment[1:-1]))
            elif segment:
                segments.append(segment)
        return segments

    def _set_nested_property(self, obj: Any, segments: List[Union[str, int]], value: Any, original_attr: str) -> None:
        """Recursively set a nested property."""
        if len(segments) == 1:
            self._set_final_property(obj, segments[0], value, original_attr)
        else:
            next_obj = self._get_next_object(obj, segments[0])
            remaining_path = '.'.join(segments[1:])
            self._set_nested_property(next_obj, segments[1:], value, f"{original_attr}.{remaining_path}")

    def _get_next_object(self, obj: Any, segment: Union[str, int]) -> Any:
        """Get the next object in the nested structure."""
        if isinstance(segment, int):
            if isinstance(obj, list):
                if segment >= len(obj):
                    raise IndexError(f'List index {segment} out of range')
                return obj[segment]
            else:
                raise TypeError(f'Cannot use integer index {segment} on non-list object')
        elif isinstance(obj, dict):
            if segment not in obj:
                raise KeyError(f'Key "{segment}" not found in dictionary')
            return obj[segment]
        elif hasattr(obj, segment):
            return getattr(obj, segment)
        else:
            raise AttributeError(f'Attribute "{segment}" not found')

    def _set_final_property(self, obj: Any, segment: Union[str, int], value: Any, full_path: str) -> None:
        """Set the final property value."""
        if isinstance(segment, int):
            if isinstance(obj, list):
                if segment >= len(obj):
                    raise IndexError(f'List index {segment} out of range')
                obj[segment] = value
            else:
                raise TypeError(f'Cannot use integer index {segment} on non-list object')
        elif isinstance(obj, dict):
            print(obj)
            obj[segment] = value
        elif isinstance(obj, Model):
            if hasattr(self, 'validation_rules') and full_path in self.validation_rules:
                setattr(obj, segment, value)
            else:
                print('NO')
                raise SetPropertyException(f"'{full_path}' is not a valid key in the validation_rules.")
        else:
            setattr(obj, segment, value)

    def _invoke_hooks(self, base_attr: str, remaining_path: str, value: Any) -> None:
        # Specific hook for the property
        updated_hook_name = f"updated_{base_attr}"
        if hasattr(self, updated_hook_name):
            if remaining_path:
                getattr(self, updated_hook_name)(remaining_path, value)
            else:
                getattr(self, updated_hook_name)(value)

        # General update hook
        if hasattr(self, "updated"):
            full_path = f"{base_attr}.{remaining_path}" if remaining_path else base_attr
            getattr(self, "updated")(full_path, value)

    def _is_public(self, name: str) -> bool:
        """Determines if the name should be considered public."""
        protected_names = (
            "render", "request", "as_view", "view", "args", "kwargs", "content_type",
            "extra_context", "http_method_names", "template_engine", "template_name",
            "dispatch", "id", "get", "get_context_data", "get_template_names",
            "render_to_response", "http_method_not_allowed", "options", "setup",
            "fill", "view_is_async", "component_id", "component_name", "component_key",
            "reset", "mount", "hydrate", "updating", "update", "calling", "called",
            "complete", "rendered", "parent_rendered", "validate", "is_valid", "errors",
            "updated", "parent", "children", "call", "js_calls", "event_calls",
            "component_cache_key", "inline_template", "placeholder", "processed_query_params",
            "query_params", "validation_rules"
        )
        return not (name.startswith("_") or name in protected_names)

    def get_property(self, attr: str) -> Any:
        """Get a property value, handling complex nested paths."""
        segments = self._parse_property_path(attr)
        obj = self
        for segment in segments:
            obj = self._get_next_object(obj, segment)
        return obj
