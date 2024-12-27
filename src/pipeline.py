import yaml
from typing import List, TypedDict, Any

from pydantic import ValidationError

from src.base.nlp_module import NLPModule
from src.module_registry import MODULE_REGISTRY


class StageType(TypedDict):
    module: NLPModule
    params: dict


class Pipeline:
    def __init__(self, config_path: str):
        """
        Initialize the pipeline by loading the configuration from a YAML file.

        Args:
            config_path (str): Path to the YAML configuration file.
        """
        self.stages: List[StageType] = []  # List of {"module": NLPModule, "params": Any}
        self._load_config(config_path)

    def _load_config(self, config_path: str):
        """
        Load pipeline configuration from a YAML file and initialize the modules.

        Args:
            config_path (str): Path to the YAML configuration file.
        """
        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        for step in config["pipeline"]:
            module_class = MODULE_REGISTRY.get(step["type"])
            if not module_class or not issubclass(module_class, NLPModule):
                raise ValueError(f"Invalid module type: {step['type']}")

            params = step.get("params", None)
            self.stages.append({"module": module_class(), "params": params})

    def _validate_pipeline(self):
        for i, stage in enumerate(self.stages):
            module = stage["module"]
            params = stage["params"]

            output_type = module.__orig_bases__[0].__args__[1]

            if output_type != str and i < len(self.stages) - 1:
                raise TypeError(
                    f"Module {type(module).__name__} produces {output_type}, but only string outputs can pass to subsequent modules. "
                    f"Ensure that {type(module).__name__} is the last module in the pipeline."
                )

            param_type = module.__orig_bases__[0].__args__[0]

            if param_type != dict and params is not None:
                try:
                    param_type.parse_obj(params)  # Use pydantic to validate
                except ValidationError as e:
                    raise TypeError(
                        f"Module {type(module).__name__} received invalid params. Validation Error: {e.errors()}"
                    )

    def run(self, input_text: str) -> Any:
        self._validate_pipeline()

        output = input_text
        for step in self.stages:
            module = step["module"]
            params = step["params"]
            output = module.process(output, params)
        return output
