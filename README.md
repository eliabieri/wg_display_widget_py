
# WG Display widget template for Python

Template repository for creating a [WG Display](https://github.com/eliabieri/wg_display) widget in Python. 

```bash
# Generate bindings
poetry run componentize-py --wit-path wg_display_widget_wit/wit --world widget bindings .
# Generate component
poetry run componentize-py --wit-path wg_display_widget_wit/wit --world widget componentize app --output widget.wasm
```
