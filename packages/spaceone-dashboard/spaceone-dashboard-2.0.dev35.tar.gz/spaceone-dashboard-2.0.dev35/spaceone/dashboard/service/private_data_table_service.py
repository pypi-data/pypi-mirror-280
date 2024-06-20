import logging
from typing import Union

from spaceone.core.service import *
from spaceone.core.error import *
from spaceone.dashboard.manager.private_data_table_manager import (
    PrivateDataTableManager,
)
from spaceone.dashboard.manager.private_widget_manager import PrivateWidgetManager
from spaceone.dashboard.manager.data_table_manager.data_source_manager import (
    DataSourceManager,
)
from spaceone.dashboard.manager.data_table_manager.data_transformation_manager import (
    DataTransformationManager,
)
from spaceone.dashboard.model.private_data_table.request import *
from spaceone.dashboard.model.private_data_table.response import *
from spaceone.dashboard.model.private_data_table.database import PrivateDataTable

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@authorization_handler
@mutation_handler
@event_handler
class PrivateDataTableService(BaseService):
    resource = "PrivateDataTable"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pri_data_table_mgr = PrivateDataTableManager()

    @transaction(
        permission="dashboard:PrivateDataTable.write",
        role_types=["USER"],
    )
    @convert_model
    def add(
        self, params: PrivateDataTableAddRequest
    ) -> Union[PrivateDataTableResponse, dict]:
        """Add private data table

        Args:
            params (dict): {
                'widget_id': 'str',             # required
                'name': 'str',
                'source_type': 'str',           # required
                'options': 'dict',              # required
                'tags': 'dict',
                'user_id': 'str',               # injected from auth (required)
                'domain_id': 'str',             # injected from auth (required)
            }

        Returns:
            PrivateDataTableResponse:
        """

        pri_widget_mgr = PrivateWidgetManager()
        pri_widget_mgr.get_private_widget(
            params.widget_id,
            params.domain_id,
            params.user_id,
        )

        ds_mgr = DataSourceManager(
            params.source_type,
            params.options,
        )

        # Load data source to verify options
        ds_mgr.load_data_source()

        # Get data and labels info from options
        data_info, labels_info = ds_mgr.get_data_and_labels_info(params.options)

        params_dict = params.dict()
        params_dict["data_type"] = "ADDED"
        params_dict["data_info"] = data_info
        params_dict["labels_info"] = labels_info

        pri_data_table_vo = self.pri_data_table_mgr.create_private_data_table(
            params_dict
        )

        return PrivateDataTableResponse(**pri_data_table_vo.to_dict())

    @transaction(
        permission="dashboard:PrivateDataTable.write",
        role_types=["USER"],
    )
    @convert_model
    def transform(
        self, params: PrivateDataTableTransformRequest
    ) -> Union[PrivateDataTableResponse, dict]:
        """Add private data table

        Args:
            params (dict): {
                'widget_id': 'str',             # required
                'name': 'str',
                'operator': 'str',              # required
                'options': 'dict',              # required
                'tags': 'dict',
                'user_id': 'str',               # injected from auth (required)
                'domain_id': 'str',             # injected from auth (required)
            }

        Returns:
            PrivateDataTableResponse:
        """

        pri_widget_mgr = PrivateWidgetManager()
        pri_widget_mgr.get_private_widget(
            params.widget_id,
            params.domain_id,
            params.user_id,
        )

        params_dict = params.dict()
        params_dict["data_type"] = "TRANSFORMED"

        pri_data_table_vo = self.pri_data_table_mgr.create_private_data_table(
            params_dict
        )

        return PrivateDataTableResponse(**pri_data_table_vo.to_dict())

    @transaction(
        permission="dashboard:PrivateDataTable.write",
        role_types=["USER"],
    )
    @convert_model
    def update(
        self, params: PrivateDataTableUpdateRequest
    ) -> Union[PrivateDataTableResponse, dict]:
        """Update private data table

        Args:
            params (dict): {
                'data_table_id': 'str',         # required
                'name': 'str',
                'options': 'dict',
                'tags': 'dict',
                'user_id': 'str',               # injected from auth (required)
                'domain_id': 'str'              # injected from auth (required)
            }

        Returns:
            PrivateDataTableResponse:
        """

        pri_data_table_vo: PrivateDataTable = (
            self.pri_data_table_mgr.get_private_data_table(
                params.data_table_id, params.domain_id, params.user_id
            )
        )

        params_dict = params.dict(exclude_unset=True)

        if options := params_dict.get("options"):
            if pri_data_table_vo.data_type == "ADDED":
                ds_mgr = DataSourceManager(
                    pri_data_table_vo.source_type,
                    pri_data_table_vo.options,
                )

                # Load data source to verify options
                ds_mgr.load_data_source()

                # change timediff format
                if timediff := options.get("timediff"):
                    if years := timediff.get("years"):
                        options["timediff"] = {"years": years}
                    elif months := timediff.get("months"):
                        options["timediff"] = {"months": months}
                    elif days := timediff.get("days"):
                        options["timediff"] = {"days": days}

                    params_dict["options"] = options

                # Get data and labels info from options
                data_info, labels_info = ds_mgr.get_data_and_labels_info(options)
                params_dict["data_info"] = data_info
                params_dict["labels_info"] = labels_info
            else:
                pass

        pri_data_table_vo = self.pri_data_table_mgr.update_private_data_table_by_vo(
            params_dict, pri_data_table_vo
        )

        return PrivateDataTableResponse(**pri_data_table_vo.to_dict())

    @transaction(
        permission="dashboard:PrivateDataTable.write",
        role_types=["USER"],
    )
    @convert_model
    def delete(self, params: PrivateDataTableDeleteRequest) -> None:
        """Delete private data table

        Args:
            params (dict): {
                'data_table_id': 'str',         # required
                'user_id': 'str',               # injected from auth (required)
                'domain_id': 'str'              # injected from auth (required)
            }

        Returns:
            None
        """

        pri_data_table_vo: PrivateDataTable = (
            self.pri_data_table_mgr.get_private_data_table(
                params.data_table_id,
                params.domain_id,
                params.user_id,
            )
        )

        self.pri_data_table_mgr.delete_private_data_table_by_vo(pri_data_table_vo)

    @transaction(
        permission="dashboard:PrivateDataTable.write",
        role_types=["USER"],
    )
    @convert_model
    def load(self, params: PrivateDataTableLoadRequest) -> dict:
        """Load private data table

        Args:
            params (dict): {
                'data_table_id': 'str',         # required
                'granularity': 'str',           # required
                'start': 'str',
                'end': 'str',
                'sort': 'list',
                'page': 'dict',
                'user_id': 'str',               # injected from auth (required)
                'domain_id': 'str'              # injected from auth (required)
            }

        Returns:
            None
        """

        pri_data_table_vo: PrivateDataTable = (
            self.pri_data_table_mgr.get_private_data_table(
                params.data_table_id,
                params.domain_id,
                params.user_id,
            )
        )

        if pri_data_table_vo.data_type == "ADDED":
            ds_mgr = DataSourceManager(
                pri_data_table_vo.source_type,
                pri_data_table_vo.options,
            )
            ds_mgr.load_data_source(
                params.granularity,
                params.start,
                params.end,
            )
            return ds_mgr.response(params.sort, params.page)

        else:
            return {
                "results": [],
                "total_count": 0,
            }

    @transaction(
        permission="dashboard:PrivateDataTable.read",
        role_types=["USER"],
    )
    @convert_model
    def get(
        self, params: PrivateDataTableGetRequest
    ) -> Union[PrivateDataTableResponse, dict]:
        """Get private data table

        Args:
            params (dict): {
                'data_table_id': 'str',         # required
                'user_id': 'str',               # injected from auth (required)
                'domain_id': 'str'              # injected from auth (required)
            }

        Returns:
            PrivateDataTableResponse:
        """

        pri_data_table_vo: PrivateDataTable = (
            self.pri_data_table_mgr.get_private_data_table(
                params.data_table_id,
                params.domain_id,
                params.user_id,
            )
        )

        return PrivateDataTableResponse(**pri_data_table_vo.to_dict())

    @transaction(
        permission="dashboard:PrivateDataTable.read",
        role_types=["USER"],
    )
    @append_query_filter(
        [
            "widget_id",
            "data_table_id",
            "name",
            "data_type",
            "source_type",
            "operator",
            "domain_id",
            "user_id",
        ]
    )
    @append_keyword_filter(["data_table_id", "name"])
    @convert_model
    def list(
        self, params: PrivateDataTableSearchQueryRequest
    ) -> Union[PrivateDataTablesResponse, dict]:
        """List private data tables

        Args:
            params (dict): {
                'query': 'dict (spaceone.api.core.v1.Query)'
                'widget_id': 'str',                             # required
                'data_table_id': 'str',
                'name': 'str',
                'data_type': 'str',
                'source_type': 'str',
                'operator': 'str',
                'user_id': 'str',                               # injected from auth (required)
                'domain_id': 'str',                             # injected from auth (required)
            }

        Returns:
            PrivateDataTablesResponse:
        """

        query = params.query or {}
        (
            pri_data_table_vos,
            total_count,
        ) = self.pri_data_table_mgr.list_private_data_tables(query)
        pri_data_tables_info = [
            pri_data_table_vo.to_dict() for pri_data_table_vo in pri_data_table_vos
        ]
        return PrivateDataTablesResponse(
            results=pri_data_tables_info, total_count=total_count
        )
