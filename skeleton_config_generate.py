#!/usr/bin/python
from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir.plugins.inventory.simple import SimpleInventory
from nornir.core.plugins.inventory import InventoryPluginRegister


def render_skeleton(task):
    """
    Takes the variables in "inventory/hosts_skeleton.yaml" and renders _skeleton
    configs for both WLCs. Saves the rendered config as a dict attached to
    task.hosts_skeleton

    returns: nothing.
    """
    template_path = f"templates/"
    template = "c9800_skeleton.j2"

    ren_result = task.run(
        task=template_file,
        name="Running render task for " + str(task.host),
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["rendered_config"] = rendered_config

    config_path = f"configs_skeleton/"
    filename = f"{config_path}{task.host['wlc_name']}_skeleton_config.txt"
    content = task.host["rendered_config"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def switch_interfaces(task):
    # Render configs from template
    template_path = f"templates/"
    template = "01_switch_interfaces.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["switch_interfaces"] = rendered_config

    # Write configs to file
    config_path = f"configs_skeleton/"
    filename = f"{config_path}{task.host['core_sw_name']}_switch_interfaces.txt"
    content = task.host["switch_interfaces"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def redundancy(task):
    # Render configs from template
    template_path = f"templates/"
    template = "02_redundancy.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["redundancy"] = rendered_config

    # Write configs to file
    config_path = f"configs_skeleton/"
    filename = f"{config_path}{task.host['wlc_name']}_redundancy.txt"
    content = task.host["redundancy"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def main(task):

    task.run(
        task=render_skeleton
    )


##
## Standard functions below for every nornir script ##
##


def get_nornir_cfg():
    """
    Returns the Nornir object.
    """
    InventoryPluginRegister.register("SimpleInventory", SimpleInventory)
    nr = InitNornir(
        runner={
            "plugin": "threaded",
            "options": {
                "num_workers": 10,
            },
        },
        inventory={
            "plugin": "SimpleInventory",
            "options": {
                "host_file": "inventory/hosts_skeleton.yaml",  # edit for your environment.
                "group_file": "inventory/groups.yaml",
                "defaults_file": "inventory/defaults.yaml"
            },
        }
    )
    return nr


if __name__ == "__main__":
    nr = get_nornir_cfg()

    result = nr.run(
        name="Main task call here",
        task=main,
    )

    c9800_1_nr = nr.filter(name="c9800_1")
    c9800_1_switch_intf = c9800_1_nr.run(
        task=switch_interfaces,
    )

    c9800_1_nr = nr.filter(name="c9800_1")
    c9800_1_redundancy = c9800_1_nr.run(
        task=redundancy,
    )

    print_result(result)
