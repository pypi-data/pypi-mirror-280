from graphlib import TopologicalSorter
from tabulate import tabulate

import goshawk.domain as domain
from goshawk.logging import LOG

from .. import app_settings
from ..utils import get_adapter

LOG.debug("deployer loading")

Adapter = get_adapter(app_settings.DB_TYPE.value)


def schema_in_mask(schema_name: str, mask: str) -> bool:
    schema_db = schema_name.split(".")[0].upper()
    mask_db = mask.split(".")[0].upper()
    mask_schema = mask.split(".")[1].upper()
    if mask_db != schema_db:
        LOG.debug(f"mask db {mask_db} not equal schema db {schema_db}")
        return False
    if mask_schema == "*":
        return True
    return mask.upper() == schema_name.upper()


def schema_matches_any_mask(schema_name: str, masks: list[str]) -> bool:
    return not masks or any(schema_in_mask(schema_name, m) for m in masks)


def convert_schema(target_db: str, qualified_schema: str) -> str:
    if qualified_schema.startswith(target_db):
        return qualified_schema
    else:
        return target_db + "." + qualified_schema.split(".")[1]


def deploy_schema(target_db: str, child_schema: str) -> None:
    target_schema = convert_schema(target_db, child_schema)
    Adapter.create_schema(target_db, target_schema)
    model_dag = domain.models.filtered_dag(child_schema)
    ts = TopologicalSorter(model_dag)
    for fqn in ts.static_order():
        if fqn.startswith(child_schema):
            LOG.debug(f"Deploying model {fqn}")
            if domain.models.sql_models.get(fqn):
                Adapter.deploy_model(target_schema, domain.models.sql_models[fqn])
            else:
                LOG.debug(f"Model {fqn} does not exist in collection")
        else:
            LOG.debug(f"Model {fqn} already deployed")


def clone_database() -> None:
    LOG.debug(f"cli_params={domain.cli_params}")
    if domain.cli_params.get("dry_run"):
        return
    print("cloning")
    source_db = domain.models.db
    target_db = source_db + "_" + domain.cli_params["db_env"].upper()
    LOG.debug(f"Cloning {source_db} into {target_db}")
    Adapter.clone_db(source_db, target_db)
    return


def deploy_database() -> None:
    LOG.debug(domain.cli_params)
    if domain.cli_params["dry_run"]:
        return
    LOG.info("DEPLOYING DATABASE")
    # masks = []
    # models = mode
    dag = domain.models.schema_dag
    mask = domain.cli_params["mask"]

    ts = TopologicalSorter(dag)
    print(mask)

    if domain.cli_params.get("db_env"):
        deploy_to_prod = False
        target_db = domain.models.db + "_" + domain.cli_params.get("db_env", "")
    else:
        deploy_to_prod = True
        temp_suffix = "deploytemp"
        target_db = domain.models.db + "_" + temp_suffix
    # TODO: make sure db exists
    # Adapter.create_database_if_not_exists(domain.models.db)
    # Adapter.clone_db(domain.models.db,target_db)
    schema_list: list[str] = []
    for schema in ts.static_order():
        schema_list.append(schema)
        LOG.debug(f"Deploying schema {schema}")
        if schema_matches_any_mask(schema, mask):
            # print(f"Deploying {schema}")
            deploy_schema(target_db, schema)
        else:
            LOG.debug("Schema doesn't match masks")
    if deploy_to_prod:
        LOG.debug("Deployment to clone complete - Swapping in schemas")
        for schema in schema_list:
            schema_name = schema.split(".")[1]
            Adapter.create_schema_if_not_exists(schema)
            Adapter.swap_schema(target_db + "." + schema_name, schema)
    if deploy_to_prod:
        print(tabulate(Adapter.get_models_in_db(domain.models.db)))
    else:
        print(tabulate(Adapter.get_models_in_db(target_db)))
