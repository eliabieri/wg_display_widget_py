import widget
from widget.imports.types import WidgetContext, WidgetResult

class Widget(widget.Widget):

    def get_name(self) -> str:
        return "Python Widget"

    def get_version(self) -> str:
        return "0.0.1"

    def get_config_schema(self) -> str:
        return "{}"

    def get_run_update_cycle_seconds(self) -> int:
        return 1

    def run(self, context: WidgetContext) -> WidgetResult:
        return WidgetResult(data="Hello World!")
