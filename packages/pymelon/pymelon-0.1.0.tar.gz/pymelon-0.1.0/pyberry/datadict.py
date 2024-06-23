from collections import defaultdict
from typing import Any


class DataDict(list):
    def __init__(self, data) -> None:
        super().__init__(data)

        self.data = data
        self.keys, self.all_types = self._get_keys_and_types()

    def _get_keys_and_types(self) -> tuple[list, dict[Any, list]]:
        """
        Extracts and returns the keys and their corresponding types from a list of dicts.

        This method processes a list of dicts, extracting each dict's keys as keys and
        the types of their corresponding values. It ensures that all entries in the list are dicts
        and aggregates the types of values associated with each key across all dicts.

        Returns:
            tuple[list, dict[Any, list]]: A tuple containing:
                - A list of unique key names found across all dicts.
                - A dict mapping each key to a list of unique types of values associated with that key.
        """

        if not isinstance(self.data, list):
            raise ValueError(f"Input should be a list - got: {type(self.data)}")

        keys = []
        all_types = defaultdict(list)

        for item in self.data:
            if not isinstance(item, dict):
                raise ValueError(
                    f"Input should be a list of dicts - got: {type(item)} in list"
                )

            for key in item.keys():
                if key not in keys:
                    keys.append(key)

                if type(item[key]) not in all_types[key]:
                    all_types[key].append(type(item[key]))

        return keys, dict(all_types)

    def _to_datadict(self, data: list[dict]) -> "DataDict":
        """
        Converts a list of dicts to a DataDict object.

        Args:
            data (list[dict]): A list of dicts to be converted to a DataDict object.

        Returns:
            DataDict: A DataDict object containing the list of dicts.
        """

        return DataDict(data)

    def _get_nested_value(self, record: dict, key_path: str) -> Any:
        """
        Helper method to get a nested value from a dictionary.

        Args:
            record (dict): The dictionary to search for the nested value.
            key_path (str): The path to the nested value.
            Each key in the key_path is seperated by a delimiter.
            The default delimiter is ".".

        Returns:
            Any: The nested value if found, None otherwise.
        """

        current_value = record
        for key in key_path.split("."):
            if isinstance(current_value, dict) and key in current_value:
                current_value = current_value[key]
            else:
                return None
        return current_value

    def select(self, *keys: str) -> "DataDict":
        """
        Selects and returns a DataDict object with the specified keys.
        The DataDict object can be treated exactly like a list of dicts, but can also perform more complex queries

        Args:
            *keys (str): The keys to select. This can be any number of keys found in the DataDict.
            Each additional key to select can be added as a new unnamed argument. For example:
            DataDict.select("name", "age")
            Nested keys can be accessed by using a delimiter (default is "."). For example: "user.name". So this query would also be valid:
            DataDict.select("name", "age", "user.name")

        Returns:
            DataDict: A DataDict object containing the selected dicts.
            The DataDict object can be treated exactly like a list of dicts, but can also perform more complex queries
        """

        result = []

        for item in self.data:
            selected_item = {}
            for key in keys:
                nested_value = self._get_nested_value(item, key)
                if nested_value is not None:
                    key = key.replace(".", "_")
                    selected_item[key] = nested_value
            if selected_item:
                result.append(selected_item)
        return self._to_datadict(result)

    def where(self, key: str, comparison: str, value: Any) -> "DataDict":
        """
        Filters the DataDict object based on the specified field and comparison.
        The DataDict object can be treated exactly like a list of dicts, but can also perform more complex queries.

        Args:
            key (str): The key to filter by. This can be any key found in the DataDict.
            comparison (str): The comparison operator to use. This can be any comparison operator found in the DataDict.
            value (Any): The value to compare the field to.

        Returns:
            DataDict: A DataDict object containing the filtered dicts.
            The DataDict object can be treated exactly like a list of dicts, but can also perform more complex queries.
        """

        result = []

        def get_nested_value(item: dict, key_path: str) -> Any:
            current_value = item
            for key in key_path.split("."):
                if isinstance(current_value, dict) and key in current_value:
                    current_value = current_value[key]
                else:
                    return None
            return current_value

        for item in self.data:
            key_value = get_nested_value(item, key)
            if key_value is not None:
                if comparison == "==" and key_value == value:
                    result.append(item)
                elif comparison == "!=" and key_value != value:
                    result.append(item)
                elif comparison == ">" and key_value > value:
                    result.append(item)
                elif comparison == "<" and key_value < value:
                    result.append(item)
                elif comparison == ">=" and key_value >= value:
                    result.append(item)
                elif comparison == "<=" and key_value <= value:
                    result.append(item)
        return self._to_datadict(result)
