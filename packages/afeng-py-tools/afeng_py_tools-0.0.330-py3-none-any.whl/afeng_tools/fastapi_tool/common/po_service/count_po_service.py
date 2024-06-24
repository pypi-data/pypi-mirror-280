from afeng_tools.fastapi_tool.common.po_service.base_po_service import PoService


class CountPoService(PoService):
    _table_name_ = "tb_count_info"
    pass
