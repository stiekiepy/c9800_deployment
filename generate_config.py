
from nornir import InitNornir
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir.plugins.inventory.simple import SimpleInventory
from nornir.core.plugins.inventory import InventoryPluginRegister
import ipdb


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
    config_path = f"configs_partial/"
    filename = f"{config_path}02_{task.host['wlc_name']}_redundancy.txt"
    content = task.host["redundancy"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def vlans(task):
    # Render configs from template
    template_path = f"templates/"
    template = "03_vlans.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["vlans"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}03_{task.host['wlc_name']}_vlans.txt"
    content = task.host["vlans"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def tacacs_radius(task):
    # Render configs from template
    template_path = f"templates/"
    template = "04_tacacs_radius.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["tacacs_radius"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}04_{task.host['wlc_name']}_tacacs_radius.txt"
    content = task.host["tacacs_radius"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def http_ssh(task):
    # Render configs from template
    template_path = f"templates/"
    template = "05_http_ssh.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["http_ssh"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}05_{task.host['wlc_name']}_http_ssh.txt"
    content = task.host["http_ssh"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def wlc_interfaces(task):
    # Render configs from template
    template_path = f"templates/"
    template = "06_wlc_interfaces.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["wlc_interfaces"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}06_{task.host['wlc_name']}_wlc_interfaces.txt"
    content = task.host["wlc_interfaces"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def guestredirect_internet_ACL(task):
    # Render configs from template
    template_path = f"templates/"
    template = "07_guestredirect_internet_ACL.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["guestredirect_internet_ACL"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}07_{task.host['wlc_name']}_guestredirect_internet_ACL.txt"
    content = task.host["guestredirect_internet_ACL"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def snmp_ntp(task):
    # Render configs from template
    template_path = f"templates/"
    template = "08_snmp_ntp.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["snmp_ntp"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}08_{task.host['wlc_name']}_snmp_ntp.txt"
    content = task.host["snmp_ntp"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def banner(task):
    # Render configs from template
    template_path = f"templates/"
    template = "09_banner.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["banner"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}09_{task.host['wlc_name']}_banner.txt"
    content = task.host["banner"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def line_configs(task):
    # Render configs from template
    template_path = f"templates/"
    template = "10_line_configs.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["line_configs"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}10_{task.host['wlc_name']}_line_configs.txt"
    content = task.host["line_configs"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def policy_tag_wlan_policy_profiles(task):
    # Render configs from template
    template_path = f"templates/"
    template = "11_policy_tag_wlan_policy_profiles.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["policy_tag_wlan_policy_profiles"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}11_{task.host['wlc_name']}_policy_tag_wlan_policy_profiles.txt"
    content = task.host["policy_tag_wlan_policy_profiles"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def apjoin_tag_profile(task):
    # Render configs from template
    template_path = f"templates/"
    template = "12_apjoin_tag_profile.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["ap_join_tag"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}12_{task.host['wlc_name']}_apjoin_tag_profile.txt"
    content = task.host["ap_join_tag"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def rf_tag_profile(task):
    # Render configs from template
    template_path = f"templates/"
    template = "13_rf_tag_profile.j2"

    ren_result = task.run(
        task=template_file,
        template=template,
        path=template_path,
        **task.host
    )
    rendered_config = ren_result[0].result
    task.host["rf_tag_profile"] = rendered_config

    # Write configs to file
    config_path = f"configs_partial/"
    filename = f"{config_path}13_{task.host['wlc_name']}_rf_tag_profile.txt"
    content = task.host["rf_tag_profile"]

    task.run(task=write_file,
             filename=filename,
             content=content
             )


def main(task):

    task.run(
        task=redundancy
    )
    task.run(
        task=vlans
    )
    task.run(
        task=tacacs_radius
    )
    task.run(
        task=http_ssh
    )
    task.run(
        task=wlc_interfaces
    )
    task.run(
        task=guestredirect_internet_ACL
    )
    task.run(
        task=snmp_ntp
    )
    task.run(
        task=banner
    )
    task.run(
        task=line_configs
    )
    task.run(
        task=policy_tag_wlan_policy_profiles
    )
    task.run(
        task=apjoin_tag_profile
    )
    task.run(
        task=rf_tag_profile
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
                "host_file": "inventory/hosts.yaml",  # edit for your environment.
                "group_file": "inventory/groups.yaml",
                "defaults_file": "inventory/defaults.yaml"
            },
        }
    )
    return nr


if __name__ == "__main__":
    #    import menu
    #    menu.main()
    #    choice = menu.main()

    nr = get_nornir_cfg()

    result = nr.run(
        name="Main task call here",
        task=main,
    )
#    print_result(result)
    # ipdb.set_trace()
